# AI-SI-TSI — lokalny asystent TSI

**Stan: 22 października 2026.** TSI łączy własne uczone modele, macierze językowe, pamięć źródeł i narzędzia obliczeniowe. Pracuje lokalnie, bez wag Bielika i Qwena. Internet służy do pobierania materiału z wybranych źródeł.

To repozytorium dokumentacyjne. Obecny kod, wagi, dane treningowe i dokumenty użytkownika pozostają lokalnie. **W panelu działa dotychczasowy model; nowszy wariant dwupołówkowy i uczona warstwa wypowiedzi są rozwijane osobno.**

## Co umie działająca aplikacja

| Obszar | Aktualne możliwości |
|---|---|
| Tekst i dokumenty | Wczytywanie treści, pytania do źródła, skróty, listy i przygotowanie wiadomości z podanego materiału; rozpoznawany zakres poleceń pozostaje ograniczony |
| Pliki | TXT, MD, CSV, PDF, DOCX, DOC i wklejanie treści; do 10 plików, 8 MB na plik i 32 MB łącznie; DOC wymaga Worda, skany wcześniejszego OCR |
| Słownik offline | **114 215 różnych haseł**, 125 720 wpisów i 1 437 842 powiązania form odmiany; znaczenia, przykłady i źródła z polskiego Wikisłownika przez Kaikki |
| Odczyt definicji | Wskazywanie jawnej cechy, uczestników relacji, przeznaczenia, składu lub warunku w rozpoznanej konstrukcji; pytanie o doprecyzowanie przy braku jednoznacznego fragmentu |
| Źródła internetowe | Wyszukiwanie i odczyt Wikipedii, zachowanie źródła oraz wykorzystanie jego treści w obsługiwanym kontekście |
| Pamięć | Trwałe notatki, historia rozmów, wersjonowanie źródeł, poprawki, cofanie zmian i eksport JSON |
| Matematyka | Obsługiwane działania, kalkulator naukowy, równania, pochodne, całki, macierze i wykresy przez narzędzia obliczeniowe |
| Logika T/F/U | Uczony moduł operatorów AND, OR, NOT, IMPLIES i EQUIV, parser nawiasów i kroki rozwiązania formalnego wyrażenia |
| Sygnały | Serie liczbowe JSON, wykres oraz uczona ocena wybranych trendów, anomalii i okresowości |
| Obsługa | Panel PL/EN, Enter wysyła, Shift+Enter dodaje wiersz, nowa rozmowa, pomoc i przykłady |

## Lokalna nauka z internetu

Nowa pętla pobiera materiał z **polskiej Wikipedii** i ćwiczy odczyt podanej treści. Zachowuje adres artykułu, rewizję, tekst oraz SHA-256. Odpowiedzi uczące pochodzą dosłownie z pobranego fragmentu. Materiał strony jest danymi, a nie poleceniem do wykonania.

| Uruchomienie w lokalnej instalacji | Działanie |
|---|---|
| **PANEL_NAUKI_TSI.bat** | Checkbox internetu i tematów, dodawanie tematu lub linku Wikipedii, limit rund i czasu, Start/Stop oraz odpowiedzi TSI |
| **NAUKA_TSI_Z_INTERNETU.bat** | Bezpośrednia pętla nauki w kolorowym oknie; domyślnie do 20 rund lub około 2 godzin |
| **COFNIJ_NAUKE_TSI_O_2.bat** | Cofnięcie o dwie zaakceptowane zapisane wersje, wraz z pamięcią; dostępne także w panelu |
| **ZATRZYMAJ_NAUKE_TSI.bat** | Zatrzymanie po bezpiecznym etapie z zachowaniem wcześniejszych zaakceptowanych wag |

- **Zielony: POLEPSZENIE** — mniejszy błąd wygenerowanych odpowiedzi uczących, zapis wag.
- **Żółty: POWTÓRKI / BEZ ZMIANY** — utrwalanie materiału lub brak postępu.
- **Czerwony: POGORSZENIE — COFNIĘTO** — przywrócenie wag i stanu optymalizatora.
- **„Nauczyłem się…”** — pytanie i rzeczywista odpowiedź z nowo opanowanego przykładu, wyłącznie po zaakceptowanej rundzie. Przy braku takiego wyniku pojawia się „Jeszcze ćwiczę…” albo zachowana odpowiedź.

Odznaczenie źródła wyłącza nową naukę z niego; poznana pamięć jest nadal utrwalana. Przy utracie opanowanej odpowiedzi wykonywane są powtórki naprawcze. Wagi obu dotychczasowych rdzeni pozostają zamrożone, a nauka zmienia dołączoną warstwę wypowiedzi. **Nowe wagi nie są automatycznie podmieniane w panelu.** Zwykła rozmowa sama nie uruchamia treningu.

## Aktualny wynik rozwoju rozmowy

