# Roadmap – ER POTA Tracker

Planul de dezvoltare al paginii **ER POTA Tracker** (statistici neoficiale pentru parcurile POTA din Moldova).
Ordinea se poate schimba în funcție de observațiile testerilor.

Legendă: ✅ gata · 🔄 în lucru · ⬜ de făcut · 💡 idee, fără prioritate

Ordinea etapelor: **stabilizare → pagina web pentru telefon → lansare publică → funcții noi → aplicație pentru telefon**.

---

## Etapa 0 – Versiune de test (v0.1) ✅

*13–14 octombrie 2026*

- ✅ Pagina **Acum**: banda live, harta, cifrele principale, top 10 activatori, top 10 parcuri, raioane, căutarea parcurilor
- ✅ Paginile **Hartă**, **Clasament** (activatori, parcuri, raioane) și **Parcuri** (cu istoricul activărilor)
- ✅ Română și engleză (butonul RO | EN, `?lang=en`)
- ✅ Colector zilnic prin GitHub Actions + publicare pe GitHub Pages
- ✅ Statisticile unui indicativ în două cartonașe: **Moldova** și **Global**
- ✅ Datele globale din profilul public pota.app (doar activările valide)
- ✅ Numele oficial **ER POTA Tracker**
- ✅ Butonul „Arată încă 10” la lista de parcuri
- ✅ README cu funcțiile, sursele de date și regulile de calcul

## Etapa 1 – Stabilizare (v0.2) 🔄

*Testare cu activatorii din Moldova*

- ✅ Verificarea rulării zilnice automate (programată la 03:23 UTC; GitHub o poate porni cu câteva ore întârziere, 14.10.2026: OK)
- ✅ Varianta pentru telefon: meniu jos cu iconuri, harta pe tot ecranul, carduri, filtre ca butoane rotunde, butonul „Sus”
- ✅ Verificarea datelor pentru toți activatorii din clasament, față de pota.app (14.10.2026: totul corect)
- ✅ Indicativele cu sufix sau prefix (`/P`, `YO/…`): pota.app le adună la indicativul de bază; căutarea face la fel
- ✅ Mențiune clară pe pagină: data ultimei actualizări în subsol, datele se actualizează o dată pe zi
- ⬜ Rezolvarea observațiilor de la testeri

## Etapa 2 – Lansare publică (v1.0) ⬜

*După ce pagina arată bine și pe telefon.*

- ⬜ Subdomeniul **erpota.qrz.md** (CNAME `erpota` → `lilixp.github.io`, HTTPS); apoi adresele din `og:url` și `og:image` trec pe erpota.qrz.md
- ✅ Eliminarea etichetei „versiune de test” și a setării „nu indexa”
- ✅ Previzualizarea linkului pe Facebook / Messenger (imagine `og.png` cu harta parcurilor)
- ⬜ Pagina **Despre**: ce date se folosesc, cum se calculează, regulile POTA
- ⬜ Email informativ către echipa POTA despre proiect
- ⬜ Anunț în grupurile de radioamatori

## Etapa 3 – Funcții noi (v1.x) ⬜

*„Prima activare” se face acum, înainte de lansare.*

- ✅ **„Prima activare”** a fiecărui parc: cine și când (fișa parcului, plăcuța „prima” în istoric, coloana „Primul în” în clasament, rândul din cartonașul Moldova)

Făcute mai devreme decât era planificat:

- ✅ **Harta unui indicativ**: pe pagina Hartă scrii indicativul și vezi parcurile activate de el (verde), cele cu doar tentative (roz) și cele neactivate

## Etapa 5 – Aplicație pentru telefon ⬜

*Doar după ce toate etapele de mai sus sunt gata și pagina e oficială pe internet.*

- ⬜ Alegerea formei: pagină instalabilă (PWA, icon pe ecranul principal) sau aplicație Android
- ⬜ Aceleași date și aceleași reguli ca pagina web

## Idei pentru mai târziu 💡

- 💡 Pagină separată **Hunteri** în meniu (top 5 hunteri pe parc, limita datelor de pe pota.app)
- 💡 Noutăți: parcuri noi în listă, activatori noi (cu puțini activatori nu spun mare lucru acum)
- 💡 Evoluția în timp: activări și QSO pe luni sau ani, grafic (la fel)
- 💡 **Regiuni**: raioanele au fost scoase din pagină (14.10.2026); revenim la o împărțire pe regiuni doar după ce reforma administrativ-teritorială e adoptată legal
- 💡 **Parcuri lângă mine (GPS)**: butonul „Lângă mine” arată parcurile cele mai apropiate, cu distanța; poziția rămâne doar în browser

## Etapa 4 – Durabilitate ⬜

- ⬜ Trecerea pe **API-ul public oficial POTA**, când va fi disponibil
- ⬜ Alertă dacă colectorul zilnic eșuează mai multe zile la rând
- ⬜ Copie de rezervă a datelor

---

*Proiect independent realizat de ER1PL. Nu este afiliat cu Parks on the Air®. Date: [pota.app](https://pota.app).*
