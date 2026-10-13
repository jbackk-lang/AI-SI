# Historia SI — procedura i wyniki z 11 października 2026

Ten zapis oddziela ukończone pomiary od prób w toku. Archiwalny README poniżej zachowuje wcześniejsze opisy i deklaracje; nie wszystkie są ponownie potwierdzone dla aktywnej wersji.

## Przebieg dzisiejszej pracy

1. Zachowano aktywny większy rdzeń: 1 888 140 parametrów, 9 warstw, 4 głowice uwagi, embedding 128, BPE 768, kontekst 128. Zmiany testowych wag nie oznaczają aktywacji.
2. Skorygowano semantykę samosprawdzania: zgodność dosłowna odpowiedzi, prawdziwość podanego stwierdzenia i brak niezależnej weryfikacji są różnymi zadaniami. Piętnaście wyuczonych przypadków nie dowodzi ogólnej samowiedzy. Nie używa się istniejącej głowicy argumentów jako wskaźnika pozycji zmiennej.
3. Przetestowano wiązanie nazw i wartości. Jedna zmienna może być poprawna, podczas gdy inne fakty nadpisują odpowiedź o niej. Dla E z innymi zgodnymi wartościami aktywny rdzeń popełniał 17 błędów na 18 przypadków. Zachowanie jest zgodne ze skrótem większościowym; nie ustalono mechanizmu wewnątrz sieci.
4. Próby podstaw wykazały 27/27 dla ćwiczonych pojedynczych zmiennych i 18/18 dla nowych nazw; dwie zmienne nie zostały opanowane. Przeprowadzono kontrolowaną próbę zamrożenia warstw i usunięcia dodatkowych celów: żaden wariant po 100 krokach nie opanował wiązania.
5. Przejrzano badania: ICML 2025, „How Do Transformers Learn Variable Binding in Symbolic Programs?” opisuje przejście od heurystyki pozycyjnej do systematycznego wiązania. Ich model, dane i liczba kroków różnią się od SI; nie można przenieść progu sukcesu.
6. Uruchomiono ciągły trening z powtórkami i przerwami 120 sekund. W pierwszym zestawie wszystkie lekcje miały A przed B. Był to błąd przygotowania danych. Po 3000 krokach treningowe AB miało 18/18, ale BA tylko 6/18; przy różnych wartościach BA 0/12. Dłuższy trening tego zestawu utrwalał skrót zamiast dowodzić postępu.
7. Zachowano wynik i checkpoint tej próby, zatrzymano ją i zrównoważono nazwy oraz obie kolejności. Na życzenie użytkownika wprowadzono nazwa1..nazwa6; nowe nazwa7/8 i niewidziane pary pozostały testem. Po pierwszych 100 krokach: ćwiczone przypadki 65→145/216, nowe nazwy 10→24/36, niewidziane pary 8→23/36. Nie jest to pełne opanowanie zasady.
8. Włączono ponownie dawne litery oraz pary mieszane z nazwami numerowanymi. Nie usunięto nazw ani tokenów: ponownie weryfikuje się ich powiązanie z aktualną wartością. Zestaw ma 576 lekcji, obie kolejności, wszystkie trzy stany; połowa batcha to powtórki wcześniejszych zadań.
9. Sprawdzono tokenizer: nazwa1 i nazwa7 mają wspólne tokeny prefiksu, ale różne tokeny cyfr. Nazwy nie są zlewane. Jedna zmienna nazwa1/nazwa7/nazwa8/X dała 12/12; przy dwóch znanych i nowych nazwach błędy pozostają. To wskazuje na problem wyboru powiązania, nie całkowite odrzucenie nowych nazw.
10. Audyt wcześniejszego treningu trzech zmiennych wykazał losowanie nazw i kolejności, więc nie znaleziono tam tego samego stałego AB. Starszy eksperyment resetował embeddingi pojedynczych liter; samo istnienie eksperymentu nie dowodzi, że naprawa obejmuje obecne wagi i nazwy wielotokenowe.
11. Ukończono niezależne testy na wcześniejszym kandydacie po 100 krokach: trzy zmienne 288/486; cztery 3866/7776 (wszystkie wartości, kolejności i pytania); pięć 405/810 i sześć 355/972 (próby losowe ze zrównoważonym stanem i pozycją celu). Żadne pytanie tych prób nie przekroczyło kontekstu. Nie są to wyniki obecnie aktywowanych nowych wag.
12. Na polecenie użytkownika uruchomiono eksperymentalną pętlę odpowiedź → niezależny sprawdzian → dobór rodziny błędów → inne ćwiczenia → test nowych kombinacji → nagroda tylko przy poprawie i zachowaniu wcześniejszych umiejętności. Zewnętrzny kontroler wybiera ćwiczenia; nie jest to jeszcze wyuczony autonomiczny planer. Osobna kontrola losuje zwykłe lekcje: oba warianty 3 rundy po 50 kroków, powtórki i przerwy 120 sekund, ten sam punkt startowy. Wynik końcowy pozostaje do dopisania.

## Zasady kontynuacji i dopisywania wyników

- Zachować wpisy historyczne; dopisywać datowany wynik, wersję/checkpoint, zakres testu, liczbę trafień, wpływ na wcześniejsze zadania i decyzję o aktywacji.
- Oddzielać trening, nowe kombinacje znanych nazw, nowe nazwy i nowe sformułowania.
- Zmiana niepytanego faktu nie może zmienić odpowiedzi; zmiana pytanej wartości powinna ją zmienić. Sprawdzać osobno stan głowicy i tekst odpowiedzi.
- Nie ogłaszać sukcesu na podstawie zapamiętania lekcji, samego pobrania źródeł lub wysokiej pewności.
- Głównego README nie rozszerzać o eksperymentalną zdolność, zanim zostanie niezależnie potwierdzona; podać, czy wynik dotyczy aktywnego rdzenia, kandydata czy modułu.
- Kod, wagi, bazy i surowe logi pozostają lokalnie. Dokumentacja nie zawiera danych uwierzytelniających.

## Próby w toku w chwili zapisu

Trening mieszanych nazw: stan `running`, krok 400; ostatni ukończony test: {"practised": {"n": 576, "correct": 464, "joint_correct": 447}, "new_symbols": {"n": 36, "correct": 24, "joint_correct": 21}, "reversed_order": {"n": 36, "correct": 25, "joint_correct": 21}, "old_names": {"n": 72, "correct": 61, "joint_correct": 60}, "retention": {"n": 66, "correct": 49, "joint_correct": 49}}. Pętla uczenia na błędach: `running`, punkt startowy krok 200. To migawka, nie wynik końcowy.

## Źródło badawcze

