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

### Rozmowa, źródła i lokalny słownik

Sprawdzono rzeczywistą rozmowę o państwach. Starszy czytnik mylił pytanie o państwa z pytaniem o możliwości TSI, prośbę o Wikipedię z wklejaniem dokumentu, a definicję z audytem poprzedniej odpowiedzi. Wytrenowano osobny klasyfikator intencji. Wybrany wariant miał 482 przykłady treningowe i wynik 85/87 na odłożonych przykładach znanych rodzin pytań z innymi tematami. To nie jest wynik swobodnej konwersacji. Dodatkowe parafrazy oraz rzeczywista rozmowa nadal ujawniały błędy, zwłaszcza przy doprecyzowaniu znaczenia i prośbie o prostsze wyjaśnienie. Kolejne warianty badawcze nie zastąpiły wybranego czytnika.

Podłączono pobieranie Wikipedii z wyborem artykułu, zachowaniem źródła i kontekstu. Poprawiono kolizję z włączonym materiałem dokumentowym oraz wybór polskiego języka komunikatów. Szesnaście kontroli HTTP objęło wcześniejszy ciąg pytań, treść artykułu, listę państw, angielskie hasło Gravity, potwierdzanie nowego wyszukania oraz wcześniejsze funkcje matematyki, logiki i dokumentów. Te kontrole poprzedzały dodanie lokalnej bazy słownikowej.

Następnie z publicznego zrzutu polskiego Wikisłownika przez Kaikki/Wiktextract zbudowano lokalną bazę: **114 215 różnych haseł, 125 720 wpisów i 1 437 842 powiązania form odmiany**. Baza zajmuje **157 716 480 B**. Zachowuje znaczenia, przykłady, źródła i informację o pochodzeniu. Jest dostępna przez polecenie `słownik: …`, a rozpoznane pytania definicyjne korzystają z niej przed pobraniem strony. Odrębne znaczenia nie są automatycznie uznawane za równoważne. Sprawdzono lokalny odczyt przy zablokowanym pobieraniu sieciowym. Nie jest to kopia PWN i nie jest to trening wag generatora. NKJP/PELCRA oraz WSJP sprawdzono jako możliwe dalsze zasoby; nie zaimportowano ich pełnych baz.

Rzeczywista próba po podłączeniu słownika poprawnie odpowiedziała na dłuższe pytanie o państwo, lecz doprecyzowanie „chodzi mi o kraj, nie grupę osób” nadal nie zostało poprawnie obsłużone. Pytanie o cechę ciał z definicji grawitacji zwróciło zbyt szerokie fragmenty, także ze starego tematu. Wyszukanie definicji i odczyt konkretnej relacji są oceniane osobno.

Dodano następnie odczyt jawnych relacji z aktywnej definicji. Własny uczony klasyfikator pytania wybiera rolę: cecha, uczestnicy, przeznaczenie, skład, warunek lub inne. Miał 535 przykładów treningowych, 112 do doboru i 112 testowych; uzyskał 109/112 etykiet w teście znanych rodzin pytań. Sam ten wynik nie mierzy trafności pełnych odpowiedzi. Matryca konstrukcji językowych wskazuje dokładny fragment źródła; nie zawiera gotowej odpowiedzi „masę”. W kontroli offline definicja grawitacji dała „masę” dla pytania o cechę i „ciałami mającymi masę” dla uczestników. Brak zapisanego warunku spowodował doprecyzowanie. Kontrole zmiany źródła sprawdziły odczyt różnych cech. To ograniczony odczyt jawnych relacji, nie dowód swobodnego wnioskowania ani opanowania parafrazy przez generator.

### Podłączenie operatorów logiki do panelu

Po powyższych badaniach wdrożono w panelu lokalnym wyłącznie sprawdzony moduł 483 uczonych parametrów operatorów, z parserem formalnych wyrażeń. Zachowano dotychczasowy model rozmowy; nie włączono słabego eksperymentalnego ucznia arytmetyki. Przykłady są dostępne w pomocy. Polecenia `logika: …` i `logic: …` działają w rozmowie i dziale rdzenia; jednoznaczne formalne wyrażenia rozpoznawane są również bez prefiksu. Odpowiedź zawiera wynik T/F/U i kroki, w wybranym języku panelu. Niepełne nawiasy i obce dopiski są odrzucane zamiast pomijania części wejścia.

