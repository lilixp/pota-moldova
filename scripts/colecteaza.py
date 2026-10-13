# Colector zilnic de date POTA pentru Moldova (rulează în GitHub Actions)
#
# Ce face:
#   1. Descarcă lista parcurilor MD (o singură cerere).
#   2. Descarcă activările DOAR pentru parcurile care s-au schimbat de ieri.
#   3. Calculează clasamentul activatorilor și îl salvează în data/clasament.json.
#
# Rulare pe PC (din folderul proiectului):  py scripts\colecteaza.py
#
# Notă: api.pota.app este API-ul intern al site-ului pota.app. Nu e documentat oficial
# și poate dispărea oricând, deci îl folosim rar și politicos:
#   - o pauză de cel puțin 1 secundă între cereri, niciodată în rafală;
#   - un User-Agent care spune cine suntem;
#   - oprire imediată dacă serverul răspunde 403 (interzis) sau 429 (prea multe cereri).

import json
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# Adresele API-ului (prefixul MD = Moldova)
URL_BAZA = "https://api.pota.app"
URL_PARCURI = URL_BAZA + "/program/parks/MD"

# Folderul cu date, lângă pagina web (scripts/../data)
FOLDER_DATE = Path(__file__).resolve().parent.parent / "data"

# Ne prezentăm clar serverului: proiect, indicativ, adresa codului sursă
USER_AGENT = ("POTA-Moldova-stats/1.0 (unofficial daily statistics for Moldova parks; "
              "ER1PL; +https://github.com/lilixp/pota-moldova)")

PAUZA = 1.0          # secunde între două cereri
INCERCARI = 2        # câte încercări pentru o cerere eșuată
MAX_CERERI = 150     # siguranță: nu facem niciodată mai multe cereri într-o rulare
QSO_MINIM = 10       # regula POTA: o activare e validă de la 10 QSO-uri

cereri_facute = 0


class OprireColectare(Exception):
    """Serverul ne-a refuzat sau am atins limita de cereri: ne oprim imediat."""


def descarca_json(url):
    """Descarcă o adresă și întoarce JSON-ul ca listă/dicționar Python."""
    global cereri_facute
    for incercare in range(1, INCERCARI + 1):
        if cereri_facute >= MAX_CERERI:
            raise OprireColectare(f"limita de {MAX_CERERI} cereri pe rulare")
        if cereri_facute > 0:
            time.sleep(PAUZA)                      # pauza dintre cereri
        cereri_facute += 1
        try:
            cerere = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(cerere, timeout=30) as raspuns:
                return json.loads(raspuns.read().decode("utf-8"))
        except urllib.error.HTTPError as eroare:
            if eroare.code in (403, 429):
                raise OprireColectare(f"serverul a răspuns {eroare.code} la {url}")
            if incercare == INCERCARI:
                raise
            print(f"   încercarea {incercare} a eșuat (HTTP {eroare.code}), reîncerc...")
            time.sleep(10)
        except Exception as eroare:
            if incercare == INCERCARI:
                raise
            print(f"   încercarea {incercare} a eșuat ({eroare}), reîncerc...")
            time.sleep(10)


def citeste(nume_fisier):
    """Citește un fișier salvat anterior (sau {} dacă nu există)."""
    cale = FOLDER_DATE / nume_fisier
    if cale.exists():
        return json.loads(cale.read_text(encoding="utf-8"))
    return {}


def salveaza(nume_fisier, continut, compact=False):
    """Salvează date în format JSON (cu diacritice păstrate)."""
    text = json.dumps(continut, ensure_ascii=False,
                      separators=(",", ":") if compact else None,
                      indent=None if compact else 1)
    (FOLDER_DATE / nume_fisier).write_text(text + "\n", encoding="utf-8")


