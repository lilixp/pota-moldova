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

- ✅ Adresa **erpota.qrz.md** (14.10.2026): redirecționare de pe serverul qrz.md spre `lilixp.github.io/pota-moldova`
- 💡 Mai târziu, opțional: CNAME `erpota` → `lilixp.github.io` + domeniu în GitHub, ca în bară să rămână erpota.qrz.md (atunci și `og:url`/`og:image` trec pe erpota.qrz.md; NU se setează domeniul în GitHub cât timp există redirecționarea, altfel apare o buclă)
- ✅ Eliminarea etichetei „versiune de test” și a setării „nu indexa”
- ✅ Previzualizarea linkului pe Facebook / Messenger (imagine `og.png` cu harta parcurilor)
- ✅ Pagina **Despre** (`#despre`): ce date se folosesc, cum se calculează, culorile hărții, contact (QRZ.com + email ascuns de roboți)
- ✅ Email informativ către echipa POTA despre proiect (14.10.2026)
- ✅ Anunț în grupurile de radioamatori (14.10.2026)

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

## Probleme cunoscute și remedieri viitoare 🔧

*Constatate prin analiza codului la commitul `f1af67b` (`main`, 15.10.2026). La acel moment datele erau coerente: 232 de parcuri, 78 activate, 134 de activări valide, fără diferențe între totalurile parcurilor și istoricul salvat. Problemele de mai jos sunt limitări ale codului, nu erori observate în datele actuale.*

### 1. Spoturi vechi afișate ca LIVE după erori

- **Statut:** confirmată prin analiza codului; remediere neimplementată.
- **Fișier și funcții:** `index.html` – `loadSpots()`, `renderLive()`, `mdSpots()`, `liveSet()`, `startSpots()`, `stopSpots()`, `drawParks()` (grupa „în aer”), etichetele LIVE din `parkCols()` / `parkCard()`.
- **Când apare și ce efect are (doar afișare):**
  - după o cerere reușită, o eroare ulterioară păstrează lista veche; banda, punctele albastre și etichetele LIVE continuă să arate „în aer acum”, fără avertizare;
  - dacă ultimul răspuns reușit a fost o listă goală, după eroare pagina afirmă în continuare „Niciun spot din parcurile MD acum”; mesajul „Spoturile live nu sunt disponibile” apare doar dacă nicio cerere n-a reușit vreodată;
  - „verificat la HH:MM” arată ora ultimului succes, dar nu spune explicit că datele sunt vechi; nu există prag de vechime pentru spoturi;
  - la revenirea într-o filă ascunsă mult timp se afișează datele vechi până la primul răspuns (sau la nesfârșit, dacă cererea eșuează).
- **Riscuri posibile, nedemonstrate în practică:** cererile nu au limită de timp, iar intervalul de 60 s poate porni o cerere nouă peste una neterminată; un răspuns vechi sosit după unul nou l-ar putea suprascrie, iar ora afișată ar fi a sosirii, nu a cererii. Comportamentul API-ului `/v1/spots` (vechimea spoturilor, formatul la eroare) nu a fost verificat.
- **Soluție propusă:**
  - starea ultimei cereri separată de conținutul ultimului răspuns reușit;
  - afișarea explicită a indisponibilității și a orei ultimei actualizări reușite;
  - un prag documentat după care datele vechi nu mai sunt prezentate ca LIVE, aplicat la fel benzii, ambelor hărți, filtrului „în aer” și etichetelor;
  - limită de timp pentru cereri, fără suprapuneri și fără aplicarea răspunsurilor în ordine inversă.
- **Criterii de acceptare:** succes cu spoturi → eroare; succes cu listă goală → eroare; revenire după o filă ascunsă mult timp; recuperare după revenirea conexiunii. În toate cazurile pagina nu prezintă date expirate drept LIVE și arată clar ora ultimei actualizări reușite.

### 2. Corectări ale istoricului nedetectate de colector

