# AI-SI-TSI — lokalny asystent TSI

**Stan: 24 października 2026.** TSI łączy własne modele uczone, macierze językowe, pamięć źródeł i narzędzia obliczeniowe. Pracuje lokalnie, bez wag Bielika i Qwena.

Repozytorium publikuje dokumentację. Aktualny kod TSI, wagi i dokumenty użytkownika pozostają lokalnie.

## Co obsługuje aplikacja

| Obszar | Możliwości |
|---|---|
| Tekst | Odczyt podanej treści, pytania do źródła, skróty, listy, przygotowanie wiadomości i obsługiwane korekty tekstu |
| Dokumenty | Wklejanie treści oraz TXT, MD, CSV, PDF, DOCX i DOC; do 10 plików, 8 MB na plik i 32 MB łącznie; DOC korzysta z Worda, skany wymagają OCR |
| Słownik offline | 114 215 haseł, 125 720 wpisów i 1 437 842 powiązania form odmiany; znaczenia, przykłady i źródła |
| Pamięć | Notatki, historia rozmów, źródła, poprawki, cofanie zmian i eksport JSON |
| Matematyka | Obsługiwane działania, równania, pochodne, całki, macierze i wykresy przez narzędzia obliczeniowe |
| Logika formalna | Dziewięć bramek T/F/U, nawiasy, symbole i kroki; odczyt formalnego wyrażenia wydzielonego w opisie PL/EN |
| Sygnały | Serie liczbowe JSON, wykresy i uczona ocena wybranych trendów, anomalii i okresowości |
| Obsługa | Interfejs PL/EN, Enter wysyła, Shift+Enter dodaje wiersz, nowa rozmowa, pomoc i przykłady |

Rozpoznawanie swobodnych poleceń pozostaje ograniczone. Panel oraz integracje aplikacyjne zachowują dotychczasowe wdrożone wagi. Poniższa ocena dotyczy rozwijanego wspólnego modelu językowego.

## Rozmowa i składnia — aktualizacja 24 października

Lokalny panel obsługuje teraz także zweryfikowane zdania wieloczłonowe: odczyt całej treści, spójniki, negację i kierunek przyczyny. Poprawiono rozpoznawanie końców zdań przy skrótach i liczbach. Kontrole: **15/15** zdań, **116/116** wcześniejszych przypisań ról, **4/4** generowania złożonych odpowiedzi ze źródła oraz **3/3** przez API.

Swobodny generator rozmowy **nie osiągnął wymaganego poziomu**. Osobny wariant połączono z pamięcią i macierzą, ale pierwsza próba nadal dawała uszkodzone wypowiedzi. Zrównoważony trening: **67 aktualizacji**, zachowanie **47/48** wcześniejszych odpowiedzi. W ręcznej ocenie pełnych odpowiedzi: **0/2 powtórek** i **1/4 nowych wypowiedzi**; poprawna odpowiedź czasowa wymagała kontroli macierzowej podczas ponownego generowania. Nowych wag nie ustawiono jako domyślnych.

[Wdrożony zakres, ograniczenia, trening i wyniki](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/ROZMOWA_I_SKLADNIA_TSI_2026-10-24.md).

## TIMDR — aktywna kontrola języka

TSI wykorzystuje macierze znaczenia do kontrolowania propozycji uczonego generatora fraz. W badanym dużym modelu macierz steruje także dopuszczalnymi kontynuacjami podczas generowania. Dodano śledzenie stanów i zmian, ról, negacji, czasu oraz struktury wypowiedzi.

Z poprawnie dostarczoną macierzą zdarzeń nowe zadania czasowe: **0/16 → 16/16**; wybrane wcześniejsze: **3/4 → 4/4**. Próby dynamiki, ról i negacji: **6/6**. To wyniki systemu z kontrolą macierzową; wag swobodnego modelu nie zmieniano. Odrębna poprawka polskiego czytnika podniosła wcześniejszą próbę semantyczną do 7/7 w kontekście źródła; dowolny tekst nadal nie jest w pełni obsługiwany. [Wdrożenie i dokładny zakres wyników](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/TIMDR_JEZYK_TSI_2026-10-24.md).

## Połączenie logiki — aktualizacja 24 października

Lokalny panel przekazuje teraz także formalne wyrażenie wydzielone w dłuższym poleceniu do wyuczonej macierzy logiki. **69/69** przypadków dziewięciu bramek; z opisami i błędną poprzednią odpowiedzią **138/138**, wyrażenia złożone **148/148**, panel przez HTTP **6/6**. Pozostałe sprawdzone odpowiedzi: **105/105 identycznych**.

To wynik aplikacji z modułem logiki. Sam najnowszy dekoder językowy nadal ma **49/69**. Wspólna paczka badawcza z macierzą: **23 019 006 parametrów**, **92.57 MB**, bez optymalizatora. Przyjętych wag językowych i portable nie zmieniono. [Zakres i wyniki](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/POLACZENIE_LOGIKI_TSI_2026-10-24.md).

## Aktualna ocena modelu językowego

**Nie osiągnął wymaganego poziomu.**

Przyjęto zapis po kontroli wcześniejszych odpowiedzi. Jest używany jako punkt wyjścia dalszych testów; nie zastąpił modelu rozmowy w panelu.