Kontrola interfejsu HTTP objęła sześć poprawnych wyrażeń PL/EN, trzy błędne zapisy i dwie wcześniejsze funkcje: przywitanie oraz dodawanie. Wszystkie 11 kontroli przeszło. Po uruchomieniu docelowego panelu ponowiono złożone wyrażenie i potwierdzono, że używa nowych wag operatorów. Zachowano kopię poprzedniego koordynatora aplikacji. To wdrożenie formalnej logiki, nie wymiana całego modelu rozmowy.

Ta aktualizacja publikuje dokumentację i dwa wcześniejsze zrzuty panelu z przykładowymi danymi. Nie dodaje kodu obecnego TSI, wag, danych treningowych, prywatnych dokumentów ani lokalnych ścieżek użytkownika. Nie wydano nowego portable. Lokalny panel otrzymał opisany powyżej moduł logiki; pełny wariant badawczy pozostaje oddzielny.


## 22 października 2026 — nauka wypowiedzi i pętla internetowa

Poprzednie główne README zachowano w [archiwum](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/archiwum/README_2026-10-21_BEFORE_WEB_LEARNING.md). Główny opis zawiera teraz stan aplikacji, lokalną obsługę nauki i aktualny pomiar rozmiaru.

Pobrano OpenAssistant OASST1 z zachowaniem pochodzenia i licencji Apache-2.0. Rozmowy rozdzielono według całych drzew. Kontrola usunęła całe drzewa z błędami i słabymi odpowiedziami. Po dodaniu autorskich przykładów uzyskano 53 przykłady treningowe, 10 do doboru i 8 testowych. Autorskie zestawy mają wspólne rodziny umiejętności, więc nie dowodzą szerokiej generalizacji. Powtórki obejmowały 1002 wcześniejsze zadania.

Trening obu generatorów wykonał 120 kroków. Wybrany według wskaźnika NLL krok 40 obniżył testowe NLL z 6,2430 do 5,8440, lecz pełne nowe wypowiedzi pozostały niepoprawne (0/8). Fakty zachowano 8/8, ale definicje spadły z 16/16 do 6/16. Wariant odrzucono. Wniosek: spadek błędu przewidywania tokenów nie wystarcza do wyboru dobrego rozmówcy.

Do zachowanej reprezentacji dwóch rdzeni dołączono dwa przyczynowe bloki transformera i odczyt słownika: 1 285 376 uczonych parametrów. Rdzenie bazowe mają 10 147 343 parametry i pozostają zamrożone. Pierwsze ćwiczenia sterowane pełnymi wygenerowanymi odpowiedziami opanowały cztery przykłady. Początkowa zbyt sztywna kontrola wszystkich wypowiedzi odrzuciła dziewięć dalszych rund, choć pierwsza poprawiała liczbę dokładnych odpowiedzi do sześciu, zachowując poprzednie cztery.

W kolejnej pętli dopuszczono zmiany nieopanowanych wypowiedzi przy zachowaniu opanowanych, dodano do 20 kroków naprawczych przed cofnięciem oraz odrębny nadzór każdej zapamiętanej odpowiedzi. Ostatni odczyt do niniejszej publikacji: 11/30 pełnych odpowiedzi uczących, runda 9. Wynik nie jest testem nieznanych rozmów. Zachowywane są migawki wag i historia decyzji. Model nie został automatycznie podmieniony w panelu.

Przygotowano lokalne BAT-y i panel nauki z internetu: checkbox Wikipedii i tematów, dodawanie tematu lub linku polskiej Wikipedii, limity czasu/rund, Start/Stop, kolorowe komunikaty postępu oraz powtórki pamięci. Pętla pobiera fragmenty ze źródłem, rewizją i SHA-256 i uczy odczytu podanej treści. Nie wykonuje instrukcji ani kodu z pobranych stron. Odznaczenie źródła wyłącza nowe uczenie z niego, zachowując powtórki opanowanej pamięci.

