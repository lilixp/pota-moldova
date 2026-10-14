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

- ⬜ Verificarea rulării zilnice automate (03:23 UTC)
- ⬜ Varianta pentru telefon (tabelele devin carduri, filtrele hărții deasupra, meniu compact)
- ⬜ Verificarea datelor pentru toți activatorii din clasament, față de pota.app
- ⬜ Indicativele cu sufix sau prefix (`/P`, `YO/…`): cum se adună la indicativul de bază
- ⬜ Mențiune clară pe pagină: datele se actualizează o dată pe zi
- ⬜ Rezolvarea observațiilor de la testeri

## Etapa 2 – Lansare publică (v1.0) ⬜

*După ce pagina arată bine și pe telefon.*

- ⬜ Subdomeniul **potatrack.qrz.md** (CNAME → GitHub Pages, HTTPS)
- ⬜ Eliminarea etichetei „versiune de test” și a setării „nu indexa”
- ⬜ Pagina **Despre**: ce date se folosesc, cum se calculează, regulile POTA
- ⬜ Email informativ către echipa POTA despre proiect
- ⬜ Anunț în grupurile de radioamatori

## Etapa 3 – Funcții noi (v1.x) ⬜

*După lansare. Începem cu raioanele colorate.*

1. ⬜ **Raioanele colorate pe hartă**, după procentul de parcuri activate (prima funcție nouă)
2. ⬜ „Prima activare” a fiecărui parc: cine și când
3. ⬜ Noutăți: parcuri noi în listă, activatori noi, parcuri activate prima dată
4. ⬜ Evoluția în timp: activări și QSO pe luni sau ani (grafic)

## Etapa 5 – Aplicație pentru telefon ⬜

*Doar după ce toate etapele de mai sus sunt gata și pagina e oficială pe internet.*

- ⬜ Alegerea formei: pagină instalabilă (PWA, icon pe ecranul principal) sau aplicație Android
- ⬜ Aceleași date și aceleași reguli ca pagina web

## Idei pentru mai târziu 💡

- 💡 Pagină separată **Hunteri** în meniu (top 5 hunteri pe parc, limita datelor de pe pota.app)

## Etapa 4 – Durabilitate ⬜

- ⬜ Trecerea pe **API-ul public oficial POTA**, când va fi disponibil
- ⬜ Alertă dacă colectorul zilnic eșuează mai multe zile la rând
- ⬜ Copie de rezervă a datelor

---

*Proiect independent realizat de ER1PL. Nu este afiliat cu Parks on the Air®. Date: [pota.app](https://pota.app).*
