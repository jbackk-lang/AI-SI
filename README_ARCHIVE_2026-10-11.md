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
