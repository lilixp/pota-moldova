# POTA Moldova

Unofficial statistics page for the Parks on the Air (POTA) parks in the Republic of Moldova.
Pagină neoficială cu statistici pentru parcurile POTA din Republica Moldova.

**This is an independent project by ER1PL. It is not an official POTA site and is not affiliated with Parks on the Air®.**
All data comes from [pota.app](https://pota.app).

## How it works / Cum funcționează

- `scripts/colecteaza.py` runs once a day via GitHub Actions (`.github/workflows/actualizeaza-date.yml`).
  It downloads the MD park list and, only for parks that changed, their activations
  (1 s pause between requests, identifying User-Agent, stops on HTTP 403/429).
  It writes `data/parcuri.json`, `data/clasament.json` and `data/meta.json`.
- `index.html` reads those JSON files. Only live spots (every 60 s, while the tab is visible)
  and per-callsign stats (on click) are requested from the visitor's browser.
- Map tiles: © OpenStreetMap contributors.

## Rulare locală / Local run

```powershell
py scripts\colecteaza.py
py -m http.server 8000
```

Then open http://localhost:8000