- **Statut:** confirmată prin analiza codului; remediere neimplementată.
- **Fișier și zone:** `scripts/colecteaza.py` – `main()` (lista `cu_activitate`, comparația cu `stare.json`, lista `de_descarcat`, salvarea), `calculeaza_clasament()`; în pagină, tot ce se calculează din `activari.json`.
- **Când apare și ce efect are (date salvate și afișare):**
  - istoricul unui parc se descarcă din nou doar dacă se schimbă `attempts`, `activations` sau `qsos`, ori dacă istoricul lipsește; nu există reconciliere periodică;
  - o corectare de indicativ, dată sau moduri care păstrează cele trei totaluri rămâne nedetectată pe termen nelimitat; afectează clasamentul, „Prima activare”, „Primul în”, „Ultima”, banda „Ultima activare” și statisticile pe indicativ;
  - un parc corectat la activitate zero iese din `cu_activitate`, dar istoricul vechi rămâne în `activari.json` și în statistici;
  - un parc dispărut din lista curentă rămâne în `activari.json` (nu există curățare) și continuă să intre în clasament.
- **Notă despre actualizările parțiale:** `parcuri.json` se salvează înaintea istoricurilor. La o eroare, workflow-ul salvează în repository ce s-a descărcat (pasul „Salvează datele noi” rulează cu `if: always()`), dar **publicarea e blocată** în acea rulare, pentru că jobul de colectare se termină cu `failure`. O publicare ulterioară (un push sau o rulare reușită) publică starea din repository; dacă între timp datele nu au fost reconciliate, ar putea expune totaluri noi lângă istoric vechi. Datele parțiale **nu** sunt publicate automat imediat după eșec. Parcurile eșuate sunt reîncercate la rularea următoare, pentru că `stare.json` nu se actualizează pentru ele.
- **Soluție propusă:**
  - reconciliere periodică sau rotație zilnică a unui număr limitat de parcuri, păstrând pauza între cereri, limita de cereri și oprirea la HTTP 403/429;
  - reguli explicite pentru parcurile cu activitate zero, retrase sau absente temporar din sursă;
  - fără ștergerea automată a istoricului doar pentru că un parc lipsește dintr-un singur răspuns;
  - păstrarea istoricului justificat, cu o regulă clară dacă intră sau nu în statistici.
- **Direcție de investigare:** validarea consistenței setului de date înaintea publicării (totalurile din `parcuri.json` față de `activari.json`) și o politică explicită de păstrare a ultimei versiuni coerente.
- **Criterii de acceptare:** corectarea unui indicativ sau a unei date cu totaluri neschimbate; activitate corectată la zero; parc retras; absență temporară din sursă; colectare întreruptă și apoi recuperată. Clasamentul și statisticile ajung la valorile din sursă într-un termen cunoscut, fără cereri în rafală.

### 3. Erori temporare memorate pentru profilul Global

- **Statut:** confirmată prin analiza codului; remediere neimplementată.
- **Fișier și funcții:** `index.html` – `loadProfile()` (memoria `glData`), `glCard()`, `renderCall()`, `showCall()`, `detaliuActivator()`, `errText()`.
- **Când apare și ce efect are (doar afișare, sesiunea curentă):**
  - la orice eroare, un obiect de eroare e memorat ca rezultat; repetarea căutării aceluiași indicativ nu mai trimite cerere până la reîncărcarea paginii;
  - căutarea și clasamentul folosesc aceeași memorie; în clasament butonul „Statistici POTA globale” dispare după eroare;
  - HTTP 404 primește mesaj tradus, rețeaua căzută are mesajul ei, iar celelalte erori (inclusiv 5xx) apar ca text brut („HTTP 503”); toate se memorează la fel;
  - mesajul se memorează deja tradus și nu se schimbă la trecerea RO/EN;
  - două clicuri rapide în căutare, înainte de răspuns, trimit două cereri (în clasament butonul se dezactivează și previne asta).