Pełna runda w odizolowanej kopii pobrała artykuł „Algorytm”, wykonała krok treningu i prawidłowo cofnęła pogorszenie (błąd 0,181 → 0,184, zachowany 0,181). Sprawdzono inicjalizację panelu z 12 tematami. Dodano sekcję „Nauczyłem się” z rzeczywistymi wygenerowanymi odpowiedziami: tylko zaakceptowana runda może ogłosić nowe opanowanie przykładu; w przeciwnym przypadku pokazywana jest wypowiedź ćwiczona lub zachowana. Sprawdzono rozróżnienie zaakceptowanej i odrzuconej aktualizacji oraz ponownie inicjalizację panelu.

Zmierzono kod, dane, modele i środowisko. [Pomiar z 22 października](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/SIZE_2026-10-22.md) zastępuje historyczne wartości rozmiaru jako bieżący punkt odniesienia. Publikacja zawiera wyłącznie dokumentację; kod, wagi, dane i prywatne ścieżki pozostają poza aktualizacją repozytorium.


### Kontrola zapominania i przekazanie pętli

Po publikacji punktu 11/30 nadzór wykrył utratę jednej wcześniej opanowanej rozmowy o dziewczynce i mapie. Zachowano migawkę rundy 8 (10/30), a następna seria obowiązkowo powtarzała gubioną wypowiedź i chroniła każdą wcześniej opanowaną odpowiedź. Zakończyła 9 rund, zachowując 10/30; błąd odpowiedzi uczących spadł z 0,45820 do 0,45494. Przyjęto 3 rundy, 6 cofnięto. Ostatnie wagi i 10 zapisów pamięci przekazano pętli BAT; model rozmowy w aplikacji pozostał bez zmian.

Panel nauki ma teraz zwartą siatkę tematów, rzeczywiste wypowiedzi po rundach oraz cofnięcie o dwie zaakceptowane wersje. Cofnięcie podczas pracy jest kolejkowane do bezpiecznego zatrzymania i odtwarza zarówno wagi, jak i pamięć. Sprawdzono kolejkowanie przy blokadzie treningu, przywrócenie dwóch wersji oraz odmowę, gdy brak dostatecznej historii.

## 23 października 2026 — wspólny dekoder, źródła i równowaga powtórek

Połączono dwa enkodery z natywnym dekoderem autoregresyjnym przez uwagę krzyżową. Łącznie model ma 14 853 139 parametrów. Kod i pełne wagi pozostają lokalnie. Zapis obejmuje obie części wejściowe i dekoder; nie użyto wag zewnętrznego modelu językowego.

Wykryto brak przekazywania jawnych ról S1/S2 w jednej ścieżce oraz interpretowanie małych odchyleń uczonych flag jako prawdy przez konwersję na bool. Poprawiono przekazywanie ról i odczyt flag z progiem. Nie uznano tych poprawek za automatyczne potwierdzenie poprawności całej rozmowy.

Przyjęty przed ostatnią korektą zapis zachowywał 48/48 odpowiedzi i uzyskiwał 38/69 przypadków odczytu reguł. Sieć miała tendencję do wybierania T lub U, a odczyt F pozostawał błędny. Próba śledzenia wykazała, że zmiana źródła zmienia reprezentacje enkoderów i wyjście uwagi; sygnał docierał, mimo błędnej decyzji dekodera.

W jednej późniejszej, odrzuconej serii popełniono błąd w celu uczenia: lista klas zawierała T/F/F/U, a indeks celu U wskazywał drugie F. Poprawiono ją do unikalnego T/F/U, dodano sprawdzenie identyfikatorów tokenów i kierunku gradientu. Wadliwych wag nie przyjęto. Sama poprawka etykiet nie usunęła pozostałych błędów czytania.

Trening wskazywania fragmentu z wynikiem reguły poprawił odczyt do 46/69 i zachował poprzednie 38 poprawnych przypadków, ale dał 47/48 na chronionych faktach. Pomyłka dotyczyła odwróconej zmiany godziny. Harmonogram powtórek faworyzował 19→9; poprawiono dobór, dodając oba kierunki i obie role czasu.

Zrównoważony program miał 40 przykładów, po 20 z podpowiedzią i bez niej, po 20 pytań o czas aktualny i poprzedni. Wyniki każdej godziny występowały jednakowo często w tym programie. Oddzielono 16 zadań z nowymi parami i inną parafrazą, bez podpowiedzi. Dodatkowe powtórki pary 9/19 były symetryczne.

