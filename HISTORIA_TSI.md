# Historia rozwoju AI-SI-TSI

Ten plik przechowuje przebieg prac i wcześniejsze pomiary. Aktualne możliwości oraz ograniczenia są opisane w [README](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/README.md). Wyników odmiennych zestawów i modeli nie należy dodawać ani porównywać jak jednego sprawdzianu.

## Stan sprzed uporządkowania dokumentacji

- [Poprzedni lokalny README — 21 października 2026](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/archiwum/README_before_current_state_2026-10-21.md).
- [Poprzedni roboczy README publikacyjny — 20 października 2026](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/archiwum/README_public_before_current_state_2026-10-21.md).
- [Zachowana wcześniejsza historia TSI](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/archiwum/HISTORIA_TSI_before_2026-10-21.md).
- [Wcześniejsza historia AI-SI](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/HISTORIA_SI_2026-10-11.md).

Kopie README zachowują historyczne opisy i pomiary. Nie oznaczają, że wszystkie wymienione tam eksperymenty są wdrożone. Odnośniki do wcześniejszych lokalnych materiałów w tych kopiach przedstawiono jako zwykły tekst.

## 20 października — wspólny moduł i aplikacja

Wprowadzono wspólny model H512, czytnika, macierzy i uczonych połączeń: runtime 0.6.0, 2 613 105 parametrów i plik wag 10 587 275 B. Integracja dotyczyła jawnych relacji i dowodów; narzędzia oraz pamięć dokumentów pozostały osobnymi częściami aplikacji.

Ówczesne wyspecjalizowane sprawdziany obejmowały 960/960, 720/720 i 640/640 przypadków, 140/140 poleceń językowych, 256/256 operacji wektorowych i 118/118 planów. Były to ograniczone zestawy znanych pojęć i jawnych danych. Nie potwierdzały swobodnej rozmowy.

Uporządkowano panel rozmowy i dokumentów, dodano odczyt kilku źródeł, wersjonowanie, poprawki i cofanie zmian. Analiza sygnałów uzyskała w osobnym sprawdzianie pięciu etykiet 95,32% micro-F1 i 1739/2000 pełnych zestawów. Są to historyczne wyniki innych modułów, a nie ocena obecnego generatora tekstu.

## 21 października — własny generator i odczyt źródeł

Pierwszy generator tekstu miał 1 826 496 parametrów i kontekst 512 tokenów; warstwa uwagi kopiującej dodawała 73 921 parametrów. Na 68 odłożonych zadaniach o fakty i definicje uzyskał 0/68 pełnych odpowiedzi, przy 25/25 odmowach przy braku informacji. Dalszy wspólny trening generatora i wyboru źródła dał 7/68. Wybór źródła potrafił być poprawny, mimo uszkodzonej odpowiedzi.

Model czytający pełną treść połączył własny generator, H512 i role macierzowe. Samo zwiększenie liczby parametrów do około 4,96 mln nie rozwiązało generowania odpowiedzi. Próby impulsów, sekwencji powtórek i zmian wag nie dostarczyły dowodu na fizyczny rezonans poprawiający naukę. Nie stosowano ich jako potwierdzonej metody produkcyjnej.

Podczas wcześniejszych prób wykryto także błędy wyznaczania zakresów źródeł. Wadliwe przebiegi oznaczono i zastąpiono poprawionymi; nie należy ich traktować jako wiarygodnych wyników nauki. Etykiety źródeł w generowanym tekście wymagały osobnej kontroli.

## Dwie połówki i wspólna odpowiedź

Początkowo sklonowano rdzeń i uczono drugą połówkę na błędach, przy zamrożonej pierwszej. Następnie połączono ich reprezentacje. Poprawiono rozdzielenie wyboru źródła od uwagi wewnątrz źródła i wprowadzono role terminu oraz objaśnienia.

