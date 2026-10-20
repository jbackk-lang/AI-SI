# TSI — lokalny asystent modułowy

**Stan: 20 października 2026.** Własny uczony rdzeń, macierze językowe, trwałe notatki i narzędzia do pracy z tekstem, dokumentami oraz matematyką. Nowa aplikacja zastępuje wcześniejszy AI-SI, zachowany lokalnie w archiwum.

Ta aktualizacja publikuje **samą dokumentację**. Kod nowego TSI, wagi, dane treningowe, dokumenty i prywatna historia pozostają lokalne. Starsze pliki obecne już w repo dotyczą wcześniejszego AI-SI i nie są instalatorem obecnej aplikacji.

## Co działa

| Obszar | Dostępne możliwości |
|---|---|
| Tekst i rozmowa | Czytanie podanego materiału, pytania z cytatem, przygotowanie wiadomości z treści użytkownika, skróty i listy |
| Poprawki | Zamiana wskazanego fragmentu źródła, cofnięcie zmiany, wersjonowanie i nowy temat |
| Dokumenty | TXT, MD, CSV, PDF, DOCX i DOC; pliki lub wklejenie całej treści; do 10 plików, 8 MB na plik i 32 MB łącznie; DOC wymaga Worda, skany wcześniejszego OCR |
| Pamięć | Wspólny kontekst źródeł z pochodzeniem i wersjami, trwałe notatki, historia oraz eksport JSON |
| Matematyka | Arytmetyka słowna w obsługiwanym zakresie, kalkulator naukowy, równania, pochodne, całki, macierze i wykresy |
| Logika i język | Logika trójstanowa, analiza odmiany i ról, kontrola wybranych reguł zapisu oraz ograniczony czytnik PL/EN |
| Audyt odpowiedzi | Przycisk lub rozpoznana prośba o sprawdzenie poprzedniej odpowiedzi; ponowienie obsługiwanych obliczeń i kontrola cytatu w zapisanej wersji źródła |
| Inne narzędzia | Daty, lokalne pliki udostępnione do odczytu, wybrane strony HTTPS i katalog sprawdzonych przykładów programistycznych |

Główny rdzeń H512 ma **2 054 186 parametrów**. Współpracuje z dodatkowymi uczonymi modułami i narzędziami. Aplikacja nie korzysta z Bielika ani Qwena. Notatki i zwykła rozmowa nie uruchamiają samoczynnego treningu wag.

## Czytnik i wykonywanie zadań — aktualizacja 20 października

Czytnik otrzymał matrycę wejściową pojęć i ról oraz matrycę wyjściową celów, wymaganych danych i zależności kroków. W obsługiwanym zakresie buduje plan, uruchamia odpowiednie narzędzia i sprawdza wyniki kroków. Współpracuje z dotychczasowym H512 oraz uczonym transformerem relacji; nie zastępuje ich.

- Kontrola przepływu: **32/32**, w tym **24/24 zadania akademickie**; testy modułu: **48/48**, kontrola wdrożenia: **12/12**.
- To wyniki określonych przypadków regresji, a nie miara rozumienia dowolnego polecenia. Matryca słownika obejmuje 1596 form w 18 kategoriach pojęć.
- Przykład: `Wyznacz pochodną i całkę: x^2` daje dwa obliczenia. `Odwróć macierz i sprawdź mnożeniem: [[2,1],[1,1]]` tworzy zależne kroki.
- Integracja nadal wymaga poprawek: ponowny audyt poprzedniej odpowiedzi w rozmowie nie zachowuje jeszcze pełnego śladu planu; dodatkowej kontroli wymagają negacje, warunki i wiązanie złożonych celów. Brakujące dane wymagają doprecyzowania.

Rozmowa i pole wpisywania znajdują się w jednym panelu. Dane i szczegóły są poniżej; wybór działu i dokumenty umieszczono z boku. [Historia poprzedniego stanu](docs/archiwum/README_2026-10-19.md).

## Jak korzystać

W lokalnej instalacji uruchom **URUCHOM_TSI.bat**; panel: **http://127.0.0.1:8791/**. **ZATRZYMAJ_TSI.bat** zatrzymuje aplikację. Enter wysyła, Shift+Enter dodaje wiersz. Pomoc i przykłady są dostępne w panelu, a przełącznik PL/EN wybiera język odpowiedzi.

| Przykład | Zastosowanie |
|---|---|
| `Przeczytaj: Anna daje książkę Markowi.` | Wczytanie źródła |
| `Komu Anna daje książkę?` | Pytanie o rolę w tekście |
| `Zamień Markowi na Ewie` | Poprawka źródła; `Cofnij` przywraca poprzednią wersję |
| `Dodaj 3 plus siedem` | Obliczenie w obsługiwanym zakresie |
| `2/7` | Rachunek z zachowaniem wyniku dokładnego |
| `Sprawdź swoją poprzednią odpowiedź.` | Rozpoznana prośba o audyt; dostępny jest też przycisk |
| `zapamiętaj: termin = piątek` | Trwała notatka |
| `nowy temat` | Wyczyszczenie aktywnego kontekstu bez kasowania trwałych notatek |

Zgodny rachunek nie potwierdza dowolnej interpretacji polecenia. Kontrola cytatu potwierdza jego obecność w źródle; gdy dostępne kontrole nie wystarczają, odpowiedź pozostaje nierozstrzygnięta. Swobodne opowiadania i szeroka rozmowa nadal wymagają rozwoju.

## Analiza sygnałów — w treningu

Rozszerzono trening o logarytmy, odwrotności i pojedyncze piki. Nowy test pięciu etykiet na szerszych rodzinach: **95.32% micro-F1**, **1739/2000** pełnych zestawów; krzywe **1499/1500**. **Dostępny w panelu: „Sygnały ogólne — seria JSON”**, z opisem PL/EN i wykresem. W pomocy znajduje się gotowy przykład; potwierdzono 8 kontroli na działającym panelu. [Zakres, błędy i porównanie zachowania wcześniejszych umiejętności](docs/SIGNALS_2026-10-19.md).

## Podgląd

Aktualne zrzuty z 20 października 2026; rozmowa demonstracyjna bez prywatnych dokumentów.

![Wspólny panel rozmowy i wpisywania poleceń](docs/tsi-panel-2026-10-20.png)

![Dokumenty i wklejanie materiału w bocznym panelu](docs/tsi-documents-2026-10-20.png)

## Rozmiar i historia

Pomiar lokalnego katalogu aplikacji przed kolejną partią treningu (19 października): **317,89 MB**, w tym około **62,08 MB** kodu, modułów, modeli, słownika i panelu. Pozostała część obejmuje m.in. lokalne eksperymenty, kopie i historię. To rozmiar plików, nie RAM ani rozmiar paczki portable. [Pomiar z 19 października i zakres](docs/SIZE_2026-10-19.md).

Pełny portable ogólnego TSI z Pythonem i współdzielonym silnikiem nie został w tej partii wydany. [Historyczny pomiar kompletnego wariantu z kodem z 18 października](docs/PORTABLE_SIZE_2026-10-18.md): 3890,86 MB przed kompresją.

- [Poprzednie README i pełniejsza historia rozwoju](docs/archiwum/README_2026-10-18.md).
- [Wcześniejsza historia AI-SI](HISTORIA_SI_2026-10-11.md).
- [TSI-math-validator-5 — osobny warsztat matematyczny](https://github.com/jbackk-lang/TSI-math-validator-5).