- **Soluție propusă:**
  - memorarea separată a răspunsurilor reușite și a erorilor temporare;
  - posibilitatea de reîncercare după eroare, fără reîncărcarea paginii;
  - o politică distinctă și documentată pentru HTTP 404;
  - păstrarea tipului erorii și traducerea mesajului la afișare;
  - fără cereri duplicate pentru același indicativ cât timp una e în curs.
- **Criterii de acceptare:** eroare de rețea → revenirea conexiunii → reîncercare fără reload; HTTP 5xx; HTTP 404; schimbarea limbii după eroare; clicuri rapide repetate; comportament la fel în căutare și în clasament.

### Probleme de interfață (audit vizual și verificare în cod, 15.10.2026)

*Auditul vizual a fost făcut în browser, cu viewport de desktop (1366 px) și mobil simulat (390 și 320 px), fără telefon fizic. Observațiile au fost verificate apoi în cod, la commitul `f1af67b`. Verdictul general: interfața e coerentă și lizibilă, nu e nevoie de o reproiectare.*

#### 4. Fișa de pe hartă se închide singură la actualizarea spoturilor (desktop)

- **Statut:** confirmată în cod și observată în browser; remediere neimplementată.
- **Fișier și funcții:** `index.html` – `loadSpots()` → `renderView()` → `renderMap2()` / `renderMap()` → `drawParks()` (`bindPopup`).
- **Când apare și ce efect are:** la fiecare actualizare reușită a spoturilor (60 s) straturile hărții sunt șterse și recreate, chiar dacă spoturile nu s-au schimbat; popup-ul legat de markerul vechi se închide în timp ce utilizatorul îl citește. Pe telefon fișa (`showPcard()`) e separată și rămâne deschisă, dar conținutul ei nu se actualizează.
- **Soluție propusă:** redesenare doar când se schimbă setul de parcuri „în aer”; sau actualizarea markerelor existente; sau reținerea parcului cu fișă deschisă și redeschiderea ei după redesenare. Trebuie definit comportamentul pentru un parc care nu mai trece de filtre.
- **Criterii de acceptare:** fișa rămâne deschisă după actualizări fără schimbări; selecția și poziția hărții se păstrează; datele live continuă să se actualizeze; închiderea voluntară nu e anulată; verificat separat pe desktop și pe mobil.

#### 5. Plural și „de” în cardurile clasamentului

- **Statut:** confirmată în cod și observată; remediere neimplementată.
- **Fișier și funcții:** `index.html` – funcția `card` din `renderClasament()` (fila Activatori).
- **Ce apare:** „1 parcuri” / „1 parks” (ER1PL, SP7FSA), „1 tentative” / „1 attempts” (SQ9NOT), „62 parcuri” fără „de”, „primul în 58” fără să spună „parcuri”.
- **Soluție propusă:** texte cu număr ca funcții care aplică singularul, pluralul și „de” (ca `nActs` și `mapCount`); „primul în 58 de parcuri” / „first in 58 parks”, fără a sugera exclusivitate (la egalitate, ambii sunt primii).
- **Criterii de acceptare:** 0, 1, 2–19 și 20+ verificate în RO și EN; fără depășiri pe 320 px.

#### 6. Numerele de loc din clasament după sortare

