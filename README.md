# ER POTA Tracker

Unofficial statistics for the **Parks on the Air (POTA)** parks in the Republic of Moldova (prefix ER, references `MD-xxxx`).

**Live (test version):** https://lilixp.github.io/pota-moldova/ · English: https://lilixp.github.io/pota-moldova/?lang=en

> **Independent project by ER1PL. Not an official POTA website and not affiliated with Parks on the Air®.**
> All data comes from [pota.app](https://pota.app). For official data, always check pota.app.

🇷🇴 [Descriere în română mai jos](#română)

---

## Features

| Page | Address | What you get |
|---|---|---|
| **Now** | `#acum` | Live band (who is on the air in MD parks right now, or the last activation), map of all parks, key numbers, top 10 activators, top 10 parks, districts, park search (10 at a time, "Show 10 more"), callsign stats |
| **Map** | `#harta` | Full-size map with filters (activated / not activated / on the air, district, search, locator). Click a park for a short card |
| **Leaderboards** | `#clasament` | Three sortable tabs: activators, parks, districts. Click an activator to see their MD parks |
| **Parks** | `#parcuri` | All MD parks, sortable, with the activation history of each park (date, activator, QSOs, CW / phone / data) |

- **Callsign stats** in two cards: **Moldova** (from this page's daily data) and **Global** (live from the public pota.app profile).
- **Romanian / English**, chosen automatically from the browser, switchable with the RO | EN button, or forced with `?lang=en`.
- **Direct links** you can share: `#harta/MD-0066` (map centred on a park), `#parcuri/MD-0066` (park history), `#clasament/ER1SKI` (an activator), `#clasament/raioane` (districts).
- **Optional locator** (e.g. `KN47`): shows distances to parks. Stored only in the visitor's browser.
- Map markers: **green dot** = activated, **white circle with brown dot** = not activated yet, **red dot with pulse** = on the air now.

## Data and sources

The data comes from `api.pota.app`, the **internal API** of the pota.app website. It is undocumented and may change or stop at any time, so it is used **rarely and politely**.

| Data | Endpoint | Requested by | When |
|---|---|---|---|
| List of MD parks | `/program/parks/MD` | GitHub Action | once a day |
| Activations of a park | `/park/activations/{ref}?count=all` | GitHub Action | once a day, **only for parks that changed** |
| Live spots | `/v1/spots` | visitor's browser | every 60 s, **only while the tab is visible** |
| Global callsign stats | `/profile/{call}` | visitor's browser | **only on click**, once per callsign per visit |

Rules used for the numbers:

- An activation is **valid** with **at least 10 QSOs** (POTA rule). Below 10 QSOs it counts as an **attempt**.
- Moldova numbers (leaderboards, parks, history) are computed from the daily `data/activari.json` and match the official per-park totals from pota.app.
- Global numbers use `stats.activator` from `/profile/{call}` (valid activations only, as shown on pota.app).
- Leaderboards and park data are updated **once a day**; an activation made today appears tomorrow. Live spots are real time.

How the daily collector behaves (`scripts/colecteaza.py`):

- identifies itself with a User-Agent: `ER-POTA-Tracker/1.0 (…; ER1PL; +https://github.com/lilixp/pota-moldova)`;
- waits **1 second** between requests, never in bursts;
- downloads activations only for parks whose numbers changed (usually 1–3 requests a day);
- stops immediately on HTTP **403** or **429**; never more than 150 requests per run.

## How it works

```
GitHub Action (daily, 03:23 UTC)
  └─ scripts/colecteaza.py  →  data/*.json  →  commit  →  GitHub Pages
Visitor's browser
  └─ index.html reads data/*.json  (+ live spots and callsign profile from pota.app)
```

| File | Purpose |
|---|---|
| `index.html` | The whole website (HTML + CSS + JavaScript, one file) |
| `scripts/colecteaza.py` | Daily collector (Python, standard library only) |
| `.github/workflows/actualizeaza-date.yml` | Runs the collector daily and publishes the site |
| `data/parcuri.json` | MD parks (reference, name, coordinates, district, activations, QSOs) |
| `data/activari.json` | All activations, per park |
| `data/clasament.json` | Activator leaderboard |
| `data/meta.json` | Update time, last activation, errors |
| `data/stare.json` | Internal collector state (which parks changed) |

## Run locally (Windows, PowerShell)

```powershell
py scripts\colecteaza.py
py -m http.server 8000
```

Then open http://localhost:8000

## Status and roadmap

**Test version.** A roadmap will follow.

## Credits

- Data: [pota.app](https://pota.app) (Parks on the Air®)
- Map: © [OpenStreetMap](https://www.openstreetmap.org/copyright) contributors, [Leaflet](https://leafletjs.com)
- Fonts: Bitter and Source Sans 3 (Google Fonts)

---

## Română

**ER POTA Tracker** este o pagină **neoficială** cu statistici pentru parcurile POTA din Republica Moldova. Este un proiect independent al lui **ER1PL** și nu este afiliat cu Parks on the Air®. Toate datele provin de la [pota.app](https://pota.app).

**Pagini:** Acum (rezumat, hartă, cifre, top 10, raioane, căutare, statistici pe indicativ), Hartă (filtre și fișa parcului), Clasament (activatori, parcuri, raioane) și Parcuri (toate parcurile, cu istoricul activărilor). Pagina e în română și engleză.

**Date:** colectorul rulează o dată pe zi prin GitHub Actions. Face o pauză de 1 secundă între cereri, se prezintă cu un User-Agent care îl identifică, descarcă doar parcurile schimbate și se oprește la 403/429. Spoturile live și statisticile globale pe indicativ se cer din browserul vizitatorului: spoturile la 60 de secunde, cât fila e vizibilă, iar statisticile doar la clic.

**Reguli:** o activare e validă de la **10 QSO**; sub 10 QSO e **tentativă**. Cifrele pentru Moldova se potrivesc cu totalurile oficiale pe parc de pe pota.app.

**Rulare locală:** `py scripts\colecteaza.py`, apoi `py -m http.server 8000` și deschide http://localhost:8000.