def calculeaza_clasament(activari):
    """Din toate activările parcurilor MD face clasamentul activatorilor."""
    pe_indicativ = {}
    for ref, lista in activari.items():
        for a in lista:
            indicativ = (a.get("activeCallsign") or "").upper().strip()
            if not indicativ:
                continue
            r = pe_indicativ.setdefault(indicativ, {
                "indicativ": indicativ, "activari": 0, "tentative": 0,
                "qso": 0, "parcuri": set(), "ultima": ""})
            qso = a.get("totalQSOs") or 0
            r["qso"] += qso
            if qso >= QSO_MINIM:
                r["activari"] += 1
                r["parcuri"].add(ref)
            else:
                r["tentative"] += 1
            r["ultima"] = max(r["ultima"], a.get("qso_date") or "")

    clasament = []
    for r in pe_indicativ.values():
        r["parcuri"] = len(r["parcuri"])
        d = r["ultima"]                            # 20260927 -> 2026-09-27
        r["ultima"] = f"{d[:4]}-{d[4:6]}-{d[6:8]}" if len(d) == 8 else None
        clasament.append(r)
    # Ordinea: activări valide, apoi QSO-uri, apoi alfabetic
    clasament.sort(key=lambda r: (-r["activari"], -r["qso"], r["indicativ"]))
    return clasament


def main():
    FOLDER_DATE.mkdir(exist_ok=True)

    # --- Pasul 1: lista parcurilor ---
    print("Descarc lista parcurilor din Moldova...")
    try:
        parcuri = descarca_json(URL_PARCURI)
    except Exception as eroare:
        print(f"EROARE: lista parcurilor nu s-a putut descărca: {eroare}")
        sys.exit(1)                                # datele vechi rămân neatinse

    # Păstrăm doar câmpurile de care are nevoie pagina (fișier mai mic)
    campuri = ["reference", "name", "latitude", "longitude", "grid",
               "locationDesc", "attempts", "activations", "qsos"]
    salveaza("parcuri.json", [{k: p.get(k) for k in campuri} for p in parcuri], compact=True)

    cu_activitate = [p for p in parcuri if p.get("attempts", 0) > 0 or p.get("activations", 0) > 0]
    print(f"{len(parcuri)} parcuri, {len(cu_activitate)} cu activitate.")

    # --- Pasul 2: activări doar pentru parcurile schimbate ---
    activari = citeste("activari.json")
    stare = citeste("stare.json")                  # cifrele fiecărui parc la ultima rulare

    de_descarcat = []
    for p in cu_activitate:
        ref = p["reference"]
        cifre = [p.get("attempts", 0), p.get("activations", 0), p.get("qsos", 0)]
        if stare.get(ref) != cifre or ref not in activari:
            de_descarcat.append((ref, cifre))
    print(f"Parcuri schimbate: {len(de_descarcat)}")

    erori, oprit = [], None
    for nr, (ref, cifre) in enumerate(de_descarcat, start=1):
        print(f"[{nr}/{len(de_descarcat)}] {ref}")
        try:
            activari[ref] = descarca_json(f"{URL_BAZA}/park/activations/{ref}?count=all")
            stare[ref] = cifre
        except OprireColectare as motiv:
            oprit = str(motiv)
            print(f"   OPRIRE: {motiv}")
            break
        except Exception as eroare:
            print(f"   EROARE la {ref}: {eroare}")
            erori.append({"parc": ref, "eroare": str(eroare)})

    salveaza("activari.json", activari)
    salveaza("stare.json", stare)

    # --- Pasul 3: clasamentul activatorilor ---
    clasament = calculeaza_clasament(activari)
    salveaza("clasament.json", clasament)

    # --- Ultima activare din MD (pentru banda „în aer acum” de pe pagină) ---
    ultima = None
    for ref, lista in activari.items():
        for a in lista:
            d = a.get("qso_date") or ""
            if len(d) == 8 and (ultima is None or d > ultima["data"].replace("-", "")):
                ultima = {"indicativ": (a.get("activeCallsign") or "").upper(),
                          "parc": ref, "data": f"{d[:4]}-{d[4:6]}-{d[6:8]}"}

    # --- Informații pentru pagină ---
    salveaza("meta.json", {
        "ultima_activare": ultima,
        "actualizat_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "parcuri": len(parcuri),
        "cereri": cereri_facute,
        "parcuri_actualizate": len(de_descarcat) - len(erori) - (1 if oprit else 0),
        "oprit": oprit,
        "erori": erori,
    })

    print(f"\nGata: {cereri_facute} cereri, {len(clasament)} activatori în clasament.")
    if oprit or erori:
        print("ATENȚIE: colectarea nu a fost completă (vezi mai sus).")
        sys.exit(1)                                # GitHub îți trimite email


if __name__ == "__main__":
    main()
