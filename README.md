# AI-SI

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23222487.svg)](https://doi.org/10.5281/zenodo.23222487)

Eksperymentalny system inspirowany TIMDR jako punktem wyjścia do budowy sterownika współpracy.

## Aktualny stan — 7 października 2026

Własny mały model językowy SI działa bez Qwena, z kontrolą źródeł, mostem sesji, wyborem strategii i ograniczoną obsługą polskiego; wagi języka trenujemy po angielsku. Zadania słowne są sprawdzane na prawdziwych zadaniach z otwartych zbiorów, a polskie pytania obsługuje maper z katalogiem sprawdzonych zdań.

## Najnowsza aktualizacja — 7 października 2026

- **Most WordNet:** nieznany czasownik w zadaniu słownym jest zamieniany na znany czasownik SI tej samej operacji przez otwarty angielski WordNet, tylko gdy wszystkie znaczenia słowa są zgodne. Nowy test zamrożony przed pracą 208→286/300; 0 błędnych potwierdzeń.
- **Most pytań:** nieznane sformułowanie pytania zamieniane na znane pytanie tej samej klasy. Nowy zamrożony test 247→272/300.
- **Sprawdzian na prawdziwych zadaniach:** na 1730 zadaniach z otwartych zbiorów SVAMP/ASDiv parser trafiał tylko 10%, czyli prawie jak losowanie; mosty działały tylko w świecie własnych szablonów (wynik negatywny).
- **Nowe podejście:** liniowy klasyfikator działania uczony na otwartym MAWPS, wskazówki ról liczb (wynik, stan początkowy, porównanie, grupy) i czytnik kontekstu czytający zadanie słowo po słowie, połączony z modelem ról. Połowa testu nieużywana do strojenia 451→512; w SI prawdziwe zadania 178→944/1730. Odpowiedzi nowego modelu zawsze wymagają potwierdzenia; 0 błędnych potwierdzeń.
- **Polski maper pytań:** katalog sprawdzonych zdań (wzór nauczyciela z 4 października) i czytnik kontekstu po formach SJP.PL. Zamrożony test 44→64/72; „nie rozpoznaję” 21→5, błędne intencje 7→3.
- **Lokalny tłumacz PL→EN:** neuronowy Opus-MT (218 MB, ok. 0,1–0,4 s na zdanie) przed angielskim rdzeniem SI. SI sprawdza, czy liczby i przeczenia przeszły bez zmian. Polskie zadania słowne 24→51/150.
- **Tabele, dokumenty, daty:** nowe moduły liczą na tabelach i arkuszach (CSV, XLSX), odpowiadają na pytania do własnych dokumentów (TXT, MD, DOCX, PDF) z cytatem zdania źródłowego oraz liczą daty i terminy. Każdy wynik jest sprawdzany drugim, niezależnym obliczeniem albo pełnym dopasowaniem pytania do zdania; testy zamrożone przed pisaniem kodu: tabele 15/15, dokumenty 15/16, daty 9/11 (pozostałe poprawnie niepotwierdzone); 0 błędnych potwierdzeń.
- **Nauka z Wikipedii:** SI czyta losowe artykuły angielskiej Wikipedii i sama wybiera, czego się uczy: rodzaj faktu, na którym najwięcej traci, i rodzaj haseł, z których najwięcej się uczy. Wikidata służy tylko jako niezależny sędzia; SI nie zapamiętuje faktów, uczy się czytać — mostów słów („birth” = „born”) i wzorców otoczenia wartości („( [DATA] –” = data urodzenia, „– [DATA]” = data śmierci). Podmiana tylko po poprawie na 120 zamrożonych hasłach: trafione 0 → 64 z 215 pytań, 0 błędów czytania. Podgląd na żywo z przyciskiem zatrzymania.
- **Pętla samouczenia:** koordynator nauki dla modułów z automatem rośnięcia pojemności, okienkiem podglądu i podmianą wag tylko po poprawie, z kopią zapasową.
- **Wyniki negatywne:**
  - dane pisane przez Qwena od zera i z przepisania zadań MAWPS nie poprawiły wyniku na straży;
  - więcej neuronów przy cechach bez kolejności słów nie pomogło;
  - kalibracja bezpiecznego potwierdzania nie dała zera błędów (ok. 10%).

[Dokładne wyniki, metody i ograniczenia — 6–7 października](docs/SI_NAUKA_2026-10-06.md). Testy użyte do wyboru wersji są odtąd rozwojowe. [Aktualizacja z 6 października](README_DETAILS.md#aktualizacja--6-października-2026-cały-dzień) jest w historii.

## Osiągnięcia

SI to mały, lokalny system: kilka własnych sieci po kilkaset tysięcy parametrów oraz dokładne narzędzia. Mówi, gdy czegoś nie jest pewne.

| Obszar | Co potrafi | Wynik na zamrożonym teście |
|---|---|---|
| **Kontrola odpowiedzi** | Trzy stany: potwierdzone / odrzucone / do potwierdzenia. Niepewne odpowiedzi nie są podawane jako fakt | 0 błędnych potwierdzeń w zadaniach słownych, także na 1730 prawdziwych zadaniach |
| **Odpowiedzi ze źródła** | Odczytuje wartości z podanego tekstu, w tym przy mieszanych wzorcach zdań | 96/96 z kontrolerem |
| **Zadania słowne (angielski)** | Proste zadania jednodziałaniowe: rozpoznaje działanie, liczy dokładnym kalkulatorem | Prawdziwe zadania SVAMP/ASDiv: 944/1730 (55%), zawsze z prośbą o potwierdzenie; znane wzory 297/300 |
| **Polskie pytania o SI** | Rozumie różne sformułowania pytań o pamięć, kalkulator, kod, walidację, kolejność kroków i o siebie | 64/72 (wcześniej 44/72) |
| **Polski interfejs** | Translator obsługiwanych formatów zachowuje zakazy, liczby i warunki; lokalny tłumacz neuronowy PL→EN pod kontrolą SI; polskie zadania słowne z prośbą o potwierdzenie | 10/10 i 5/5; polskie zadania słowne 51/150 |
| **Zakazy i brak danych** | „Nie wykonuj” zatrzymuje działanie; przy braku liczby SI prosi o nią | 10/10 (blokada języka), 5/5 (pętla decyzji) |
| **Strategie i most sesji** | Mała sieć wybiera zachowanie odpowiedzi; wspólny dziennik sesji | 240/240 na stanach walidatora; próba 7/16 → 14/16 |
| **Tabele i arkusze** | CSV i XLSX: suma, średnia, największa, najmniejsza, liczba wierszy; filtry („gdzie Region = North”, „w Krakowie”, „w kwietniu”), grupowanie „według kategorii”, kolumny dat; liczenie dokładne i sprawdzane drugim obliczeniem; nieużyte słowo polecenia → prośba o potwierdzenie | 15/15 |
| **Pytania do dokumentów** | TXT, MD, DOCX, PDF, plik lub folder: odpowiedź wycięta z dokumentu z cytatem (plik, akapit, zdanie); czego nie ma w dokumencie — mówi, że nie ma; kilka pasujących miejsc — pokazuje wszystkie | 15/16, brak informacji poprawnie rozpoznany |
| **Daty i terminy** | Różnica dni, data po N dniach/miesiącach/latach, dzień tygodnia, koniec miesiąca wg k.c., termin w weekend; nieistniejąca data odrzucona | 9/11, pozostałe 2 poprawnie niepotwierdzone |
| **Nauka z Wikipedii** | Sama wybiera, czego się uczy; uczy się czytać artykuły (mosty słów, wzorce otoczenia dat), sędzią jest Wikidata, niezgodności źródeł liczone osobno; przycisk „Zatrzymaj naukę” | 120 zamrożonych haseł: 0 → 64/215 trafionych, 0 błędów czytania |
| **Słownik** | Lokalna baza SJP.PL (4,69 mln par forma–lemma) jako pierwsze źródło odmian | — |
| **Samouczenie** | Koordynator nauki: przykłady od nauczyciela → sito → automat rośnięcia pojemności → podmiana wag tylko po poprawie | Pierwsze rundy bez podmiany (zabezpieczenie zadziałało) |

Każdy wynik dotyczy opisanego testu.

[Dokładne wyniki, rozmiary i ograniczenia — 6 października](docs/SI_AKTUALIZACJA_2026-10-06.md) · [Historia i wcześniejsze konfiguracje](README_DETAILS.md).

Aktywne wagi SI: około **6,06 MB** (stan rano 6 października; nowe moduły z 6 października dodają ok. **5 MB**, 1,25 mln parametrów, a z 7 października ok. **2,5 MB**: czytniki kontekstu, klasyfikator działania, mosty i polski maper), sterownik strategii: **4,5 KB**, lokalny indeks słownika: **154,55 MB**; to nie rozmiar kompletnego pakietu z bibliotekami.

## Cytowanie

Wydanie zarchiwizowane w Zenodo: **DOI [10.5281/zenodo.23222487](https://doi.org/10.5281/zenodo.23222487)**.

```
Kielich, J. AI-SI. Zenodo. https://doi.org/10.5281/zenodo.23222487
```

## Zakres publicznego repo

Publiczne repo zawiera interfejs, integrację, narzędzia treningowe, testy i dokumentację. **Rdzeń SI/TIMDR, prywatny silnik, wagi, checkpointy i pamięć pozostają prywatne.** Samo pobranie repo nie udostępnia całego silnika. [Zakres publikacji](docs/PUBLIC_SCOPE.md).

## Uruchomienie

Uruchom posiadany prywatny silnik zgodnie z jego instrukcją, następnie klienta przez Uruchom_AI_SI.bat albo python run_ui.py i wskaż backend. Bez silnika klient zgłosi brak połączenia.

Wyniki pochodzą z ograniczonych prób rozwojowych; nie sumujemy ich jako niezależnego benchmarku i nie przedstawiamy jako dowodu ogólnego rozumienia języka.