Ostatnia zachowana wersja po kontroli zapominania: **10/30 pełnych odpowiedzi na ćwiczonych rozmowach**; punkt wyjścia wynosił 4/30. Wariant z 11/30 utracił jedną wcześniej opanowaną wypowiedź, więc wrócono do wcześniejszej migawki i przeprowadzono powtórki. Kolejna seria zachowała 10/30 bez ponownej utraty chronionej rozmowy. Te wagi i pamięć przekazano lokalnej pętli BAT. To wynik materiału uczącego, a nie sprawdzian nieznanych pytań.

Potwierdzono uruchomienie panelu nauki, pobranie rzeczywistego artykułu i pełną rundę w oddzielnej kopii: pobranie, trening, wykrycie gorszego wyniku i cofnięcie zmiany. Osobno sprawdzono, że komunikat „Nauczyłem się” nie przypisuje sukcesu odrzuconej aktualizacji.

Swobodna rozmowa, rozumienie dowolnej parafrazy i samodzielne opanowywanie dowolnej wiedzy nie są jeszcze osiągnięte. Model nadal potrafi mieszać zapamiętane wypowiedzi lub odpowiadać na inny temat. Dlatego **pozostawiono dotychczasowy model w panelu**. Szczegóły prób i wcześniejsze wyniki są w [historii](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/HISTORIA_TSI.md).

## Ile zajmuje

Pomiar plików z 22 października 2026. MB = 1 000 000 B; to rozmiar na dysku, nie zużycie RAM. Wiersze częściowo zawierają się w sobie — nie należy sumować całej tabeli.

| Składnik | Rozmiar |
|---|---:|
| Aplikacja TSI z kodem, modelami, modułami i danymi; bez treningów, kopii, runtime i testów | **254,44 MB** |
| Cały roboczy katalog TSI, także treningi, archiwa i runtime | **1618,18 MB** |
| Lokalna baza słownikowa, zawarta w aplikacji | **157,72 MB / 150,4 MiB** |
| Dwupołówkowy model bazowy: 10 147 343 parametry | **40,94 MB wag** |
| Nowa uczona warstwa wypowiedzi: 1 285 376 parametrów | **5,15 MB wag** |
| Pakiet pętli internetowej z kodem i początkowymi wagami, zawarty w treningach | **46,84 MB**, bez Pythona |

Model bazowy i nowa warstwa mają łącznie **11 432 719 parametrów**. W obecnej pętli trenuje się 1 285 376 parametrów warstwy wypowiedzi; pozostałe są zachowane.

Pełny konserwatywny budżet z kodem, archiwami, współdzielonym silnikiem, aktualnymi bibliotekami i bazowym Pythonem wynosi **5466,69 MB przed kompresją**. Nie jest to gotowy ani przetestowany portable. [Zakres i składniki pomiaru](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/SIZE_2026-10-22.md).

Obecny komputer używa **CPU i PyTorch 2.14.0+cpu**, z grafiką Intel HD; CUDA jest niedostępna. Pętla nauki domyślnie korzysta z dwóch wątków CPU.

## Jak korzystać z asystenta

Uruchom **URUCHOM_TSI.bat**; panel działa pod `http://127.0.0.1:8791/`. **ZATRZYMAJ_TSI.bat** zatrzymuje aplikację. Pliki BAT opisane tutaj należą do istniejącej instalacji lokalnej; to repozytorium nie jest instalatorem obecnego TSI.

| Polecenie | Zastosowanie |
|---|---|
| `Przeczytaj: Anna daje książkę Markowi.` | Dodanie źródła |
| `Komu Anna daje książkę?` | Pytanie do materiału |
| `słownik: państwo` | Odczyt znaczeń offline |
| `Zamień Markowi na Ewie` / `Cofnij` | Korekta i cofnięcie |
| `Wyznacz pochodną i całkę: x^2` | Narzędzia matematyczne |
| `logika: NOT (T AND U) OR F` | Logika trójstanowa; wynik U z krokami |
| `zapamiętaj: termin = piątek` | Trwała notatka |
| `nowy temat` | Nowy kontekst |

## Podgląd panelu

Zrzuty z 20 października przedstawiają działający panel asystenta i przykładowe dane. Nie przedstawiają nowego panelu treningu ani podmiany modelu.

![Rozmowa i polecenia TSI](https://raw.githubusercontent.com/jbackk-lang/AI-SI-TSI/main/docs/tsi-panel-2026-10-20.png)

![Dokumenty i wklejanie treści](https://raw.githubusercontent.com/jbackk-lang/AI-SI-TSI/main/docs/tsi-documents-2026-10-20.png)

Historia prac: [HISTORIA_TSI.md](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/HISTORIA_TSI.md). Źródło słownika: [Kaikki/Wiktextract](https://kaikki.org/dictionary/rawdata.html). Powiązany projekt: [TSI-math-validator-5](https://github.com/jbackk-lang/TSI-math-validator-5).
