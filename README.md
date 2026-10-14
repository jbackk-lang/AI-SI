# timderSI (TSI) — dokumentacja zaktualizowana 14 października 2026

TSI to lokalny, uczony system wiążący nazwy z wartościami i wykonujący operacje logiki trójstanowej. Rozwijana warstwa językowa rozpoznaje polskie polecenia oraz ich argumenty. Kod, wagi i bazy pozostają lokalnie; to repozytorium udostępnia dokumentację.

## Bieżący stan — ostatnie udokumentowane pomiary z 13 października 2026

System nie jest jeszcze gotowy do ogólnego rozumienia poleceń. Pamięć i logika pozostają zamrożone. Najsilniejszy zachowany kandydat językowy `word_operator_control_50` ma 72 641 parametrów parsera, łącznie 186 729 przy jednokrotnym liczeniu wspólnej pamięci. Nie został automatycznie wdrożony. Wcześniejsza tabela poniżej opisuje starszy wybrany zestaw, a nie ten kandydat.

Diagnostyka na danych treningowych pokazała, że niepotrzebny dopisek zmienia zarówno odczyt operatora z końca tekstu, jak i wsteczne reprezentacje słów używane przez argumenty. Diagnostyczne odtworzenie wcześniejszych aktywacji naprawia część błędów, ale wymaga znanej granicy i czasem szkodzi innym przypadkom. Nie jest to metoda odpowiadania ani wdrożona naprawa.

Ograniczone próby nowego, uczonego odczytu operatora dodały 66 parametrów i początkowo zachowały identyczne wyniki. Na 1200 przypadkach z nazwami wydzielonymi dla tej adaptacji źródło miało 925 dokładnych interpretacji. Próba pośredniego uczenia uzyskała 923 (2 utraty, 0 zysków), bezpośredni nadzór końca tekstu 925 (0 utrat, 0 zysków). Etykiety końca tekstu zawierały 69 sprzecznych identycznych początków wejścia. Spójny cel wskazujący ostatni wymagany argument poprawił wybór pozycji do 476/800, lecz pełne interpretacje nadal spadły do 923/1200. Poprawa pomocniczego zadania nie oznacza poprawy systemu. Te nazwy mogły być historycznie widziane przez źródło; to nie końcowy niezależny test gotowości.

Sygnał adresowania pamięci także nie stanowi bezpiecznej reguły wyboru parsera: w kontrolnych przypadkach z nieobecną pytaną nazwą i niepotrzebnym wspomnianym faktem wskazywał błędny parser 20 razy, poprawny 2 razy. Pytanie o nieznany fakt jest dozwolone. Nie wdrażamy reguł obecności, wycinania dopisków ani odpowiedzi referencyjnych.

Serie selektorów, małych kar i tego odczytu zostały zamknięte bez wdrożenia. Wszystkie modele i stany optymalizacji zachowano. Dalszy krok wymaga odmiennego, uzasadnionego mechanizmu ochrony reprezentacji polecenia i argumentów, a następnie nowych niezależnych testów oraz kontroli każdej utraconej poprawnej interpretacji. Chronologia i szczegółowe wyniki są osobno w `HISTORIA_SI_2026-10-11.md`. Kod, wagi i dane pozostają lokalne.

## Budowa i parametry — starszy wybrany zestaw

| Część | Architektura | Parametry |
|---|---|---:|
| Pamięć faktów | wspólny znakowy encoder nazw: dwukierunkowy GRU, szerokość 96; uczona adresowana pamięć klucz–wartość; wyjście trójstanowe | 108 725 |
| Logika | embedding sześciu operatorów i MLP 14 → 64 → 64 → 3 | 5 363 |
| Język poleceń | embedding znaków 32; dwukierunkowy GRU po 64 jednostki; siedem klas operacji i cztery granice argumentów | 42 699 |
| **Wybrany zestaw łącznie** | pamięć + logika + język | **156 787** |

Pamięć przyjmuje do ośmiu jawnych faktów, nazwy do 16 znaków oraz wartości `prawda`, `fałsz`, `nieznane`. Warstwa językowa obsługuje wejście do 160 znaków. Fakty są obecnie podawane jako uporządkowane rekordy; naturalny język służy poleceniu o tych faktach.

Konstruktor wykorzystuje rzeczywisty `TIMDRWorkflow` z TIMDR-AI-Core, z zachowaną wersją źródeł i kontraktem konstrukcji. TSI używa GRU i uczonej pamięci adresowanej. Koordynator TIMDR organizuje konstrukcję i walidację; nie przypisujemy tym warstwom równoważności z fizycznymi operatorami TIMDR.