Punkt po 10 krokach dał 48/48, ale stracił jeden z 46 poprawnych przypadków logiki — U IMPLIES T. Odrzucono go. Przyjęto punkt po 6 krokach: **48/48**, zachowane **46/46**, a pełna kontrola odczytu dała **47/69**. Na nowych opisach czasu uzyskano **3/16**. To przyjęty punkt do dalszych testów, nie podmiana panelu ani potwierdzenie swobodnego rozumienia języka.

Nowa wspólna pętla internetowa rzeczywiście pobrała artykuł „Rekurencja” z Wikipedii (rewizja 80072510), przeprowadziła trening i wykryła pogorszenie: zachowano 23/38 poprzednich przypadków logiki, bez opanowania nowej definicji (0/1). Wagi odrzucono, a pętlę zatrzymano. Materiał zachowano z adresem, rewizją i skrótem treści; nie wykonywano kodu pobranego ze strony.

Pomiar przyjętego modelu: **59,41 MB** parametrów FP32 i **162,82 MB** pełnego zapisu ze stanem treningu. Katalog aplikacji z kodem, danymi, modułami i artefaktami, z wyszczególnionymi wyłączeniami, zajmuje **1 989,89 MB**. Nowy model jest przechowywany oddzielnie. Szczegółowy zakres jest w [pomiarze](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/POMIAR_TSI_2026-10-23.json).

Szczegóły obecnej oceny: [OCENA_TSI_2026-10-23.md](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/OCENA_TSI_2026-10-23.md). Poprzedni README przeniesiono do [archiwum](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/archiwum/README_przed_ocena_2026-10-23.md).

## 23 października 2026 — korekta klas i odczytu wyniku ze źródła

Wykonano 16 aktualizacji pierwszej próby oraz 8 aktualizacji drugiej. Uczono oba enkodery i dekoder; reguły formalne pozostały zamrożone. Oceniano ponownie wczytane wagi i pełne odpowiedzi sieci, bez podmiany wyniku przez nauczyciela.

| Zapis | Zachowane wcześniejsze odpowiedzi | Tablica źródłowa | T | F | U | Decyzja |
|---|---:|---:|---:|---:|---:|---|
| Próba 1, krok 8 | 89/98 | 50/69 | 12/23 | 11/19 | 27/27 | Odrzucony |
| Próba 1, krok 16 | 92/98 | 45/69 | 15/23 | 4/19 | 26/27 | Odrzucony |
| Próba 2: wyrównanie i uwaga, krok 8 | 92/98 | 49/69 | 15/23 | 7/19 | 27/27 | Odrzucony |

Chronione 98 przykładów obejmuje 48 wcześniejszych odpowiedzi o faktach i języku, 47 poprawnych wyników logiki oraz 3 poprawne opisy czasu. Podwyższenie łącznego wyniku nie wystarcza do przyjęcia zapisu, jeżeli stracił wcześniej poprawne odpowiedzi.

Audyt pierwszej próby wykazał, że po doliczeniu powtórek udział celów wynosił **T 53, F 32, U 58**, mimo równej liczby nowych ćwiczeń. Druga próba wyrównuje łączny nadzorowany błąd klas: liczby przykładów to T 37, F 16, U 42, a wagi błędu dają każdej klasie taki sam łączny udział. Dodatkowo uwagę sieci uczono kierować na fragment „Wynik reguły”, zamiast na same operandy. Tablica jest materiałem źródłowym dla enkoderów; nie zastępuje wyjścia dekodera.

Pierwsza próba pokazała konkretny błąd: odpowiedź F dla `F NOR F`, chociaż źródło podawało T. Poprawa klasy F kosztem poprawnych odpowiedzi T została rozpoznana jako regresja.

Dodatkowy sprawdzian 16 nowych opisów czasu, z innymi pytaniami i liczbami, dał **0/16** dla bezpiecznych wag oraz **0/16** dla drugiej próby. Te sformułowania nie weszły do treningu. Oddzielnie przygotowano program 72 przykładów czasowych; w tym etapie go nie trenowano. Starszy test 3/16 i nowy sprawdzian stanowią odrębne zbiory. Trzy poprawne przykłady starszego zestawu weszły do chronionych powtórek nowych prób.