- **Statut:** comportament intenționat (rangul general după activări), dar neclar; remediere neimplementată.
- **Fișier și funcții:** `index.html` – `renderClasament()` (valoarea `rank`), `tabel()`.
- **Ce apare:** după sortarea după QSO, cardurile arată 1, 2, 5, 3; utilizatorul poate crede că numerotarea e greșită.
- **Soluție propusă (recomandată, varianta A):** numărul rămâne rangul general, pentru că e același cu „locul N în clasamentul MD” din cartonașul Moldova, dar e explicat vizibil (de exemplu „#5 general” la alte sortări, antet „Loc” pe PC). Alternative: B – renumerotare la fiecare sortare; C – număr ascuns la alte criterii.
- **Criterii de acceptare:** semnificația numărului e clară și la fel pe PC și pe mobil; egalitățile sunt tratate după regulile proiectului.

#### 7. Instrucțiunea de pe pagina Parcuri nepotrivită pe mobil

- **Statut:** confirmată; remediere neimplementată.
- **Fișier și funcții:** `index.html` – textul `parksPageNote`, `tabel()` (varianta cu carduri).
- **Ce apare:** pe mobil scrie „Clic pe titlul unei coloane pentru sortare”, dar acolo sunt carduri și butoane de sortare, nu coloane.
- **Soluție propusă:** un text comun, valabil pe ambele variante (de exemplu „Apasă pe un parc pentru istoricul activărilor”), sau texte separate care se schimbă și la redimensionarea ferestrei.
- **Criterii de acceptare:** instrucțiunea corespunde controalelor vizibile, în RO și EN.

#### 8. Accesul cu tastatura și cititoarele de ecran

- **Statut:** riscuri confirmate în cod; necesită testare cu tastatura și cu un cititor de ecran.
- **Fișier și funcții:** `index.html` – `tabel()` (carduri `.pc`, rânduri `tr`, antete `th.s`), panoul de filtre `#side`, butonul `#fab`, `closeSheets()`.
- **Ce s-a găsit în cod:** cardurile, rândurile și antetele sortabile au doar `onclick` (fără focus, rol de buton, `aria-expanded`, Enter/Space); panoul de filtre închis e doar deplasat în afara ecranului, deci controalele lui pot rămâne accesibile cu Tab; focusul nu intră în panou la deschidere și nu revine la butonul Filtre la închidere; Escape nu închide panoul.
- **Soluție propusă:** un buton real în fiecare card sau rând extensibil, cu `aria-expanded` și legătură spre detalii, fără conflict cu linkurile din interior; antete sortabile accesibile din tastatură; panoul închis cu adevărat ascuns, focus mutat și restaurat, închidere cu Escape.
- **Criterii de acceptare:** totul se poate folosi doar din tastatură; focusul e vizibil; când panoul e închis, Tab nu ajunge în el.

#### 9. Stările de pe hartă diferențiate doar prin culoare

- **Statut:** risc de accesibilitate confirmat în cod; decizie de design încă necesară.
- **Fișier și funcții:** `index.html` – `drawParks()`, legenda.
- **Ce apare:** activat, neactivat, tentative și „în aer” au aceeași formă și diferă doar prin culoare; verde/roșu e perechea cea mai greu de distins la daltonism. Vechiul marcaj „cerc cu punct” oferea o diferență de formă, dar a fost înlocuit la cerere, pentru vizibilitate.
- **Soluție propusă:** un indiciu discret de formă doar pentru neactivate (de exemplu un punct alb mic în centru), păstrând culorile alese; de stabilit împreună cu Octavian.
- **Criterii de acceptare:** stările se disting într-un simulator de daltonism, inclusiv în zonele dense (Chișinău), fără a aglomera harta.

#### 10. Constatări din auditul propriu (15.10.2026)

*Site-ul publicat, verificat la 1366×900, 390 și 320 px, în RO și EN. Fără erori în consolă, fără derulare orizontală la 320 px pe nicio pagină, contrastul textelor măsurate de cel puțin 4,9:1, încărcare în aproximativ 1 s. Remedieri neimplementate.*

- **A. Detalii foarte lungi în clasament pe telefon** (observat; prioritate medie-mică). La ER1SKI, cele 62 de plăcuțe de parc ocupă aproximativ 1850 px, câte una pe rând, până la butonul „Statistici POTA globale”. *Fișier:* `index.html` – `detaliuActivator()`. *Propunere:* primele 12 plăcuțe și „Arată toate (62)”, sau două coloane pe telefon. *Acceptare:* butonul Global se vede fără derulare lungă; toate parcurile rămân accesibile.
- **B. Harta mică de pe telefon foarte densă** (observat; mică). La 320 px punctele din zona Chișinău se suprapun și nu se poate alege un parc fără zoom. *Fișier:* `index.html` – `drawParks()`, `renderMap()`. *Propunere:* puncte mai mici pe ecrane înguste sau grupare (*clustering*) la zoom mic. *Acceptare:* parcurile se pot deosebi și apăsa la zoom-ul inițial.
- **C. Harta fără etichetă și fără acces din tastatură** (confirmat în cod; mică). Niciunul dintre cele 232 de puncte nu primește focus, iar containerul hărții nu are etichetă pentru cititoarele de ecran. Lista de parcuri e o alternativă completă. *Fișier:* `index.html` – `newMap()`, `drawParks()`. *Propunere:* etichetă care descrie harta și trimite spre lista de parcuri. *Acceptare:* un cititor de ecran anunță harta și alternativa.
- **D. Lipsește linkul „Sari la conținut”** (confirmat în cod; mică). *Propunere:* un link ascuns care apare la primul Tab și duce la conținutul paginii curente. *Acceptare:* primul Tab îl arată, iar Enter mută focusul la conținut.
- **E. Fără JavaScript pagina e goală** (confirmat în cod; foarte mică). Toate textele vin din JavaScript și nu există un mesaj `<noscript>`. *Propunere:* un mesaj scurt în RO și EN care explică de ce e nevoie de JavaScript și trimite la pota.app.
- **F. Linkul `#harta/@INDICATIV` nu există** (idee rămasă nefăcută, nu defect). `#harta/@ER1PL` deschide harta fără indicativ completat. *Propunere:* dacă e util, linkul completează căsuța „Parcurile unui indicativ”, iar cartonașul Moldova poate avea „Vezi pe hartă”.
- **G. Eticheta „parcuri MD” sub cifra 1** în cartonașul Moldova (de evaluat). Ca etichetă sub o cifră e acceptabil; de decis dacă se adaptează la singular, la fel cu corectura de la punctul 5.

#### Observații fără defect demonstrat

- Pagina principală: harta ocupă mult din primul ecran pe mobil; e o alegere de prioritizare, de păstrat.
- Filtrele mobile la 0 rezultate: butonul „Arată 0 parcuri” e intenționat; contorul și „Resetează filtrele” permit recuperarea. O formulare mai explicativă e opțională.
- Netestate încă: contrastul tuturor textelor, zoom 200–400 %, cititor de ecran, telefon fizic (iOS/Android).

### Ordinea propusă și decizii încă necesare

1. **Ordinea după impact:**
   - date: 2 (date salvate, efect persistent) → 1 (afișare LIVE înșelătoare) → 3 (sesiunea curentă, se rezolvă cu reîncărcare);
   - interfață: 4 (fișa hărții) → 5 (plural) → 8 (tastatură) → 6 (numerele de loc) → 10A (detalii lungi pe telefon) → 7 (instrucțiunea mobilă) → 9 (culori) → 10B–E (densitate, etichete, skip link, noscript).
2. **Decizii încă necesare:**
   - pragul de vechime după care un spot nu mai e „în aer acum”;
   - frecvența reconcilierii și câte parcuri pe zi, în limita de cereri;
   - ce se întâmplă cu istoricul parcurilor retrase sau cu activitate zero (păstrat, ascuns sau exclus din statistici);
   - dacă un HTTP 404 la profil se memorează pe toată sesiunea;
   - semnificația numerelor de loc din clasament (recomandat: rang general, explicat);
   - indiciul de formă pentru markerele neactivate (de discutat cu Octavian).

---

*Proiect independent realizat de ER1PL. Nu este afiliat cu Parks on the Air®. Date: [pota.app](https://pota.app).*