## Wyniki wcześniejszych walidacji modułów i starszego parsera

| Zakres | Wynik | Co sprawdzono |
|---|---:|---|
| Odczyt wartości z pamięci | **2208/2208** | nowe pełne nazwy, 2–8 faktów, trzy wartości, obie kolejności faktów |
| Rozpoznanie braku podobnej nazwy | **455/480** | pytana nazwa nieobecna, różniąca się znakiem od obecnej |
| Złożenia operatorów na wartościach | **10 000/10 000** | świeże rozgałęzione drzewa głębokości 1–5, wartości dwustanowe i trójstanowe |
| Złożenia na faktach wskazywanych nazwą | **240/240** | nowe nazwy, osiem faktów, cztery operandy; część pytań o brakujący fakt |
| Cały przebieg polskiego polecenia | **251/252** | rozpoznanie polecenia i argumentów, odczyt faktów, odpowiedź; 126 znanych form i 126 nowych połączeń zwrotów |

Uczone operatory: negacja, AND, OR, XOR, implikacja i równoważność, według przyjętej logiki trójstanowej. Brak faktu ma stan `nieznane`; negacja nie zmienia go w `prawda` ani `fałsz`.

Wyniki dotyczą podanych zakresów i syntetycznych testów. Wykluczano pełne testowe nazwy z nauki w świeżych próbach; użyte już testy służą później diagnostyce. Referencyjne reguły logiczne tworzą etykiety treningu i testów. Podczas odpowiadania wynik obliczają uczone moduły neuronowe.

## Ograniczenia starszego parsera — wcześniejszy szerszy test

Poniższe wyniki dotyczą wcześniejszego parsera znakowego, opisanego w tabeli 156 787 parametrów; nie są wynikami kandydata `word_operator_control_50`. Test 251/252 obejmował wąski zakres sformułowań. Szerszy test sześciu form i czterech rodzin nazw ujawnił nadal istotne braki:

| Rodzina nazw | Dokładne rozpoznanie operacji i argumentów | Poprawna odpowiedź |
|---|---:|---:|
| Pojedyncze litery `E`, `F` | 18/378 | 77/378 |
| Podobne nazwy numerowane | 306/378 | 299/378 |
| Polskie nazwy z diakrytyką | 108/378 | 190/378 |
| Polskie nazwy różnej długości | 135/378 | 179/378 |

Poprawna odpowiedź bez poprawnego rozpoznania polecenia może być przypadkowa. Dlatego oba pomiary są raportowane osobno. Warstwa językowa nadal wymaga nauki krótkich nazw, polskich słów i przenoszenia między sformułowaniami. Nie deklarujemy rozumienia dowolnych zdań, swobodnej rozmowy ani zagnieżdżonych poleceń w języku naturalnym. Nie ma jeszcze pełnego uczonego wyboru wielu modułów i oceny ich wyników.

## Ochrona wiedzy i stan prac

Podczas nauki języka pamięć faktów i logika pozostają zamrożone. Ich niezmienione pliki wag potwierdzono sumami SHA-256. Każdy krok treningu jest zapisywany wraz ze stanem optymalizatora i generatorów losowych. Najlepsze wersje są przechowywane osobno; pogarszające się próby nie zastępują ich.

Wariant logiki z 16 wymiarami pamięci pośredniej jest zbudowany i zachowany. W sprawdzonych złożeniach nie wykazał przewagi poprawności nad mniejszym modułem. Nowa wiedza i kolejne moduły mają być weryfikowane przed utrwaleniem w chronionej pamięci.

TSI pozostaje kandydatem lokalnym w rozwoju. Dotychczasowa aplikacja SI i jej starsze wagi są zachowane osobno. Według ostatniego wpisu historii z 13 października żaden proces treningowy nie był aktywny, a monitoring miał status ACTIVE/notready. To zapis historycznego statusu, nie bieżący odczyt procesów ani potwierdzenie działania monitoringu 14 października. Eksperymentalne wagi pozostają niewdrożone.

## Możliwe zastosowania po walidacji

Najbliższy zakres zastosowań to lokalna pamięć nazwanych faktów, kontrola reguł z jawnym stanem niepewności oraz niewielki uczony kontroler współpracujący z osobnymi modułami. Testy nie potwierdzają jeszcze niezawodności produkcyjnej ani zastosowań wymagających wysokiej pewności.

## Historia

[Historia procedur, pomiarów i zmian](HISTORIA_SI_2026-10-11.md) pozostaje osobnym dokumentem. README przedstawia aktualny stan i potwierdzone wyniki; wcześniejsze modele oraz przerwane eksperymenty nie są bieżącymi możliwościami TSI.