[ICML 2025](https://proceedings.mlr.press/v267/wu25j.html).

## Pełny README sprzed aktualizacji

# AI-SI — stan na 11 października 2026

Lokalny, eksperymentalny system SI rozwijany w dwóch trybach: własny uczony rdzeń oraz SI korzystająca z narzędzi. **Kod bieżącej wersji, wagi, bazy i logi pozostają lokalnie. Ta aktualizacja publikuje wyłącznie dokumentację.**

## Własny rdzeń

Aktywny rdzeń ma **1 888 140 parametrów, 9 warstw, wektory o wymiarze 128, słownik BPE 768 tokenów i kontekst 128 tokenów**. Poprzednia wersja miała 903 820 parametrów i 4 warstwy. Rozbudowa zachowała początkowe odpowiedzi, a potem rdzeń przeszedł dodatkowe uczenie.

W tym trybie odpowiedź powstaje z własnych wag, bez kalkulatora, słownika, translatora ani zewnętrznego modelu podczas odpowiadania. Rdzeń ćwiczy krótkie zadania językowe, działania oraz logikę trójstanową: **prawda, fałsz, nieznane**. Jego odpowiedzi są oznaczane jako wymagające sprawdzenia; pewność modelu nie stanowi potwierdzenia poprawności.


| Parametr sieci | Aktywna konfiguracja |
|---|---:|
| Architektura | autoregresyjny Transformer |
| Liczba uczonych parametrów | 1 888 140 |
| Warstwy Transformer | 9 |
| Głowice uwagi w warstwie | 4 |
| Wymiar wektora / embeddingu | 128 |
| Wymiar jednej głowicy uwagi | 32 |
| Słownik BPE | 768 tokenów |
| Maksymalny kontekst | 128 tokenów |
| Dropout podczas treningu | 0,05 |
| Bias w konfiguracji Transformera | wyłączony |
| Głowica stanu logicznego | 3 wyjścia |
| Pomocnicze głowice treningowe | argument: 6 wyjść; operacja: 3 wyjścia |

Liczba parametrów dotyczy rdzenia wraz z jego głowicami; nie obejmuje baz, pamięci, narzędzi ani innych modeli. Głowice pomocnicze nie zastępują samodzielnej generacji odpowiedzi.
## Wyniki i ograniczenia

| Próba | Mniejszy rdzeń | Aktywny większy rdzeń |
|---|---:|---:|
| Te same 120 nowych zadań — poprawne odpowiedzi | 75/120 (62,5%) | 82/120 (68,3%) |
| Zachowanie wcześniejszych umiejętności — 120 zadań | 85,8% | 87,5% |
| Dawny problem z trzema zmiennymi — te same 33 zadania | 20/33 (60,6%) | 20/33 (60,6%) |

Większa wersja poprawiła wynik części prób, ale nie usunęła wszystkich trudności. Wzrostu nie można przypisać wyłącznie pojemności: większy rdzeń otrzymał także dodatkowy trening. Wyniki dotyczą tych konkretnych zestawów, nie ogólnej inteligencji ani pełnego rozumienia języka.

Próg 95% nie blokuje każdego kolejnego etapu ćwiczeń. Przejście dalej może opierać się na powtarzalnej poprawie i zachowaniu wcześniejszych umiejętności. Aktywna wersja pozostaje eksperymentalna. Sam upływ czasu nie utrwala wag; utrwalanie wymaga powtórek i aktualizacji treningowych. Nie potwierdzono, że proponowany rezonans mierzy pojemność lub przyspiesza naukę.

## SI z narzędziami

Osobny tryb zachowuje lokalne moduły:

- interpretację polskich poleceń, liczb i operatorów oraz obsługę części literówek;
- kalkulator naukowy, funkcje, równania, pochodne i całki, działania na macierzach oraz opcjonalne wykresy;
- logikę trójstanową, sprawdzanie nawiasów i walidację wyrażeń;
- uczony moduł argumentów, pamięć i odpowiedzi na podstawie wskazanych źródeł;
- katalog znaczeń Słowosieci, relacje między znaczeniami i kontekstowe rozstrzyganie części wieloznaczności.

Dokładne obliczenia wykonane przez narzędzie są wynikiem narzędzia. Nie oznaczają, że sam rdzeń nauczył się rozwiązywać wszystkie takie zadania.

## Pętla nauki z internetu

Uruchomiono ograniczoną pętlę: **wykrycie braku → pytanie → wybór źródła → przygotowanie ćwiczeń → trening z powtórkami → niezależny test zastosowania → zachowanie albo wycofanie wag**.

Obecny katalog obejmuje dodawanie, odejmowanie, mnożenie, potęgi, wartość bezwzględną i wybrany zakres logiki. Błędy rdzenia decydują o wyborze tematu. Pytania korzystają z przygotowanych form, a rdzeń ocenia kandydatów na źródło. Ta ocena nie jest zweryfikowanym miernikiem wiarygodności. To ograniczony mechanizm wyboru, a nie swobodny planer internetowy.

Źródłami tej próby była oficjalna dokumentacja Pythona. Strony jednego wydawcy nie są dwoma niezależnymi potwierdzeniami. System zapisuje pochodzenie i czas odczytu. Przykłady z poprawnymi odpowiedziami przygotowuje lokalny sprawdzalny mechanizm; pobrany tekst nie staje się automatycznie prawdą ani materiałem do aktualizacji wag.

Powtórki towarzyszą nowym przykładom. Test zastosowania i kontrola wcześniejszych umiejętności są oddzielone od powtórek. Nagroda przysługuje za poprawę zastosowania wiedzy przy zachowaniu wcześniejszych umiejętności, nie za pobranie strony. Nieudana próba przywraca poprzednie wagi.

**Pierwsze dwie rundy zakończono:**

| Wybrany temat | Poprawność przed próbą | Po próbie | Decyzja |
|---|---:|---:|---|
| Dodawanie — 24 nowe zadania | 58,3% | 50,0% | Wycofano nowe wagi |
| Potęgi — 22 nowe zadania | 50,0% | 54,5% | Wycofano nowe wagi |

W potęgach poprawa obejmowała tylko jedno zadanie i wystąpił spadek łącznego wyniku kontroli wcześniejszych umiejętności. Żadna runda nie spełniła warunków utrwalenia; nagroda wyniosła zero. Pętla działa, lecz ta próba nie wykazała skutecznej trwałej nauki z internetu.

## Możliwe zastosowania i nisza systemu

**Proponowana nisza to lokalny asystent do wąskiego zakresu zadań, w którym odpowiedź można sprawdzić, a brak danych jawnie oznaczyć.** Połączenie małego uczonego rdzenia, pamięci źródłowej i dokładnych narzędzi pozwala badać rozumienie poleceń bez powierzania wszystkich obliczeń samym wagom. To propozycja kierunku rozwoju; nie przeprowadzono badania rynku ani wdrożenia potwierdzającego popyt.

| Zastosowanie | Co SI mogłaby wnosić | Stan i warunek użycia |
|---|---|---|
| Lokalny pomocnik matematyczny i edukacyjny | Polskie polecenia, obliczenia, macierze, logika i wykresy; porównanie odpowiedzi rdzenia z wynikiem narzędzia | Funkcje narzędziowe istnieją; szersze zadania i wyjaśnienia wymagają sprawdzania |
| Interfejs do jednego programu lub urządzenia | Zamiana krótkiego polecenia na ograniczony zestaw dozwolonych operacji | Kierunek rozwoju; potrzebne testy rozpoznawania, uprawnień i skutków wykonania |
| Pomocnik do lokalnych instrukcji i dokumentacji | Wyszukanie informacji, wskazanie źródła i wykrycie sprzecznych opisów | Istnieją elementy pamięci źródłowej; potrzebna walidacja na dokumentach konkretnego użytkownika |
| Kontrola kompletności danych i reguł | Rozróżnienie „spełnione”, „niespełnione” i „brak wiedzy”, np. gdy formularz nie zawiera wymaganej wartości | Logika trójstanowa jest dostępna; reguły domenowe i integracja wymagają przygotowania |
| Laboratorium uczenia małych sieci | Pomiar transferu, regresji, wpływu pojemności i skuteczności powtórek; porównywanie kolejnych wag | Obecnie najlepiej udokumentowane zastosowanie własnego rdzenia |

Luka, którą warto sprawdzić w praktyce, występuje tam, gdzie użytkownik ma **powtarzalne, krótkie zadania, własne dane lokalne i jednoznaczny sposób kontroli wyniku**. Przykładem byłby pomocnik do instrukcji warsztatowej: rozpoznaje pytanie, odczytuje właściwy fragment, wykonuje obliczenie narzędziem i sygnalizuje brak potrzebnego parametru. Taki pilotaż wymaga dopiero zbudowania i oceny na nowych pytaniach.

Niewielki rdzeń ułatwia eksperymenty nad uczeniem i kontrolę zmian. Sama liczba parametrów nie dowodzi jednak szybkości, niskiego zużycia energii ani przydatności na konkretnym urządzeniu — to trzeba zmierzyć. Tryb bez internetu może korzystać z lokalnych wag i danych; pętla pobierająca nowe źródła wymaga połączenia.

**Najbliższy krok do zastosowania:** wybrać jedną domenę, zebrać rzeczywiste polecenia i oczekiwane wyniki, oddzielić zestaw testowy od treningu, a następnie mierzyć poprawność, wykrywanie braków, czas odpowiedzi i regresję. Obecny wynik rdzenia nie uzasadnia jeszcze samodzielnego podejmowania decyzji o istotnych skutkach. Najpierw potrzebny jest pilotaż z weryfikacją odpowiedzi.


## Uruchamianie lokalne

W przygotowanej instalacji uruchom `SI_RDZEN_I_INTERNET.bat`. Interfejs działa pod `http://127.0.0.1:8791/`. Można wybrać uczony rdzeń albo tryb narzędziowy. Panel „Nauka rdzenia z internetu” pozwala uruchomić dwie rundy i obejrzeć ich wybory oraz wyniki.

Instalacja wymaga lokalnego środowiska Python, kodu, wag i odpowiednich baz. Publiczne README nie jest pakietem instalacyjnym bieżącej prywatnej wersji. Domyślny rdzeń nie potrzebuje modułów obrazu ani dźwięku.

## Dane leksykalne

Lokalny katalog korzysta ze **Słowosieci / plWordNet 4.2**. Źródło i warunki wykorzystania: [rekord CLARIN-PL](https://clarin-pl.eu/dspace/items/ded4732c-7e3f-4ca8-9794-7a559817ceb3), [licencja plWordNet](https://clarin-pl.eu/license/plwordnet-2/.html). Baza nie jest dołączana do tego pushu.

## Wcześniejsza dokumentacja

Poniżej zachowano wcześniejszy opis projektu. Datowane wyniki dotyczą wskazanych tam wersji i prób; aktualny stan opisano powyżej.

---

# AI-SI

## Aktualizacja — 10 października 2026: kontrola wag i wykonywanie zadań

Poprawiono rozpoznawanie pytań o moduły SI i połączono pamięć rozmowy, obliczenia oraz walidację w ograniczonych poleceniach angielskich, bez Qwena.

- **Pełne odpowiedzi:** 72/72 wcześniejszych pytań w regresji i 6/6 nowych pytań o opis, cel i sprawdzanie modułów.
- **Wykonywanie zadań:** 16/16 przebiegów obejmujących kolejność, wartości z historii użytkownika, zakazy, brak danych i sprzeczności; dodatkowo 28/28 niezależnie obliczonych przykładów.
- **Kontrola własnych wag:** osiem podłączonych modułów; trzy próby, kopie poprzednich wag i ochrona przed regresją. NLI i translator pozostają zamrożone.

Wykonawca korzysta z jawnej, ograniczonej gramatyki i dokładnych narzędzi; nie jest wyuczonym ogólnym planerem. Wyników różnych testów nie sumujemy w benchmark ogólnego rozumienia języka. [Metoda, zakres i dalsze braki](README_DETAILS.md#aktualizacja--10-października-2026-kontrola-wag-i-wykonywanie-zadań).

## Aktualizacja — 9 października 2026: wydzielone SI

Podłączono uczoną semantykę SI, pamięć źródłową w rozmowie oraz pętlę treningu internetowego z podglądem; wyniki, wymagane zależności i ograniczenia opisuje [szczegółowa historia](README_DETAILS.md#aktualizacja--9-października-2026-semantyka-pamięć-i-sesje-internetowe).



[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23222487.svg)](https://doi.org/10.5281/zenodo.23222487)

Eksperymentalny system inspirowany TIMDR jako punktem wyjścia do budowy sterownika współpracy.

## Stan wcześniejszej konfiguracji — 9 października 2026

Własny mały model językowy SI działa bez Qwena, z kontrolą źródeł, mostem sesji, wyborem strategii i ograniczoną obsługą polskiego; wagi języka trenujemy po angielsku. Zadania słowne są sprawdzane na prawdziwych zadaniach z otwartych zbiorów, a polskie pytania obsługuje maper z katalogiem sprawdzonych zdań.

## Aktualizacja — 9 października 2026

- **Fakty w swobodnej rozmowie:** SI sama sprawdza fakty w kilku źródłach: Wikipedii polskiej i angielskiej (czytanej tym, czego nauczyła się w pętli), Wikidanych i Bibliotece Narodowej. Każde źródło jest pokazane z ✓ albo ✗ i adresem. Potwierdza tylko wtedy, gdy zgadzają się co najmniej dwa źródła i żadne nie przeczy. Zamrożony test: 76 ze 126 pytań po angielsku i 78 ze 126 po polsku potwierdzonych.
- **Sieć czytająca (bez Qwena):** mała sieć neuronowa wskazuje w artykule datę albo liczbę odpowiadającą na pytanie o fakt. Uczy się na przykładach ocenionych przez Wikidane jako sędziego; automat rośnięcia zaczyna od 8 neuronów ukrytych i rośnie tylko, gdy rośnie trafność na walidacji (zatrzymał się na 8). Działa tylko tam, gdzie wyuczone wzorce nie znalazły odpowiedzi, i tylko powyżej progu pewności wybranego na walidacji. Zamrożone hasła angielskie 83 → 91 z 215, 0 błędów czytania; model 1,5 MB.
- **Słownik:** „co to jest rakieta?”, „co znaczy …?” → dosłowne znaczenia ze Słownika PWN i Wikisłownika oraz początek hasła z Wikipedii, z adresami.
- **Ciekawość:** gdy SI nie zna odpowiedzi na pytanie o wiedzę, sama szuka w Wikipedii i słowniku („Sama tego nie wiem, ale sprawdziłam…”) i zapisuje brak w dzienniku. Pętla nauki czyta najpierw hasła, o które pytał użytkownik.
- **Jeden koordynator nauki:** nauka z Wikipedii i samopoprawa modułów w jednej pętli; SI wybiera moduł według świeżych braków z rozmów.
- **Dziś i święta:** „jaka dziś data?”, „święta w 2026”, „kiedy Wielkanoc w 2027?” — polskie dni wolne od pracy według ustawy; Wielkanoc liczona dwiema niezależnymi metodami (zgodne dla lat 1583–4099).
- **Poprawianie literówek:** gdy SI nie zrozumie wiadomości, poprawia literówki słownikiem SJP.PL (brakujące polskie znaki, przestawione litery, jedna litera za dużo, za mało lub zamieniona) i pokazuje „Zrozumiałam: …”. Poprawka jest przyjmowana tylko wtedy, gdy na poprawione zdanie odpowiada konkretny moduł.
- **Własne pytania i mapa wiedzy:** SI zapisuje, co sprawdziła, i widzi swoje dziury („znam urodzenie, nie znam śmierci”). Pyta sama o powiązane hasła (nauczyciel, rodzina, miejsce urodzenia, dzieła). Gdy źródła się różnią, szuka wyjaśnienia w artykułach (kalendarz juliański, data chrztu, data nieznana) i rozpoznaje własne błędy czytania. Wybiera to, w czym najszybciej robi postęp. Gdy komputer jest bezczynny, uczy się w tle. W rozmowie: „czego się dowiedziałaś?”, „sprawdź dlaczego”, „co wiesz o …?”.
- **Wiedza o świecie w rozmowie:** „co nowego na świecie?”, „jakie wybory są w tym miesiącu?”, „jakie trwają wojny?”, „co słychać we Francji?”, „ile dni do wyborów w Hiszpanii?” — z mapy wiedzy, którą SI zebrała sama, od razu i bez internetu; fakt potwierdzony na mapie podaje z datą sprawdzenia i źródłami.
- **Samoobsługa modułów:** „co potrafisz?” → lista modułów z przykładami; „jak działa moduł dat?” → opis modułu z jego kodu; „sprawdź się” → SI uruchamia swoje zamrożone testy i sprawdza słownik, pakiety oraz dostęp do źródeł (✓/✗); przy pytaniu bez potrzebnej części (np. bez ścieżki pliku) podpowiada poprawny format.

[Literówki, samoobsługa i Wikisłownik — 8 października](docs/SI_LITEROWKI_I_MODULY_2026-10-08.md) · [Ciekawość, mapa wiedzy, nauka w tle](docs/SI_CIEKAWOSC_2026-10-08.md) · [Sieć czytająca — 9 października](docs/SI_SIEC_CZYTAJACA_2026-10-09.md).

## Aktualizacja — 7 października 2026

- **Most WordNet:** nieznany czasownik w zadaniu słownym jest zamieniany na znany czasownik SI tej samej operacji przez otwarty angielski WordNet, tylko gdy wszystkie znaczenia słowa są zgodne. Nowy test zamrożony przed pracą 208→286/300; 0 błędnych potwierdzeń.
- **Most pytań:** nieznane sformułowanie pytania zamieniane na znane pytanie tej samej klasy. Nowy zamrożony test 247→272/300.
- **Sprawdzian na prawdziwych zadaniach:** na 1730 zadaniach z otwartych zbiorów SVAMP/ASDiv parser trafiał tylko 10%, czyli prawie jak losowanie; mosty działały tylko w świecie własnych szablonów (wynik negatywny).
- **Nowe podejście:** liniowy klasyfikator działania uczony na otwartym MAWPS, wskazówki ról liczb (wynik, stan początkowy, porównanie, grupy) i czytnik kontekstu czytający zadanie słowo po słowie, połączony z modelem ról. Połowa testu nieużywana do strojenia 451→512; w SI prawdziwe zadania 178→944/1730. Odpowiedzi nowego modelu zawsze wymagają potwierdzenia; 0 błędnych potwierdzeń.
- **Polski maper pytań:** katalog sprawdzonych zdań (wzór nauczyciela z 4 października) i czytnik kontekstu po formach SJP.PL. Zamrożony test 44→64/72; „nie rozpoznaję” 21→5, błędne intencje 7→3.
- **Lokalny tłumacz PL→EN:** neuronowy Opus-MT (218 MB, ok. 0,1–0,4 s na zdanie) przed angielskim rdzeniem SI. SI sprawdza, czy liczby i przeczenia przeszły bez zmian. Polskie zadania słowne 24→51/150.
- **Tabele, dokumenty, daty:** nowe moduły liczą na tabelach i arkuszach (CSV, XLSX), odpowiadają na pytania do własnych dokumentów (TXT, MD, DOCX, PDF) z cytatem zdania źródłowego oraz liczą daty i terminy. Każdy wynik jest sprawdzany drugim, niezależnym obliczeniem albo pełnym dopasowaniem pytania do zdania; testy zamrożone przed pisaniem kodu: tabele 15/15, dokumenty 15/16, daty 9/11 (pozostałe poprawnie niepotwierdzone); 0 błędnych potwierdzeń.
- **Nauka z Wikipedii (angielskiej i polskiej):** SI czyta losowe artykuły i sama wybiera, czego się uczy: rodzaj faktu, na którym najwięcej traci, i rodzaj haseł, z których najwięcej się uczy. Wikidata służy tylko jako niezależny sędzia; SI nie zapamiętuje faktów, uczy się czytać — mostów słów („birth” = „born”) i wzorców zapisu dat („( [DATA] –”, „– [DATA]”, „ur. [DATA]”, „zm. [DATA]”). Podmiana tylko po poprawie na zamrożonych hasłach; każdy język ma własną konfigurację; automat rośnięcia poszerza okno wzorców przy zastoju. Zamrożone hasła: angielskie 0 → 77 z 215 pytań, polskie 0 → 87 z 287 (stan 8 października), 0 błędów czytania. Podgląd na żywo z przyciskiem zatrzymania.
- **Pytania o fakty w czacie:** „Kiedy urodził się Mikołaj Kopernik?”, „When did Marie Curie die?” — SI znajduje hasło (polskie pytanie przez polską wyszukiwarkę), wycina odpowiedź z artykułu z cytatem zdania i sprawdza ją w Wikidacie. Potwierdzone tylko przy zgodności obu źródeł; przy różnicy pokazuje obie wartości. Zamrożony test: 62 ze 126 pytań potwierdzonych dwoma źródłami, po polsku i po angielsku.
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
| **Nauka z Wikipedii** | Sama wybiera, czego się uczy; uczy się czytać artykuły po angielsku i po polsku (mosty słów, wzorce zapisu dat); sędzią jest Wikidata; automat rośnięcia, przycisk „Zatrzymaj naukę” | Zamrożone hasła: en 0 → 77/215, pl 0 → 87/287, 0 błędów czytania |
| **Pytania o fakty** | Daty urodzenia, śmierci, wydania i założenia oraz kto teraz pełni urząd (głowa państwa, premier, władze miasta) — z Wikipedii (pl, en), Wikidanych i Biblioteki Narodowej, z cytatem i adresem każdego źródła; przy różnicy pokazuje wszystkie wartości | Zamrożony test: 68/126 po angielsku, 70/126 po polsku, potwierdzone co najmniej dwoma źródłami |
| **Słownik i definicje** | „co to jest X?”, „co znaczy X?” — Słownik PWN, Wikisłownik, początek hasła z Wikipedii | — |
| **Ciekawość** | Gdy nie wie, sama szuka w źródłach i zapisuje brak dla pętli nauki | — |
| **Dziś i święta** | Dzisiejsza data, polskie dni wolne od pracy, Wielkanoc dwiema niezależnymi metodami | 0 rozbieżności metod w latach 1583–4099 |
| **Literówki** | Poprawia literówki i brakujące polskie znaki, gdy nie zrozumie wiadomości; pokazuje „Zrozumiałam: …” | 1311 tekstów z zamrożonych testów: 0 zmienionych odpowiedzi |
| **Samoobsługa modułów** | „co potrafisz?”, „jak działa moduł …?”, „sprawdź się” (autotest ✓/✗), podpowiedź formatu | 1311 tekstów: 0 przechwyconych |
| **Własne pytania** | Mapa wiedzy z dziurami i powiązaniami; pytania z dziur, powiązań, sporów źródeł i świeżych wydarzeń; fakty, które się zmieniają (urzędy, liczba mieszkańców), sprawdza ponownie i zapisuje zmiany; wyjaśnianie sporów; nagroda za postęp; nauka w czasie bezczynności | 1311 tekstów: 0 przechwyconych; test faktów bez zmian |
| **Wiedza o świecie** | Wiadomości, wybory, konflikty, zawody, wydarzenia kraju i miesiąca, ile dni do wydarzenia — z własnej mapy wiedzy | 1311 tekstów: 0 przechwyconych |
| **Odmiana słów** | Lokalna baza SJP.PL (4,69 mln par forma–lemma) jako pierwsze źródło odmian | — |
| **Samouczenie** | Koordynator nauki: przykłady od nauczyciela → sito → automat rośnięcia pojemności → podmiana wag tylko po poprawie | Pierwsze rundy bez podmiany (zabezpieczenie zadziałało) |

Każdy wynik dotyczy opisanego testu.

[Literówki, samoobsługa i Wikisłownik — 8 października](docs/SI_LITEROWKI_I_MODULY_2026-10-08.md) · [Dokładne wyniki — 6 października](docs/SI_AKTUALIZACJA_2026-10-06.md) · [Historia i wcześniejsze konfiguracje](README_DETAILS.md).

Rozmiary — stan 8 października 2026 (zmierzone na plikach, które czat SI wczytuje):

| Składnik | Rozmiar |
|---|---|
| Własne wagi SI (14 plików: model językowy z głowicami tematu, widoku i odniesienia, polski maper i czytnik kontekstu, bramka i głowica trzech stanów, parsery i czytnik zadań słownych, klasyfikator działania, rodziny polskich zadań, sterownik strategii) | **11,20 MB**, **2,81 mln parametrów** |
| Wyuczona wiedza czytania (mosty, wzorce, katalogi zdań; pliki JSON) | **0,37 MB** |
| Lokalny tłumacz PL→EN Opus-MT | **221,6 MB** |
| Lokalny indeks słownika SJP.PL | **154,55 MB** |

To rozmiary składników, nie kompletnego pakietu z Pythonem i bibliotekami.

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


## Zakończenie porównania pętli — 11 października, 19:01 czasu polskiego

Obie próby ukończyły 3 rundy po 50 aktualizacji z tego samego checkpointu200. Testy zastosowania (nowe nazwy, niewidziane pary, dawne nazwy) dały łącznie: przed próbą107/144; pętla rodzin błędów106/144; zwykłe losowanie107/144. Wcześniejsze zadania: przed50/66, pętla48/66, kontrola47/66. Nowe nazwy w obu wariantach24/36. Nagroda0 w obu: nie zachowano wcześniejszych umiejętności. W tej pojedynczej próbie nie wykazano przewagi doboru rodzin błędów. Nie aktywowano wag tych dwóch ramion. Wynik nie wyklucza innych metod uczenia na błędach.

Użytkownik wcześniej polecił aktywować checkpoint400 mimo niepełnego wyniku; wykonano podmianę z kopią zapasową, SHA3319d8b23e77918fa02469ea7ef54e35a019dcc6641f6a17350c33e15f9ce9e1. Dalszy trening działa niezależnie od podmiany wersji w czacie. Checkpoint500 miał52/66 wcześniejszych zadań, ale został nadpisany600; nie zachowały się jego dokładne wagi. Ujawniono błąd użytkownikowi. Uruchomiono osobny watcher, który archiwizuje przyszłe ukończone checkpointy i aktywuje wersje z poprawą przy braku spadku łącznej trafności trzech testów zastosowania oraz minimum51/66 wcześniejszych zadań. Checkpoint600 zachowany osobno, nieaktywowany. Dalszy główny trening w toku.


## Przywrócenie wpisu kroku 500 na końcu historii

Na polecenie użytkownika ponownie odnotowano wynik kroku500: lekcje484/576, nowe nazwy24/36, niewidziane pary24/36, dawne nazwy60/72, wcześniejsze zadania52/66. To archiwalny pomiar, a nie obecny krok treningu. Dokładnych wag500 nie ma w dostępnych checkpointach ani kopiach aktywacji; zapis został nadpisany600. Nie wykonano fikcyjnego przywrócenia. Aktywne wagi400; dalszy trening i archiwizowanie kontynuują.


## Restart od aktywnych wag400 z pełnym cyklem powtórek nazw

Użytkownik wyjaśnił, że prosi o ponowne ćwiczenie nazw, nie odtworzenie nieistniejącego checkpointu500. Następnie autoryzował przerwanie próby i start od400. Zatrzymano poprzedni trening i watcher, zachowano jego ostatni checkpoint oraz wynik w SI_przed_powtorkami_od_400.json. Nowa próba zaczyna od aktywnych wag400 i świeżego optymalizatora (nie zachowano optymalizatora400). Licznik401i dalej. Do każdego batcha32 dodano8systematycznych lekcji z576przypadków: oba porządki, wszystkie3stany, stare litery, nazwy numerowane i ich mieszane pary. Jeden pełny cykl powtórek trwa72aktualizacje. Testy nowych nazw i niewidzianych par pozostają poza lekcjami. Watcher archiwizuje nowe checkpointy w osobnym katalogu checkpoints_repetition_from_400, żeby nie nadpisać wcześniejszych prób o tych samych numerach. Aktywacja po sukcesie autoryzowana przez użytkownika; kopia każdej poprzedniej aktywnej wersji. Odczyt kontrolny: nowy trening425, monitor działa, brak jeszcze ukończonego testu500 nowej próby.


## Naprawa reakcji na pytaną nazwę — wyniki 700 i 800

Na aktywnych600 przeprowadzono diagnostykę:54/54 parpytań dawały identyczną odpowiedź po zmianie celu, w tym36/36parzróżnymiwartościami. Uruchomiono na polecenie użytkownika uczenie parami tych samych faktów i różnych celów z różnymi poprawnymi etykietami, obiema kolejnościami i pomocniczą stratą rozdzielającą logity poprawnych stanów. Każdy batch16lekcji+16replay. Checkpointy osobno checkpoints_query_repair. Wynik700:496/576lekcje,25/36nowe,25/36niewidzianepary,60/72dawne,50/66retention. Wynik800:494/576lekcje,23/36nowe,25/36niewidzianepary,60/72dawne,50/66retention. Oba zapisane, nieaktywowane; aktywne600. Użytkownik wyraźnie polecił kontynuować także przy pogorszeniu800. Autoryzowana podmiana po rundzie bez pogorszenia każdego oddzielnego testu i retention, remisy dopuszczone. Przerwy120sekund pozostają. Osobna diagnostyka reakcji na pytanie800 w toku.
`nDiagnostyka checkpointu800 zakończona: przy różnych wartościach zmiana pytanej nazwy zmieniła odpowiedź w3/36par (wcześniej0/36); obie odpowiedzi poprawne w1/36par. Jedna nowa nazwa pozostaje12/12. Źródło: SI_pytana_nazwa_800.json.


## Trening z pomocniczym wskazaniem właściwego faktu

Na polecenie użytkownika zatrzymano kontrastowy trening po900 i uruchomiono od zapisanych600 nową próbę z dwiema projekcjami128x128, wyłącznie podczas treningu. Queryhiddenstate porównywany z hiddenstate początków wartości dwóch faktów, niezależna etykieta wskazuje fakt pytanej nazwy. Cel pomocniczy uczy rdzeń; projekcje nie są eksportowane do natywnego modelu i nie zastępują jego odpowiedzi. Dodatkowe32768parametrów treningowych poza1888140rdzenia. Checkpointy zapisują projekcje i optimizerz2grupami. Poprawiono wznowienie, żeby zachowywać oba. Wyniki700:490/576lekcje,24/36nowe,24/36pary,60/72dawne,49/66retention. Wyniki800:491/576lekcje,23/36nowe,23/36pary,60/72dawne,51/66retention. Wagi zapisane, aktywne600. W kroku850 wskazanie prawidłowe16/16na ostatniej porcji treningowej, strata0,03; to nie jest niezależny test uogólnienia. Osobny test wskaźnika vs końcowej odpowiedzi na checkpoint800 uruchomiony, wynik do dopisania w SI_wskaznik_a_odpowiedz_800.json. Trening kontynuuje.
Test wskaźnika800 zakończony: A/B, E/M, M/E — wskaźnik15/18 i odpowiedź18/18 w każdej parze; nazwa1/nazwa2 — wskaźnik9/18 i odpowiedź12/18; nazwa7/nazwa8 — wskaźnik8/18 i odpowiedź11/18; odwrotnie — wskaźnik9/18 i odpowiedź12/18. Wynik różni rodziny nazw, nie dowodzi jeszcze mechanizmu przyczynowego.

## Nazwy wieloczęściowe — pomiar 1200 (2026-10-11)
Kontynuacja od checkpointu 900 z zachowaniem wag, projekcji i optymalizatora. Sześć z ośmiu par na batch dotyczy nazw numerowanych; dodatkowy cel stanu na ostatnim tokenie pytanej nazwy. Nazwa7 i nazwa8 pozostają wyłącznie testowe. Pięciominutowa pauza zachowała stan procesu i zakończyła się automatycznym wznowieniem.
Runda 1100: lekcje 492/576, nowe nazwy 24/36, niewidziane pary 24/36, dawne nazwy 60/72, retention 48/66. Runda 1200: odpowiednio 491/576, 23/36, 24/36, 59/72, 48/66. Checkpoint: work/continuous_binding/checkpoints_multitoken_repair/step_1200.pt. Oba zapisy zachowane, nieaktywowane; aktywne 600.
Osobna diagnostyka 1200: A/B, E/M, M/E — wskaźnik 15/18, odpowiedź 18/18 w każdej rodzinie; nazwa1/nazwa2 — 9/18 i 12/18; nazwa7/nazwa8 — 9/18 i 12/18; odwrotnie — 9/18 i 11/18. Raport SI_wskaznik_a_odpowiedz_1200.json. Dodatkowy cel nie usunął dotąd trudności z nazwami wieloczęściowymi. Trening trwa; brak dowodu opanowania wiązania nowych nazw.

## Kontrolowana diagnostyka pamięci — 2026-10-11
Trening zatrzymany. Wykonano 552 przypadki na aktywnych600 oraz552 na checkpoint1200: zmieniano rodzinę nazw, kolejność, wartości, położenie dodatkowego tekstu i jego treść. Bez aktualizacji wag. Testy obejmują powtórzenia kontrolne, nie1104niezależne zadania. Sprawdzono zgodność trzech wyników batchowych z publiczną funkcją natywnej odpowiedzi:3/3.
Pary różnych wartości z pytaniem o oba cele: A/B i E/M po12/12par z obiema odpowiedziami poprawnymi na obu modelach. X/Y:0/12takichpar na obu; odpowiedź nie zmienia się po zmianie celu. Nazwa1/nazwa2:0/12 na obu. Nazwa7/nazwa8:0/12 na600 i1/12 na1200. Nazwy pojedynczych faktów:wszystkie24unikalne podstawowe zadania poprawne na obu modelach (w raporcie90wierszy z powtórzeniami kontrolnymi).
Sześć powtórzeń tekstu „tekst.” przed faktem:60015/24,120016/24; między faktem a pytaniem:60010/24,12009/24. Porównanie zachowuje całkowitą treść i długość, ale zmienia pozycje, odległość i lokalne sąsiedztwo — nie izoluje samej odległości. Dodatkowe niepytane fakty również wpływają na wynik.
Wniosek:brak uogólnienia wiązania nazw z wartościami, nie wyłącznie wielotokenowe kodowanie. Wagi rozróżniają pewne rodziny nazw, inne ignorują mimo pojedynczych tokenów. Dodatkowy trening900..1200 nie usunął mechanizmu błędu. Budowa umożliwia poprawne wiązanie w pewnych przypadkach; badanie nie wyklucza jej wpływu na trudność uczenia. Następny etap powinien sprawdzać rozpoznanie pełnej tożsamości nazwy oraz wybór i kopiowanie wskazanego faktu na nowych rodzinach nazw, z osobnym testem treści rozpraszającej. Nie zwiększać pojemności ani kontynuować niezmienionej próby bez nowego pomiaru. Raport SI_kontrolowany_test_pamieci.json; kontrola SI_kontrola_testu_pamieci.json. Brak aktywacji.

## Nocna naprawa dokładnego kopiowania — uruchomienie
Na polecenie użytkownika uruchomiono monitorowanie i kontynuację naprawy. Próba podstaw nazw zakończona po200:copy0/14,select_name0/14,single34/42,new17/36,reverse16/36,old59/72,fresh55/108,retention45/66; brak aktywacji. Diagnostyka wskazuje zastępowanie nazw znanym wariantem, np.nazwa1/nazwa2/nazwa7->nazwa4,X/Y->U.
Nowy eksperyment work/train_exact_copy_repair.py od kopii aktywnych600, zapisy work/exact_copy_repair, raport SI_dokladne_kopiowanie.json. Losowe świeże kombinacje znaków i zmienne końcówki10..999 zamiast zamkniętej listy nazw. Pełne nazwy testowe wykluczone. lr3e-5,50%replay i distillation względem zamrożonego źródła. Kontrole100,przerwy120s,maks1200; automatyczny stop do diagnozy przy braku postępu kopiowania po300. Wiązanie faktów dopiero po opanowaniu obu testów kopiowania14/14. Podmiana tylko bez regresji każdego testu, backup każdej aktywacji. Użytkownik idzie spać; monitor ma powiadamiać wyłącznie znaczący postęp, ukończenie, awarię lub potrzebę decyzji. Bez obietnicy wyniku. Wagi600 zachowane jako źródło, kod i wagi lokalne.

## Dokładne kopiowanie — rundy100 i200, diagnostyka częściowa
Eksperyment exact_copy_repair działa; ostatni odczyt275. Rundy100/200:copy0/14,select_name0/14;single38/42,new24/36,reverse24/36,old60/72,fresh71/108 następnie72/108,retention48/66 następnie47/66. Brak aktywacji. Diagnoza źródło vs200 na12nazwach: model źródłowy generował prawda/nieznane zamiast nazwy;200generuje fragmenty nazw (obiekt7->obiekt,nazwa7->nwa). Teacher-forced loss spadł na wszystkich12próbach, np.obiekt7:14,09->1,49 i poprawne6/7tokenów przy podanym poprawnym prefiksie. To postęp częściowy, nie poprawne samodzielne kopiowanie. Raport SI_dokladne_kopiowanie_diagnostyka.json. Dlatego automatyczny stop przy0exactpo300 nie wystarczy do oceny stagnacji: po zakończeniu należy sprawdzić checkpoint300 i rozważyć wznowienie z zachowaniem optymalizatora, oceniając również generację fragmentów i błędy zakończenia. Nie resetować do źródła bez potrzeby. Aktywne600 chronione, proces nieprzerwany.

## Kopiowanie —300 i krótszy program nauki
Exact_copy_repair zakończony po300:copy0/14,select0/14,single37/42,new22/36,reverse23/36,old60/72,fresh72/108,ret47/66; brak aktywacji. Diagnostyka300 potwierdza częściowy postęp generacji względem200: name7->name,kod7->kod,obiekt7->obiekt; teacher-forced CEodpowiednio1,16/1,04/1,05. To nie dokładne kopiowanie;0exactnieoznacza braku każdej zmiany. Próba zakończona i zapisy zachowane.
Uruchomiono train_copy_short_curriculum.py z wagami i optymalizatorem300; nauczyciel600. Świeże krótsze ciągi1..3znaki do600, potem1..6; końcówki0..99 zamiast10..999. Pełne nazwy testowe nadal wykluczone. lr3e-5,replay50%+distillation. Raport SI_kopiowanie_krotkie.json; checkpointy copy_short_curriculum. Maks1200,kontrole100,pauzy120sekund; brak pełnego kopiowania po700 wymaga diagnozy. Bezpodmiany aktywnych600;monitor zaktualizowany.

## Krótsze nazwy —400 i500
Runda400:copy0/14,select_name0/14,single36/42,new22/36,reverse22/36,old61/72,fresh70/108,ret48/66. Runda500:copy1/14,select_name3/14,single36/42,new22/36,reverse22/36,old61/72,fresh68/108,ret48/66. To pierwsze dokładne poprawne odpowiedzi na pełnych nazwach testowych wykluczonych z nauki; mały zestaw i pojedyncza runda nie potwierdzają opanowania ani stabilności. Checkpointy400/500zachowane wwork/copy_short_curriculum. Brak aktywacji ze względu na regresję części testów; aktywne600. Treningcopy_identitydalej działa; międzyrundowa pauza120s pozostawiona.

## Krótkie kopiowanie —600/700 i kontrola generacji
Runda600:copy3/14,select4/14,single36/42,new22/36,reverse22/36,old61/72,fresh67/108,ret46/66. Runda700:copy3/14,select4/14,single36/42,new22/36,reverse22/36,old59/72,fresh64/108,ret46/66. Zapisy600/700wcopy_short_curriculum,brakaktywacji;aktywne600 źródłowe. Odczyt procesu775, nadal działa.
Osobna diagnoza700:poprawne pełne nazwa7 i kod7;name7->name8,obiekt7->obiekt6,v7->v6. Nazwy losowe XY/Ab3/kL9 nadal zastępowane innymi ciągami. W porównaniu300 poprawa generacji i teacher-forcedCEdla rodzin nazw, ale ogólna reguła kopiowania arbitralnych ciągów nieopanowana; pojedyncza seria14nazw to mały test. Raport SI_kopiowanie_diagnostyka700.json. Dalsza bieżąca próba ograniczona do1200; monitor pozostawiony. Po ukończeniu rozdzielić błędy cyfr od błędów identyfikacji liter, ocenić pełną generację na świeżym nietuningowym zestawie, przed nowym etapem lub aktywacją. Nie resetowano optymalizatora ani postępu.


## Krótkie kopiowanie — ukończone rundy800..1000
Krok 800: copy 3/14, select_name 4/14, single 36/42, new_symbols 22/36, reversed_order 22/36, old_names 58/72, fresh_families 66/108, retention 44/66; aktywacja: False.
Krok 900: copy 3/14, select_name 4/14, single 36/42, new_symbols 22/36, reversed_order 22/36, old_names 57/72, fresh_families 65/108, retention 46/66; aktywacja: False.
Krok 1000: copy 5/14, select_name 4/14, single 36/42, new_symbols 22/36, reversed_order 22/36, old_names 58/72, fresh_families 68/108, retention 45/66; aktywacja: False.
Checkpointy zachowane. Aktywne wagi600. Najnowsze kopiowanie5/14, wybór4/14; to postęp na monitorowanym zestawie, nie potwierdzenie opanowania. Retention45/66 poniżej bazowych51/66. Próba działa, pauza120s po1000; zakończenie zaplanowane1200. Dalsze etapy wymagają osobnego pomiaru świeżych nazw i analizy kompromisu kopiowanie/retention, nie samego przedłużenia tego programu.

## Zakończenie krótkiego kopiowania1200; sonda i końcówki
Runda1100:copy5/14,select4/14,single36/42,new22/36,reverse22/36,old58/72,fresh68/108,ret46/66. Runda1200:copy4/14,select4/14,single36/42,new22/36,reverse22/36,old57/72,fresh67/108,ret46/66. Proces zakończył próbę, wszystkie zapisy zachowane, brak aktywacji.
Przeprowadzono sondę liniową zamrożonych reprezentacjiostatniejcyfry:210przykładów do dopasowania sondy,90nowych końcówek i100nowyprefixv. Przy źródłowych600:na końcu nazwy71/90 i29/100;na pozycji generacji59/90 i12/100. Przy1200:67/90 i19/100;na pozycji generacji45/90 i12/100. Raport SI_reprezentacja_koncowki.json. Sonda nie jest modułemodpowiedzi;odczytywalnośćnie dowodzi przyczynowego użycia. Wynik niepotwierdza ogólnej poprawy reprezentacji końcówki, choćkopiowanie części nazw siępoprawiło.
Uruchomiono train_copy_suffix_repair.py od1200zoptymalizatorem, nauczyciel600. Zadanie pełnego kopiowania i odczytu ostatniegoznaku;75%replay+2xdistillation. Zapisycopy_suffix_repair,raportSI_kopiowanie_koncowek.json. Maks1800,kontrole100,pauzy120s;aktywacja wyłącznie bezregresjiwszystkichtestów. Monitorzaktualizowany;aktywne600zachowane.


## Końcówki — runda1300
Checkpoint work/copy_suffix_repair/step_1300.pt zachowany. last_character0/14,copy4/14,select_name4/14,single36/42,new23/36,reverse22/36,old58/72,fresh66/108,retention44/66. Brak aktywacji; źródłowe600 pozostają aktywne. Trener działa, pauza120sekund po kontroli. Pierwsza runda nowego zadania nie wykazała poprawnego odczytu końcówki; nie deklarowano poprawy.


## Końcówki —1400 i diagnostyka
Runda1400:last_character0/14,copy4/14,select4/14,single36/42,new24/36,reverse24/36,old59/72,fresh68/108,ret46/66;checkpoint zachowany,nieaktywowano. Trener działa (odczyt1450). Osobna diagnostyka1400 na12nazwach daje A->A,name456->6 poprawnie, ale większość nazw z inną cyfrą również->6, częśćpuste. To zgadywanie dominującego wyjścia w tej próbce, nie odczyt końcówki. RaportSI_koncowki_diagnostyka1400.json. Po ograniczonej próbie1800 należy sprawdzić zbilansowanie cyfr i reakcję na minimalną zmianę ostatniegoznaku przy stałymprefixie, zamiast uznawać znajomość typu odpowiedzi za umiejętność odczytu. Wagi600bez zmian.


## Końcówki — ukończona runda1500 (12 października, czas Warszawy)
last_character0/14,copy4/14,select_name6/14,single36/42,new24/36,reverse22/36,old58/72,fresh67/108,ret44/66. Checkpoint zachowany wcopy_suffix_repair,brakaktywacji. Odczyt report.step1600 oznacza trwającą następną kontrolę;historyjeszcze1500. Nie uznano wartości latestza ukończony1600. Trener nadal działa; aktywne600zachowane. Poprawa select_name4->6 na małejpróbce, lastcharacterbezpoprawy.


## Końcówki1600/1700 i mikropróba pojemności
1600:last0/14,copy4/14,select5/14,single36/42,new23/36,reverse22/36,old58/72,fresh70/108,ret44/66.1700:last0/14,copy4/14,select5/14,single36/42,new22/36,reverse22/36,old56/72,fresh68/108,ret44/66. Oba zapisy zachowane,bez aktywacji;trening działa, limit1800.
Uruchomiono oddzielną diagnostyczną mikropróbę work/micro_suffix_capacity.py (sesja35481),na kopii1700:20nazw,wszystkie10cyfr zbilansowane,dwa prefixy. 200aktualizacjiCE odpowiedzi;testtrainvsnowekońcówki/nowyprefix/krótkienazwy. To diagnostyka zdolności dopasowania i uogólnienia,bezaktywacji,bezreplay;nieprzeznaczona do wdrożenia. RaportSI_mikroproba_koncowki.json;checkpointdiagnostycznywork/micro_suffix_capacity/diagnostic.pt. Na następnym monitorze sprawdzić ukończenie, nie powielać procesu i nie mylić dopasowania20nazw z generalizacją.


## Zakończenie1800; mikropróba i kontrolowany treninguwagi (12października)
1800:last1/14,copy2/14,select5/14,single36/42,new23/36,reverse22/36,old57/72,fresh72/108,ret46/66;bez aktywacji,proceszakończony. Mikropróba200:updateCEna20stałych nazwach zdziesięciomacyframi:train20/20,nowesuffix5/20,nowyprefix2/10,short1/10. To dowód dopasowania20przykładów, nieopanowaniaoperacji. Checkpoint mikropróbyzachowany,nieprzeznaczony doaktywacji.
Nowatrain_attention_copy_repair.py(sesja81661):kontynuuje wagi1800, nowyoptimizer zpowoduzmianyzestawuparametrów;uczytylkoprojekcjeuwagi,embeddingi/MLP/headszamrożone. Dziesięć przykładówna jednymświeżymstem,każdacyfra0..9raz,6pełnychkopiowań,48replay+2xdistillation600. Testrek101..140,całyprefixrekwykluczonyznauki. RaportSI_uwaga_koncowki.json,zapisyattention_copy_repair,maks2400,pauzy120s,kontrole100. Nie deklarowanoskuteczności, aktywne600zabezpieczone. Następnymonitor ma sprawdzić poprawnośćprocesuiwyniki,nieuruchamiaćstarszychtrenerów.


## Uwaga — runda1900
Fresh_last_character4/40,last_character0/14,copy4/14,select4/14,single36/42,new24/36,reverse22/36,old57/72,fresh72/108,ret44/66. Checkpoint1900 zapisany wattention_copy_repair,brakaktywacji. Wynik4/40samw sobie nie przekracza poziomu trafień stałą cyfrą w zbilansowanym zestawie10cyfr;nieuznano go za opanowanie odczytu. Trener działa, odczyt1925;aktywny600bezpodmiany.


## Uwaga — runda2000
Freshlast4/40,last0/14,copy4/14,select4/14,single36/42,new24/36,reverse22/36,old59/72,fresh71/108,ret44/66. Checkpoint2000zapisany,bez aktywacji. Trener działa,odczyt2050. Nieuznano4/40za poprawę reguły, ponieważ wynik odpowiada stałejcyfrze w zbilansowanym teście. Aktywne600bez zmian.


## Uwaga — rundy2100/2200
2100: fresh_last_character 4/40, last_character 0/14, copy 3/14, select_name 4/14, single 35/42, new_symbols 22/36, reversed_order 22/36, old_names 59/72, fresh_families 72/108, retention 44/66; aktywacja False.
2200: fresh_last_character 4/40, last_character 0/14, copy 3/14, select_name 4/14, single 34/42, new_symbols 23/36, reversed_order 22/36, old_names 58/72, fresh_families 72/108, retention 45/66; aktywacja False.
Trener żywy, pauza120s po2200;checkpointy zachowane,aktywne600. Freshlast4/40 nadal zgodne z trafianiem jedną stałą cyfrą; brak dowodu poprawy generalizacji. Zaplanowane zakończenie2400 bez nieuzasadnionego przedłużania tej samej konfiguracji.


## Uwaga2300 i dodatkowy audyt tokenizacji
Freshlast4/40,last0/14,copy3/14,select4/14,single34/42,new24/36,reverse21/36,old58/72,fresh72/108,ret44/66. Brak aktywacji,checkpoint2300zachowany,trenerżywy2350;kontrola2400dopieroprzednim.
AudytSI_tokeny_koncowek.json:rek101->re,k,10,1;rek107->re,k,10,7;abc170->a,b,c,17,0. W obecnym zbilansowanymtreningu końcowyznakjestosobnymtokenem. Natomiast mikropróba nazwa10..19 miała10/19 jako połączonytoken:jej20/20może obejmować mapowanie całego tokenu liczby na cyfrę, więc nie należy porównywać wprost z odczytem oddzielnego tokenu. To nowa kontrola interpretacji,nie dowód jednej przyczyny. Po końcu2400należy oddzielić treningkopiowania pojedynczego tokenu od dekompozycji tokenu zawierającego kilka znaków; testgeneralizacjiwłasnychformatów,niepojemnośćbezpomiaru.


## Koniecuwagi2400; pojedynczytoken
2400:freshlast4/40,last0/14,copy0/14,select3/14,single34/42,new22/36,reverse20/36,old58/72,fresh72/108,ret45/66. Proces zakończony, zapis2400zachowany,bezaktywacji. Konfiguracjiattention-onlynieprzedłużono.
Uruchomionosekwencyjnemikropróbywork/micro_single_digit.py iwork/micro_digit_attention.py(sesja12316). Obiekopieźródłowych600,10jednocyfrowych nazw0..9,300aktualizacjiCE,te same dane/seed;armfullbackbonevsattention-only. Natywne poleceniePodajostatniznaknazwy;przyjednocyfrowejnazwie jestkopiowaniem jejtokena. Testprefixynazwa/name20,rek10,v10niewidzianewdopasowaniu. RaportySI_mikroproba_pojedynczej_cyfry.json iSI_mikroproba_cyfry_tylko_uwaga.json. Checkpointydiagnostyczne nieaktywować:brakretentionorazuczenienamałymstałymzbiorze. Potrzebnazakończonaocena obuarmówprzedkolejnązmianą;nie dublowaćtrwającejsekwencji. Monitorzaktualizowany;aktywny600bez zmian.


## Pojedynczacyfra — porównanie zakończone; kontekstznaku
Full300:train10/10,newprefixname/nazwa1/20,rek1/10,v0/10. Attention-only300:train8/10,name/nazwa2/20,rek0/10,v0/10. Obaodźródłowych600,zachowane,bezaktywacji. Proste10przykładówdopasowano,brakprzeniesieniaregułydozmienionegootoczenia;uwaga-onlyniewystarczyła.
Uruchomiono train_character_context.py:kopiamicro_single_digit300,nauczyciel600,nowyoptimizer(brakzapisuoptimizera wdiagnostyce),10cyfrnazmiennymprefixie1znakudo500,potem1..3;6losowychkońcówekliterowych/cyfrowych;48replay+2xdistillation. Pełne nazwytestowe wykluczonezobustrumieni(przed naukąpoprawionowykrywaniekolizji). Testone_prefixv0..9,maks900,kontrole100,pauzy120s,zapisycharacter_context_curriculum,raportSI_znak_kontekst.json. Aktywne600chronione;mikroźródłonieaktywowane. Monitorzaktualizowany.


## Znakw kontekście —400
One_prefix1/10,last1/14,copy0/14,select0/14,single35/42,new24/36,reverse24/36,old59/72,fresh64/108,ret47/66. Checkpoint400zapisanywcharacter_context_curriculum,bez aktywacji. Procesżywy,pauza120s. Pojedynczegotrafienia1/10wzbilansowanym teście nieuznanoza dowódgeneralizacji; aktywne600bez zmian.


## Znakw kontekście —500
One_prefix3/10,last2/14,copy0/14,select0/14,single36/42,new24/36,reverse24/36,old59/72,fresh69/108,ret45/66. Checkpoint500zachowany,bezaktywacji. Trenerżywy550. Wynik na10cyfrach większy od pojedynczej stałejodpowiedzi,ale mały zestaw i brakniezależnego potwierdzenia nieuprawniajądo deklaracjiopanowania. Przechodzi do1..3znakówprefixu wedługprogramu;kontrole i ochrona aktywnych600pozostają.


## Znakw kontekście —600 i kontrola końcówek7/8
One_prefix2/10,last5/14,copy0/14,select0/14,single35/42,new23/36,reverse24/36,old56/72,fresh69/108,ret45/66. Brak aktywacji,zapis600zachowany,trenerżywy675.
Osobna diagnostykaSI_znak_diagnostyka600.json:pięćrodzinnazwkończącychsię7 daje7poprawnie;końcówka8daje9wczterechrodzinach iIgawjednej. X/Y/Z/M->3. Wynik5/14niemówi o ogólnymopanowaniu;jednakniejestidentyczną stałąodpowiedziąnawszystkichwejściach,widać reakcję na zmianęcyfry,częstobłędną. Kontynuacjaograniczonejpróbydo900,aktywny600źródłowyniezmieniony.


## Powrót400 na polecenie użytkownika; odnaleziona baza sprzed testów
Treningcharacter_contextzatrzymany. Dokładny400 SHA3319d8b23e77918fa02469ea7ef54e35a019dcc6641f6a17350c33e15f9ce9e1 przetestowanyidentycznymzestawem:one_prefix0/10,last0/14,copy0/14,select0/14,single37/42,new24/36,reverse24/36,old60/72,fresh73/108,ret49/66. RaportSI_powrot400_test.json.600baseline:single38,fresh72,ret51;pozostałe wynikitestsjak400. Powrót400wyraźnieautoryzowanyprzezuser,nieautomatycznydowódniergresji. Kopia600przedprzywróceniem.
Userpytao wagisprzedtestu (punkt0):odnalezionobackup latest_user_activation_1791737123274238100/model.safetensors,SHA8026c2efc0214372873b86b904eb7d1300761b56c2f765212cb9cd2321117762. To wcześniejszywyuczonyrdzeńsprzedciągłegouczeniawiązanianazw,nie losowa nieuczonainicjalizacja. Zachowany,niepodmienionyautomatyczniezapytańoistnienie.


## Wagi0 — identyczny test i przejścia odpowiedzi
Userpoleciłtestod0,podejrzewa niechcąceutrwalenie błędu. Dokładnycheckpoint0SHA8026c2efc0214372873b86b904eb7d1300761b56c2f765212cb9cd2321117762 przetestowanybeztreningu:one_prefix0/10,last0/14,copy0/14,select0/14,single38/42,new21/36,reverse20/36,old60/72,fresh71/108,ret51/66. RaportSI_wagi0_test.json.400:new24,reverse24,old60,fresh73,ret49.600:new24,reverse24,old60,fresh72,ret51. Brakogólnegoopanowaniakopiowaniaprzedpróbami.
Porównano wszystkieidentyczneprzykłady0vs400,nie tylkoaccuracy (SI_porownanie0_400_600.json):new8poprawnych0stałosiębłędnew400,11błędnych0stałosiępoprawnew400;reverse8regresji/12popraw;old9regresji/9popraw (oba60/72ukrywająinne błędy);fresh15regresji/17popraw;retention9regresji/7popraw. To potwierdza konkretnewprowadzoneregresjeprzezuczenie,ale częśćbłędówistniała jużw0,a części przypadków naukapomogła. Nieustala przyczynykonkretnegomechanizmu. Aktywne400nadalzwyboruuser,0tylkoprzetestowano;nieuruchomionotrenera.


## Naprawaod0 z ochroną konkretnych odpowiedzi
Na polecenieróbco trzeba uruchomiono work/train_binding_guarded0.py(sesja17357),raportSI_wiazanie_od0_ochrona.json,zapisybinding_guarded0. Startodwyuczonego0SHA8026...,aktywny400pozostaje.16lekcji paramitesamefakty/różnepytaniaróżnewartości+32replay,lr2e-5,distillation0. Dodatkowy kontrast NATIVELOGITÓWpierwszego tokenupoprawnejodpowiedzi,niewskaźnikpomocniczy. Kontrole100,pauzy120s,maks400. Chronione317unikalnychpytań poprawnychw0LUB400;nieużywanedotrenowania,evalpokazujekonkretneprotected_failures,zamiastsamegoaccuracy. Skryptnieaktywujeautomatycznie;przedwdrożeniemniezależneświeżezadania,niergresjametrykvsaktywny400i0chronionychbłędów,backup.
Userpodkreśliłmożliwośćwewnętrznejkopiiwektorowejbezodtworzenia1:1,i poleciłkontynuować. Rozdzielamywiernośćzapisu od tożsamościobiektu i poprawnościodczytufaktu. Nieuznajemy0/14kopiowaniazadówodbrakureprezentacjiznaczenia;nieprzyjmujemyteżżewewnętrznakopiajestpoprawnabeztestu. Obecnatreningwiązanienie wymagaopanowaniacharcopyjako bramki. Powiadamiajtylkoistotnepostępy,chronioneaktywny400iwszystkiedawnecheckpointy.


## Polecenie bez przerw i stop przy regresji
Na wyraźnepolecenie usera przerwanostaryguarded0przyodczycie75,przedpierwszymzapisem100;niezapisanych75krokówniezachowano,wyjaśnionouserowi. Nowytrain_binding_no_pause0.py(sesja25867)odkopii0,raportSI_wiazanie0_bez_przerw.json,zapisybinding_no_pause0. Żadnychsleep;zapis i pełnytestco25,max400. Zatrzymuje pierwszą utratękonkretnejpoprawnejodpowiedzisource0;po udanejkontrolirozszerzachroniony zbiórnowymi poprawnymi. Union317poprawnych0lub400pozostajebrama przyszłejaktywacji,niemożnago użyćjako nowejregresjistart0,bo częśćbaselinebłędówjużistnieje. Raportrozróżnianew_regressions odprotected_failures. Aktywne400chronione,skryptnieaktywuje. Monitorzaktualizowany:po stopieregresjiniewznawiaćuczeniaautomatycznie,tylkodiagnozaiwynik;warunekstopuusera ma pierwszeństwo.


## Stop na regresji —25 bezprzerw
Próba train_binding_no_pause0.py zakończyłasięautomatycznieprzy25:19odpowiedzipoprawnychwsource0stałosiębłędne. Zapiswork/binding_no_pause0/step_25.ptzachowany. New20/36 vs0baseline21,reverse20/36bezsumarycznejzmiany,old60/72bezsumarycznejzmiany,fresh73/108vs71,ret51/66bezsumarycznejzmiany. Te sumy ukrywająregresjepojedynczychprzykładów;ochronaperprzykładadziała. Brakaktywacji,aktywny400bez zmian. Warunekhumanprzerwijjakregresjaspełniony;nieuruchomionokolejnego treningu. AutomatykazmienionanaPAUSED do nowegopolecenia. RaportSI_wiazanie0_bez_przerw.jsonzawierakonkretnenew_regressions.


## Odtworzenie dawnej metody nazw od0
Userwyraźnieautoryzowałkolejnąpróbę jakdawne400,uznającże poprzednianiepowtarzałatejmetody. Uruchomiono train_names_original_method0.py(sesja36817),adaptację zachowanegotrain_continuous_binding_before_repetition.py.576lekcjiA..F/nazwa1..6/parymieszane,obakolejności,3wartości,batch16lekcji+16replay;CEodpowiedzi+.35stateCE,AdamW1e-4,wd.01,clip1;operand/operationheads zamrożone. Nie kontrast,nie kopiowanieznaków,nie distillation,nie nowehelpery. Źródłowy0work/retest0/source.ptzweryfikowanySHA8026...,optimizerświeżybo0backupniezawieraoptimizera. To odtworzenie curriculum/hyperparametrów,dokładna ścieżka historycznych400obejmowaławcześniejszesekwencjeiresume200,więc nie deklarowanoidentycznychwagwynikowych. Pola input_sha256legacy wskazująaktywnyplik400,niefaktycznytreningowy0;sourceassertwskrypciepoświadcza0.
Zachowanoostatniewarunkiusera:bezsleep,max400,zapis/heldouttest25,stopnapierwszejutracie wcześniejpoprawnejodpowiedzibaseline0,ratchetpo udanych kontrolach. Praktykowanecasesniebramkastopu. RaportSI_nazwy_metoda400_od0.json,zapisynames_original_method0. Skryptnieaktywuje,aktywny400bezpodmiany. Automatykawznowiona wyłącznie natęautoryzowanąpróbę;nastopieregresjiniewznawiaćbeznowejdecyzji.


## Dawna metoda nazw od0 —stop25
Practice399/576->425/576,new21/36->23/36,reverse20/36->24/36,old60/72->59/72,ret51/66->52/66.16wcześniejpoprawnychheldoutodpowiedziutraconych(5new,3reverse,6old,2ret). Zgodniezpoleceniemstopprzyregresjiproceszakończyłsięprzy25,checkpoint names_original_method0/step_25.ptzachowany. Sumarycznapoprawanieoznaczabrakuregresji,zapisanyraportzkonkretnymiprzykładami. Waginieaktywowane,aktywny400bez zmian. AutomatykaPAUSED,niewznowiononauki.


## Interwencjapo25 — autoryzowanakorekta
Userpoleciłwejśćostatnimpomysłem przedutrwaleniem. Uruchomiono train_correction_after25.py(sesja97161),raportSI_korekta_po25.json,zapisycorrection_after25. Wagi25zdawnejmetody ioptimizerzachowane,lr2e-5.8parpytańtesamefakty/różnecele(16lekcji)+16replay;CEodpowiedzi+.35stateCE+kontrastnativenext-tokenlogitów+.KLzamrożonego0. BindingKLtylkodlawierszy,wktórychteacher0ma poprawny pierwszytoken,co niegwarantujejego całejodpowiedzi;replayKLwszystkietokeny. Heldoutregresjenieużywanedo trenowania. Kontrole/zapisyco5 od26do75,BEZPAUZ. Stopnanowejregresjiodpoprawnychodpowiedzi25,ratchetpo udanychkontrolach;reportrestored_original_errorsocenia odzysk16utraconych0->25. Skryptnieaktywuje;400aktywneniezmienione. Naukasprzed25nienastąpiłaźródłowejinstancjiprodukcyjnej,więcnieinterpretowano czasu jako utrwalaniabezaktualizacji. Monitorwznowionyna nowąwyraźnieautoryzowanąpróbę;nastopnieuruchamiaćkolejnejautomatycznie.


## Korekta —stop30
Po5aktualizacjach(25->30):pract427/576,new24/36,reverse24/36,old60/72,ret51/66. Odzysk4z16błędówwprowadzonych0->25. Powstały3noweregresjewobec25:podajnieznanewnazwa7->prawda,podajfałszwnazwa1->prawda,Adamprzekazuje->Ada. Skryptzatrzymałsięna30zgodniezwarunkiemusera. Checkpointcorrection_after25/step_30.ptzachowany,bezaktywacji. Aktywny400nadalchroniony. AutomatykaPAUSED,niewznowionouczenia. Poprawasumienieoznaczaczystejnaprawy;raportSI_korekta_po25.jsonzachowujespecyficznebłędy.


## Autoryzowane75krokówpoczątkowych
Userwybrał75krokówbezstopupojedynczejregresjiwpoczątkowymetapie. Uruchomiono train_names75_original0.py(sesja21315),od0,dawnąmetodą576lekcji/CEanswer+.35stateCE/batch16+16/lr1e-4. Bezsleep,max75,kontrole/zapisy25/50/75;regresjezapisane vsstałybaseline0,niezatrzymująprzed75. RaportSI_nazwy75_od0.json,zapisynames75_original0. Skryptnieaktywuje;400aktywnybezpodmiany. Po75próba kończy siędooceny,kolejna naukanieautoryzowanaautomatycznie ponadtennowy etap. Monitorwznowionynatępróbę.


## Ukończone75kroków początkowych
Bezprzerw,nieprzerywanoza regresje.25:pract420,new25,reverse24,old57,ret50,21utraconychpoprawnych0.50:pract426,new23,reverse25,old60,ret50,13utraconych.75:pract430/576,new24/36,reverse24/36,old60/72,ret48/66,17utraconych. Źródło0:pract399,new21,reverse20,old60,ret51. Przedłużenie pozwoliłoodrobićczęśćbłędów25,aleniezapewniłopoprawyretentioni nieopanowałonazw. Zapisy25/50/75zachowane,bezaktywacji.400pozostajeaktywny. Proceszakończony,monitorPAUSEDdo dalszejdecyzji. Userpostawiłhipotezętożsamośćnazwyprzedwiązaniemwartości;do sprawdzeniaosobno,niepotwierdzonaprzeztenwynik.


## Dodatkowe75 — kontynuacja75->150
Na polecenieuseruruchomiono train_names150_original0.py(sesja77868),checkpoint75zoptimizermzachowany,nieresetowanowag. Samadawnametoda576lekcji/lr1e-4/batch16+16replay. Bezprzerw;76..150,kontroleizapisy100/125/150,regresjeraportowaneodstałego0bezearlystopwtejautoryzowanejserii. Zapisynames150_original0,raportSI_nazwy150_od0.json. SamplingRNGodtworzonodoprzed75,alecheckpointniezapisywałdropoutRNG,więckontynuacjazpostępemniebitowoidentyczna. Aktywne400nadalchronione,żadnychpodmian. Po150ocenatrenduiprzykładów,monitorPAUSEDdo nowegopolecenia.


## Ukończonakontynuacja150
100:pract436,new24,reverse24,old59,ret50,29utraconychpoprawnych0.125:pract438,new24,reverse25,old59,ret50,30utraconych.150:pract436/576,new25/36,reverse23/36,old60/72,ret48/66,16utraconych. Vs75(pract430,new24,reverse24,old60,ret48,17utraconych):mieszana niewielkazmiana,nieopanowanie. Jointpract150407vs425w75,stan/tekstniespójne w części przypadków. Wszystkiezapisyzachowane,bezaktywacji. Aktywny400chroniony. Treningzakończony,monitorPAUSED,zgodniezautoryzacją tylko75dodatkowychkroków.


## Od0 — tożsamośćnazwprzedskojarzeniami
Userpoleciłzachować150,jedziemyod0naprawanazwpóźniejskojarzenia. Uruchomiono train_name_identity0.py,startźródłowy0SHA8026...:natywnezadanieczydwapisy totasamanazwa,24zbilansowanychlekcji+24replay,CEanswer+.35stateCE+replayKL0,lr5e-5. Brakuczeniabindingnaetapienazw. Heldout28zadańXYZM i7/8,daneheldoutnietrenowane. Max300,kontrola50,bezprzerw;dotychczasowywarunek75początkowychbezstopuregresjizachowano,od pierwszejkontrolipo75(step100)stopjeślikonkretnapoprawnaodpowiedź0zostanieutracona. Warunekdodanyprzed rozpoczęciemnauki,wtrakcieinicjalnegobaselinetestu. Skryptnieaktywuje,400aktywnyzachowany. Po28/28identityosobnyświeżytestnazw/formulatów,przedautoryzowanymetapemskojarzeń. RaportSI_tozsamosc_nazw_od0.json,zapisyname_identity0. Wyniki150iwszystkiewcześniejszecheckpointyzachowane.


## Tożsamośćnazw —50/100,stop
Źródło0identity14/28.50identity16/28,ret50/66,25chronionychodpowiedziutraconych;warmup75nieprzerywał.100identity16/28,single38/42,new24/36,reverse24/36,old58/72,fresh73/108,ret50/66,11chronionychodpowiedzi0utraconych. Skryptzatrzymałsięprzy100zgodniezwarunkiemregresjipo75warmup. Zapisy50/100zachowane;identitynieopanowana,16/28bliskiebaseline14/28wzbilansowanejpróbce. Nieuruchomionoetapuwartości,bezaktywacji;400aktywnyniezmieniony. MonitorPAUSED.


## Trudne pary tożsamości — kontynuacja od100 gałęzi0
Userpoleciłróbażnauczy sięnazw i ponowiłróbdalej. Analiza100:wszystkieequalprawda,niemalwszystkieparysameprefixdifferentdigitteżprawda;staretreningnegativeslosowane różnychprefixów niepokrywałyproblemuwspólnychprefixów. Uruchomiono train_identity_hard_pairs.py(sesja59750),wznowienie100zoptymalizatorem,pozostaje gałąźod0nie400.5/6grupwsameprefix/różnakońcówka1..6,prefixynazwa/name/kod/obiekt/v oraz świeżer+litery,1/6gruparóżnychliter. Każda4przykłady(a,a)(b,b)(a,b)(b,a)truefalsebalanced;24lekcje+24replay,CEanswer+.35stateCE+replayKL0,lr5e-5. Testowepełnenazwy7/8iXYZMwykluczone. Kontrole/zapisy50,max700,bezprzerw;regresjekandydatówmierzone,nieblokująnowejautoryzowanejnauki,400aktywnychroniony. Po28/28heldoutnajpierwświeżytestnazw,końcówek,order/formulatu,dopieropóźniejskojarzenia. CheckpointyzRNGstanem,zapisyname_identity_hard_pairs,raportSI_tozsamosc_trudne_pary.json. Baselinewznowionegomodeluidentity16/28,ret50/66. Uruchomionomonitorautorecurring,aleuserpoleciłbieżącepilnowanie:obserwowaćdo pierwszegowynikubez kończeniaturystatuszamiastpracy.


## Trudnepary150 — bieżącypomiar i niezależnapróba
150:identity16/28,jakbaseline100;single37/42,new24/36,reverse24/36,old57/72,fresh69/108,ret49/66,19chronionychpoprawnych100utraconych. Zapisy150zachowane. Procesżywy175,niewstrzymano,nieresetowanopostępu.
Świeża read-onlykontrolaSI_tozsamosc_swiezy_test_150.json:lek3/4=3/4,tak3/tok3=3/4,pozostałeA/B,zor7/8,lumA/B,len3/33,nazwa7/8po2/4;łącznie16/28. KontrolatypównazwtreningowychSI_tozsamosc_typy_treningowe_150.json:13/28;stateheadrównież13/28,świeżestate14/28. Nie jestto tylko znajomośćcyfr7/8 ani wyłącznieodczytlmhead. Kontynuacjatego poprawionegoprogramu,przedkolejnązmianąsprawdź200/250. Testyświeżerazujawnione traktujodterazdiagnostyczne,do finalnejgeneralizacji wygenerujnowe niesłużącetuningowi.


## Hipotezablokującejwagi — kontrolowaneinterwencje
Na prośbęuserasprawdzonoodizolowanychkopiiźródłowego0ikandydata200:baseline,bypass każdejz9warstw,zerowaniekodowaniapozycji,zamianareprezentacjicyfr7/8(tiedembedding).Waginumericalfinitewn obu checkpointach:brakNaN/Inf,maksabs1,683/1,685wln_fnorm,nienaprawionoaktywnychplików. RaportySI_warstwa_blokada_diagnostyka.json iSI_wagi_poprawnosc_numeryczna.json.
58zadań/interwencję (28identity,12binding,18retention). Source0identity15/28,candidate20014/28. Żadnepojedynczeusunięciewarstwynieodblokowałotożsamości:bestcandidateblock3identity15/28zamiast14,pozostałefaleutracone;source0żadneponad15. Bypassblock0oba0trafieńwewszystkichgrupach;block1mocnopogarszaretention. Bezpozycjiidentity14/28,binding4/12źródłoi5/12candidate,ret9/18vs14/18baseline. Swap7/8niemiałpoprawy. Wyniknieidentyfikujejednejwadliwejwagi,niewykluczawyuczonegoblokującegoskrótulubrozproszonegomechanizmu;małytestnieuzasadniausuwaniawarstw. Diagnozarozdzielonaztrenerem,tylkokopiemodelów;natywneaktywne400niezmienione. Treninghardpairsnadalmonitorowany.


## Hipotezazbytotwartejścieżki — maskaprzyszłości
Userpostawiłhipotezęktórejśotwartejwagi zamiastblokady. Sprawdzononaźródle0ikandydacie250czydopisanaprzyszłaodpowiedźprawda/fałsz/nieznane/7/Adamzmienialogityna końcupromptu,jakpodczasteacherforcing.3promptyx5przyszłychtekstów/model. Maksróżnicaoutputlogitów0:4,77e-6,kandydat250:3,81e-6;state7,15e-7/4,77e-7. To poziomniewielkichróżnic numerycznych,gdyzmieniadługośćoperacjibatch,brakdowoduprzeciekuinformacjizprzyszłości. RaportSI_test_przecieku_przyszlej_odpowiedzi.json. Nieustalaczymaska uwagi przeszłościjestzbytrozproszona;tego testuniewolnouznaćza wykluczeniekażdegomechanizmuotwarcia. Aktywne400nietknięte,treninghardpairsnadalżywy.
Dodatkowakontrolatrainingtypes250:wszystkie7gruppo2/4 (14/28),więcniebrakujejedynieprzenoszeniana7/8;nieopanowanejeszczeznanecombinations.Nierestartowanobieżącejpróby,pozostawionoaktywnekontrolowanepomiary.


## Activationpatching i naprawadecyzjitożsamości
Izolowanycheckpoint250,4paryjednoznakowe(nazwa7/8,name1/2,lek3/4,A/B),matchedlengths;porównano9warstwi podmianęaktywacjipojedynczego zmienionegotokenunazwy lubanswerposition z equalrun do differentrun. RaportSI_sledzenie_tozsamosci_aktywacje.json. Różnicawreprezentacjinazwy ianswerpositionobecnawszystkichwarstwach;niema punktucałkowitegogubienia. NatywnyTminusFmargin:nazwaeq.157,diff.062;nameeq.153,diff.148;lekeq-.057,diff-.183;Aeq.491,diff.467. Częstoklasa jednakowa mimo widocznejsygnałowejróżnicy. Namepositionpatchmaxabsdelta.0044/.0018/.0130/.0086;answerpositionpatchmax.0967/.0289/.1279/.0290. To mały przyczynowytestzmianlogitów,nieidentyfikacjajednejwagi;ostatniablockanswerpatchjestbliskimoutputintervention więcnieświadczy o specjalnejfunkcjiostatniejwarstwy.
Hardpairs300identity15/28,35014/28,350ret49/66. Skryptzatrzymano po saved350;checkpointy150..350 ioptimizerzachowane. Userpoleciłnaprawę. Uruchomiono train_identity_decision.py(sesja52325),od350zoptymalizatorem iRNG. DodanozwiększonąCEnaPIERWSZYMnatywnymtokenieodpowiedzi i matchedmarginT-Fw(a,a)vs(a,b),(b,b)vs(b,a);bezhelperainference. ZachowanereplayKL0 istateCE,lr5e-5,max950,bezpauz,zapis/test50. RaportSI_tozsamosc_decyzja.json,zapisyname_identity_decision.400aktywnenietknięte;28/28monitorowanychnazwprzerywado NIEZALEŻNEJświeżejwalidacji,niejestautomatycznymwdrożeniem.


## Decyzjao tożsamości — ukończone400/450/500
400: one_prefix 0/10, last_character 0/14, copy 0/14, select_name 0/14, single 36/42, new_symbols 21/36, reversed_order 21/36, old_names 59/72, fresh_families 64/108, retention 49/66, identity 15/28; protected_regressions 7; activated False.
450: one_prefix 0/10, last_character 0/14, copy 0/14, select_name 0/14, single 35/42, new_symbols 14/36, reversed_order 17/36, old_names 59/72, fresh_families 62/108, retention 49/66, identity 14/28; protected_regressions 25; activated False.
500: one_prefix 0/10, last_character 0/14, copy 0/14, select_name 0/14, single 37/42, new_symbols 20/36, reversed_order 21/36, old_names 59/72, fresh_families 65/108, retention 49/66, identity 18/28; protected_regressions 10; activated False.
Odczyt550oznacza trwającąkontrolę,historyjeszcze500. Modelżywy,checkpoint400/450/500zachowane,name_identity_decision. Identity18/28to niewielkipostępmonitorowanego zbioru,nieopanowanieani niezależnageneralizacja. Aktywne400historycznenietknięte.


## Podmiana500 i kontynuacja na wyraźnepolecenie
Userzatrzymałbieżącąpróbę,potemjawniepoleciłpodmieńna500iruszaj. Treningdecisions52325zatrzymany,checkpointy500/550zachowane. AktywowanoEXACTcheckpoint500name_identity_decisionSHA446b9e50f9ef3d4394006f59653f8d70a7161137fe9bf147bf72a46e8befc5e3(18/28identity,ret49/66),backupaktywnychhistorycznych400wykonany. To useroverride,nieautomatycznanie-regressionakceptacja. SmokeA=fałsz/B=prawda/podajA->prawda,błędnie;nieustalonobrakuregresji. RaportSI_aktywacja_ostatnich_wag.jsonzawieramanifest/backup/SHA.
Uruchomiono train_identity_from500.py(sesja46243),wznowienie500 zoptimizerm iRNG,kroklrzmniejszonyz5e-5do2.5e-5 (poprzednio550pogorszyłidentity18->15),bezpauz,max1100,test/zapis50. Nie powtarzaidentycznejtrajektorii550;pozostałycel/training/replay/KLjakdecision. RaportSI_tozsamosc_od500.json,zapisyname_identity_from500. Skryptnieaktywujenastępnychwag;monitorACTIVEnaaktualnąwyraźnąautoryzację. Przyszławeryfikacjawdrożeniaochronatestów AKTYWNYCH500,niezakładanie400. Gałąźwciążwywodzi sięod0,produkcja500 zgodniezuserem.


## Autoryzacja iteracji do najlepszegowyniku
Userpoleciłpostępowaćtak ażdomaxwyniku. Zachowano odrębnybestcheckpoint500(18/28)wwork/name_identity_best/best.pt+best.json,nie nadpisywaćgorszym. Monitorzaktualizowany:kontynuujaktualnąpróbę,przy3kolejnychpogorszonychk ontrolachwróćdobestzoptimizerm,dostosujlr/balans,bezślepegorestartu. Zachowujlepszecheckpointy;przyszłeaktywacje tylko poprawaidentityi niergresja każdejpozostałejmetrykiAKTYWNYCH500lubnowszych plusniezależnesprawdzenieświeżychnazw,backup. Candidatezlepsząidentity ale słabszymretentionzachowaj,niewdrażaj. Nieobiecywanoglobalnegomaksimum. Po rzeczywistymopanowaniutożsamościkolejnyautoryzowanyetapskojarzeńwartości. Trener46243nadalobecny,bezduplikatów.


## Powrótdobest500; uzupełnieniepokryciadanych
From500:550identity16/28,60015/28,65016/28,70016/28(po kontroli700przerwano). Wszystkieniejniżbest18/28;sumarycznejwiększościnieuznanoprogress. Checkpointy550..700zachowane,raportSI_tozsamosc_od500_przed_powrotem.json. Trener46243zatrzymany,niezdublowano.
Wznowionobest500zoptimizerm iRNGwwork/train_identity_coverage.py(sesja57194),lr1.25e-5. Uzupełniono lukę:wcześniejidentitytrainingtylkocyfry1..6igołeliterybezXYZM. Teraz cyfry0..9iwszystkieuppercasew świeżychpełnychnazwach,zpełnymiheldoutnazwami nadalwykluczonymi;porównaniesameprefix/differentsuffix,differentprefix/sameending,differentlengths orazknownnames.6balancedfour-casegroups24lesson+24replay,lossjakdecision. Kontrole/zapisy50,bezpauz,max1100,rapportSI_tozsamosc_pokrycie.json,zapisyname_identity_coverage. NIEzmienionoprodukcyjnych500SHA446b...,niemodyfikowanobest. Nowykandydatdopierotestowany,niezadeklarowanoskuteczności. Monitorzaktualizowany.


## Podpowiedź — matchedtest i stopnioweusuwanie
Userpoleciłpomócpodpowiedziąprzytejsamejanalizienazw. Zamrożonycoverage600,28te same zadania3tryby,żadnelearning:plain16/28,generalrulehint12/28,końcówkihint14/28. RaportSI_tozsamosc_podpowiedz_test.json. Generalhintniepodajeodpowiedzi;końcówkihintdostarczaczęśćinformacjiotaskuniei niejestdowodemsamodzielności. Samodopisanieinstrukcjipogorszyłowynik;nieuznanogoza naukę.
Coverage650identity16/28,ret49/66;proces57194zatrzymanypo checkpoint650,resztazachowana,raportSI_pokrycie_przed_podpowiedzia.json. Nowatrain_identity_hint_fading.py(sesja71552),zbest500ioptimizerm/RNG,lr1.25e-5. Hintbezlabelleak:sprawdźdługośćikażdyznakobunazw.501..550alltaskshint,551..600halfmatchedgroups,601..800none. Walidacjaplainunchanged,abyodróżnićkorzystaniezpomocyodsamodzielności. Zachowanepokryciedanych/24identity+24replay/nativeloss/stateCE/KL. Max800,kontrole50,bezpauz,zapisyname_identity_hint_fading,rapportSI_tozsamosc_nauka_podpowiedzi.json. Skryptniewdrażanowychwag,aktywnebest50018/28chronione. Po firstcheckpointsprawdzićhintscoreosobno orazfadingtransfer,zanimprzedłużaćnaukę.


## Równoległa naukaróżnicy / matchedtestzaprzeczenia
Userpoleciłtrenowaćrównolegle. Hintfading71552dalejdziała;uruchomiono osobnytrain_identity_difference.py(sesja8926),odsamegobest500zoptymalizatorem/RNG,l r1.25e-5,max800,kontrole50,bezpauz. Oddzielnezapisyname_identity_difference,rapportSI_tozsamosc_roznica_rownolegle.json. TASKCzytenazwysąróżne?,truthiffa!=b,odwróconestateetykietyi matchedmargin. Dodatkowytestidentity_same_transferna tychsamych28parach pilnujeodwróceniapytaniabezbłędów. NIEporównywaćdifferentaccuracybezpośrednio zbest500sameaccuracy. Produkcyjne500nienaruszone;żadnaprób anieaktywuje.
Read-onlymatchedtest84promptów/model:best500same18/28,different14/28,negatedsame11/28;hint550same16,different14,negatedsame12. RaportSI_tozsamosc_zaprzeczenie_test.json. Samazmianazdanianiezwiększaaccuracy;negacja niestabilna. Próbanauki różnicy służy sprawdzeniuczyodpowiednieetykietyiwynikciągłyzmieniąoperatorrozpoznawania. Checkpointygoldsprawdzono przednauką.


### 2026-10-12 — niezależny test logiki i nazw na aktywnych wagach 500
Test bez uczenia i bez podmiany. SHA: 446b9e50f9ef3d4394006f59653f8d70a7161137fe9bf147bf72a46e8befc5e3. Logika silna Kleene’a; implikacja = NOT A OR B. Wyniki: {"negacja": {"n": 3, "correct": 1}, "podwojna_negacja": {"n": 3, "correct": 3}, "AND": {"n": 9, "correct": 6}, "OR": {"n": 9, "correct": 6}, "XOR": {"n": 9, "correct": 5}, "implikacja": {"n": 9, "correct": 4}, "równoważność": {"n": 9, "correct": 2}, "trzy_zmienne": {"n": 27, "correct": 14}, "fakt_bez_zmiany": {"n": 27, "correct": 12}, "nazwy_rowne": {"n": 28, "correct": 18}, "nazwy_rozne": {"n": 28, "correct": 14}, "bledna_nazwa_pozycja": {"n": 64, "correct": 0}, "bledna_nazwa_zapis": {"n": 48, "correct": 0}}.
NOT prawda i NOT fałsz zwracają niezmieniony fakt. Podwójna negacja 3/3 nie odróżnia zastosowania reguły od kopiowania. Test sam nie rozdziela braku rozpoznania instrukcji od błędu operatora. Listy obejmują cały katalog treningowy w krótkich grupach; nie oznacza to opanowania tych nazw. Rozpoczęto kontrolę wariantów sformułowań i pojedynczego faktu względem dwóch faktów. Aktywne wagi pozostają bez zmian.


### 2026-10-12 — osobny adapter logiki
Na polecenie użytkownika zatrzymano pełny trening rdzenia i zastąpiono go dziewięcioma adapterami residual bottleneck16: 38160 parametrów. Aktywne wagi500 SHA446b9e50f9ef3d4394006f59653f8d70a7161137fe9bf147bf72a46e8befc5e3 zamrożone wraz z wyjściami lm/state i używane w eval. Adapter przechowywany osobno, sprawdza SHA wymaganej bazy, może być wyłączony lub zamrożony. Test zabezpieczeń przeszedł: początkowe odpowiedzi identyczne, po aktualizacji brak zmian i gradientów rdzenia, adapter aktualizowany, ponowny odczyt dokładny, wyłączenie przywraca bazę, freeze_logic blokuje uczenie. Wynik outputs/SI_adapter_zabezpieczenia.json. Nowe uczenie work/train_logic_adapter.py, raport outputs/SI_adapter_logiki.json, checkpointy work/logic_adapter500. Nie wdrożono adaptera do produkcji; poprawność reguł i generalizacja dopiero podlegają pomiarowi. Monitoring ograniczony do adaptera logiki.

### Adapter logiki — kontrola 100
Podstawowe operatory poprawiły się z81/192 do148/192: NOT4→11/12,AND21→35/36,OR16→16/36,XOR13→29/36,implikacja16→28/36,równoważność11→29/36. Złożenia17→9/27; pojedyncze fakty37→25/42,dawne nazwy59→47/72,retention49/66 bez zmiany liczby lecz105 utraconych poprawnych odpowiedzi w całym zestawie ochronnym. Rdzeń bitowo niezmieniony (assert przed zapisem); adapter nieaktywny w produkcji. Zapisy adapter100 i200 zachowane; trwa kontrola200. Poprawa podstaw nie oznacza pełnej poprawności ani zachowania wszystkich odpowiedzi.

### Adapter logiki — kontrole 200 i300
200: podstawy169/192,złożenia9/27,retention49/66,140 utraconych poprawnych odpowiedzi całego zestawu.300:podstawy171/192,złożenia18/27,retention51/66,109 utraconych odpowiedzi;NOT12/12,AND35/36,OR33/36,XOR30/36,implikacja30/36,równoważność31/36. Rdzeń nadal zamrożony,adapter niewdrożony. Rozpoczęto niezależny test zapisanej wersji300 na nazwach lum4,zor9,tek2 oraz polskich formach negacji; outputs/SI_adapter300_swieza_logika.json. Trener kontynuuje do400 bez dublowania.

### Adapter400 i transfer reguł
Próba400 ukończona: podstawy181/192,złożenia19/27=200/219,104 utracone wcześniej poprawne odpowiedzi mimo retention51/66. Rdzeń bitowo niezmieniony,niewdrożony. Świeży test300: podstawy33/48,polskie formy negacji5/9,złożenia15/27. Uruchomiono test400 na tych samych diagnostycznych zadaniach oraz nowy etap401..800 od400 z zachowaniem optimizer/RNG,lr3e-4,24logika+12odczytfaktów+48replay,więcej złożeń i losowych pełnych nazw. Dane monitorowane nie służą finalnej deklaracji generalizacji. Raport SI_adapter_logiki_transfer.json.

### Transfer adaptera — krok500
Logika202/219 (podstawy180/192,złożenia22/27 vs19/27 przy400). NOT12/12,AND35/36,OR33/36,XOR35/36,implikacja32/36,równoważność32/36. Retention50/66,pojedyncze23/42; niewdrożony. Raport protected_regressions27 dotyczy POPRAWNYCH ADAPTERA400 jako baseline tej próby, nie aktywnego rdzenia500; nie porównywać bezpośrednio z104 przy wcześniejszej próbie. Świeży test400 na już diagnostycznych nazwach: podstawy33/48,negacjaPL6/9,złożenia16/27. Uruchomiono taki sam test transfer_adapter500. Rdzeń niezmieniony; potrzebna świeża końcowa walidacja przed aktywacją.

### Transfer adaptera — kontrola600
Logika196/219 vs202/219 przy500; złożenia21/27 vs22/27. Odrębny best adapter500 i pełny optimizer/RNG skopiowane do work/logic_adapter_best, wszystkie inne wersje zachowane. Test nowych nazw500: podstawy34/48,negacjaPL5/9,złożenia17/27. Nie opanował jeszcze przenoszenia. Rozpoczęto sondę tych samych tablic literalne wartości vs przypisanie nowym nazwom, aby oddzielić operator od odczytu operandów. Bez aktywacji.

### Zakończenie transfer800 i diagnoza zapisu
700=202/219,800=201/219; najlepszy suma500=202/219 zachowany osobno, niewdrożony. Sonda500: dosłowne wartości38/48? Weryfikacja sum:3+7+6+7+5+3=31/48; nazwane2+7+4+6+6+9=34/48. Zatem błąd nie sprowadza się do nazw: równoważność literalna3/9 vsnazwana9/9,ORliteral6/9 vsnazwane4/9. Rozpoczęto od best500 z optimizer/RNG etap różnych form: literalne operandy, polskie negacje, złożenia,24fakty+48replay,lr1e-4; osobne zapisy, rdzeń zamrożony.

### Różne formy — kontrola600
Logika196/219 vs202/219 punktu startowego500; NOT12/12,AND35/36,OR30/36,XOR33/36,implikacja33/36,równoważność32/36,złożenia21/27. Pojedyncze fakty23→28/42,nowe rodziny57→62/108,tożsamośćsame13→16/28,retention50→49/66.16 regresji względem poprawnych odpowiedzi kandydata500 (nie rdzenia). Cel zwiększenia zgodności formatów oceniany dodatkowo tą samą sondą literalne/nazwane dla form600, bez uczenia na pełnych diagnostycznych nazwach. Trening trwa, rdzeń niezmieniony i adapter niewdrożony.

### Rozdzielenie celu, kolejności i przypisania
Test readonly rdzeń500 i adapterformy700,4rodziny po6 różnych par wartości: zmiana pytanej nazwy,odwrócenie faktów,zamiana przypisań. Rdzeń E/M wszystkie3kontrole6/6;A/Bpoprawneobie1/6,1/6,2/6;nazwa7/8=1/6,1/6,2/6;ul5/ven9=0/6,2/6,0/6. Adapter700 E/M4/6,3/6,6/6;A/B2/6,1/6,4/6;nazwa7/8=2/6,3/6,0/6;nowe0/6,0/6,0/6. Wniosek: brak uogólnionego przyporządkowania i odporności kolejności,umiejętność zależy od rodziny nazw; sama niezmienność odpowiedzi nie dowodzi poprawności. Wynik SI_test_przyporzadkowania_i_kolejnosci.json. Adapter nadal niewdrożony;bez uczenia wag podczas sondy.

### Autoryzowana korekta faktów w adapterze
Forms zatrzymany po775; ostatni pełny zapis700 wznowiony z optimizer/RNG,75 niezapisanych kroków nie przeniesiono i ujawniono użytkownikowi. Nowy etap701..1100:24logiki+24parowanychfaktów+48replay. Każda grupa8: pytania o oba cele,odwrócona kolejność,zamienione wartości,jawna Korekta jednej wartości. Korekta zmienia tylko wskazany fakt;operator NOT wyprowadza wynik bez zmiany faktu. Dodano test48przypadków na rodzinę X/Y,nazwa7/8,ul5/ven9. Raport SI_adapter_korekta_faktow.json. Rdzeń zamrożony,adapter produkcyjnie niewdrożony,best500202/219 zachowany. Cel rozdziela przyporządkowanie od aktualizacji faktu.

### Audyt regresji i ograniczenie zakresu adaptera
Wszystkie treningi zatrzymane;factrepair800zachowany. Identyczne E/M: baza18/18,bestadapter50016/18,factrepair80016/18. Literalna negacja3/3wewszystkich;AND4/9→7/9→8/9;OR7/9→6/9→7/9. Potwierdzono regresję zachowania od globalnego adaptera mimo stałejbazy. Implementacja lokalna work/si_safe_logic_modes.py:domyślny trybbase adapterOFF, jawny tryblogic adapterON,freezeall,finallyresetOFF. Brak automatycznego klasyfikatora lub solvera. Nie wdrożono do aplikacji; poprawność logic mode nadal niepełna. Obecny kierunek: ograniczyćzakres zamiast mieszać kolejne treningi. Audyt outputs/SI_audyt_poprawek.json.

### Wdrożenie jawnego trybu i kontrolowana naprawa przypisań
Użytkownik autoryzował aktywację poprawionego rdzenia; NIE żąda powrotu do0 (wcześniejsza odpowiedź sprostowana). Wdrożono bestadapter500 w osobnym trybie logic_mode, API iHTML uruchomione na8791 z kopią plików. Wagi bazowe500 pozostają bez zmian. Test żywego API: E=fałsz odczyt przed/po logicmode fałsz,negacjanieprawda fałsz,adapter_used poprawny; pytanienazwa8 nadal błędne=wartośćnazwa7. Zatem tylko ochrona trybów aktywna,nie naprawa wszystkich problemów. Rozpoczęto osobną kontrolowaną próbę świeżych9adapterów na kopii bazy500:24sparowanecele/kolejność+48replay,nativefirstCE+matchedmargin,lr5e-4,max600. Bez mieszanego celu logicznego i bez dodatkowego schematu warstw. Raport SI_adapter_przypisanie_kontrolowane.json;nieaktywny kandydat. Produkcyjnebadanie SI_aktywna_aplikacja_test.json.

### Kontrolowana próba przypisania —100
Single37→40/42,new20→26/36,reverse21→24/36,fresh65→71/108,old59→57/72,ret49/66,36utraconychpoprawnychbazowych. Nieaktywowanykandydat. Rozdzielenie par/porządku/zamiany/korekty: {"fact_pairs_X": {"pierwotne_przypisanie": {"correct": 6, "n": 12, "both_correct": 0, "pairs": 6}, "odwrocona_kolejnosc": {"correct": 6, "n": 12, "both_correct": 0, "pairs": 6}, "zamienione_przypisanie": {"correct": 6, "n": 12, "both_correct": 0, "pairs": 6}, "jawna_korekta_nietrenowana": {"correct": 8, "n": 12, "both_correct": 3, "pairs": 6}}, "fact_pairs_nazwa7": {"pierwotne_przypisanie": {"correct": 7, "n": 12, "both_correct": 1, "pairs": 6}, "odwrocona_kolejnosc": {"correct": 7, "n": 12, "both_correct": 1, "pairs": 6}, "zamienione_przypisanie": {"correct": 7, "n": 12, "both_correct": 1, "pairs": 6}, "jawna_korekta_nietrenowana": {"correct": 6, "n": 12, "both_correct": 2, "pairs": 6}}, "fact_pairs_ul5": {"pierwotne_przypisanie": {"correct": 4, "n": 12, "both_correct": 0, "pairs": 6}, "odwrocona_kolejnosc": {"correct": 7, "n": 12, "both_correct": 1, "pairs": 6}, "zamienione_przypisanie": {"correct": 4, "n": 12, "both_correct": 0, "pairs": 6}, "jawna_korekta_nietrenowana": {"correct": 7, "n": 12, "both_correct": 2, "pairs": 6}}}. Korekta nieuczonalekcjach tejpróby, odrębny pomiar. Wprodukcyjnej aplikacji tryblogiki best500 niezmieniony.

### Zatrzymanie controlledbinding po400 i diagnoza trainability
300single41,new25,old55;400single41,new25,old58,ret49. Sonda checkpoint200 nazwytrenowaneA/B,nazwa1/2,rabc1/2 wszystkie0/6zmianodpowiedzii0/6obiepoprawne;nie tylko heldout. Controlledbinding zatrzymany po pełnymzapisie400. Mikrodiagnoza odadapter400:4stałeA/Bprawda/fałszobiequery/order,lr1e-3,200max,brakreplay,tylkoCEgeneracjii pierwszegotokena. Sprawdza dopasowanie, niegeneralizację;nieaktywować. Raport SI_mikroproba_adapter_przypisanie.json. Waplikacjibestlogic500 i base500 nietknięte.

### Mikropróba i kontrolowane porównanie powtórek
Mikropróba4stałeA/B osiągnęła4/4po25krokach,bezreplay. Nie jest generalizacją. Userautoryzował dalsze działanie po odczytaniu prac Wu/Geiger/Millière ICML2025 oraz Geirhos2020. Uruchomiono3sekwencyjnearmodidentycznychmicro25weights: samcel,cel+replayCE,cel+replayCE+2xKLteacher500. Każde75kroków,testsave25,identycznezadaniaA/Bwszystkie9stanówobiequeryiorder,niezmienionawagataskCE+firstCE. Test trening36,niewidzianenazwy36,ret66. Stanbaseline microtransfer mierzony przedstartem; zapisyoddzielne. Raport SI_przypisanie_porownanie_replay.json. Wagi aplikacji niezmienione.

### Porównanie replay — wyniki częściowe
{"task_only": {"step": 75, "metrics": {"A/B": {"n": 18, "correct": 13}, "B/A": {"n": 18, "correct": 13}, "X/Y": {"n": 18, "correct": 12}, "nazwa7/nazwa8": {"n": 18, "correct": 10}, "retention": {"n": 66, "correct": 49}}, "different_values": {"A/B": {"both_correct": 2, "changed_answer": 3, "n": 6}, "B/A": {"both_correct": 2, "changed_answer": 3, "n": 6}, "X/Y": {"both_correct": 0, "changed_answer": 0, "n": 6}, "nazwa7/nazwa8": {"both_correct": 0, "changed_answer": 1, "n": 6}}}, "replay_CE": {"step": 75, "metrics": {"A/B": {"n": 18, "correct": 13}, "B/A": {"n": 18, "correct": 13}, "X/Y": {"n": 18, "correct": 12}, "nazwa7/nazwa8": {"n": 18, "correct": 11}, "retention": {"n": 66, "correct": 51}}, "different_values": {"A/B": {"both_correct": 2, "changed_answer": 3, "n": 6}, "B/A": {"both_correct": 2, "changed_answer": 3, "n": 6}, "X/Y": {"both_correct": 0, "changed_answer": 0, "n": 6}, "nazwa7/nazwa8": {"both_correct": 0, "changed_answer": 1, "n": 6}}}, "replay_CE_KL": {"step": 50, "metrics": {"A/B": {"n": 18, "correct": 14}, "B/A": {"n": 18, "correct": 13}, "X/Y": {"n": 18, "correct": 12}, "nazwa7/nazwa8": {"n": 18, "correct": 11}, "retention": {"n": 66, "correct": 49}}, "different_values": {"A/B": {"both_correct": 3, "changed_answer": 4, "n": 6}, "B/A": {"both_correct": 2, "changed_answer": 3, "n": 6}, "X/Y": {"both_correct": 0, "changed_answer": 0, "n": 6}, "nazwa7/nazwa8": {"both_correct": 0, "changed_answer": 1, "n": 6}}}}
Samcel75 i replayCE75 podobne dopasowanieA/B13/18 iB/A13/18,ret49vs51. Nie wskazuje powtórek jako wyłącznejprzyczynybrakuopanowania. KLramięwtrakcie,zachowaćkońcowewyniki. Rozbite pary zróżnymi wartościami zamiastmylenia3łatwychrównychparz querybinding. Nieaktywowane.

### Koniec porównania replay i sonda uwagi
CEKL75A/B14/18,B/A13/18,newXY12/18,nazwa7/8 11/18,ret48/66;CE75ret51,taskonly49. Brak pełnego opanowania train niezależnieodreplay,nieuzasadnionewskazaniepowtórekjakowyłącznejprzyczyny. Następna izolowana próba: pełnybatch36 tychsamychA/Bprzypadków każdemuupdate,zamiastcyklu12,100max. Odjednakowegobase500+micro25 porównuje adapteronly i attentiononly,c_attn/c_proj,LR5e-4. Bezreplay iinnychauxwewszystkich. Uwaga-only zmieniawagi wyłącznielokalnejkopii,nie aktywnegoSI. Wynik SI_przypisanie_pelny_batch_uwaga.json;nieaktywowaćdiagnozybezgeneralizacji/retention. Porównanienieidentyfikujesamo w sobiepojedynczejprzyczyny ze względu naróżnąliczbęparametrów.

### 2026-10-12 — nowa sieć od losowych wag
Na polecenie użytkownika zbudowano niezależny core483459params,4warstwy4heads96emb256znaków,stałyalfabetpolski/ASCII,jedno uczonewyjście3stanów. Nieprzeniesiono starychwag/adapterów. Pierwszy etapnameidentity online zbliskimiparami,różnedługości/prefiksy;heldoutnazwywykluczone. Etapbindingdopieropo3kontrolachidentity≥95%;binding≥95%i różnevaluebothpair≥90%przezkolejne3kontrole przedniezależnąwalidacją. Brak swobodnegogenerowaniatekstu,solverów,dictionaries. Baselineidentity22/48,binding51/216;100identity23/48,jeszczebrakpostępu. Kontrolacharroundtrip,namesdistinct,causalprefixinvariance,finitegradsprzeszła. RaportSI_nowy_rdzen.json;opisNOWY_RDZEN_SI.md. StaraSIwaktywnymtrybiebazyilogiki zachowana. Wcześniejszyfullbatchdiagnoza:adapter10029/36,attention75 36/36ALEnewXY11/18,newnames7/18,ret41/66;nieaktywowano.

### Kontynuacja nowego rdzenia
Userpoleciłuczyćażdoprawidłowegorozwoju. Aktualnyidentity475;kontrole20028/48,30030/48,40028/48. Najlepszy300zachowanyoddzielniezoptimizer/RNG;źródłowelatestikolejnecheckpointynienadpisanenajlepszym. Przypisaniei logikaniemająjeszczepotwierdzonychumiejętności. Trenerdalejdziałabezduplikowania;przylimit/stagnacjikoniecznadiagnozabłędnychpar/trainvsheldout,zamiastślepejpowtórki.

### Wykryty skrót długości i korekta programu nauki
Fresh2000identity28/48,binding67/216-nieopanowane. Diagnoza224przypadki:equal32/32,differentlength32/32;0/32suffixdigit,suffixletter,prefixchange,middlechange,anagram. Jasnakorelacjakryteriumdługościz decyzją,niepełneporównanieznaków. Wznowiono checkpoint2000 zoptimizer/RNG,bezrestartusieci;lr1e-4;niegenerujemyłatwychróżnychdługościwpierwszych650krokach. Curriculum1znak250,potem1..3do650,potem1..8,nearnegativezmieniadokładnie1znakwkażdejmożliwejpozycji. Wskazanewraporcieinicjalizationresume;initial.ptwfolderzerepair jestSTARTEM ETAPU2000nieoryginalnymi random0 (tenzachowanywinitialoryginalnymfolderze). RaportSI_nowy_rdzen_naprawa_nazw.json. Wagi/aplikacjapoprzedniejSIbez zmian.

### Freshname repairlimit i atomdiagnoza
Repair2000final32/48,best33/48przy1800/1900zachowanyoddzielniezoptimizer/RNG. Nieprzeszedłdobinding. Dotychczasowegatingdługościbyłczasowy:1char250bezpotwierdzeniajejopanowania,możliwybłądcurriculum-dozmiany dopieropodiagnozie. Nowyatomtest2armodrepair2000,z identycznymfull100orderedcyfry0..9,ważonąCEbalansklas (10equal90diff),sameLR5e-4. Shorta|b? versusnativepolishfullquestion. Max300,zapis/eval25;100/100trainkończyarm,heldletters100rozbiteequal10/diff90. Notdeployablediagnosis. WynikSI_nowy_rdzen_atom_porownanie.json. StaraSIbez zmian.

### Atomdiagnoza zakończona i etap krótkich nazw
Shortdigit100/100po200 vs polskiepełnepytanie77/100po300. Shortheldletters68/100 z równymi4/10i różnymi64/90,polskieheldletters10/100constanttrue. Brakgeneralizacji samegooperatora naalfabet;wpływzapisu jestduży ale liczbakroków/seed jednorazowe nieuniwersalnypowód. Wznowiono short200 zoptimizer,lr3e-4;nieoriginal0/stareSI. Trenercompactidentity64rowsonline62lettersdigits,4matchedcases,pairsnearnegativesame_length1changedcharatanyposition. Stage1,2,4,8max1500każda,gating3kolejnesukcesyequal95%i different95%. Testpairswykluczonezdanymiwobuorderach;equalshortnamesmoże byćseencontrol,niepełneunseenwords. Nowapróbanieuczyjeszczepolskichinstrukcji/binding. RaportSI_nowy_rdzen_krotkie_nazwy.json. Wagi produkcyjne SI niezachwiane.

### Kompaktowe nazwy — rzeczywisty postęp
Length1kontrole800254/256,900250/256,1000251/256spełniły95%osobnoequal/different3razy;przejścielength2. Length2best1400250/256(equal128/128,diff122/128),final1500245/256(equal126,diff119)-brakstabilnych3kontroli;limitpróby. Zachowanobestlength2step1400oddzielnie. Rozpoczętoutrwalanieodbestweightsoptimizer/RNG,LR8e-5vs3e-4,wciążten samrodzeń,mały matchedmargin. Dalszelength2,4,8tylkopogating,żadnychskokówlogika/binding. RaportSI_nowy_rdzen_utrwalenie_nazw.json. Wynikmonitorowanyniefinalheldout;dłuższenazwyniewopanowane.

### Utrwalenie length2 i diagnoza length4
Length2passed100252/256,200252,300251;przeszedł3checks95%equal/diff. Length4best1900227/256,final2000224/256,limit. Errorslatestdiffpos1=29/32,pos2=28/34,pos3=26/34,pos4=15/28,ostatni znaksłaby. Best4weightsoptimizerRNG zachowaneoddzielnie. Wznowionobest4:nativeten samcore,train-onlyhelper194params Linear96→2,per-characterbalancedCE.2 odhiddenpozycjib-drugiejnazwy. Targetcomputed onlytraining,niepredeterminowanaodpowiedźinferencji. Odpowiedźnativedecisionhead,CE+.05margin,LR8e-5,stages4,5,6,7,8gating3≥95%. Checkpointchar_auxweightsseparately,opt2groupsresumeuwaga. RaportSI_nowy_rdzen_porownanie_pozycji.json. Brakaktywacji/newlanguage/bindingjeszcze.

### Naprawa błędu technicznego helpertrenera
Pierwszytrain_compact_positions padłprzedpierwszymopt.step:literówkaTensor.clampminzamiastclamp_min. Nieważnepierwszeuruchomienienieaktualizowałowag. Poprawiono,wykonano na osobnejkopii pełnyforward/auxloss/backward/opt.step PASSfinitegrads. Uruchomionotrenerponownieodzachowanegobestlength4step1900,nowasesja17675;helpercelniezmieniony. Nieuznawaćtejbłęduza niezdolnośćmodelu,brakwynikutreninguwnieudanymhelperrun.

### Helperpozicyjny — best248/256 i stabilizacja
Run1500final246/256(equal127,diff119),best1200248/256(equal125,diff123),wcześniejszybest227/256. Bez porównania kontrolnego nieprzypisujemycałego wzrostutylkohelperowi;pomocniczycharauxlossfinal.6109niedowodzipełnegomechanizmu. Best1200zachowanooddzielniezcore+charaux+optimizer2group+RNG. Nowystableodbest1200,zmniejszono LR8e-5→2e-5,wznowionoobiegłowyigrupyoptpoprawnie,max1000/stage,gatingnatywny95%pozostaje. StaraSIbez zmian,kandydatniewdrożony. RaportSI_nowy_rdzen_stabilizacja_pozycji.json.

### Stabilizacja length4passed i length5limit
Length4kolejne100247/256(eq125,diff122),200247(eq124,diff123),300250(eq127,diff123)passed95%both3checks. Zapispoprawnegolength4_step300zachowanyoddzielniewbest/compact_stable_length4.ptzhelper/optimizer/RNG. Length5best800145/256,final1000142/256(eq61,diff81),limit-diagnozawymagana. Nieprzechodzidolength6,naturalPolish/binding/logikanadalniewopanowane. RaportSI_nowy_rdzen_stabilizacja_pozycji.json. Nieinterpretowaćpassedmonitoringjakofinalgeneralizacja. Wszystkieoryginalnecheckpointy/staraSIzachowane.

### Przenoszenie długości i nauka mieszana
Read-only na niezależnych nazwach/bestpassedL4: L1=128/128,L2=126,L3=63(eq0/64),L4=122,L5..8=64(eq0/64). PoL5próbie1000:127,122,62,113,80,72,64,64 odpowiednio. Potwierdzona zależnośćodprzećwiczonej długości,nieprzypisujemybezinterwencjiwinnemuweightpositional. WznowionodobrybestpassedL4step300 zcore/helper/opt/RNG,LR8e-5,każdybatchwszystkiedługości1..5potem1..8,matchedclassbalance,niewyzerowano. Testby_length128caseskażda,negativepairsreservedbothorders,gatingkażdejklasykażdejdługości3razy95%. RaportSI_nowy_rdzen_mieszane_dlugosci.json. Niepowtarzajnieopanowanychlength5fixedserii. Staraaplikacjazachowana.

### Interwencja końcowej pozycji i wariant wspólnych indeksów pól
Mixed2500skończony528/640,perlength3/5niestałe;pozostajeniezdolnośćuogólnienia. Sonda read-onlycopylastanchorL4niepomogła3/5,zeroanchorniemalconstantfalse;nieuprawnionedowierdzeniejednejzawieszonejwagi. NowyalternatywnyvariantPairedCore:sharedlocalindicesdlaznakówlewegoprawegopola,learnedroleembeddings3x96=288params,syntaxanchorconst,483747nativeparams. Inputgrammarjedynyseparator|,wyznaczaroles/positions,nieporównujeznakówlubstanów i niewylicza odpowiedzi. Causalprefix/finite rolegradPASS. Wznowionyoldnative/sourcebeststableL4,helper+opt2groups,nowyrole3group;read-checkpoint PairedCore nieFreshCore,weightrolesflag. Wszystkiepotwierdzonewagi/oldSIzachowane. To testhipotezyreprezentacjipól,niefinalnaprawa. W100nowegowariantuwynik399/640mniejszyniżsamomixedbaseline-nieukrywamystartu. RaportSI_nowy_rdzen_pozycje_pol.json.

### Pairedfields592/640 i kontrola pomocniczego celu prefiksu
Pairednativewariant1500skończony592/640 vsMixed528/640: L1eq64/diff64,L2eq64/diff62,L3eq63/diff61,L4eq63/diff43,L5eq62/diff46. Nierównywynik,nieopanowanealllengths. Nowe2sekwencyjnedziałania odidentycznego checkpoint1500core/helper/optimizer3group/RNG:localcharCEhelper vs cumulativematchingprefixteacherhelper. NativeoutputCE+.05matchedmargin taka sama,aux.2balancedclassweight,lr8e-5,500max/save100. Daneidentycznewobuarm,bylength640test. Prefixteacherlabeltylkoceltreningowy:zmienionyznakpowinienprowadzićdoprefixfalsewkażdejkolejnejpozycji;inference nadalwyuczonyPairedCore. To testhipotezyutrzymywaniaróżnicy,nieudowodnionyalgorytm. RaportSI_nowy_rdzen_prefiks_porownanie.json,checkpointmodel_kindpaired_core. StaraSIzachowana.

### Porównanie prefiksu zakończone i odczyt decyzji
Localchar500609/640,prefix500604/640,bestprefix400612/640. Niejednoznacznaprzewaga jednejmetody;wybrano do sondybest612. Helperlastprefixwordreadout:92+78+76+74+63=383/640 vsnative612,więcnienadapisano wyjściahelperem. Następnamikrokalibracjawyłącznie3biasesnativeclassifierfrozenencoder,1280świeżychbalancedrows,negativepairsmonitora640wykluczone,CE500Adam.02. Wyniknatywnywagi decision.bias,niezewnętrznejreguły. Diagnozaniewdrożona,nowycpoptmetadatahistoryczne sprzedbiasfit. RaportSI_nowy_rdzen_kalibracja_decyzji.json. StaraSIbez zmian.

### 2026-10-12 — kalibracja i sonda zamrożonego odczytu
Kalibracja trzech biasów poprawiła 612/640 do 613/640; nie wdrożono. Uruchomiono kontrolowaną sondę liniową na zamrożonym PairedCore prefix400: odczyt pozycji końcowej, ostatniego znaku i ich konkatenacji. Świeże porównania testowe wykluczono z danych treningowych. Sonda jest diagnostyczna, nie zmienia produkcji ani wag enkodera. Wynik: SI_nowy_rdzen_sonda_odczytu.json po zakończeniu.

Sonda zakończona: świeże L4 native238/256, nowy final-readout237/256; L5 native226/256, final230/256, konkatenacja228/256. Sam ostatni znak znacznie słabszy. Nie wykazano naprawy samą zmianą odczytu liniowego. Przy L1 wykluczenie znanych identycznych par pozostawiło wyłącznie negatywy (0 pozytywów); ten podzbiór nie sprawdza obu klas. Brak wdrożenia. Kolejna diagnoza powinna rozbić błędy L4/L5 według miejsca zmienionego znaku, zanim zmieni się cel nauki.

### 2026-10-12 — rozkład błędów i kontrola trudnych przykładów
Świeża sonda wyłącznie negatywów: L4 pozycje115–116/128, L5 105–112/128. Błędy rozproszone, brak jednej szczególnie dominującej pozycji. L6 108–119/128 nie jest pełną walidacją, bo brak pozytywów. Uruchomiono compare_hard_examples.py: dwa sekwencyjne ramiona200 kroków z identycznego prefix400/optimizera/RNG i identycznych batchy. Kontrola zwykłego CE versus dwukrotna waga aktualnie błędnych przykładów (normalizacja sumą wag); pozostałe cele i architektura identyczne. Zapis100/200, brak wdrożenia, wyniki SI_nowy_rdzen_trudne_przyklady.json.

Porównanie zakończone: kontrola612/640, ważenie błędów613/640. Świeża walidacja1938 przykładów: źródło1630, kontrola1624, ważenie1606. Nie wybrano nowszych wag. Wyniki szczegółowe SI_nowy_rdzen_trudne_swieza_walidacja.json ujawniają brak transferu na różne długości i identyczne nazwy L6–8. Dotąd training obejmował tylko L1–5 i negatywy jednej zmiany tej samej długości. Nowa ograniczona próba300 kroków od zachowanego prefix400: matchedquartets długości1–8, negatywy singlechange/anagram/differentlength. Ten sam model/optimizer/helper, brak wdrożenia. Zestawy już ujawnione służą diagnostyce, późniejsza finalwalidacja musi być świeża.

Pokrycie300: stary monitoring609/640 versus source612. Świeży seed39174821: source1606/1936,kandydat1634;157 nowych poprawnych,129 wcześniej poprawnych utraconych. Niewdrożony. L6equal40→62/64,L7 24→56,L8 42→62; różne długości L6 42→25,L7 45→32,L8 38→31. Hipoteza konfliktu pomocniczego prefixaux: na parze a/ab wspólne znaki mają same-prefix labels, a pełna odpowiedź ma different. Aux zip pomija dodatkowe końcówki. Uruchomiono kontrolowane200 kroków obu ramion od identycznego coverage300 z pełnym optimizer/RNG: prefixaux.2 versus0; pozostały trening i batches identyczne. To test wpływu celu, nie dowód przyczyny.

### 2026-10-12 — test hipotezy konfliktu auxiliary
Monitoring zaux618/640,bezaux611. Świeża walidacja1934: sourcecoverage3001656,zaux1690(74zyski40utraconych),bezaux1660(55zysków51utraconych). Hipoteza, że usunięcieprefixaux naprawi wyniki, niepotwierdzona w tej próbie. Kandydat zaux zachowany, niewdrożony. Najsłabsze nadal prefix-related differentlength, np.L4 32/64,L8 28/64. Uruchomiono bounded200-step length_focus od lepszegozaux z optimizer/RNG: matched64row z równymi nazwami i wspólnymprefiksem różnejdługości, wszystkieL1–8, ten sam model/aux. Próba zdolności nauki konkretnego przypadku; bez automatycznej aktywacji, możliwe regresje wymagają pełnej późniejszej kontroli.

### 2026-10-12 — nauka różnych długości i zachowanie poprzednich odpowiedzi
Lengthfocus100 monitoring624/640,200623. Fresh seed78419623 total1948: source1672,focus1001723(92gains41lost),focus2001744(132gains60lost). Kategorie source→200: equal510→478/512;singlechange438→461/512;differentlength339→419/512;anagram385→386/412. Wagi200 zachowane, niewdrożone. Uruchomiono kontrolowane200 kroków obu ramion od identycznego focus200: zwykłe mixedcoverage versus KL2 do zamrożonego wcześniejszego withaux200 tylko na online wierszach poprawnie rozwiązanych przez nauczyciela. Gold używany tylko jako dane treningowe, inference beznauczyciela/solverów. Teacher wcześniejsze błędy nie są utrwalane tym celem. Pełne porównanie na świeżych przykładach po próbie.

### 2026-10-12 — ochrona wcześniejszych odpowiedzi
Monitoring obu ramion200622/640. Freshseed87139251:source1715/1930,uniform1694(93lost72gained),protected1722(67lost74gained). Kategorie źródło→protected:equal498→504/512,singlechange457→453/512,differentlength398→385/512,anagram362→380/394. Silna KL2 ogranicza regresję, ale osłabia differentlength; brak wdrożenia. Kontrolowana stabilizacja od tego samego focus200: lr2e-5 (z8e-5), dwa ramiona300steps identyczne dane, KL0 versusKL.2(z2). Obie zmiany oddzielnie wskazane: efekt KL tylko wewnątrz nowego porównania przy wspólnym lr2e-5, nie przypisujemy całej zmiany jednej przyczynie.

### 2026-10-12 — łagodniejsza stabilizacja i izolowana sonda przypisania
Monitoring624/640oba. Freshseed98517364 total1942:source1769,uniform1772(39lost42gained),protected1779(36lost46gained). Protectedequal502/512,onechange464,differentlength430,anagram383/406. Niewdrożony, pełnyoperator nieopanowany. Izolowana sonda przypisania od protected300, bez resetu wag/optimizera/RNG:600maxsteps,lr3e-5,32factrows(twofacts,bothqueries/bothorders)+16identityreplay. Explicitcompactsyntax facts|query?, braksolverainference; gold wyłączniegeneratortrain. Trzy niezależne monitoringrodzinynazw wykluczonezgeneratora. To diagnosticfeasibility nie ogłoszenie ukończenia fundamentów ani swobodnego języka. Kontrole100binding108 iidentity640, wszystkiezapisyoddzielnie bezaktywacji.

### 2026-10-12 — izolowana sonda binding zakończona
600steps:binding33→63/108,identity624→613/640. Świeże4rodziny144twofact:singlechar24/36,similar23,differentlength22,distinct21. 48par różnychwartości:odpowiedźzmieniała się5/48par,obiesłuszne1/48. Same sumy maskują queryignorowanie. Raport SI_nowy_rdzen_przypisanie_swieza_diagnoza.json. Uruchomiono controlled300perarm od identycznegobinding600weights/opt/RNG:control vs query_contrast natywnychlogitów. Wobu dodano KL na16identityreplay do frozenprotectednames300. Kontrast.2 dotyczywyłącznieróżnychprawidłowychstanówobu pytań przytychsamychfaktach;braknowychheadów/solverainference. Wszystkiecheckpointyosobne,niewdrożone.

### 2026-10-12 — kontrast query nie naprawił przypisania
Monitorcontrol65/108identity614,contrast63identity611. Fresh4family144:control89,contrast85;differentstatepairs48bothcorrectcontrol3,contrast1. Nie wykazano poprawy kontrastem. Uruchomiono ograniczone porównanie samegostructuralencoding400/arm od identycznegobinding600. RecordCore NIEdodajeparametrów ani nieinterpretuje stanów/porównujenazw: = i ; wyznaczają pola, pozycjeznakówresetowane wkażdej nazwiefaktu, wartości dostają odrębne pozycje128+,queryrole1. Identitycompactbez=przechodzioryginalnymPairedforward. ObiearmsnativeCE+identityKL1lr3e-5,samebatches/RNG. Sourcewagiidentyczne,wyłącznikrecord_encodingrozróżniainference; checkpointmodel_kind musi być odczytany. Wszystkiewaginiewdrożone.

Kontrola mixedbatch odkryła błąd kodowania identityrow w batchu z factsrow; poprawiono per-row fallback. Fullforward/backwardfinitePASS483747params. Próbę zatrzymano w ramieniuoriginal_fields (zapis100 zachowany, kopiareportSI_pola_faktow_przed_korekta_batcha.json), wznowiono całe kontrolowaneporównanieodidentycznegosource600 dla obuarm z poprawionymkodem. Nie przeniesiono niezapisanych kroków, produkcjanietknięta.

### 2026-10-12 — wynik strukturalnego kodowania faktów
Original400binding66/108identity620;records400binding72/108identity615. Fresh4families:original97/144,records96/144. Singlefact original17/24,records24/24;differentstatepairs BOTHcorrectoriginal7/48,records2/48. Kodowanie pomaga pojedynczymfaktom, nie potwierdza poprawy dwufaktowego wyboru. Bezwdrożenia. Uruchomiono micro_record_binding.py:4stałeprzykładyG/T,dwaquery/bothorder,sourceRecord400,freshAdamWlr3e-4,200maxstop4/4. Bezreplay,tylkodiagnoza czy wybórfaktumożnawyuczyćna4stałych. Nieaktywowaćmikrowagbezretention/generalizacji.

Mikropróba osiągnęła4/4po10updateach(loss.00651). To dopasowanie czterech stałych, nie generalizacja. Uruchomiono validate_micro_transfer.py:zmienionewartościG/Tall9combos plus pozostałe3rodziny jużdiagnostyczne; raport SI_nowy_rdzen_mikro_transfer.json. Produkcjanietknięta.

### 2026-10-12 — kontrola stałego przypisania nazw
Mikro4sampleG/T10updates4/4,aletransferall9statesG/T12/36vsbefore25/36;inne3familie49/108vs71/108. Zapamiętane stałe wartości nazw nie są wiązaniem faktów; kandidatnieaktywowany. Uruchomiono micro_variable_states.py od nietkniętegoRecord400,znowymAdamW3e-4:36fullG/Tall9statesbothquery/order,400maxstop36/36; bezreplay tyłkodiagnoza zdolnościdopasowania operatora na2stałych nazwach. Postęp tejmikropróby nigdy nie oznacza jeszcze generalizacji nowych nazw.

### 2026-10-12 — komplet stanów G/T
36/36trainpo140steps;differentstates12/12bothcorrectG/T. Transfer:similar20/36,differentlength23/36,distinct21/36,brakpełnejgeneralizacji. Mikrowaginiewdrożone. Kontynuacja source140zoptimizer1group/TorchRNG (PythonRNGnowyexplicitseed573192):train_short_binding600max,lr8e-5. Jednolosowapara1charz62alphabet wbatchuFULL36stan/query/ordercases+16identityreplay,zKLteachernameguardtylkonapoprawnychteacheronlinecases. 4testpairsH/N,U/W,c/r,7/9ireversewykluczonezgeneratora;nieinterpretowaćseenindividualcharacters jako unseenalphabet. Kontrole100,checkpointyoddzielne,produkcjanietknięta.

### 2026-10-12 — shortbinding600 zakończenie
Monitoringbest300102/144both9/48,final60099/144both3/48. Freshaudit:30099/144both6/48,60096/144both1/48;onefact60022/24. Dwiejednoznakowepary600odpowiedźniezmieniała sięw12/12differentstates każda. Uwaga metadatafamilydifferent_length w tym audycie używa ba/bb, więc to dwa znaki tej samej długości, nie test różnych długości. Sourcebest300zachowany; uruchomionodiversitycomparisonod300weights/optimizer/RNG:200/arm,jednaparaFULL36powtórzona4x versus4różneparyFULL36,144binding+16identicalreplayperbatch. Sameupdates/rowcount/teacher/lr,4xdifferentpairs exposure wdiversityjestzamierzonymczynnikiem. Generator4pairs zużywaidentycznyRNGwobuarm,teacherKLguardidentyczny. Brakwdrożenia.

### 2026-10-12 — różnorodność batcha
Kontrola1pair20095/144both3/48;fourpairs200113/144both18/48. ŚwieżyreportSI_nowy_rdzen_roznorodnosc_swiezy_test:source97/144both7/48,single100both9,diverse100both11;partwocharsnu/nv(metadatafamilydifferent_length)niejestdifferentlength,obadwa2chars. Świeżetestnamesniewykluczonez wcześniejszychhistoricalrandomarms,niedeclarujemystrictunseenpairs. Kontynuacjazlepszegofourpairs200optimizer/RNG:600maxlr4e-5,4pairs×36+16identityguard,20monitorpairs720casesexcludedfurthertrainingbothorder,identitymonitor640. Old4pairsjużheldoutwpoprzedniejpróbie;16nowychmogływystąpićhistorią,nieweryfikowano. Finalunseenvalidationpo zakończeniu niezbędna. Brakwdrożenia.

Stabilizacja trwa,kontrola400:533→570/720;bothdifferentstates73→106/240;identity606→620/640. Checkpoint400skopiowanyosobniewbest/binding_stable_400.pt,treningniewstrzymany600max. To monitoringnietestfinal,brakwdrożenia.

Stabilizacja600zakończona:588/720both116/240identity625/640;baseline533both73identity606. Best600osobniewbest/binding_stable_600.pt(400takżezachowany). Uruchomionoread-onlyprobe_binding_lengths:16nowychmonitoringpairskażdejL1/2/4/8,full36statesqueryorder,porównaniesource200/400/600. Seed847192631,stare20reservedparwykluczone,testpairsstrictcałahistoriaexposurenieweryfikowana;nieprzedstawiaćL1jakopełnegofinalunseen. Brakwdrożenia.

Readonlytransfer600full576perlength: L1source401→442,both33→70/192;L2 408→428,both39→58;L4 379→383,both9→21;L8 376→376,both25→33. Postęp głównie1char,niepełnyoperator. Rozpoczęto uzasadnionymixedL1–2curriculum odstable600weights/optimizer/RNG,lr4e-5,600max:2paryL1+2paryL2full36perpairplus16identityguard. Monitoring28reservedpairsL1–2/1008cases,bothorderexcludedfuturetraining,perlengthmetrics. L1earlierpostępnadalretentionkontrola,bezresetu,waginotdeployed.

MixedL1–2kontrola300(treningsiętoczy):baseline786/1008both135/336identity625→824/1008both171/336identity618/640. L1 608/720both137/240,L2 216/288both34/96. Postępprzypisaniazlekkimspadkiemidentity;checkpoint300zachowany,produkcjanietknięta. Nieingerowanowdziałającyproces,600max.

### 2026-10-12 — mixedL1–2 ukończone
Final600846/1008both194/336identity625/640vsbaseline786/both135. Freshseed96827314,L1source451→486/576both71→103/192;L2 430→524both68→143;L4 379→429both13→64;L8 370→404both19→54. Nowe2charfaktyrandomdifferentnamesłatwiejszeniż8stałychmonitoringpairsnearnegative;niezmieniamykryterium nawybranylepszytest. Best600kopiaoddzielna. Controllednativeattention300perarm frommixed600:baselineCE+KLidentity versusdodatkowe.2CE naqueryfinal#q i dwóchlastvaluekey w istniejącejostatniejwarstwiehead0. TargetktóryrecordwskazujenamescomputedONLYtraining,scoreszactualqkvusednativeforward,nie ma nowegoparametru/headainference. Structuremaskcausalkeypositionsprzedquery,noanswerlookupinference. Wszystkieresztabatches/optimizerRNGidentyczne. No deployment.

Attentioncomparisoncontrol300zakończony872/1008both215/336identity625/640;baseline846/both194/identity625. Savedcontrol300osobno,besty600pozostają. Drugiarmattention_supervisiontrwa,niedeclarujemyprzewagiśrodkadoprzedukończeniaporównania. PełnyupdatepointerPASSfinite483747noextraweights.

### 2026-10-12 — nadzór istniejącej uwagi
Controlled300:control872/1008both215/336identity625;attentionsupervision884/1008both229identity625. Ostatnionlinepointer113/144vscontrol79/144,niezależniemierzonanativeodpowiedź. Bestattention300zachowanyoddzielnie,bezwdrożenia. Readonlyfreshseed16839427:po8parL1/2/4/8randomi8nearnegativeoraz8prefixdifferentlength,full36stan/query/order,controlvsattention. Nowytestniewykorzystywanydooptymalizacji,historyexposureformalnieniezbadana;pojegoobejrzeniumonitoringdiagnostyczny.

Freshattentiontotal2592control1989,bestattention1998;bothdiffstates340→358/864. Efektniewielki,nieudowadniauniwersalnejnaprawy. L8nearcontrol9/best12/96both;prefixdifferentlength11→17/96. Uruchomionocurriculumhard1–4(+prefixextra1char) odattention300fulloptimizer/RNG,600max. 4pairsbatchsizes1/2/3/4, typyrotująceindependentrandom/1charnear/prefixdiff-length;full36valueseach,16identityguard,nativepointer.2sameexistinghead. Nie wdrożono,wagibestzachowane. Generatorpokrywawcześniejsze2chari nowe3–4takżew obuquery/order,niesamefixedmappings.

Hard1–4zakończone600:915/1008both249/336identity625/640versussource884both229. StaticmonitorONLYL1–2:L1 665/720both189/240,L2 250/288both60/96;emptyL3–5nieuznawaćzaopanowanie. Best600oddzielniezachowany. Freshreadonlyvalidate_hard14seed251983764:8pairsrandom+8near eachL1/2/3/4/8 i8prefixdifferentlength,full36cases,comparesourceattention300vshard600. Nie używany dotrain,historyexposureformalnieunchecked.

Freshhardtestsource→600:nearL3 225→244/288,both36→55/96;nearL4 214→235,both34→51;prefixdifferentlength194→208,both18→23. Wszystkie11kategorie nativecorrectnondecrease na tym seed251983764,nie stanowi uniwersalnej gwarancji. Kontynuacja exacthard600weights/opt/RNG do1200 w oddzielnymwork/binding_hard14_continuation,4pairsL1–4/near/random/prefix+identityguard/nativepointerunchanged. Monitoringrozszerzony28oldpairs+20nearL3/4+8prefixdiff,łącznie56pairs2016cases,excludedfuturetrainandreverses; nowe testcasewygenerowaneindependentseed5973802. Same earliercorrecttest cases preservedpluswidercases, identity640. Produkcjanietknięta,finalvalidationdalejrequired.

Kontynuacja800wtrakcie: rozszerzonybaseline1719/2016both403/672identity625;7001677both371identity627;8001773both453identity628. Najlepszybieżący800zachowanyosobno,bests600nietknięty. Procesnieingerowany,niewdrożony,1200max.

Kontynuacja1100wtrakcie:najlepszy10001780/2016both464/672identity631/640;11001769both457identity629. Best1000osobnozachowany,besty800/600zachowane. Procesdalej1200maxbezingerencji.

Kontynuacja1200zakończona:1798/2016both484/672identity627/640;10001780both464identity631.1200lepszeprzypisania,1000lepszaidentity;obiecopieszachowaneosobno bezglobalnegoogłoszeniabezwzględnegobest. Readonlyvalidate_1000_1200seed317592840eightpairsrandom+8nearL1/2/3/4/8+8prefixdiff,full36statesqueryorder;identitywobu. Nieautoaktywacja;historyexposurenotverified,widocznecasesdiagnosticnotfinal.

Fresh1000vs1200seed317592840:identity631vs627;nearL3 264vs270/288,both74vs84/96;nearL4 remis217/288,both31vs33/96;randomL4 279vs277;nearL8 206vs204. Niewielkiróżnytradeoff,niezastąpionowag1000przez1200wprodukcji. Uruchomionoread-onlybinding-positionprobe4char8pairsperpositionfull36states/query/order1152cases,seed39268140,both1000/1200. Cel diagnozy lokalizacjiróżnicy w czteroznakowychnear nazwach,nieblindmoretraining.

### 2026-10-12 — pozycja różnicy w przypisaniu
Seed39268140L4near:1000positions1/2/3/4correct248/233/270/236na288;1200248/227/277/233. Brakpojedynczejblokującejpozycji,2i4słabsze. Source1000wybranyfork ze względuidentity631v627i zbiorczo podobnybinding,1200zachowany. Controlled300perarm odIDENTYCZNEGO1000weights/opt/RNG:istniejącyvaluekeypointerhead0.2 vsdodatkowenamekeypointerhead1.2. Queryfinal#dotkeysostatnichznakówobu nazw PRZEDwartościami;samecorrectfacttargetcomputedONLYtrain. Bez nowychparams/headinference. Nativeoutputretentionweryfikowaćoddzielnie,nieauxaccuracyzasukces.

### 2026-10-12 — zatrzymanie na polecenie użytkownika
Trening przerwany, automat PAUSED. Oddzielna pełna kopia fresh_si i outputs w zapis_SI_2026-10-12_zatrzymana. Ostatni kompletny checkpoint attention_supervision_200, bieżące porównanie nieukończone; dalszych niezapisanych kroków nie odzyskano. Nowy rdzeń Transformer, nie TIMDR.

### 2026-10-12 — nowa autoryzacja budowy TSI
Na polecenie budowy z koordynatora TIMDR utworzono osobny work/TSI, nazwany przez użytkownika timderSI (TSI). Rzeczywisty TIMDRWorkflow steruje kontraktem i konstrukcją. Nowy shared-GRU/addressed-memory model49957params,150steps444/445. Drugi test1525unseennamecases1502correct,existingfacts1440/1440;missingnear14/37. Ograniczenie zapisane, nie poprawiano wag na tym teście. Oldpausedexperimentarchiveunchanged,nopush/noactivation.


### 2026-10-12 — TSI: utrwalanie rozpoznawania braku nazwy
Zachowany najlepszy checkpoint multifact_100.pt: monitoring 4610/4658, zero utraconych wcześniej poprawnych. Nowy test pełnych nazw wykluczonych z treningu: przypisania 2206/2208, podobne nieobecne nazwy 438/480. To pomiar strukturalnych faktów, nie języka naturalnego. Uruchomiono ograniczone 200 kroków od tego checkpointu z optymalizatorem, lr 5e-5, obok podobnych nieobecnych nazw także podobne obecne nazwy. Native CE + pointer CE 0.5 + KL tylko poprawnego nauczyciela. Każdy krok zapisany atomowo z optimizerem/RNG; kontrola finite. Wcześniejsze wagi i aplikacja bez podmiany. Sesja 19983, raport TSI_UTRWALENIE_BRAKU_NAZW.json.


### TSI — świeże porównanie utrwalenia
Consolidation175 SHA974ca98d66674d52cab16a23928e266921fb3c95379ada89228d6946f4808c0b: nowy test 3–12 znaków, przypisania2206/2208, nearabsent449/480 vs441/480 bazy;8gains,0lost. Zapis best/near_absence_175.pt. Generator testu pierwotnie utknął na prawie wyczerpanych nazwach długości2: poprawiono ograniczenie prób i jawnie zmieniono zakres na3–12. Bez wdrożenia. Kolejny ograniczony etap początek/koniec/dodatkowy znak, od best175 z optymalizatorem.


### TSI — diagnoza wariantów i ograniczona kalibracja
Warianty przerwano po125:14lost. RO diagnoza: obecne8490→8492/8496,0lost2gain;nieobecne1425→1417/1538,14lost6gain. Wszystkie utracone przypadki były nieobecnymi podobnymi nazwami. Best175 zachowane. Uruchomiono ograniczone100kroków kalibracji wyłącznie2 istniejących parametrów null_similarity/log_scale;encoder nazw,values i decision zamrożone,nowy optimizer2paramów. Wyniku jeszcze nieustalono. Zapis każdego kroku, finite checks.


### TSI — kalibracja i podstawy operatorów
Kalibracja2paramów best75:9939/10034 zeroLost. Świeżytest seed71392846:2208/2208 przypisane,455/480nearabsent,3gain0lostvsbest175; zachowano best/null_gate_75.pt. Rozpoczęto odrębny uczony moduł LearnedLogic,6operatorów NOT/AND/OR/XOR/IMPLIES/EQUIV,probabilistyczneodczyty2operandów+operator embedding+MLP. Dane goldtruthtable wyłącznie trening, braklookupwforward. Rdzeńfaktówzamrożony.75update54/54named i54/54literal,bitwisebaseunchanged. To pełne kontrolowane podstawy3stanów, nie niezależnytestzłożonychwyrażeń/języka. Wymaganadalszawalidacja.


### TSI — pierwsze złożenia operatorów
Foundation75: nameddepth1present40/40,depth2present36/40,depth3present35/40 (retrieval40/40). Wykryto błędy propagacji wyjść operatorów mimo poprawnego odczytu faktów. Literalne1000-case testy pierwotnie losowały operator wspólny dla batcha, więc niepełne pokrycie; generator poprawiono na losowanie każdej próbki osobno. Nowa ograniczona200-krokowa nauka tego samego modułu,3kolejne uczone operacje z backprop przezsoftmax,primitiveCEreplay;frozenbase nadal chronione,każdykrok zapisany. Interfejs wyrażeń to strukturalne drzewo, nie język naturalny. Funkcje prawdy służą wyłącznie etykietom referencyjnym/nauce;inference korzysta zNN.


### TSI — porównanie miejsca na wyniki pośrednie
Użytkownik wskazał potrzebę miejsca przy złożeniach. Dodano LogicWorkspace16:uczony16-wymiarowystan każdego węzła,zerowo inicjalizowana korekta zachowuje początkowe logity dokładnie. Kontrola5363parametrowvsworkspace z dodatkowymi parametrami;nie izoluje samego efektu pamięci. Oba ramiona identyczne100batchesdepth8,lr.0005. Po nauce oba5000/5000 kontrolnychłańcuchów głębokości1,2,4,8,16. Brak wykazanej przewagi dokładności. Trwa świeżytest rozgałęzionych drzew1–5 i nowych nazw/missingfaktów. Poprzedni composition200fresh:4000/4000literal,120/120knownnamed,118/120missingnamed;to zakres strukturalny,nienaturalnyjęzyk.


### TSI — sprawdzone drzewa i rozpoczęcie polskich poleceń
Oba warianty logiki: świeże10000/10000 drzewdepth1–5 (1000każdydepth×2rodzaje alfabetu stanów),240/240nazwane rozgałęzienia na nowych pełnych nazwach. Brak przewagi poprawności workspace16;zachowano oba,mainbestlogic_100.pt=probabilities_only100. Wcześniejszy prompt monitor błędnie podał20k;poprawna liczba10k. Rozpoczęto osobny uczonyInstructionBridge:charEmbedding32+biGRU64+7operatorlabels+4spanpositions. Trenuje odczyt/NOT/AND/OR/XOR/IMPLIES/EQUIV z polskich zdań,nowe pełne nazwy,4formy/op;monitorrozbityknownform/newform. Pamięćfaktów i logika nie uczestniczą woptimizacji. Każdykrokweights/optimizer/RNG;500boundedupdates. Nie jest jeszcze parserem dowolnego języka ani zagnieżdżonych zdań;trzebaswieżegoendtoendtestu.


### TSI — język: przenoszenie sformułowań i ochrona pamięci
InstructionBridge500:knownforms168/168,newforms42/168;forma200168known33new,350168known47new. Sourcebest350 zachowany. Rozpoczęto300boundedupdates tego samegoBridge z optimizerem i niższymLR.0005,50%oldformreplay+50%kombinacjezwrotówprefix/body/suffix. Dawne heldoutforms mają jawny status development po poszerzeniu treningu;osobny test nowych kombinacji. Nie uznano dopasowania form za rozumienie dowolnego języka. User wskazał przyszłąarchitekturę:zamrożona sprawdzonapamięć,uczony rdzeńdecyzyjny;zapisano module_policy.json z SHA pamięci i logiki. Obecne NLuczenie dotyka tylkoBridge;samodzielnywybór wielu modułów/ocenawyników jeszcze niezaimplementowany.


### TSI — wykryty skrót w pierwszym argumencie
Languagevariation300:knownforms168/168,formyrozwojowe168/168,nowezłożonewstępy0/168 dokładnych ekstrakcji. ROdiag source250 pokazała systematycznie pierwszyargument=czasownik określ (poProszę), drugiargument właściwy. Nie uznano sumyzageneralizację. Nowy300-krokowy etap odbestvariation250,bezresetu:różne wstępy/wieloczęściowe ramki i replay,training-onlyLinear128→2charnamevscontext258parametrów,balancedauxCE.2. Headpomocniczyniewchodzi doinference,checkpointzachowujegoosobno+optimizer2groups. Pamięćilogikazamrożone.


### TSI — poprawa ekstrakcji i pierwsze działanie od polecenia
Prefixrepair300known168/dev168/newcombinations151/168exact. EndtoendROsourcevariation250 vsrepair100/150,252cases7ops×9states×2order×known/newframe,newfullnames. Wszystkieknown126/126. Newframebaseline0exactparse,50/126answers (część przypadkowo poprawne);repair100122/126exact/answers,150123/126. Zarejestrowano3lost odpowiedzi względem źródła mimo błędnejparsy źródła i75/76gain;tego nie ukryto. Najnowsze250/300trwa osobneświeżeporównanie. Genericdispatcher TSISystem służy integracji uczonejparsy, pamięci i NNlogiki,niewprowadza słownika odpowiedzi. Zakres jedno polecenie +z góry strukturalne fakty,bezpełnegojęzyka/nestedNL.


### TSI — aktualizacja bieżącego README
Przepisano bieżący README na stan12października:156787parametrówłącznie(pamięć108725,logika5363,język42699). Ujęto świeże wyniki w zakresie i szeroką diagnozę języka1512case:singleletter77/378answers18parse,numbered299/378answers306parse,Polish190/378answers108parse,difflength179/378answers135parse. Starszy README zachowany jakoREADME_SI_STAN_2026-10-11.md. Protected memory/logichashunchanged. Dokumentacja nie deklaruje pełnej gotowości.


### TSI — poszerzenie rodzajów nazw
Szerszytest1512ukończony, wynik wREADME. Zidentyfikowano lukę danych:wcześniej losoweASCII min3znaki. Nowy300-krokowy etap odlanguage_prefix300+auxiliary+optimizer2grupy,lr.0003:randomreplay/singleuppercase/numberedprefix/Polishstems/shortmixed1–3. Pełne testowe nazwy E/F i polskiefamilie wykluczone. TemplateFormatter zapisuje dokładnepozycjeargumentów przy składaniu tekstu;nie używa szukania litery w całym zdaniu do etykiet treningowych. Zapobiega labelcollision krótkichnazw i nazw będącychprefixem drugiej. Logika i pamięć nadalzamrożone,każdykrok zapisany,last_batch dodany docheckpointu. To nowy zakres testowany,nie gotowafunkcja. Dokumentację bieżącą wypchnięto wcześniej bezkodu jako d48a409.


### TSI — wynik pokrycia nazw i ochrona języka
Coverage300 diagnosticparse:single351/378,numbered378/378,Polish369/378,difflength297/378,known168/dev168;newcompoundcombinations0/168. Zapisano tradeoff,nie wdrożono. Nowybounded300updateodcoverage300weights/aux/opt,teacherfrozenprefix300language,KL2wyłączniecorrectoperator lub całkowiciecorrectspans naonlinegold;krótkie/złożonepoleceniamixedbalancednames. Pamięć/logikanieuczone. User pytał oEnglish:docelowa osobna uczona warstwa wejściowa mapująca do tychsamychoperatorów/argumentów;pełnetłumaczenietekstu niejest konieczne wtymzakresie. Englishjeszczenieimplementowany,najpierw stabilizacjaPolish.


### TSI — diagnoza bez języka podczas stabilizacji
Readonlyexpectedquerytestźródłowejpamięci(bestnull_gate75)na tychsamych4familiach:letters36/36,Polish36/36,difflength36/36,numberedprefix32/36. TestomijaBridge,zachowanobasesHA. WiększośćbłędówszerschpoleceńwięcwBridge;4prefix-numberedcasejużwpamięci. Nieodmrożonopamięci/logiki. Retentionrepairtrwa,150newcompound80/168vs0coverage,tradeoffinnefamilieraportowany,nieaktywowany.


### TSI — проверка pojemności warstwy języka
Retentionrepair300 przywrócił częśćcompoundform114/168 (best250119),ale innefamiliepogorszone;nie wdrożono. Uruchomiono100update×2armskontrolowanej nauki Bridgewidth64vs128odidentycznychcoverage300weights. Rozbudowano wyłączniebiGRU iwyjścioweprojekcje,embedding32bez zmian;wagi starych jednostek przeniesione,nowe kanałyzerowe z małymi połączeniamiwyjściowymi,initiallogit/predpreservationtest wszystkich2016kontroli. Identycznefrozenbatches70row×100,5namefamilies/4sentenceforms,nowyoptimizerjednakowyobuarmLR.0003,correctteacherKL.5,bezauxwobu(nowyoptimizer jawnie). Rdzeńpamięci/logiki zamrożony. Wynik nieustalony;każdykrokweights/opt/RNG+nextbatchindex,frozenschedule.


### 2026-10-13 — wynik pojemności i arność argumentów
Kontrolowana100-step próba języka42 699vs130 891parametrów nie wykazała przewagiszerszego:model64lost117/gain38,128lost126/gain27 względemcoverage300;gorszeniewdrożone. To krótkipomiar,nie dowód braku korzyści pojemności wogóle. ROinterwencjasuffix:coverage300READfirstnamepoprawny,unusedsecondspan=danych tylko przy nowymfooterze;przyknownfooterze/bezfooterunaryspanduplicatecorrect. Ustalonobłądinterfejsu:READiNOTmają1operand,niepotrzebnydrugi nie może blokowaćwykonania. interpretpoprawiono naarity1,referencjamiaryparseradostosowanowoddzielnychdalszychpróbach,historycznychliczbnie przeliczono potajemnie. Rozpoczęto200-krokowe uczenie Bridge odcoverage300zmaskąloss tylko wymaganychheadów,różnymifooterami inazwamicorpus;teacherchroncorrectrequiredheads,memory/logicfrozen.


### 2026-10-13 — dopiski i właściwe argumenty: kontrola w toku
Suffixarity100:known168/dev168,compound165/168,letters378/378,num369/378,Pol369/378,difflength279/378. Miara wymaga tylko jednego argumentu READ/NOT;nieporównywaćbezpośrednio z wcześniejszą błędną miarąduplikowanych2argumentów. Wagi kandydat100zachowane,próba200w toku;przygotowano NOWYfreshendtoendfooterseed81927364po zakończeniu. Bez podmiany źródła.


### 2026-10-13 — alternatywna reprezentacja poleceń jako słów
Suffixarityfresh252:sourceprefixknown125/newfooter41answers (28exact),candidate100known125/newfooter94answers (63exact),200known125/newfooter90answers (68exact). Gapsnewformremain,lost2/4respectivelyreported,notchosenproduction. Zastosowano diagnozę kontekstów i braku przewagi largercharBridge;uruchomiono odrębnyWordInstructionBridge. Tokenizer słów/punktuacji określa tylko granice składni,bez reguł operacji/odpowiedzi. ZamrożonynameencoderTSI dostarcza96-wymiarowe wektory słów;uczą sięcontextbiGRU64+op7+2word-pointers. Cacheprzechowuje tylko wektoryencodera,nie etykiety/odpowiedzi. BazazachowanaSHA i bitwisechecks. Nativewordfrontend63369paramsplus współdzielona pamięć108725;starycharBridgewszystkiewagizachowaneosobno,niewdrożonoalternatywy. Bounded300updatesfromrecordedtrainingpool(frozenbatches+savedlastbatches),każdykrokzapisany,testing wymaganychoperandów. Researchinspirationword+charsequence tagging https://aclanthology.org/P16-1101/;nie jest kopią tego modelu ani dowodemuniwersalnejsemantyki.

### 2026-10-13 — słowna warstwa poleceń, krok 300
Zakończono 300 kroków. Diagnostyka: krótkie nazwy 378/378, polskie nazwy 378/378, numerowane 369/378, różne długości 333/378, kombinacje wstępów 166/168. Pamięć bitowo niezmieniona. Dodano obsługę słownego checkpointu z kontrolą SHA bazy w TSISystem. Trwa niezależny test całego działania na nowych pełnych nazwach (sesja 98520); wyniki diagnostyczne nie oznaczają gotowości ani wdrożenia.

### 2026-10-13 — sprawdzona warstwa słowna i stabilizacja
Świeży test 252: word300 znane formy 125/126 odpowiedzi i 121/126 dokładnych interpretacji; nowy dopisek 123/126 odpowiedzi i 119/126 interpretacji. Char prefix300: 126/126 oraz 53/126 odpowiedzi. Word300 utracił 3 wcześniejsze poprawne odpowiedzi, zyskał 72; niewdrożony. Zachowano best/word_language_300.pt. Błędy: wybór słowa bez zamiast drugiej nazwy, pomyłki XOR/OR i powielenie drugiego argumentu implikacji. Wznowiono dokładne wagi/optimizer/RNG word300, lr0.0007, maks600, correct-teacher KL0.2 tylko na poprawnych operatorach/argumentach treningowych. Zamrożona pamięć i logika; pool zapisany osobno, każdy krok atomowo. Sesja61151, raport TSI_JEZYK_SLOWA_STABILIZACJA.json. Nowa końcowa walidacja wymagana po tej adaptacji; dotychczasowy test staje się diagnostyczny.

### 2026-10-13 — stabilizacja słownej warstwy ukończona
Krok600: krótkie, numerowane, polskie i różnej długości nazwy po378/378 dokładnych interpretacji diagnostycznych; znane formy161/168, wcześniej ujawnione warianty141/168, kombinacje167/168. Baza bitowo niezmieniona. Wszystkie kroki301–600 zapisane z optimizerem/RNG. Trwa nowy test504 przypadków w4 formach na świeżych pełnych nazwach, porównanie word300/500/600 (sesja99854). Osobno utracone poprawne odpowiedzi i utracone poprawne interpretacje z odpowiedzią. Wynik monitorowanego zestawu nie oznacza gotowości ani aktywacji.

### 2026-10-13 — walidacja i zbalansowanie operatorów
Świeży test504: word300471 odpowiedzi, step500491 (6lost26gain), step600492 (7lost28gain). Poprawne interpretacje z poprawną odpowiedzią:500 utracił10 i zyskał46,600 utracił13 i zyskał50. Żaden automatycznie niewdrożony. Szczególnie AND z oraz bywa mylony z IMPLIES/NOT/XOR mimo poprawnych nazw. Nowa ograniczona próba od500 z wagami/optimizer/RNG, lr0.0005,200update: osiem par świeżych nazw, każda przy wszystkich siedmiu operatorach, wspólny wstęp/dopisek dla operatorów danej pary. Hipoteza ograniczenia zależności decyzji od nazw/kontekstu, nie udowodniona przyczyna. Teacher word300 ochronny KL tylko gdy poprawny na treningowym przykładzie. Baza/logika zamrożone. Sesja82026, train_word_operator_balance.py, raport TSI_JEZYK_OPERATOR_NIEZALEZNY_OD_NAZW.json. Każdy krok atomowy, nativeNN bez reguł operatora w inference. Po700 nowy niezależny test i lost/gained wymagane.

### 2026-10-13 — zbalansowane operatory: weryfikacja
Krok700: diagnostyczne378/378 w każdej czterech grup nazw, known164/168,development143/168,compound168/168; baza bitowo niezmieniona. Nowe pełne nazwy,504cases w4 już diagnostycznie ujawnionych formach: word300469/504 odpowiedzi;500477/504 lost10gain18;700487/504 lost5gain23. Krok700 znana forma126/126 zarówno interpretacje jak odpowiedzi, pozostałe odpowiedzi119/121/121 ze126. Nie wdrożono regresji. Nazwy nowe, formy nie są finalnym nieujawnionym heldoutem języka. Następna diagnoza zależności klasy operatora od podstawienia samych nazw.

### 2026-10-13 — test podstawiania nazw i kontrolowane porównanie
Sonda1050: word300944 dokładnych interpretacji;word500994;word7001007. Z21 szablonów operator zależał od podstawienia nazw w4/2/3 odpowiednio. Singleletters znane tokeny, wieloznakowe nazwy wykluczone trackedtraining. Przykład systematycznego błędu: Proszę sprawdź A i B teraz klasyfikowane jako XOR/OR zamiast AND. Uruchomiono dwa SEKWENCYJNE ramiona100update od identycznego700 z tym samym optimizer/RNG/lr0.0003 i batchami:control versusoperator_consistency. Każdy batch4grupy, po2podstawienia nowych nazw dla tych samych7operatorów/szablonów. Eksperyment dodaje symetryczny KL między natywnymi logitami operatora pary (.15 wagi każdej strony). Oba zwykłe CE i correctteacherKL0.2. Brak nowych parametrów lub reguł inference. Każdy stan zapisywany, baza/logika zamrożone. Sesja20457, skrypt train_word_operator_consistency_arm.py. Nie aktywuje. Preparedvalidate_word_consistency_e2e.py uruchomić dopiero po zakończeniu obu800. Hipoteza stabilności nieudowodniona do porównania.

Porównanie kontrolne zatrzymało się po zapisanym750 przez TypeError: łączenie Path i str przy ścieżce raportu. Poprawiono nawiasy ścieżki, wznowiono dokładny checkpoint750 z optimizer/RNG; last_batch wszystkich zapisanych kroków odzyskuje tracking nazw. Nie utracono aktualizacji. Nowa sesja89884 kontrola do800, potem sekwencyjnie consistency700→800.

### 2026-10-13 — porównanie spójności: wynik
Oba ramiona ukończone800. Kontrola zgodności wszystkich100 batchów: identyczne dane treningowe i brak wzrostu parametrów. Świeże504 przypadki:source700496 odpowiedzi;control800497(0lost1gain),consistency800500(1lost5gain). Dodatkowy loss spójności nie daje jednoznacznej niergresji. Zachowano osobno best/word_control_800.pt, bez aktywacji. Rozpoczęto validate_word_independent_forms.py sesja78885: pięć rodzin nowych pełnych nazw i dwie nowe całościowe ramy poleceń plus znana kontrola,1890cases,porównanie700/control800. Zewnętrzne fakty nadal strukturalne; nazwy blocked całymseen/priorfixtures, dwaorderfactów, wszystkie9kombinacji. Przed interpretacją sukcesu sprawdzić każdąformę/rodzinę,parseansweriutraconekonkretne odpowiedzi.

### 2026-10-13 — szerszy heldout: dopisek udający operator
1890cases5family×known/newA/newB:source700 known628/630,newA620,newB437;control800 known628,newA622,newB424;lost27/gain16 i niewdrożony. Nowe ramy B negacja...i podaj wynik jest błędnie odczytywane jako AND/XOR z podaj jako drugim argumentem. To błąd parsera, nie zamrożonej logiki. Uruchomiono ograniczoną naprawę od700 weights/optimizer/RNG, kroki701–900,lr0.0003: te same nazwy/operator/wstęp z dopiskiem typu i podaj wynik/oraz zwróć rezultat/i wypisz odpowiedź i bez niego,56rowsbatch/all7ops. Teacher700KL tylko poprawny onlinegold. Scope bez reguł inference/nowych parametrów; pamięć/logika frozen, każdy checkpoint atomowyfiniteguards. Sesja87711, train_word_footer_disambiguation.py, TSI_JEZYK_ODROZNIENIE_DOPISKU.json. Po900 przygotowany validate_word_footer_transfer.py(seed319872645),1890cases nieuwefullnames/priorblocked,known+seen-distractor/newnames+newcombination a potem pokaż odpowiedź. Użyty poprzedni heldout jest teraz diagnostyczny, nie finalna walidacja. Finalny niezależny test wymagany przed wdrożeniem.

Naprawa dopisków zakończyła900; diagnostycznieknown160/dev130/compound167,short378,num351,Pol378,diff333. Regresje na starych formach raportowane, źródło700 nietknięte. RO validate_word_footer_transfer.py sesja99727 uruchomiona. Konsultacja źródła pierwotnego https://arxiv.org/abs/1701.06538 (uczona bramka wyboru ekspertów) jako potencjalny kierunek zgodny z zamrożonymi modułami i decyzyjnym rdzeniem; niczego takiego jeszcze nie wdrożono, obecna architektura nie jest kopią tej pracy. Decyzję o bramce poprzedzi pomiar uzupełniania błędów specjalistów.

### 2026-10-13 — specjaliści i uczony wybór
Nowy test1890 footer900: zwykłe627/630(vs700630),dopisek623(vs447),nowakombinacja576(vs495);łącznie1826/1890,lost15gain269. Nie wdrożono regresji. Oracle wyłącznie diagnostyczny na testgold: union obu1841/1890 odpowiedzi i1791/1890 poprawnychinterpretacjizodpowiedzią;to górna granica,nie realny wynik bramki. Uruchomiono train_language_selector.py sesja81448. Zamrożone parsery700/900,pamięć i logika;uczy się tylko17 986parametrowa bramka278→64→2 na hidden/logitach/confidence/entropy parserów. Szablony wybiera wyłącznie NN, bez reguł słownych/odpowiedzi. Treningowe dane:40batchów wcześniejszych dwóch prób i40batchów starego treningowego poolu;goldselektora tylko op+argumenty treningowe. Gdyobapoprawnepreferuje700,gdyobaźlepróbkapominięta(wciąż ograniczenie systemu). Żadnego testgold wtrain/inference. Cachefeatures tylko modele frozen,treningbezodpowiedzi faktów. Każdy krokweightsgate/optimizer/RNG/expertSHA atomowofiniteguards,200updatesbounded. Kandydat eksperymentalny niewdrożony,niepełny arbiter jakości. Po ukończeniu niezależne nowe dane i indywidualne odpowiedzi/parse/retention wymagane.

### 2026-10-13 — selektor ukończony i walidacja
Ukończono200kroków selektora17 986parametrów,6666/6872 wyborów zgodnych z treningowymi etykietami (nie wynik generalizacji ani e2e). Oba pliki ekspertów mają niezmienione SHA; loader LanguageSelector.from_checkpoint odrzuca mismatch zanim użyje wag. Pamięć wspólnej bazy zgodna SHA,flagirequires_gradfalse dla ekspertów i logiki. Rozpoczęto validate_language_selector.py sesja35105:1890matchedcases5namefamilies/9states/2orders,knownform,znanytyppodajwynik,nowe Z dostępnych danych proszę określ...i napisz odpowiedź. Fullnamesexcludedtrackedseen/frozen. Porównuje700/900/gate200;wynikiop/args/answerosobno,priorcorrectlostgainedisemantic. Trening selektora nie używa testgold; oracle wcześniejszy nadal tylko upperbound. Niewdrożony.

### 2026-10-13 — selektor: generalizacja i nierównowaga danych
Fresh1890:parser7001407 odpowiedzi,9001813 lost22gain428,selector2001695 lost8gain296. Selektor genuinecorrectparse+answer lost1;nieaktywowany. Zachowanie zwykłychpoleceń630/630 zostało utrzymane, lecz traci część poprawnych przypadków w innych grupach. Cachetreningowy6872eligible:6261classold/611classnew,na50trainingaccuracy6261(przewaga klasy większościowej);nieudowodniona jedyna przyczyna OOD. Uruchomiono kontrolowane2sekwencyjnearms200eachod identycznego selector200weights/optimizer/RNG/cache,lrs0.0005:uniform_controlCE vs inverse-frequencyclassweightedCE. Wszystkie dane, minibatch_ids i parametry poza wagąloss identyczne. Całeeksperty/pamięć/logika frozen;uczytylko17986gate. Każdykrok201–400atomowyweights/opt/RNG/expertSHA/batchids. Sesja70211 compare_selector_class_balance.py,raport TSI_SELEKTOR_BALANS_KLAS.json. Poobu400 preparedvalidate_selector_class_balance.py新seed4918273561890casesoldselector200/uniform400/balanced400.newfullnames,newframeZgodnieztymizapisamiwyznacz...poczympodajrezultat. Ordinaryfacts/policyfrozen. Wyniktreningowyniesukces,finalświeżevalidationpluspriorcorrectkontroleprzedwdrożeniem.

Obie próby wyrównania klas ukończone400. Uniform: poprawnewyborytreningowe6161/6261old i522/611new. Balanced:5957old i594new — tradeoff,niegotowość. Uruchomiony validate_selector_class_balance.py sesja90556, test1890nowychprzypadków. Brakaktywacji;wagiekspertów,pamięciilogikinienaruszone.

### 2026-10-13 — balans klas: efekt i etykiety jakości
Nowy test1890:selector2001695 odpowiedzi,uniform4001721 lost9gain35,balanced4001796 lost6gain107. Każdy zachował630/630zwykłychpoleceń;balanceddopiski623/630,nowywariant543/630. Niewdrożonyzpowodu6utraconychpoprawnychodpowiedzi. Datasetetykietobiepoprawne→zawszeold zawiera sztuczną preferencję, więc uruchomiono ograniczone porównanie odbalanced400weights/optimizer/RNG naidentycznychcachedtrainfeaturesieligiblemask: preference_controlbalancedCE vsquality_scoresBCE osobnopoprawnośćkażdegoeksperta. Gdyobaźle nadal pomija(ograniczenie jakości),gdyobapoprawneBCE[1,1],aCEpreferujeold. GoldTYLKOpoprawnyoperator/argtreningowy,nietestanswers. Wszystkiestany401–500weights/opt/RNG/expertSHA/batchidsatomicfinite;uczytylkogate17986,frozenparsersmemorylogic. Sesja30332 compare_selector_quality_targets.py,cachequalitylabelsrecomputes7280frozentrainingcases(niepowielatrainingexperts). Przygotowanyvalidate_selector_quality.pyseed6281937451890newnamesforms,wordframeKorzystajączapisanychwartościsprawdź...anastępnieprzedstawwynik;launchdopieropoobu500.Nie deklarować pełnego arbitra ani gotowości na podstawie trainingloss.

Walidacja4917 długo działała z pojedynczymi odczytami; przerwano WYŁĄCZNIEreadonlytest (bez zmian wag). Dodano interpret_batch/answer_parsed w LanguageSelector, kontrola32mieszanychpróbekpotwierdziłaidentyczneoperator/argument/wybóreksperta(batchvssingle). Wznowiono ten sam fixture1890 bez regeneracji nazw jako validate_selector_quality_batched.py sesja45853; partialwynikiarmów zapisuje TSI_SELEKTOR_OCENA_POSTEP.json. Pełny raport nadal TSI_SELEKTOR_OCENA_SWIEZY_TEST.json. To przyspieszenie walidacji, nie nowy trening ani zmiana modelu.

### 2026-10-13 — granica selektora i pomocnicze role wyrazów
Quality-targettest1890:balanced4001682 odpowiedzi,preference5001685 lost1gain4(genuinesemanticlost0),quality5001683 lost63gain64(genuinesemanticlost7). Nie wybrano qualityBCE, niewdrożony. Sonda oracleparse obu ekspertów na tych samych1890:1497 możliwych exactparse,393bothwrong,z czego376/630na nowymcałoścowymwariancie. Testgoldtylkodiagnostycznyniegatinginference. Większości tych błędów selektor nie może naprawić. Uruchomiono2SEKWENCYJNEarms200odidentycznegoparserfooter900weights/optimizer/RNG/lr0.0003,samebatches:control vsword_roleshelperLinear128→9(1161TRAININGONLYparams). Nativefrontend63369sameinferencearchitecture. Auxothercontext/name/operatorbodytype7 nauczane z adnotacji położeń generowanego tekstu WYŁĄCZNIEtraining. BodyrangeexactFormatter/goldoperator,nie instrukcjeruleinference. 50%starypoolreplay/50%sparowaneramywithwithoutdistractor includinganastępnieprzedstawwynik. NativeCE+correctteacher700KL.2wobu. Helperwobuarms/2optimizergroups,controlbezauxloss;resumehelperinitialize+addgroupPRZEDloadopt. Every901–1100atomicnativeweights/auxseparate/optimizer/RNG/lastbatch/expertbaseSHAfiniteguards. Baza/logika i stariparsery frozenprotected,nativecontextnowego parsera tylkojedynatrenowana kopia. Sesja48849,train_word_role_arm.py;preparedvalidate_word_roles.pyseed5192837461890casesformWoparciuozapisaneinformacjeustal...anakoncuwypiszrezultat. Noneactivated. Po1100freshandpriorcorrectlossspecificversuscontrolnotjustsum.

### 2026-10-13 — role wyrazów: negatywny wynik i diagnoza głów
Pełny świeży test 1890: source900 1777 odpowiedzi/1663 exactparse; control1100 1733/1576 (lost57,gain13); word_roles1100 1725/1561 (lost66,gain14). Nowy wariant630:source529,control474,role466. Roleauxniepotwierdzone jako naprawa, żaden kandydat niewdrożony. Wszystkie200batchesidentyczne potwierdzono mmap checkpointów w TSI_ROLE_KONTROLA_POROWNANIA.json. Readonlyprobe role1100:unseen630 auxiliaryrozpoznałName874/1080 prawdziwychtokenównazw i odrzucał jakoName wszystkie224błędnie wskazane słowa kontekstu. To partialinformacja wrepresentation,niepełnyalgorytm;pomocniczejgłowynie użyto jako inference. Uruchomiono ograniczoneporównanie200updatesod tychsamychrole1100nativeweights/RNG/data: full_control(CPUcontextuczone63369params) vsfrozen_context(tylkoistniejąceop+argumenty1161params). Freshoptimizer W OBU bo listaparametrówróżna,oryginalnyopt2groupsrole1100zachowanynieprzenoszony. LR.0003;50%oldpool50%pairedbodywithwithoutfooter,newprepositionprefixescontexts o;nativeCE+correctteacher700KL.2;auxNIEuczonynie używany. Każdy1101–1300atomicweights/opt/RNG/lastbatch/baseSHA/freezeparamsmetadatafiniteguards;memorybaseunchangediheadarmcontextbitwisechecked. Sesja45682 train_word_readout_arm.py. Przygotowano validate_word_readout.py seed482193756,newframes/names: Dla wartości zapisanych w pamięci oblicz...i zakończ podaniem odpowiedzi,1890matchedcases. Poobu1300 kontrolakategorii/priorcorrect,notclaimfixfrommonitor.

### 2026-10-13 — zamrożony kontekst i uwaga nad słowami
Nowy test1890:role1100 1751 odpowiedzi/1619parse;full_control1300 1749/1603 lost40gain38;frozen_context1300 1765/1638 lost2gain16. Frozen zachował630/630znane i630/630dopisane,nowywariant505/630. Lepszy kierunek,ale niewdrożony z2regresjami. Uzasadnione kolejne porównanie: odfrozen1300 identyczne nativeweights/headoptimizer/RNG/dane,obiecontextGRU i baza frozen;controlheadonly1161 vsaddition learned word attention readout1032params (score128→1,pooledcontextdelta128→7). Delta-zero początkowo dokładnie zachowuje wszystkie oparglogity:126mixedexamples,maxdiff0 i wszystkiepredictionssame, outputs/TSI_UWAGA_TRANSFER_POCZATKOWY.json. To transfer funkcji przed treningiem,nie sukces nauki. Nie standardTransformer. Uwaga zmienia tylko odczyt operatora, natywne głowyop/args uczonewobu;wzrostpojemności1032częśćtestowanejzmiany,nieizolowanyczystyefektuwagi. Modelkindword_attention_bridge wymagaWordAttentionBridge i explicitloader,TSISystemuzupełniony. Native63369→64401,trained1161→2193;headopt1300zachowany,wattentionnowagroupdla4nowychparametrów,nativeiattentionLR.0002. Every1301–1500atomicweights/opt/RNG/lastbatch/baseSHA/contextfreeze finiteguards,sourcesprotected. Sesja14481 train_word_attention_arm.py(controlpotemattentionsekwencyjnie). Preparedvalidate_word_attention.pyseed7139284651890newnamesknown/distractor/newphrase Mająctezapisanefaktyustal...poobliczeniupokażrezultat. Noregressionautoactivation;posttestpergroup/individualpriorcorrectrequired.

Obie próby odczytu uwagą ukończyły1500, baza i kontekst pozostały bitowo niezmienione. Monitorcontrolknown164/dev145/compound168,attentionknown164/dev144/compound168;wczterechgrupachnazw378/378każda. Brak korzyści w samym monitorowanym zestawie. Uruchomiona niezależna validate_word_attention.py sesja95651; wyniki aktualnej hipotezy dopiero po świeżym teście.

### 2026-10-13 — uwaga: brak poprawy i słaby sygnał gałęzi
Nowy test1890:sourcefrozen1300 1788 odpowiedzi/1673parse,control1500 1785/1671 lost3gain0,attention1500 1786/1673 lost4gain2. Uwaga niepotwierdzona jako naprawa,nie wdrożono. Readonlyprobe1500:δmaksymalnie0.257logita na nowychformach vsnativeśrednimargines4.10;operatorδalone251/630,combined501 vsnative498. Gradientnormδweight z nativeCE0.01769,zniezależnejδCE0.82952 naostatnim TRAINbatch. Goldtylkotrainingdla gradientu,testdo nieoperacyjnejdiagnostyki,żadnychweightupdateswsondzie. Uzasadnione porównanie200updateodsamegoattention1500weights/optimizer2groups/PythonTorchRNG,obiearch64401 i contextmemory frozen: native_CE vsbranch_CE dodające.5CEδ na goldoperatorach treningowych. Brak nowych parametrów;nie zastępuje całegoopheadδw inference. Pooledbranch samodzielnie uczy się operatora,a nativehead nadal CE+correctteacher1300KL.2 iargumentCE. Obagroupyoptimizerz1500zachowane,LR.0002. Every1501–1700atomicweights/opt/RNG/lastbatch/baseSHA/branchflagfiniteguards;oldstatesprotected. Sesja66504 train_attention_supervision_arm.py. Przygotowano validate_attention_supervision.pyseed5938172641890freshnameframes: Na bazie informacji z pamięci określ...a potem przedstaw otrzymany wynik. Wybraćpo nowymteściepercategory/priorcorrectnie samąsumą;hipotezasłabszegosygnałuniestwierdzeniemglobalnegopowodu błędów. Metadataopisoptimizeruodziedziczonyze wcześniejszegoscriptu;rzeczywiście z1500wczytanocałeDWAgroupystate,niezresetowano żadnegogrupu.

### 2026-10-13 — kalibracja siły gałęzi operatora
Native CE1700: 1818/1890 odpowiedzi, 9 odzyskanych, 0 utraconych oraz 0 utraconych poprawnych interpretacji względem attention1500 na identycznej próbce. Branch CE1700: 1817/1890, 8 odzyskanych, 0 utraconych odpowiedzi i 1 utracona poprawna interpretacja. Kandydat native1700 zachowany osobno, niewdrożony.
Uczono następnie tylko jeden nowy parametr skali dla każdego źródła na danych treningowych. Wszystkie wcześniejsze wagi bitowo niezmienione. Skale po 200 krokach: 3.552 i 1.749. Wartości nie zostały wybrane z testu. Uruchomiono niezależne porównanie czterech kandydatów na nowych nazwach i ramie polecenia; wynik oczekiwany w TSI_UWAGA_SILA_SWIEZY_TEST.json.

### 2026-10-13 — ograniczenie kalibracji i wpływ kontekstu
Świeży test 1890 przypadków: native1700 1653, jego skalowanie 1654 (3 utracone, 4 odzyskane, 1 utracona poprawna interpretacja). Branch1700 i jego skala po 1654; skalowanie utraciło 1 i odzyskało 1 odpowiedź. Nie wybrano skal do wdrożenia.
Sonda tej samej ujawnionej ramy: pełny kontekst 140/630 poprawnych interpretacji, bez wstępu 377, bez dopisku 264, sam korpus 491. Usuwanie kontekstu jest diagnozą, nie nowym sposobem odpowiadania. Uruchomiono ograniczone 100 kroków sparowanych wariantów kontekstu z zachowaniem źródłowego optymalizatora i RNG. Pamięć, logika i GRU kontekstu pozostają zamrożone; każdy krok archiwizowany.

### 2026-10-13 — zakończenie próby sparowanych kontekstów
Krok 1800 zapisany. Monitor: 165/168 znane formy, 145/168 grupa rozwojowa, 168/168 kombinacje oraz 378/378 w każdej z czterech rodzin nazw. Pamięć i GRU kontekstu bitowo niezmienione. Nie jest to dowód generalizacji. Uruchomiono porównanie źródła1700 i kandydata1800 na 3150 przypadkach, trzech nowych ramach polecenia i nowych pełnych nazwach, z oceną utraconych poprawnych interpretacji i odpowiedzi.

### 2026-10-13 — wynik kontekstów i kontrola marginesu argumentów
Porównanie 3150 przypadków: źródło1700 2807 odpowiedzi, kandydat1800 2827. Kandydat utracił 19 wcześniej poprawnych odpowiedzi i odzyskał 39; poprawne interpretacje z odpowiedzią: utracone10, odzyskane41. Nie wdrożono.
Diagnoza rankingów argumentów: na2160 wymaganych argumentach źródło wybiera1754 poprawnie; właściwy argument jest w pierwszych3 w2127 przypadkach. To pomiar z testowym wzorcem, nie metoda odpowiadania. Uruchomione kontrolowane ramiona po100 kroków od identycznego źródła1700: zwykła nauka kontra dodatkowy margines właściwego argumentu nad najsilniejszym błędnym, liczony wyłącznie z treningowych etykiet. Oba ukończyły1800 z bitowo zachowaną pamięcią i kontekstem; świeża walidacja1890 przypadków trwa.

Świeży test marginesu ukończony: źródło1762/1890 odpowiedzi i1625 interpretacji, kontrola oraz dodatkowy margines identycznie1768 i1642. Oba utraciły6 odpowiedzi i odzyskały12, utraciły5 poprawnych interpretacji z odpowiedzią. Nie potwierdzono korzyści marginesu, nie wdrożono. Uruchomiono odczytową diagnozę aktywności marginesu na treningu i nowej ramie; nie dodano testowych przykładów do nauki.

Diagnoza aktywności marginesu zakończona: trening67 błędnych z984 argumentów, margines aktywny87; nowa rama39 błędnych z1080, aktywny68. Ten pomiar nie potwierdza, że argumenty nowej ramy są trudniejsze niż treningowe. Następna diagnoza odczytowa rozdziela błędy operatora od argumentów i mierzy skupienie uczonej uwagi na treści zadania względem dopisków. Żadne testowe etykiety nie sterują odpowiedzią ani nauką.

### 2026-10-13 — diagnoza i kontrolowana nauka uwagi na treść
Na1890 ujawnionych przypadkach operator poprawny1488, błędny402. Średnia masa uwagi na korpusie zadania0.1904 i0.1888, przy udziale tokenów korpusu około0.235 w obu grupach. Pomiar nie potwierdza, że sama uwaga wyjaśnia błędy.
Uruchomiono ograniczone kontrolowane porównanie100 kroków od identycznego źródła1700: kontrola kontra dodatkowy treningowy cel uwagi na korpusie. Korpus jest oznaczany przez generator wyłącznie podczas treningu. Nie ma nowego parametru ani maski odpowiedzi przy inference. Wiedza pamięci i logiki oraz GRU kontekstu zamrożone, wszystkie kroki zapisywane. Przed wyborem konieczne nowe porównanie końcowych odpowiedzi i utraconych poprawnych interpretacji.

### 2026-10-13 — audyt generatora po konsultacji Claude’a
Odczytowy audyt poolu i100 aktualizacji:9681/2665 unikalnych ram;7646/1900 występują pojedynczo. Sonda znana forma628/630, rekombinacja znanych słów504, zmieniony wstęp404, dopisek333. Brak nowego treningu. Wnioski i ograniczenia w TSI_AUDYT_RAM_WNIOSKI.md.

### 2026-10-13 — wykonanie programu kombinacji ram
Na ponowne polecenie działaj uruchomiono200 kroków na każde z dwóch sekwencyjnych ramion od identycznego źródła1700 i pełnego stanu optymalizatora/RNG. Kontrola losowych ram kontra cykliczne24 z36 kombinacji6 wstępów i6 dopisków. Budżet aktualizacji i liczba wierszy są takie same, przykłady intencjonalnie różne;50% replay. Bez nowych strat/warstw/parametrów. Pamięć, logika i GRU kontekstu zamrożone. Rezerwowane kombinacje dotyczą nowego generatora; przed deklaracją heldout trzeba sprawdzić ich historyczną ekspozycję w replay. Każdy krok zapisywany. Monitor wznowiony po nieudanym przekazaniu pracy.

### 2026-10-13 — program ram zakończony, brak przewagi
Oba ramiona200 kroków zakończone. Mały test630: źródło562 odpowiedzi, kontrola oraz zbalansowany program561, po3 utracone i2 odzyskane odpowiedzi. Dokładne interpretacje nowych słów:22/126 źródło,28 kontrola,24 balanced. Niewdrożone. Program zbalansowania danych nie potwierdził oczekiwanej przewagi.
Dopasowanie560 rzeczywistych nowych wierszy treningowych programu: źródło478 dokładnych interpretacji, kontrola494, balanced496. Nie opanowano nawet tej próbki treningowej; to nie wyłącznie błąd transferu na nowe ramy. Dalszy krok wymaga diagnozy ograniczeń adaptacji zamrożonego kontekstu i głów, nie ślepego wydłużenia danych.

### 2026-10-13 — sprawdzenie pierwszego błędu TSI na prośbę użytkownika
Pierwszy raport to444/445, nie potwierdzono16/17. Odtworzono444/445 na zachowanym candidate150. Jedyny błąd: facts signalA=prawda, signalB=fałsz, query missingQ; oczekiwane nieznane, odpowiedź prawda. Obecna chroniona pamięć null_gate75 zdała ten sam ujawniony zestaw445/445 i dawny błędny przypadek poprawnie. Nie ciągnie się ten konkretny błąd; test nie dotyczył języka, którego frontend wtedy nie istniał. Wagi niezmienione. RaportTSI_PIERWSZY_BLAD_POROWNANIE.json.

### 2026-10-13 — izolowana diagnoza dopasowania kontekstu językowego
Uruchomiono50 kroków na każde ramię, stały56-wierszowy zestaw treningowy od źródła balanced1900. Zamrożony kontekst kontra trenowany kontekst językowy. Nowy AdamW w OBU ramionach, identyczne wagi/dane/LR, bez przenoszenia optymalizatora przy zmienionej liście parametrów. Pamięć faktów i logika pozostają zamrożone. Każdy krok zapisany. To mikroskopijna diagnoza dopasowania, nie kandydat do wdrożenia ani dowód generalizacji. Żadnych nowych parametrów ani solvera.

### 2026-10-13 — wynik mikropróby kontekstu i transferu
Oba warianty osiągnęły56/56 na stałym treningu: kontekst zamrożony po40 krokach, trenowany po10. Nie potwierdza to niezdolności zamrożonej reprezentacji do dopasowania.
Zmiana nazw przy tych samych ramach: źródło459/560, frozen466, trainable511 dokładnych interpretacji. Znane polecenia: źródło252/252, frozen252, trainable237. Uczenie kontekstu poprawia przenoszenie w tej sondzie, ale powoduje15 regresji znanych poleceń. Mikrowagi niewdrażalne, stanowią tylko diagnozę kompromisu. Nowe losowe nazwy nie zostały sprawdzone względem całej historii, więc to nie finalheldout. Pamięć faktów bitowo niezmieniona, logika zamrożona.

### 2026-10-13 — kontrolowana adaptacja kontekstu z ochroną
Uruchomiono po100 kroków control/protected od źródła balanced1900, nie od mikrowag. Pełny stan dotychczasowych2 grup optymalizatora zachowany; dodana3 grupa kontekstu zLR2e-5, głowy/uwagaLR.0002. Pamięć i logika zamrożone. Ten sam program danych i replay w obu ramionach. Protected dodajeKL2 do źródła1900 wyłącznie na treningowych replay, gdzie źródło ma poprawny operator i wszystkie wymagane argumenty. Żadnych etykiet testowych. Każdy krok zapisany atomowo, kontrolafinite i niezmienności bazy. Kandydaci nieaktywują się automatycznie. Kontekst językowy ma się zmieniać; jego bitowa niezmienność nie jest kryterium tej próby.

Adaptacja kontekstu z ochroną ukończona2000 w obu ramionach.100 identycznych batchy potwierdzono. Monitor identyczny:znane165/168,rozwojowe144/168,kombinacje168/168,każda rodzina378/378. Pamięć bitowo niezmieniona, kontekst zmieniony zgodnie z celem. Uruchomiono małą walidację630 przypadków źródło1900/control2000/protected2000. Brak aktywacji.

Mały test ochrony kontekstu630 ukończony: źródło558 odpowiedzi,control567 (lost3 gain12 semanticlost0 gain17),protected564(lost3gain9semanticlost0gain13). Dodatkowa ochronaKL2 nie wykazała przewagi nadkontrolą. Trzy utracone odpowiedzi miały w źródle błędną interpretację mimo przypadkiem poprawnej odpowiedzi; nie ukryto regresji. Control skierowany tylko do szerszej walidacji1890 na nowych pełnych nazwach pięciu rodzin i nowej całej ramie. Brak aktywacji, brak nowego treningu.

### 2026-10-13 — szerszy test adaptacji: niepotwierdzona naprawa
Szerszy1890 test adaptacji: źródło1725 odpowiedzi,control1722;lost10gain7semanticlost16gain8. Znane628/630 i dopisek630/630 w obu; nowa rama467→464 odpowiedzi i349→341 interpretacji. Mały test nie przeniósł się na szerszy. Controlniewdrożony. Protected2000 sprawdzany odczytowo na dokładnie tej samej fixture wobec tych samych baselinearrays;nie jest to nowy niezależnytest. Nie uruchomiono kolejnego treningu.

### 2026-10-13 — zamknięcie ochrony kontekstu, nowa hipoteza cech słów
Protected na tej samej1890 fixture1720 odpowiedzi,1594 interpretacje;lost9gain4semanticlost16gain4. Ochrona nie naprawiła szerszego testu. Seria zamknięta bez wdrożenia.
Przygotowano frontend WordLexicalAttention: niezależny resztowy encoder znaków słów8240 parametrów, tylko dla parsera; baza pamięci niezmieniona. Zerowa projekcja zachowała wszystkie630 sprawdzonych logitów dokładnie(maxdiff0);gradient projekcji finite i niezerowy(norm5.502). Zapisinitialoddzielny. To transfer początkowy, jeszcze bez treningu i bez dowodu korzyści. Hipoteza: uczone cechy językowe zamiast wyłącznie zamrożonych cech encodera nazw. Kolejny test ma izolować tę zmianę od strat/danych.

### 2026-10-13 — rozpoczęcie kontrolowanego testu nowych cech słów
Po50 kroków od źródła balanced1900: kontrola dotychczasowego parsera kontra nowy kanał8240 cech znakowych słów. Nowy kanał ładuje dokładnie zachowaneinitialz zerowym wpływem. Istniejące2 grupy optymalizatora przeniesione w obu, dodatkowa3 tylko dla cech. Ten sam LR.0002 i programdanych. Kontekst, pamięć i logika zamrożone. Każdy krok archiwizowany. Systemobsługujejawniekindword_lexical_attentioni weryfikacjębaseSHA. Początkowy transfer nie jest dowodem sukcesu nauki; konieczna walidacja. Łącznie186729 parametrów z jedną współdzieloną bazą.

Test nowych cech słów: oba ramiona50 kroków zakończone;50 identycznych batchy potwierdzono. Monitor kontrola378/378 wszystkie rodziny;lexical369/378 różne długości,pozostałe378. Brak aktywacji. Uruchomiono małą walidację630 na nowych nazwach i nowym połączeniu ramy: source1900/control1950/lexical1950. Dokładna architektura i baseSHA są weryfikowane przez system.

### 2026-10-13 — wynik małego testu cech słów
Źródło572 odpowiedzi/519 interpretacji630; kontrola573/523 lost1gain2semanticlost1gain5; lexical588/559 lost4gain20semanticlost5gain45. Nowe cechy dały przewagę nadkontrolą, ale nie bezregresyjną naprawę. Znane i dopisek po125/126 w każdym. Uruchomiono szerszy1890 test źródło1900/lexical1950 na nowych pełnych nazwach pięciu rodzin i nowej całej ramie. Brak aktywacji.

### 2026-10-13 — szerszy zysk nowych cech i regresje
Źródło1590/1890 odpowiedzi,lexical1664,lost5gain79semanticlost4gain119. Nowa rama331→406 odpowiedzi i107→223 interpretacji. Known629/630both,seen630→629. Kandydat zapisany oddzielnie best/word_lexical_1950.pt SHA945dd35b2580abf7c6fbedd86be19aa03e72e2db645aeb19c4baff661572dbdc,bez aktywacji. Na6 przypadkach regresji przywrócenie źródłowych głów nie zmieniło błędnych odpowiedzi;diagnoza wskazuje wpływ nowych cech,nie dowodzi jedynej globalnej przyczyny. Lokalne README zaktualizowane;kopie repo i push jeszcze nie wykonane.

### 2026-10-13 — ochrona cech nazw podczas adaptacji leksykalnej
Pomiar treningowych wystąpień: normaresidualnazw średnio0.0664(1248),słówkontekstu0.0539(4774). Nie jest to dowódprzyczyny regresji. Uruchomiono kontrolę i name_invariance po50 kroków od lexical1950 z wagami,pełnym stanem3 grup optymalizatora iRNG. Jedyna dodatkowa strata: średni kwadrat normy residualu na nazwach oznaczonych przez treningowy generator. Brak etykiet testowych i bramkowania przy inference. Pamięć,logika,kontekst zamrożone;każdykrok zapisany. Bestlexical1950nietknięty.

Ochrona cech nazw i kontrola ukończone2000. Potwierdzono50 identycznych batchy. Oba monitoryznane168/168,rozwojowe144/168,kombinacje168/168,każda rodzina378/378,pamięćikontekst bitowo niezmienione. Brak jeszcze wykazanej przewagi ochrony. Uruchomiono mały630 test1950/control2000/nameguard2000 na nowych nazwach i nowejramie. Niewdrożone.

Mały test ochrony nazw630: wszystkie3 warianty623 odpowiedzi,no lostgain. Interpretacje źródło602,control604(semanticlost0gain2),guard603(semanticlost1gain2). Dodatkowa ochrona nie wykazała korzyści w tejramie. Uruchomiono odczytowy test retencji obu2000 na dokładnie starej1890 fixture względem źródła1900 i porównania lexical1950. To test naprawy ujawnionych regresji, nie nowafinalwalidacja. Nie trenuje się na testowych przypadkach.

### 2026-10-13 — ochrona normy nazw nie poprawiła retencji
Na tej samej1890 fixture lexical1950 miał1664 odpowiedzi,lost5gain79. Control2000 ma1655,lost5gain70semanticlost4gain104;guard2000 ma1645,lost5gain60semanticlost3gain72. Oba naprawiły tylko1 z5 dawnych strat. Zachowały63/79(control) i55/79(guard) dawnych zysków. Ochrona normy nazw niepotwierdzona;seria zamknięta bez dalszego strojenia kary. Zachowano1950 jako lepszy kandydat, nie produkcję. Dalsze2000 stany archiwalne, niewdrożone.

### 2026-10-13 — selektor zamrożonych parserów jako ograniczona ochrona
Testowy pułap union oryginał1900+lexical1950:1669 odpowiedzi i1485 poprawnych interpretacji z odpowiedzią;405 przypadków obaj źle interpretują. To tylko pułap ztestgold,nie osiągnięta skuteczność selektora.
W danych treningowych znaleziono48 exclusive-correct:8 starszyparser,40 lexical. Nauka100 kroków wyłącznie17986 parametrów gate,zrównoważone próbkowanieklas,osiągnęła48/48 dopasowania. Obajpoprawni i obajbłędni nie uczą selektora. Żadne testowe etykiety nie weszły do nauki. Eksperci,pamięć,logika zamrożone. Uruchomiono odczytowy test ochrony na dokładnie starej1890 fixture;bardzo mały zbiór treningowy ogranicza wnioski. Niewdrożony.

### 2026-10-13 — brak poprawy selektora i brakujący typ danych
Gate100 na tej samej1890 fixture1663 odpowiedzi wobec1664 lexical;naprawił0/5strat i zachował78/79zysków. Niewdrożony. W48 treningowych exclusive-correct nie było przykładu duplikacji argumentu nowego parsera przy poprawnym starszym. Wejściegate nie zawiera jawnej zgodności argumentów ani duplikacji.
Zebrano1792 nowe przykłady TRENINGOWE z nazwami wykluczającymi testy. Znaleziono3old-onlycorrect i3new-onlycorrect, wszystkie3old-onlyto duplikacja nowego parsera. Zapisano dane i cechy bez zmiany wag. To bardzo mały przyrost świadectwa; nie wolno traktować go jako gotowości ani używać wzorca testowego do wyboru odpowiedzi. Następne kontrolowane porównanie ma sprawdzić uczone cechy zgodności, bez deterministycznego zakazu powtórzonych argumentów.

### 2026-10-13 — kontrolowany selektor z cechami zgodności
Uruchomiono100 kroków kontroli278 cech kontra282 cechy. Dodano4 cechy wyłącznie z przewidywań ekspertów:duplikacja starego/nowego,niezgodność operatorów/argumentów. Nie ma reguły zakazującej tego samego argumentu. Kolumny nowych cech początkowozerowe, decyzjeźródła zachowane. Wagigate100przeniesione, noweAdamWw OBUramionach z powodu zmianykształtu. Identyczny zapisany harmonogram100batchy,54 treningoweexclusive-correct(11old/43new). Eksperci,pamięć,logika zamrożone. Każdykrok atomowoz optimizer/RNG/nextindex/expertSHA. Wymagana walidacja retencji i prawidłowych poleceń o dwóch identycznych argumentach. Żadnego testgoldw nauce.

### 2026-10-13 — prawidłowe powtórzone argumenty
Niezależnie nowe pełne nazwy wykluczone z zapisanych treningowych/testowych manifestów:120 poprawnych poleceń z dwoma identycznymi argumentami,AND/OR/XOR/IMPLIES/EQUIV po24. Lexical1950,controlgate100 i consistencygate100 osiągnęły120/120 interpretacji i odpowiedzi. Nie utrwalono w tym zakresie deterministycznego zakazu powtórzeń. Nie dowodzi to poprawności wszystkich form. Trwa osobny test retencji obu selektorów na starej ujawnionej1890 fixture;bez nowych treningów i aktywacji.

### 2026-10-13 — zamknięcie selektorów, ochrona udanych cech słów
Control i consistencygate mają identycznie1659/1890 odpowiedzi,lost4gain73semanticlost3gain113 wobecoryginału;naprawiły1/5strat,zachowały73/79zysków. Gorsze od samegolexical1950(1664). Seria gatezamknięta,niewdrożona.
Uruchomiono50 kroków control/adapt_context odlexical1950. Udane8240 cechy słów zamrożone w OBU,wraz z pamięciąilogiką. Głowyuwaga.0002obie;eksperymentdodajeuczeniekontekstu1e-5nową4grupą. Pełne3 wcześniejszegrupyoptzachowane,zamrożonagrupalexicalpomijana przy update. Nauczycielcorrect-maskzmieniony naźródłolexical1950w OBUarmach,chroniącaktualnezachowanie. Każdykrok zapisany,finiteibazy/lexicalbitwiseassert. Nowa hipoteza,niesukces.

Adaptacja kontekstu zatrzymała się przed pierwszymupdate:4grupy zbudowane przedloadźródłowych3 grup. Kontrolaukończona2000,nietknięta. Poprawiono kolejność:load3źródłowychgrup→dodanie4grupykontekstuLR1e-5. Uruchomiono wyłącznieadapt_context,bez powtarzaniakontroli. Brakutraconychadaptupdate. Dodanometa lexical_frozenTRUE. Połączenie pamięci/lexicalz bazą pozostaje chronione;potrzebnatestretencji.

Kontrola i adaptacja kontekstu na zamrożonych udanych cechach ukończone2000. Potwierdzono50 identycznych batchy i bitową niezmienność8240 cech wewszystkich krokach obu ramion. Monitoridentyczny:known165/dev144/compound168,różnedługości369/378inne378. Brak jeszcze korzyści wmonitorze. Uruchomiono małą630 walidacjęsource1950/control2000/adapt2000. Zero nowych treningów wtrakcie. Po negatywnym wyniku seria ma zostać zamknięta,nie przedłużana ślepo.

### 2026-10-13 — zamknięcie kontekstu i pomiar siły cech
Mały630 test zamrożonychcech:source599 odpowiedzi555interpretacje,control598lost1gain0semanticlost3gain1,adapt599lost1gain1semanticlost4gain3. Brakprzewagi;seria zamknięta.
Odczytowy pomiar WYŁĄCZNIE danychtreningowych:alpha0 exact342 loss.390,0.5 exact354loss.308,1 exact361loss.260,2 exact366loss.223,4 exact349loss.325. Wagi plików niezmienione. Uruchomiono30 kroków nauki tylko1nowego skalarasiły cech przed GRU,wszystkie dotychczasoweparametry zamrożone. Nie wybieranoalphy ztestu. Każdykrok zapisany;konieczna nowawalidacja. Niesukcesdopókibrakpomiaru.

### 2026-10-13 — plateau korekt i diagnoza pewności
Kalibracja1parametru skończona30 kroków,skala1.7359. Małytestsource578/630 i519parse,scale581/528,lost9gain12semanticlost9gain18. Sameargs119→118/120. Niewdrożone,seria zamknięta. ROconfidence1890:1481poprawnychparse/409błędnych,meanjoint.932/.649,ponad.9poprawne1222/błędne13. Softmaxniegwarantujepoprawności;nie wybierano progudo inference. Dalszy kierunek to kontrolowana ocena jakości z treningowych etykiet,bez zmieniania chronionej wiedzy. Skrócono stanmonitorado TSI_STAN_NADZORU.md dla oszczędzania limitu.


### 13 października — ocena wiarygodności zamrożonego parsera
100 aktualizacji na ramię, tylko114/2290 parametrów oceny; parser/memory/logic zamrożone. TRAIN64 błędnych/3282 poprawnych; progi wyłącznie walidacja treningowa. Nowy test2010 (1890 pięć rodzin/3formy+120 poprawnych powtórzeń), pełne nazwy wykluczone z seen/frozen. {"confidence": {"n": 2010, "parse_correct": 1955, "accepted": 1993, "accepted_correct": 1943, "false_acceptance": 50, "correct_rejected": 12, "precision": 0.9749121926743602, "coverage": 0.9915422885572139}, "context": {"n": 2010, "parse_correct": 1955, "accepted": 1968, "accepted_correct": 1921, "false_acceptance": 47, "correct_rejected": 34, "precision": 0.9761178861788617, "coverage": 0.9791044776119403}}. Wynik nie spełnia celu99% precision; brak wdrożenia, brak zmiany odpowiedzi, odrzucenie nie jest stanem logicznym nieznane. Nie dobierano progu z testu.


### 13 października — reprezentatywność błędów oceny jakości
Audyt read-only: stary pool jakości77 błędów/4264, trudny ujawniony test409/1890, inny udział błędów operatora/argumentów i obu. Nowy treningowy pool1008 różnych kontekstów daje490 poprawnych/518 błędnych interpretacji; operator-only129,arg-only245,both144. Nazwy zablokowane względem seen/frozen. Zapisane dane i cechy zamrożonego parsera, bez nauki lub wdrożenia. Źródła testowe służyły tylko diagnozie, nie etykietom treningowym.


### 13 października — kontrolowane rozszerzenie treningu oceny jakości
Obie próby100updates zachowały sourcejudge100/optimizer/RNG,2290param, frozenparser. Wspólna wholeframe TRAINvalidation:control brak progu99%/100akceptacji;expanded próg.5128069 coverage78%,8błędnych zaakceptowanych. Nowy test2010seed482719365: {"source": {"n": 2010, "parse_correct": 1890, "accepted": 2008, "accepted_correct": 1889, "false_acceptance": 119, "correct_rejected": 1, "precision": 0.9407370517928287, "coverage": 0.9990049751243781}, "control": {"n": 2010, "parse_correct": 1890, "accepted": 0, "accepted_correct": 0, "false_acceptance": 0, "correct_rejected": 1890, "precision": null, "coverage": 0.0}, "expanded": {"n": 2010, "parse_correct": 1890, "accepted": 1794, "accepted_correct": 1779, "false_acceptance": 15, "correct_rejected": 111, "precision": 0.9916387959866221, "coverage": 0.8925373134328358}}. Odrzucenie nie oznacza poprawnej odpowiedzi; nie wdrożono, nie wybierano progu ztestu.


### 13 października — ograniczenie generalizacji oceny jakości
Read-onlyretencja na starym trudnym1890fixture, progi wyłącznie TRAINval niezmienione. {"source": {"all": {"n": 1890, "parse_correct": 1481, "accepted": 1887, "accepted_correct": 1479, "false_acceptance": 408, "correct_rejected": 2, "precision": 0.7837837837837838, "coverage": 0.9984126984126984}, "known_form": {"n": 630, "parse_correct": 629, "accepted": 628, "accepted_correct": 627, "false_acceptance": 1, "correct_rejected": 2, "precision": 0.9984076433121019, "coverage": 0.9968253968253968}, "distractor_seen": {"n": 630, "parse_correct": 629, "accepted": 630, "accepted_correct": 629, "false_acceptance": 1, "correct_rejected": 0, "precision": 0.9984126984126984, "coverage": 1.0}, "unseen_distractor": {"n": 630, "parse_correct": 223, "accepted": 629, "accepted_correct": 223, "false_acceptance": 406, "correct_rejected": 0, "precision": 0.35453100158982515, "coverage": 0.9984126984126984}}, "expanded": {"all": {"n": 1890, "parse_correct": 1481, "accepted": 1511, "accepted_correct": 1335, "false_acceptance": 176, "correct_rejected": 146, "precision": 0.8835208471211119, "coverage": 0.7994708994708994}, "known_form": {"n": 630, "parse_correct": 629, "accepted": 629, "accepted_correct": 628, "false_acceptance": 1, "correct_rejected": 1, "precision": 0.9984101748807631, "coverage": 0.9984126984126984}, "distractor_seen": {"n": 630, "parse_correct": 629, "accepted": 627, "accepted_correct": 626, "false_acceptance": 1, "correct_rejected": 3, "precision": 0.9984051036682615, "coverage": 0.9952380952380953}, "unseen_distractor": {"n": 630, "parse_correct": 223, "accepted": 255, "accepted_correct": 81, "false_acceptance": 174, "correct_rejected": 142, "precision": 0.3176470588235294, "coverage": 0.40476190476190477}}}. Wynik99.16% na nowej ramie nie przenosi się na wcześniejszą trudną ramę. Nie wdrożono, źródła niezmienione; nie powtarzać epok/progów bez nowej diagnozy języka.


### 13 października — pokrycie słów i oddziaływanie dopisku
Audit25000distinctsavedTRAINrows (allfrozenpools+actualbalanced1900/lexical1950,niecałalineage). Cztery słowa trudnej ramy nieobecne:zgodnie,podanymi,informacjami,obliczeniu. Read-onlyexposed630:exact223baseline;zamiana samego obliczeniu na ocenie389,lost5gain171;informacjami na danymi255;wszystkiecztery188. Kontekst ma istotne znaczenie, nie dowód samej nowości słów. Żadnej podmiany inference/treningu testowych przykładów, bez modyfikacji wag.


### 13 października — nowe treningowe kontrasty dopisków
840TRAINcases,168identycznychbody/namepairs×5dopisków. {"plain": {"n": 168, "operator": 168, "arguments": 168, "exact": 168, "lost_vs_plain": 0, "gained_vs_plain": 0, "operator_changed": 0, "arguments_changed": 0}, "neutral": {"n": 168, "operator": 139, "arguments": 138, "exact": 131, "lost_vs_plain": 37, "gained_vs_plain": 0, "operator_changed": 29, "arguments_changed": 30}, "calculation": {"n": 168, "operator": 105, "arguments": 98, "exact": 83, "lost_vs_plain": 85, "gained_vs_plain": 0, "operator_changed": 63, "arguments_changed": 70}, "checking": {"n": 168, "operator": 80, "arguments": 8, "exact": 6, "lost_vs_plain": 162, "gained_vs_plain": 0, "operator_changed": 88, "arguments_changed": 160}, "evaluation": {"n": 168, "operator": 137, "arguments": 36, "exact": 36, "lost_vs_plain": 132, "gained_vs_plain": 0, "operator_changed": 31, "arguments_changed": 132}}. Największe straty argumentów checking/evaluation, nie izolowany operator/calculationcue. Żadnego treningu wag ani podmian inference, źródłowyparser1950 niezmieniony; dane i manifest saved.


### 13 października — kontrastowe dopiski50updates: pozytywny mały test
Source462/630answers294parse,plaincontrol474/313lost6gain18semanticlost3gain22;contrast605/569lost1gain144semanticlost0gain275. Każdeznane126answers125parse retained. COPYcandidate2000savednieaktywny. Replay/pairids/rowbudgetmatched,differentdataintended,sourceopt3RNGpreserved,base/contextbitwiseTRUE. Potrzebnybroadfivefamily iretencja,niegotowość.


### 13 października — kontrast dopisków szerszy test
1890freshnamesfivefamilies2newfooters+known:source1691answers1502parse/control1710/1534/contrast1784/1668. CandidatevsSource lost7gain100semanticlost9gain175,known630→629. Newcheckingparse616→626,newcalculation256→413. Stronggainbutnotnonregressive,notactivated. Oldfixture retention nowrun vslex1950notoriginal1900. Testerrorrowsdiagnosticnevertargettraining.

Stara1890retencja vsLEX1950: {"answers": 1644, "parse": 1436, "lost": 40, "gain": 20, "semanticlost": 67, "semanticgain": 22}. Nowedopiskizyskaleoldregression,niewdrożone. Każdystanzachowany.


### 13 października — retencja działa na treningu, nie gwarantuje transferu
Readonly1470TRAIN rows (9actualreplaybatches630+paired840):OLDreplay629/630exact identicalsource/control/contrast0lost. Newcontrasttrainplain168/neutral166/calculation168/checking167/evaluation167of168. Silnyfit iochronareplayniezapobiegłyoldTESTlost67semantic. Nie dowodziwiedzymemoryforgetting; potrzeba szerszych nowych TRAINkompozycji/sourcecorrectretention,nieblindKL/replayquantity. Brakzmianwag/aktywacji.


### 13 października — nowe treningowe kompozycje retencji
NEWTRAIN1008 przypadków6wstępów6dopisków7ops4pary,fullnamesblocked. Source858exact/candidate871,source-only37 w31ramach,candidate-only50,bothwrong100. Zapisanypool+manifest,żadnego testgoldtraining/weightupdate. To mierzalny TRAINwzorzecstratpozasameoldreplay;niegateoracleclaim/readiness.


### 13 października — rozszerzone replay: wholeframeTRAINvalidation
50updates2arms source2000weights/FULLopt3RNG,35samefooterpractice+35replaydifferentcoverage;source1950-correctnewcontextsheldwholeframesexcluded. Held200 source181/candidate2000180/control2050185/expanded195lost0gain14vs1950. All840footerTRAINcorrectboth2050. Memory/contextbitwiseTRUE. Matchedfooterbudget/splitverified. Newsmallfivefamily630screeningrunning,noactivation.


### 13 października — replay kompozycji: nowy mały test
630fivefamilies3selectedstatepairs/known/newcomposition/newfooter:1950550answers513parse,2000603/590,control2050605/595,expanded2050617/611lost1gain68semanticlost0gain98vs1950. Newcomposition186→200answers172→196parse;newfooter154→207answers132→206parse. COPYcandidate2050preservednonmain,sourceallkeep. Oldretentionrunning,noactivation.


### 13 października — szersze replay przywraca większość retencji
Oldexposed1890 vsLEX1950(1664answers1481parse):control20501654/1474lost33gain23semanticlost33gain26;expanded20501732/1584lost13gain81semanticlost8gain111. Previouscandidate20001644semanticlost67. Expandedrecoverolderformsbutnotnonregressive,NODEPLOY. New1890all9statesforms validationrunning.


### 13 października — replay2050: szeroka walidacja i argumenty
NEW1890all9states source1614answers1356parse/expanded1780/1639lost17gain183semanticlost0gain283. OLD8semanticlossALLopcorrect:2ANDcontextwordpodaj,1XOR+5IMPLIESdupname. Other9unionanswerlossessourcechancecorrect. Readonlydiagnosis,noactualtestnames/rowstrain,nohardcodedduprejection;noactivation.


### 13 października — błędy wyboru argumentów w treningu
Readonly1008compositionTRAIN+120sameargTRAIN:source1950exact858→2050979,argswrong109→26,dup12→6,contextarg72→14. ALLsourcecorrectTRAINpreserved0lost. Validsamearg118→119/120. Poprawa na treningu nie dowodzi naprawy 8 regresji argumentów w innych formach testowych. Nie używać testowych nazw ani przykładów w treningu. Wagi niezmienione, bez aktywacji.


### 13 października — niezależne poprawne powtórzenia argumentów
NEW360testcases8charfullnamesblocked:sourceknown119/120parseanswers,newfooter70parse97answers,newneutral1parse67answers;2050known119same,newfooter119/119,newneutral89/104. No deterministicduplicatereject,validsameargsallowed. WordargsLinear128→2 independentsoftmaxscoresconfirmed,notcauseproof. Weightsunchanged,noreadiness/activation.


### 13 października — rozkłady argumentów i zachowujący funkcję odczyt
TRAINwrongdup6 overlap.626 vsdistinctcorrect710 .011;truepairtop3all6,validsameargsselecttwooccurrenceslowoverlap. READONLYranksnotinferencegold. PreparedWordJointPointer6306 learnedresidualparams391→16→2 fromcontext+softpointerpools+opprobs. Zeroinitialpreserves402mixedTRAINlogitsmaxdiff0,finitegrad.582. Source2050unchanged,initialcpseparate;notlearningproof/systemfactorynotyetimplemented. No duplicateconstraints/wordsolver,baseandlogicfrozen.


### 13 października — wspólny odczyt50: monitor bez przewagi
Source2050heldTRAIN195/200,control50/joint50both196lost0gain1,all840footerTRAINcorrect/samearg119/120unchanged. BOTHfreshAdamWargumentonly/control258joint6564params,SAME50x70schedule,frozenotherweightsTRUE. Branchzerotransferpreservedinitialnottrainingproof. Fresh630screeningrunning,notactivated.


### 13 października — wspólny odczyt bez wykazanej korzyści
NEW630source2050/control50/joint50identical612answers600parse,alllostgained0. Branch50controllednoobservedgainclosed;allweightsopt/RNGpreserved. Source2050andbaseSHAunchangedverified. Best2050notactiveold8semanticregressionsremain. LocalverifiedREADMEupdated,historyseparate,no codepush.


### 13 października — rodziny nazw w nowych kompozycjach
NEWTRAIN840fivefamilies/plain+2authoredcontextforms:1950exact704/2050838;short167,long168,numbered167,Polish168,difflength168each168. Sourceonlycorrect0,gain134,bothwrong2. Familycoveragealonefailsreproducingold8inthisset,notglobalproof. No training/weightchanges,savedcorpusmanifest,no nearperfectdatasetepochs.


### 13 października — słownictwo i interakcja kontekstu
NEW588TRAINmatched84pairs7variants:2050exact84/78/61/69/71/84/48;195084/80/31/76/63/84/16. Sourceonly14,newonly75,bothwrong79. Novelbothcontextarg26/dup6,knownfootercontext8/dup6. Knownbothperfect meanscontextinteractionnotnoveltyonly. TRAINreproducesfailurewithoutactualTESTrows/names,no weightsupdated.


### 13 października — różnorodność kontekstu: walidacja kombinacji
50updatesBOTHsource2050FULLopt3RNG,common35expandedreplay+35differentcontext,50x70budget. Held336 source292/control322lost1gain31/diverse336lost0gain44. All840oldfooterTRAINcorrect/sameargs119unchanged. Allheldcells excludedverified,basedataTRAINnotfinalheldout. Base/contextbitwiseTRUE;new630screeningrunning,noactivation.


### 13 października — różnorodność słownictwa: mały test
630freshfivefamilies3statepairs SOURCE2050598answers582parse/control2100617/604/diverse2100628/624. Diversevs2050lost1gain31semanticlost2gain44,known209parse→208regression. Newcomposition163→206parse,footer210retained. Oldretentionvs2050running,COPYsavednonmain,noactivation.


### 13 października — retencja słownictwa2100: oba warianty poprawiają stary test
Old1890control1802answers1703parse,diverse1815/1709. Vs2050controlsemanticlost0gain119/diverse2gain127;vs1950control2gain224/diverse3gain231. Overallstrongbutnotnonregressivevsold1950;controlpreserves2050better. Newall9statesvalidationrunning,noautomaticselection/activation.


### 13 października — słownictwo2100: szeroki test i regresje
NEW1890source20501876answers1864parse/control21001865/1838/diverse21001881/1873. Diversevs2050lost1gain6semanticlost2gain11;controlsemanticlost34gain8. TwoNEWdiversegenuinelossknownXORduplicate2ndarg;OLDvs1950diverse3genuineloss. Readonlytestdiagnosisnoactualtestnames/rowstrain,noactivation. Bothsourcecandidatearchivespreserved.


### 13 października — rzadkie błędy binarne na nowych nazwach treningowych
NEW2000TRAIN100pairs/fivefamilies/XOR/IMPLIES/distinct+same:19501980exact/20501982/21001982. 2100lost6gain8vs1950/lost3vs2050. Freshnamesblockedseen/tests,rareknownbodyfailurelegitimatelyreproducedwithoutactualtesterrors. Savedrows/masks/manifest,nolearning/activation.


### 13 października — odczyt i cechy znakowe: wyłączone nazwy
HeldNAMEPAIR400source2100398/control399/features400withoutlost. Formerfooter840source/controlcorrectfeatures839oneoperatorloss;validsamearg119/120all. Weightfreezeverifieddoesnotfreezeoperatorfunctioniflexicalfeaturesmove. ControlledSAME50x70freshAdamWBOTH,rareTRAINoversampling7. NEW750screeningrunning,noactivation.


### 13 października — wybór według ograniczenia szkody
Userauthorizedmaximizegainundercontrolledleastdamage. selection_policy.json/constrained_selection.py explicitgainconstraints/Pareto;conservativeepsilon0untilnumericbudgetdefined,known/sameargsemanticprotected/memorylogicfreezehard. NEW750 source2100745answers739parse/control748/743lost0semanticlost0gain3/4/features742/735lost8semanticlost10. SelectedcontrolNEXTvalidationNOTactivation,featuresclosed. OldretentionvsSOURCE2100running.


### 13 października — kontrola argumentów a jawny koszt szkody
OLD1890source21001815answers1709parse/control1816/1714lost1gain2semanticlost0gain5. LostonesourcesemanticFALSE(chancecorrectanswer),reportstillexplicit. Strictinitialepsilon0 policy rejects weightedharm1, no automaticrelaxation/deployment. READONLYonecase saved actualtestnames nevertrain. Userleastharmdirectionretained,needclassifycostprioritizationnotonlysum.


### 13 października — przerwa na polecenie użytkownika i dokumentacja
Użytkownik polecił wstrzymać naukę z powodu limitu i uaktualnić/wypchnąć README. Nadzór czasowo PAUSED, gotowość nieosiągnięta; bez automatycznego wznowienia. Ostatnia rozpoczęta diagnoza read-only zakończyła się przed zapisem: 5 zysków poprawnego rozumienia, pojedyncza strata odpowiedzi przy błędnym operatorze obu wariantów. Wszystkie stany zachowano. README ma jeden aktualny opis kandydatów, miar szkody i ograniczeń; historia osobno. Push wyłącznie README i historia, kod/wagi/dane lokalnie.


### 13 października — wznowienie na polecenie użytkownika
Użytkownik „możesz ruszać!” odwołał pauzę. NadzórACTIVE, źródła zachowane; bez powtarzania zakończonej nauki. Rozpoczęto NEW2010all9statepairs/fivefamilies+validsameargreadonlycomparisonSOURCE2100/controlargs50. Kontrola wybierana z jawną polityką szkody, oldonechancecorrectanswerloss nadal raportowany i nie spełnia zerowego budżetu. Noactivation, codeweightslocal.


### 13 października — wznowiony niezależny test kontroli argumentów
NEW2010source21002005answers1993parse/control2006/1995lost0gain1semanticlost0gain2. Jawna polityka szkodyepsilon0 spełniona w tej próbce;oldonechancecorrectanswerlossstillfailsbudget,noactivation. COPYword_argument_control_50savednonmain. Read-onlyremaining15errorsALLoperatorwrong(7oponly8opargs),4wronganswers,no core-onlyerror;needsTRAINoperatorcoverage notmemoryunfreeze/testrowstraining.


### 13 października — nowe treningowe pary dla operatorów
1680NEWTRAINsamefullnamesacross7ops/fivefamilies/fourforms:1619opcorrect1617parse. XOR→EQUIV27,AND→EQUIV16,OR→EQUIV9,EQUIV→XOR7,AND→READ1/IMPLIES1. GeneratorgoldTRAINonly/seenfrozenblocked,rowsandmanifest saved,no weightslearning. Remainingopfailuremodelegitimatelyreproduced;selectedargumentfixfeaturesfrozenneededtoavoidnameaddressregression.


### 13 października — naprawa odczytu operatora50updates
Same50x70TRAINbatches sourceargcontrolweights/RNGmatched,freshAdamWBOTH. Controlnativeop903 versusop+existingattention1935learned,allcontext/lexical/arguments/MEMORYLOGICfrozenbitwiseTRUEeachupdate. NAMEPAIRfloor20%12pairs/family actual2/family =>280heldcases16.7%;all7ops4formsstaysplit. OpCE+correctsourceTRAINKL.2unchanged,nogoldTEST. Heldvalidationrunning,noactivation.


### 13 października — wybranie naprawy operatora z ograniczeniem szkody
Held280source270/control277lost0gain7/attention278lost1gain9. Oldfooter840correct/samearg119unchangedALL. Constrainedpolicyepsilon0choosecontrolNEXTtest,attentionnoteligibledespitesumgreater/noextraepochs. Samebudget/frozenguardsverified. New750freshnamesformsrunning,nogoldTESTlearning/noactivation.


### 13 października — naprawa odczytu operatora: świeży mały test
NEW750fivefamilies3statepairs+120validsamearg sourceargcontrol747answers747parse/nativeopcontrol748/748lost0gain1semanticlost0gain1. Constraineddamageepsilon0acceptednextvalidationonly. COPYoperatorsourcebestnonmain,old1890retentionrunningvsargcontrol1816/1714. No TESTtraining/noactivation.


### 13 października — odczyt operatora zachowuje bieżącą retencję
OLD1890candidate1830answers1736parse versusargcontrol1816/1714lost0gain14semanticlost0gain22. Constrainedepsilon0feasible. Older1950/2050/2100comparison savedseparatelynotignored. NEW2010independentbroadrunning,noactivation/corefreeze.


### 13 października — wybrany odczyt operatora: nowy szeroki test
NEW2010sourceargcontrol1992answers1980parse/nativeopcontrol1994/1982lost0gain2semanticlost0gain2,epsilon0acceptednextvalidation. Remaining28semanticerrors26args-only2op+args16wronganswers;differentfreshframesnotproofargsregression(unchangedfunction). Old1830answers1736parse,oldsemanticretentionall1950/2050/2100zero lossesbutchance-answerlossesreported. Noactivation;actualtestrowsnevertrain,needsnewTRAINcontextfailurebeforemorelearning.


### 13 października — oddzielne komponenty kontra połączenie
Initial1344TRAINdoubleimperativeframesnotcleanenough,NOTchosenfortraining. Corrected1344TRAINcontextclauses+originalcompleteimperativeinclperiod:plain83/84,30bothwrongwhileeachcomponentcorrect. Savedcleancorpusmanifest,no weightslearning/testrows. Justifiescontrolledexposurecomparison(prefix+footerseparate versusboth+plain)equalwordcounts,notcapacityclaim.


### 13 października — odseparowane komponenty wystarczają w walidacji treningowej
Matchedexactwordexposure50x70bothsourceopcontrol/freshAdamWBOTHnewfulltrainablelist. Held252source220/separate251/joint251bothlost0gain31;formercomponents/footer/sameargsno losses. Jointcooccurrencenoextraobservedbenefit,notglobalproof. Newgrammatical750freshnamestransferrunning/noactivation. Metadatalegacytextsourceincorrect2050 boundactualoperatorcontrolSHAinrun_manifest;checkpointskeptunchanged.


### 13 października — koszt pojedynczej regresji
NEW750source735answers716parse/separate745/737semanticlost2gain23/joint747/744semanticlost1gain29. BOTHepsilon0ineligible. OnejointXOR→ANDlossanswercoincidesunderoriginalfacts,butREADONLY9states source9/9candidate4/9. Potential5/9futureharm,no TESTnames/rowstrain/no goldinference. Closevariant/bestopsourcepreserved/noactivation.


### 13 października — konflikt gradientu nie jest konieczny
READONLYTRAINclean1344+footer840:89opwrong/2095protectedcorrect;nativeopgradients cosine+0.3487. Virtualsteps restoredsource,protectedargmaxloss0all,wrongrepaired0/1/5,protectedCEdecreases. NotTEST/LRselection/readiness. Majoritycomponenterrorsoperator(69vs30arg both). Supportsboundednativeop-only guardedupdatecomparison ratherblindarg/fullfeaturetraining;no persistedweightsupdated.


### 13 października — ograniczenie szkody w przyjmowaniu aktualizacji
25matchednativeop-onlySGDupdates/CE+correctteacherKL.2. PlainprotectedTRAINlost1/guarded0,guardlastupdate rejectedafter7backtracks. Actualprotected1807/TRAIN1890/held294:224cleanheld+70extraexcludedpriorreplay duepairidnamespaceoverlap conservativeBOTH,actualmaskrecordednotexpectedcounts;notdata leakage. Frozenallnonopweightsverifiedall50checkpoints,sourceunchanged. FullNNheldvalidation done;noactivation/guaranteeTESTpreservation.


### 13 października 2026 — ochrona aktualizacji nie przeniosła się na świeży test
Na 750 nowych przypadkach source uzyskał 716 odpowiedzi i 709 dokładnych interpretacji, guarded25 714 i 706. Utracono 3 odpowiedzi i 4 poprawne rozumienia, zyskano po 1; dwie straty dotyczyły chronionych grup. Polityka wyboru odrzuciła kandydata (koszt7, budżet0). Pomimo zerowych regresji na chronionym zbiorze treningowym ochrona nie zapewniła generalizacji. Eksperyment zamknięty; source, pamięć, logika i wszystkie stany zachowane, bez aktywacji. Raporty TSI_OPERATORY_GUARD_MALY_TEST.json, TSI_OPERATORY_GUARD_MALY_WYBOR.json i TSI_OPERATORY_GUARD_GENERALIZACJA_DIAGNOZA.json.


### 13 października — diagnoza wpływu kontekstu po zamknięciu guard
Readonly750:41 błędów interpretacji źródła obejmuje15 błędów samego operatora,2 samych argumentów i24 obu. Diagnostyczne odtworzenie znanego korpusu bez otaczającego tekstu naprawiło40, ale zepsuło1 poprawny przypadek z powtórzonym argumentem. Wynik nie jest poprawą rzeczywistego inference: korpus odtworzono z gold tylko do diagnozy. Nie wprowadzono usuwania dopisków ani reguł słownikowych, nie zmieniono wag. Raport TSI_OPERATORY_RAMY_TRYBY_DIAGNOZA.json.


### 13 października — reprezentacja korpusu na danych treningowych
Readonly sourceoperatorcontrol50,1344 zapisanychTRAINwierszy. W1260 wariantach z kontekstem1154 dokładnych interpretacji i106 błędnych. Cosine stanów korpusu względemplain .846/.790 dla poprawnych/błędnych; masa uwagi korpusu .388/.280. Nie jest to dowód przyczynowy. Kod uwagi wpływa tylko na operator, argumenty czytają pełne stany kontekstu. Wagi niezmienione, bez wdrożenia. Raport TSI_KONTEKST_REPREZENTACJA_TRENING.json.


### 13 października — liniowa próba rozpoznawania korpusu
Diagnostyczny Linear128→1 na zamrożonych stanach sourceoperatorcontrol50,30 kroków; każdy stan/optimizer/RNG zapisany, parser/core bitowo niezmienione. Dokładne granice:TRAIN213/910,held-namepairs48/224,held-combos53/210. Tokenaccuracy87–89% nie oznacza bezpiecznego wycinania polecenia. Moduł niewłączony do inference, nie traktowany jako naprawa ani finalheldout. Raport TSI_KORPUS_LINIOWY_PROBE.json.


### 13 października — typy błędów granic
Readonlyprobe30:heldnames pomija3/384 tokenów nazw,125/736 innych słów korpusu i przyjmuje282/2072 kontekstu;heldcombos0/360,100/690,306/2590. Predykcyjny dekoder spójnego fragmentu poprawia exact48→54/224 i53→58/210, nadal za słaby do użycia. Bez zmiany wag lub inference. Raport TSI_KORPUS_GRANICE_TRYBY.json.


### 13 października — koszt interpretacji przewidywanego fragmentu
Readonlyfrozenprobe30→maxsumspan→frozenparser naTRAINcache. Heldnames215→217/224, lost7gain9;heldcombos180→195/210,lost9gain24;TRAIN842→807/910,lost77gain42. Wybór korzystał tylko z logitów, gold wyłącznie metryki. Występują realne regresje interpretacji; metoda niewdrożona i zamknięta jako kandydat inference. Wagi source/core niezmienione. Raport TSI_KORPUS_FRAGMENT_INTERPRETACJA_TRENING.json.


### 13 października — domknięcie diagnozy fragmentu
93 utraty exact naTRAIN:13 sameoperator,40 sameargs,40 oba. Metoda zamknięta bez wdrożenia. LokalnyREADME zaktualizowano o wznowienie, operatorcontrol50 oraz negatywne wyniki ochrony i fragmentów. Dokumentacji w tym kroku nie wypchnięto.