| Sprawdzian | Wynik |
|---|---:|
| Wcześniejsze odpowiedzi o faktach i języku — chroniony zestaw powtórek | **48/48**, zachowane |
| Odczyt i weryfikacja podanej tablicy logiki trójstanowej | **47/69**, wcześniej 38/69 |
| Poprawne przypadki logiki z poprzedniego etapu | **46/46**, zachowane |
| Opisy zmiany godziny ocenione przed obecną serią powtórek | **3/16** |
| Dodatkowy zestaw nowych opisów i pytań o czas, bez treningu na tych sformułowaniach | **0/16** |

W teście 69 przypadków poprawna tablica reguł trafia jako treść źródła do enkoderów, a odpowiedź generuje sieć. Wyniki nie są podmieniane odpowiedzią nauczyciela. To ocena czytania źródła, odrębna od formalnego modułu logiki w aplikacji.

Rozbicie wyniku według oczekiwanej wartości: **T 21/23**, **F 0/19**, **U 26/27**. Rozpoznawanie fałszu i nowych parafraz pozostaje głównym brakiem. Wynik 48/48 mierzy zachowanie znanego zestawu, a 3/16 pokazuje ograniczone przenoszenie umiejętności na nowe opisy.

Najnowsza wspólna pętla internetowa została zatrzymana po regresji; jej wagi odrzucono. Bieżące korekty odbywają się na kontrolowanych przykładach. Zwykła rozmowa nie uruchamia treningu wag.

[Najnowsza kontrola treningu i zapominania](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/UTRWALANIE_TSI_2026-10-24.md). [Zakres oceny i decyzja o wagach](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/OCENA_TSI_2026-10-23.md). [Przebieg prac i wcześniejsze wyniki](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/HISTORIA_TSI.md).

## Model i rozmiar

Ostatni zakończony trening: **67 aktualizacji — 24 października**, **47/48** zachowanych wcześniejszych odpowiedzi. Przyjęte wagi pozostają bez zmian. [Bieżąca ocena](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/ROZMOWA_I_SKLADNIA_TSI_2026-10-24.md). Wcześniejsze pomiary utrwalania znajdują się w historii.

Rozwijany wariant zawiera **dwa enkodery z H512 i macierzami językowymi oraz własny dekoder transformera z uwagą krzyżową**. Wspólny zapis obejmuje enkodery i dekoder. Dekoder ma 12 warstw, 4 głowy uwagi, szerokość 256 i kontekst 384 tokenów łącznie z poleceniem i odpowiedzią.

Pomiar z **23 października 2026**; MB = 1 000 000 bajtów. Wiersze opisują różne zakresy i nie stanowią rozmiaru gotowej paczki portable.

| Zakres | Parametry lub rozmiar |
|---|---:|
| Dwa enkodery | **10 147 343 parametry** |
| Dekoder z uwagą krzyżową | **12 871 180 parametrów** |
| Wspólny model | **23 018 523 parametrów** |
| Same parametry modelu w FP32 | **92,07 MB** |
| Zapis przyjętych wag bez stanu optymalizatora | **92,52 MB** |
| Lokalny katalog aplikacji z kodem, danymi, modułami i artefaktami; bez treningów, kopii, osobnego runtime i testów | **1 989,89 MB** |

Osobne środowisko Pythona nie jest wliczone w pomiar katalogu aplikacji. Nowy model badany jest przechowywany osobno; nie włączono go do nowej paczki portable. [Dokładne zakresy pomiaru](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/POMIAR_TSI_2026-10-23.json).

## Jak korzystać z lokalnej instalacji

Uruchom **URUCHOM_TSI.bat**. Domyślny adres panelu to `127.0.0.1:8791`. **ZATRZYMAJ_TSI.bat** zatrzymuje aplikację. Repozytorium dokumentacyjne nie zawiera instalatora obecnych wag.

| Przykład polecenia | Zastosowanie |
|---|---|
| `Przeczytaj: Anna daje książkę Markowi.` | Dodanie źródła |
| `Komu Anna daje książkę?` | Pytanie do podanego materiału |
| `słownik: państwo` | Znaczenia ze słownika offline |
| `Wyznacz pochodną i całkę: x^2` | Narzędzia matematyczne |
| `logika: NOT (T AND U) OR F` | Formalne obliczenie z krokami |
| `zapamiętaj: termin = piątek` | Trwała notatka |

## Podgląd panelu

Zrzuty z 20 października przedstawiają panel aplikacji i przykładowe dane. Układ panelu jest niezależny od opisanej oceny nowych wag.

![Rozmowa i polecenia TSI](https://raw.githubusercontent.com/jbackk-lang/AI-SI-TSI/main/docs/tsi-panel-2026-10-20.png)

![Dokumenty i wklejanie treści](https://raw.githubusercontent.com/jbackk-lang/AI-SI-TSI/main/docs/tsi-documents-2026-10-20.png)

[Historia](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/HISTORIA_TSI.md) · [Słownik: Kaikki/Wiktextract](https://kaikki.org/dictionary/rawdata.html) · [TSI-math-validator-5](https://github.com/jbackk-lang/TSI-math-validator-5)