## Rozwój parsera słownego — wyniki do 13 października 2026

W toku opisanych prac z 13 października praca i nadzór były wznawiane na polecenie użytkownika; późniejszy końcowy wpis odnotował brak aktywnego procesu treningowego. Wszystkie źródła, kandydatury i stany uczenia zachowano. Nie wdrożono eksperymentalnych parserów; gotowość nadal wymaga niezależnej walidacji i ochrony wcześniejszych poprawnych odpowiedzi.

Aktualne kandydatury używają słownego dwukierunkowego GRU, uczonych wskaźników argumentów, odczytu operatora z uwagą oraz dodatkowych znakowych cech słów. Parser ma **72 641 parametrów**; razem z pamięcią 108 725 i logiką 5 363 daje **186 729**, licząc wspólny encoder tylko raz. Pamięć i logika pozostają zamrożone.

| Porównanie na tym samym zestawie | Źródło | Kandydat | Ograniczenie |
|---|---:|---:|---|
| Nowe nazwy i formy, 1890 przypadków; rozszerzone odtwarzanie 2050 | 1614 odpowiedzi / 1356 interpretacji | 1780 / 1639 | bez utraty wcześniejszego poprawnego rozumienia w tej próbce; osobna retencja wykazała regresje |
| Nowe nazwy i formy, 1890 przypadków; różnorodne konteksty 2100 | 1876 / 1864 | 1881 / 1873 | 1 utracona odpowiedź i 2 utracone poprawne interpretacje zakończone poprawną odpowiedzią |
| Wcześniejszy trudny zestaw, 1890 przypadków; różnorodne konteksty 2100 względem 1950 | 1664 / 1481 | 1815 / 1709 | 12 utraconych odpowiedzi, 163 odzyskane; 3 utraty poprawnego rozumienia i 231 zysków |
| Nowe nazwy i formy oraz poprawne powtórzenia argumentów, 750 przypadków; naprawa samego odczytu | 745 / 739 | 748 / 743 | bez utrat odpowiedzi ani poprawnego rozumienia w tej próbce |
| Retencja tej naprawy, wcześniejszy trudny zestaw 1890 | 1815 / 1709 | 1816 / 1714 | 5 zysków poprawnego rozumienia bez jego utrat; 1 utracona i 2 odzyskane odpowiedzi |

Dokładna interpretacja oznacza właściwy operator i wymagane argumenty: READ i NOT mają jeden operand, pozostałe operacje dwa. Poprawne rozumienie liczymy jako dokładną interpretację zakończoną poprawną odpowiedzią. Odpowiedź zgodna z etykietą mimo błędnej interpretacji jest wykazywana osobno; jej utrata nadal pozostaje jawna. W ostatniej retencji pojedyncza utracona odpowiedź pochodziła z przypadku, w którym oba warianty błędnie rozpoznały operator.

Poszczególne wiersze dotyczą różnych zestawów i nie tworzą jednej porównywalnej serii wyników. Pełne nowe nazwy wykluczano ze śledzonych danych treningowych i wcześniejszych zamrożonych testów. Nowe całe formy mogą zawierać wcześniej znane słowa. Po ujawnieniu wyników zestaw staje się diagnostyczny; wcześniejszy trudny zestaw jest celowo używany do retencji, a nie przedstawiany jako nowy test niezależny.

### Najlepszy zachowany kandydat i późniejsze próby

Zachowany kandydat word_operator_control_50 na nowym zestawie 2010 przypadków uzyskał **1994 poprawne odpowiedzi i 1982 dokładne interpretacje**, wobec 1992 i 1980 dla źródła, bez utrat w tej próbce. Na wcześniej ujawnionym trudnym zestawie 1890 uzyskał **1830 odpowiedzi i 1736 interpretacji**, wobec 1816 i 1714, także bez utrat względem bezpośredniego źródła. Różne zestawy nie stanowią wspólnej skali wyników. Kandydat pozostaje niewdrożony.

Dalsza próba ochrony aktualizacji zachowała treningowe poprawne przypadki, lecz na nowych 750 pogorszyła wynik 716/709 → 714/706: utraciła 3 odpowiedzi i 4 poprawne interpretacje, zyskując po jednej. Została odrzucona zgodnie z budżetem szkody. Ochrona treningu nie gwarantuje ochrony nowych poleceń.