Przed wspólnym odblokowaniem obu połówek potwierdzono 7/8 na niezależnych faktach, 8/16 na mieszanych starszych źródłach i 5/7 na wcześniejszych zadaniach językowych. W zestawie mieszanym fakty miały 8/8, a definicje 0/8. Późniejszy trening samych macierzy definicji podniósł starsze definicje do 4/8 i nowe do 10/16.

Wspólny trening 60 kroków odblokował oba generatory i obie pamięci H512. Potwierdzono przepływ gradientów oraz zmianę wag obu połówek. Wariant pojedynczy i dwupołówkowy dostały te same partie danych. Oba uzyskały 23/24 na zestawie doboru i 16/16 na nowych definicjach. Dwupołówkowy uzyskał 49/85 na starszych zadaniach, pojedynczy 48/85. To mała różnica, nie dowód ogólnej przewagi dwóch rdzeni ani szybszego uczenia.

W obu wariantach wystąpiła regresja starszego zestawu faktów: 8/8 → 6/8. Wybrano dwupołówkowy kierunek dalszego rozwoju, zachowując wcześniejsze wagi do cofnięcia. Nie podmieniono działających paneli.

## Eksperyment jednej podpowiedzi

Bez aktualizacji wag podano ogólną wskazówkę o zachowaniu pełnego początku imienia, bez ujawniania imienia, źródła ani odpowiedzi:

| Miejsce podpowiedzi | Pełne odpowiedzi |
|---|---:|
| Bez podpowiedzi | 6/8 |
| Tylko pierwsza połówka | 7/8 |
| Tylko druga połówka | 8/8 |

Nie utracono wcześniejszych sześciu trafień. Był to efekt kontekstu, nie potwierdzone trwałe uczenie. Wynik nie dowodzi, że jedna połówka samodzielnie diagnozuje i uczy drugą.

## Trening z powtórkami i wycofywaniem podpowiedzi

Wykonano 400 kroków. Każda partia zawierała trzy zadania dotyczące faktów i jedną definicję jako powtórkę. Zbiór zawierał 195 różnych treningowych zadań o faktach i 160 definicji; osobny zestaw doboru i nowy test faktów miały po 24 różne zadania. Podpowiedź trafiała tylko do drugiej połówki: początkowo co drugi krok, następnie co czwarty, a w ostatnich 200 krokach była wyłączona.

Ćwiczono macierze uwagi, pozycji i bramki kopiowania. Obie wcześniej wytrenowane sieci bazowe i pamięci H512 zachowano. Trening wspólnego odczytu poprawił fakty, ale zepsuł jedną wcześniej poprawną definicję przez powtórzenie słowa. Rozdzielono więc macierze odczytu definicji i faktów w tym samym modelu; podział wykorzystuje wcześniej istniejące role terminu i objaśnienia, a nie listę konkretnych odpowiedzi.

Po tej ochronie ponowiono pełne sprawdziany bez podpowiedzi:

| Zestaw | Przed | Po |
|---|---:|---:|
| Wcześniejsze błędy faktów | 6/8 | 8/8 |
| Pierwotne źródła | 12/16 | 12/16 |
| Starszy zestaw doboru | 9/14 | 9/14 |
| Starszy zestaw słownikowy | 17/40 | 19/40 |
| Wcześniejsze zadania językowe | 5/7 | 5/7 |
| **Starsze zadania łącznie** | **49/85** | **53/85** |
| Nowy zestaw faktów | 23/24 | 24/24 |
| Osobne proste definicje | 16/16 | 16/16 |

Nie utracono żadnej wcześniej poprawnej odpowiedzi w tych zestawach. Po ponownym wczytaniu zapisanych wag ponowienie ośmiu przypadków nadal dało 8/8. Model po ochronie odczytu ma 10 147 343 parametry, plik 40 944 075 B. Porównanie dotyczy pełnych odpowiedzi, nie tylko etykiet źródeł; historyczne zestawy nie są nowymi ślepymi testami.