**Stan przyjęty pozostaje bez zmian:** 48/48 wcześniejszych odpowiedzi, odczyt źródła logicznego 47/69 (T 21/23, F 0/19, U 26/27), starsze parafrazy czasu 3/16. Nowe próby odrzucono. Panel, MUZ, walidator i paczki portable nie otrzymały tych wag. Nauka internetowa pozostaje zatrzymana.

## 23 października 2026 — większy model i pięć etapów powtórek

Model rozszerzono z 14 853 139 do **23 018 523 parametrów**, a dekoder z 4 do **12 warstw**. Przy samym rozszerzeniu 98/98 wcześniejszych odpowiedzi i ich logity pozostały identyczne.

Następnie odtworzono pięć zapisanych programów nauczania w kolejności od najstarszego do najnowszego. Powtarzano poprawne etykiety, a nie wcześniejsze błędne wypowiedzi sieci. Oryginalne enkodery i cztery warstwy dekodera były zamrożone; uczyło się osiem dodanych warstw.

| Etap | Aktualizacje łącznie | Zachowane odpowiedzi | Logika ze źródłem |
|---|---:|---:|---:|
| 1/5 | 16 | 107/109 | 45/69 |
| 2/5 | 26 | 106/109 | 45/69 |
| 3/5 | 42 | 104/109 | 45/69 |
| 4/5 | 50 | 105/109 | 48/69 |
| 5/5 | 60 | 102/109 | 46/69 |

Końcowa próba: znane opisy czasu **15/40**, nowe opisy bez podpowiedzi **0/16**. Znany zestaw 40 przykładów był materiałem powtórek. Zestaw nowych opisów nie był materiałem treningu tego eksperymentu.

Nie przyjęto nowych wag: zachowano zapis sprzed powtórek.

**Nie osiągnął wymaganego poziomu.** Model badany nie został wdrożony do panelu, MUZ ani walidatora. Internetowy trening wag pozostaje wyłączony.

## 23 października 2026 — dalsze utrwalanie po pięciu etapach

Trening kontynuowano z ostatnich wytrenowanych wag, z mniejszym tempem aktualizacji. Co krok powracano do utraconych odpowiedzi, a zestaw ochronny rozszerzono ze 109 do **117**: dodano osiem nowych poprawnych przypadków. Starsze parametry pozostały zamrożone; uczyły się dodane warstwy.

| Aktualizacje | Zachowane ze 117 | Zachowane z pierwotnych 109 | Logika | Znane godziny |
|---|---:|---:|---:|---:|
| 8 | 106/117 | 104/109 | 44/69 | 15/40 |
| 16 | 109/117 | 107/109 | 46/69 | 15/40 |

Nowe opisy czasu, nieużywane w treningu tej serii: **0/16**. Wynik końcowy T/F/U: **T 20/23**, **F 0/19**, **U 26/27**.

Zachowano wcześniejszy przyjęty zapis; kolejne wytrenowane wagi pozostają materiałem do dalszych badań. Panel, MUZ i walidator nie zostały podmienione. Internetowy trening wag pozostaje wyłączony. **Nie osiągnął wymaganego poziomu.**

## 23 października 2026 — równy udział stanów w całych powtórkach

Audyt poprzedniej serii wykazał nierówny udział stanów po dodaniu materiału ochronnego: **T 46, F 22, U 65** ekspozycji logicznych. Wyrównano cały dobór przykładów, łącznie z powtórkami. Kolejne osiem aktualizacji zawierało dokładnie **T 32, F 32, U 32** ekspozycje. Liczby potwierdzono z faktycznie użytych partii.

Po dodatkowym treningu: **109/118** zachowanych odpowiedzi, w tym **100/109** z pierwotnego zestawu i **48/48** podstawowych. Logika **51/69**; T **16/23**, F **12/19**, U **23/27**. Znane godziny **15/40**, nowe opisy **0/16**.

Najnowszy zapis zachowano do dalszych badań, bez zastąpienia wcześniejszych przyjętych wag. **Nie osiągnął wymaganego poziomu.** Bez podmiany panelu, MUZ i walidatora.

## 24 października 2026 — utrwalanie odczytu źródła

