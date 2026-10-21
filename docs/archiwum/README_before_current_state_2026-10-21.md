> Kopia historyczna sprzed uporządkowania dokumentacji 21 października 2026. Opisy i wyniki odnoszą się do ówczesnego stanu.

# AI-SI-TSI — lokalny asystent TSI

**Stan: 21 października 2026.** Własny uczony rdzeń, macierze językowe, trwałe notatki i narzędzia do pracy z tekstem, dokumentami oraz matematyką. Nowa aplikacja zastępuje wcześniejszy AI-SI, zachowany lokalnie w archiwum.

Ta aktualizacja publikuje **samą dokumentację**. Kod nowego TSI, wagi, dane treningowe, dokumenty i prywatna historia pozostają lokalne. Starsze pliki obecne już w repo dotyczą wcześniejszego AI-SI i nie są instalatorem obecnej aplikacji.

## Aktualny rdzeń i trening językowy — 21 października 2026

Zainstalowany wspólny model **TSI-UNIFIED-H512-7573fd65**, runtime **0.6.0**, zawiera H512, transformer czytnika, matryce i połączenia w jednym module: **2 613 105 parametrów**, checkpoint **10 587 275 bajtów (10.59 MB)**. Sam wcześniejszy H512 ma 2 054 186 parametrów. Zakres integracji.

Osobno kontynuowano trening własnego generatora tekstu: **1 826 496 parametrów**, kontekst 512 tokenów; dodana uczona uwaga kopiująca ma **73 921 parametrów**. Dane: 1002 przykłady treningowe, 60 rozwojowych i 98 odłożonych. Pierwszy generator na odłożonych zadaniach uzyskał **0/68 pełnych poprawnych odpowiedzi na pytania o fakty i definicje**, natomiast poprawnie odmówił odpowiedzi przy braku informacji **25/25**. Kolejna warstwa kopiowania nadal gubi części faktów i myli źródła mimo spadku straty. **Kandydaci nie zastępują działającego rdzenia i nie są wdrożeni do rozmowy.** Wyniki treningu i dalsze kryteria.

**Dalszy wspólny trening:** generator i wybór źródła, 1 974 338 parametrów. Pełne odpowiedzi: 7/68 na wcześniejszych dodatnich zadaniach; na nowym teście fakty 4/16, definicje 0/16. Wybór źródła faktów 16/16, lecz pisanie nadal gubi treść i cytowanie. Kandydat niewdrożony. Wyniki i pomiar ograniczeń połączeń H512.

**Naprawa odczytu pamięci:** kolejne teksty rozmowy pozostają osobnymi aktywnymi źródłami; korekta i cofnięcie dotyczą wybranego źródła. Potwierdzono 13 kontroli oraz odczyt wcześniejszego tekstu w uruchomionym panelu. Nowy kandydat sieci z pełną treścią (4.96 mln parametrów) nie poprawił odpowiedzi i nie został wdrożony. Wyniki, przebieg pamięci i test pustych impulsów.

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

## Wspólny model H512 i czytnika 0.6 — stan aktualny

H512, transformer i matryce są zapisane w **jednym modelu i jednym pliku wag**. Uczone połączenia tworzą obieg czytnik → H512 → ocena odpowiedzi oraz przekazują reprezentacje H512 do czytnika. W tej wersji dotyczą jawnych relacji i dowodów; narzędzia oraz pamięć dokumentów nadal są osobnymi częściami aplikacji.

Zachowano wcześniejsze wyniki: **960/960, 720/720, 640/640**, odpowiedzi **140/140** poleceń językowych i **256/256** operacji wektorowych oraz **118/118** planów bez błędnych akceptacji. Obie wcześniejsze części zachowały wagi, a trening objął połączenia. Nie potwierdzono jeszcze poprawy swobodnego rozumienia języka.

Zakres integracji, trening i pomiary. Poprzedni stan.

## Jak korzystać

W lokalnej instalacji uruchom **URUCHOM_TSI.bat**; panel: `http://127.0.0.1:8791/`. **ZATRZYMAJ_TSI.bat** zatrzymuje aplikację. Enter wysyła, Shift+Enter dodaje wiersz. Pomoc i przykłady są dostępne w panelu, a przełącznik PL/EN wybiera język odpowiedzi.

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

Rozszerzono trening o logarytmy, odwrotności i pojedyncze piki. Nowy test pięciu etykiet na szerszych rodzinach: **95.32% micro-F1**, **1739/2000** pełnych zestawów; krzywe **1499/1500**. **Dostępny w panelu: „Sygnały ogólne — seria JSON”**, z opisem PL/EN i wykresem. W pomocy znajduje się gotowy przykład; potwierdzono 8 kontroli na działającym panelu. Zakres, błędy i porównanie zachowania wcześniejszych umiejętności.

## Podgląd

Aktualne zrzuty z 20 października 2026; rozmowa demonstracyjna bez prywatnych dokumentów.

(Zrzut historyczny: Wspólny panel rozmowy i wpisywania poleceń)

(Zrzut historyczny: Dokumenty i wklejanie materiału w bocznym panelu)

## Rozmiar, pojemność i sprzęt — pomiar 20 października

| Moduł | Parametry | Plik wag |
|---|---:|---:|
| Wspólny H512 + pamięć nazw + transformer + matryce + połączenia | 2 613 105 | 10.59 MB |
| W tym nowe uczone połączenia | 147 552 | w powyższym pliku |

Pomiar katalogu TSI sprzed tej konsolidacji: **432.31 MB** z kodem, danymi, kopiami i historią treningów. Nowe kopie bezpieczeństwa zwiększają tę wielkość; pełnego katalogu po wdrożeniu nie zmierzono ponownie. Python poza katalogiem nie jest wliczony. To rozmiar plików; RAM, VRAM i aktualna kompletna paczka portable nie zostały tu zmierzone. Liczba parametrów nie określa limitu notatek.

Wspólny czytnik dobiera urządzenie i wątki na podstawie wykrytych możliwości oraz pomiaru. Na tym komputerze działa na **CPU**: Intel HD Graphics nie jest udostępniona przez zainstalowany PyTorch CPU. Ścieżki CUDA/MPS wymagają zgodnego środowiska; fizycznego GPU nie testowano. Na tym komputerze wspólny model i solvery pracują na CPU. Panel walidatora ma jedno kontrolowane ponowienie po awarii procesu czytnika, z zachowaniem zapisanego postępu.

Dokładny zakres pomiaru, sprzęt i ponawianie. Wcześniejsze pomiary portable pozostają historyczne; nie wydano nowej paczki w tej partii.

- Poprzednie README i pełniejsza historia rozwoju.
- Wcześniejsza historia AI-SI.
- TSI-math-validator-5 — osobny warsztat matematyczny.