## Pozostałe błędy i kolejny etap

W starszych 85 zadaniach wyniki według rodzaju to: fakty 37/40, definicje 7/30, brak informacji 9/13, swobodne pisanie i wyjaśnianie 0/2. Występują ucięte słowa, powtarzanie fragmentów, niezgodność wypisanej etykiety S1/S2 z poprawnie wybranym źródłem i nieuzasadnione odpowiedzi przy braku danych.

Sprawdzono starsze zapisy: etykieta [S1] pojawiała się w odpowiedzi na prośbę o opowiadanie już w pojedynczym rdzeniu bez źródeł. Problem nie został więc zapoczątkowany dopiero przez połączenie połówek. Dokładnego pierwszego kroku jego powstania nie ustalono.

Kolejny trening zakończono po 600 krokach. Rozpoznanie braku informacji wzrosło z 9/13 do 13/13, ale fakty spadły z 37/40 do 31/40, a definicje z 7/30 do 4/30. Łącznie uzyskano 48/85 zamiast 53/85. Wariant odrzucono; poprzednie sprawdzone wagi pozostają zachowane.

## Nauka od solvera i nauczyciela logiki

SymPy przygotował dokładne odpowiedzi dla 768 przykładów treningowych: działania, ułamki i równania liniowe. Zestaw doboru miał 48 przykładów, test 72. Po 800 krokach uczeń uzyskał 2/72. Dodatkowe 1000 kroków uczenia reprezentacji wejścia i ról liczb dało 7/72. Nowy zestaw 48 zadań, wykluczający także wcześniej widziane odwrócenia działań przemiennych, dał 5/48. Zakresy liczb pozostawały znane z treningu. Solver nie był wywoływany podczas odpowiedzi ucznia. Wyniki są nadal niewystarczające do niezawodnego liczenia.

Wprowadzono trening silnej logiki trójstanowej Kleene’a: T — prawda, F — fałsz, U — nieznane. Bezpośredni odczyt tekstu uzyskał 36/39 powtarzanych przypadków podstawowych i 30/48 nowych złożeń. Jeden eksperyment ujawnił błąd wybierania fragmentu wejścia: zamiast wyrażenia wybierano końcową instrukcję „Wynik: T/F/U”. Jego wyników nie traktujemy jako wiarygodnego sprawdzianu wejścia. Po poprawce i powtórkach kolejny wariant uzyskał 38/39 oraz 29/48; problem odczytu złożonych wyrażeń pozostaje.

Osobny wariant formalny łączy parser składni z uczonym modułem operatorów o 483 parametrach. Nauczyciel podał wszystkie 39 elementarnych kombinacji AND, OR, NOT, IMPLIES i EQUIV. Podczas wykonania parser wyznacza kolejność kroków, a sieć przewiduje wynik każdego operatora. Uzyskano 39/39 nauczonych przypadków, 48/48 wcześniejszych złożeń i 100/100 nowych zagnieżdżonych wyrażeń. Nowe są złożenia znanych operatorów; wynik nie dowodzi rozumowania na dowolnym opisie słownym ani samodzielnego odkrywania reguł.

Wagi wcześniejszego odczytu źródeł zachowano bez zmian; kontrola ośmiu wcześniejszych przypadków ponownie dała 8/8. Moduły matematyki i formalnej logiki mają osobne wejścia badawcze. Nie podmieniono działających paneli. Pełny zapis wariantu z tymi modułami ma 11 239 938 parametrów; nie zastępuje zaakceptowanego modelu źródeł opisanego w głównym README.

## Publikacja

Ta aktualizacja publikuje dokumentację i dwa zrzuty panelu z przykładowymi danymi. Nie dodaje kodu obecnego TSI, wag, danych treningowych, prywatnych dokumentów ani lokalnych ścieżek użytkownika. Nie wydano nowego portable i nie podmieniono modeli w działających panelach.