Diagnostyczny odczyt fragmentu polecenia także nie zapewnił retencji. Na rozdzielonych treningowych parach nazw zyskał 9 interpretacji, tracąc 7; na rozdzielonych kombinacjach ramek zyskał 24, tracąc 9. Nie wdrożono wycinania tekstu ani reguł słownikowych. Ta próba dotyczy diagnozy na danych treningowych, nie nowego testu końcowego.

### Kontrola zysku i szkody

Na polecenie użytkownika stosujemy jawny wybór kandydatów według celu:

**maksymalizować zysk, przy ograniczeniu ważonej szkody do ustalonego budżetu.**

Pamięć i logika są chronione twardym zamrożeniem. Podstawowe znane polecenia i poprawne powtórzenia argumentów mają osobną ochronę. Raportujemy zyski, utraty odpowiedzi, utraty poprawnego rozumienia i kompromisy Pareto. Początkowy budżet regresji wynosi zero; nie ustalono dodatniej tolerancji. Jest to kryterium wyboru i dalszej walidacji, nie twierdzenie, że sieć sama realizuje prawo matematyczne, ani nowa wdrożona funkcja sterowania. Wcześniejsza naprawa samego odczytu (wiersze 750 i 1890 w tabeli) przeszła mały test bez strat, ale utraciła jedną odpowiedź w retencji, więc nie spełniła zerowego budżetu. Późniejszy `word_operator_control_50` nie wykazał strat względem bezpośredniego źródła w opisanych próbach 2010 i 1890; nie oznacza to braku regresji względem wszystkich wcześniejszych wersji ani gotowości do wdrożenia.

Próba wspólnego odczytu argumentów z dodatkowymi 6306 parametrami zachowała początkowe logity dokładnie, lecz po 50 aktualizacjach nie dała przewagi ponad kontrolę; została zamknięta. Próba uczenia cech znakowych razem z naprawą odczytu również wykazała regresje. Wszystkie stany zachowano, bez podmiany źródłowych wag.

**TSI nie jest jeszcze gotowe do ogólnego użycia.** Zakres pozostaje ograniczony do pojedynczego polskiego polecenia i zewnętrznych strukturalnych faktów. Nie ma swobodnego dialogu, zagnieżdżonych poleceń naturalnojęzykowych, parsera faktów z tekstu ani pełnego arbitra jakości. Angielski frontend jest planowany, nie wdrożony. Przed aktywacją potrzebna jest niezależna walidacja, ocena konkretnych strat i backup.

## Podsumowanie zamkniętej serii odczytu operatora

Na tym samym zestawie 1200 przypadków źródłowy `word_operator_control_50` uzyskał 925 dokładnych interpretacji. Każdy wariant dodawał 66 parametrów, przy zamrożonych wcześniejszych wagach; łącznie daje to 186 795 parametrów eksperymentalnego zestawu. Nie zastąpił on zachowanego kandydata.

| Wariant po 50 aktualizacjach | Dokładne interpretacje / 1200 | Utraty / zyski względem źródła | Decyzja |
|---|---:|---:|---|
| Pośrednie uczenie odczytu | 923 | 2 / 0 | bez wdrożenia |
| Bezpośredni nadzór końca pierwotnego tekstu | 925 | 0 / 0 | brak poprawy względem źródła; bez wdrożenia |
| Nadzór pozycji ostatniego wymaganego argumentu | 923 | 2 / 0 | bez wdrożenia; seria zamknięta |

Nazwy wydzielono dla tej adaptacji, lecz mogły być wcześniej widziane przez źródło. Zestaw nie stanowi końcowej niezależnej walidacji. Wariant z nadzorem argumentu osiągnął 476/800 poprawnych wyborów pozycji, ale nie poprawił interpretacji. Audyt wykazał 69 sprzecznych identycznych prefiksów dla etykiet końca tekstu i zero takich konfliktów dla etykiet argumentu na 972 analizowanych wierszach treningowych. Usunięcie tej sprzeczności nie naprawiło parsera.

Najbliższy uzasadniony kierunek badań to wspólna ochrona reprezentacji argumentów i odczytu operatora przed nieistotnym kontekstem. Jest to kierunek do sprawdzenia, nie ukończona funkcja ani polecenie uruchomienia treningu. Potrzebne są nowe niezależne testy nazw i sformułowań, kontrola każdej utraty oraz jednoznaczna decyzja o aktywacji konkretnej wersji.

Aktualizacja dokumentacji z 14 października porządkuje zapis pomiarów do 13 października. Nie dodaje nowych wyników eksperymentalnych; opisane wyniki pochodzą z historii i nie zostały ponownie zweryfikowane na wagach ani surowych logach podczas tej korekty.