Wykonano osiem aktualizacji od ostatnich wytrenowanych wag. Utrzymano równą liczbę ekspozycji logicznych wraz z powtórkami: **T 32, F 32, U 32**. Uczenie uwagi na właściwy wynik ze źródła objęło również materiał ochronny. Zmniejszono tempo aktualizacji i powtarzano utracone fakty. Enkodery i cztery starsze warstwy dekodera pozostały zamrożone; trenowano osiem dodanych warstw.

Kontrola zapisanych i ponownie wczytanych wag: **113/124** zachowanych odpowiedzi, **104/109** z pierwotnego zestawu, **48/48** podstawowych. Logika **49/69**, znane godziny **16/40**, nowe opisy czasu **0/16**.

Rozkład logiki: **T 16/23**, **F 7/19**, **U 26/27**.

Sprawdzono hipotezę o wymuszaniu dwóch stanów na aktywnej ścieżce: T/F/U mają osobne tokeny w obu tokenizerach, ich reprezentacje w obu enkoderach są różne, a dekoder wybiera z pełnego słownika. Niezależnie zweryfikowano 69 wyników tablic reguł. Nie stwierdzono twardej zamiany U na T/F w tych punktach. Błędne odpowiedzi dla oczekiwanego F: osiem T i cztery U; dla oczekiwanego U: jedno T.

Zachowano nowe wagi do dalszych badań; przyjęty wcześniej zapis pozostaje bez zmian. **Nie osiągnął wymaganego poziomu.** Bez wdrożenia nowych wag do panelu, MUZ i walidatora. Trening internetowy pozostaje wyłączony.



## 2026-10-24 — połączenie wyuczonej macierzy logiki

Naprawiono odczyt wydzielonego wyrażenia w opisach PL/EN i wywołanie macierzy operatorów. Dodano wspólną paczkę badawczą zachowującą jej wagi. Testy: 138/138 poleceń, 148/148 złożeń, 6/6 HTTP, 105/105 pozostałych odpowiedzi identycznych. Nie zmieniono przyjętych wag językowych. [Pełny raport](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/POLACZENIE_LOGIKI_TSI_2026-10-24.md).


## 2026-10-24 — TIMDR: kontrolowane generowanie i dynamika znaczenia

Dodano kontrolę macierzy znaczenia w uczonym generatorze fraz aplikacji oraz ograniczanie tokenów we wspólnym modelu badanym. Jawne zdarzenia tworzą kolejne stany bez nadpisywania historii. Wyniki: 0/16 → 16/16 na nowych zadaniach czasowych przy dostarczonych macierzach, 3/4 → 4/4 wcześniejszych, 6/6 dynamiki/ról/negacji, 105/105 zachowanych pozostałych odpowiedzi. Polski czytnik: 5/7 prób rozstrzygniętych, 2 nierozstrzygnięte. Bez treningu i podmiany wag, bez nowej portable. [Raport](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/TIMDR_JEZYK_TSI_2026-10-24.md).

## 2026-10-24 — przebudowa rozmowy, skróty i zdania złożone

Wdrożono wspólny podział zdań oraz obsługę wielu członów z zachowaniem spójników, negacji i kierunku przyczyny. Zlikwidowano globalny wymóg jednej relacji przy generowaniu fraz; zachowano ograniczenia techniczne analizy. Kontrole: 15/15, 116/116, 13/13, generowanie 4/4 i API 3/3.

Próba starego panelu: 12 tur, 9 odmów, dwie nietrafione Wikipedie i jedno nietrafione wyszukanie dokumentu. Osobny nowy przepływ uruchamia rzeczywisty generator, ale jego pierwszy trening zachował 47/48 dawnych odpowiedzi i nie poprawił swobodnej rozmowy do wymaganego poziomu. Wagi odrzucono jako domyślne. Zrównoważony trening: **67 aktualizacji**, zachowanie **47/48** wcześniejszych odpowiedzi. W ręcznej ocenie pełnych odpowiedzi: **0/2 powtórek** i **1/4 nowych wypowiedzi**; poprawna odpowiedź czasowa wymagała kontroli macierzowej podczas ponownego generowania. Nowych wag nie ustawiono jako domyślnych.

Zbadano także zakończenia: EOS sieci w 12/12 odpowiedzi, identyczne wyniki przy 72 i 160 tokenach na dwóch wejściach, zachowanie znaków 54/54. [Szczegóły](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/ROZMOWA_I_SKLADNIA_TSI_2026-10-24.md).
