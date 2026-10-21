> Kopia historyczna sprzed uporządkowania dokumentacji 21 października 2026. Opisy i wyniki odnoszą się do ówczesnego stanu.

# Historia TSI

## 18.10.2026 — przejęcie roli lokalnego AI-SI

Wybrano adaptację potrzebnych modułów do TSI zamiast nakładania nowego rdzenia na dawny koordynator. Zachowano cały poprzedni zestaw w archiwum. Nowy program otrzymał wspólny rdzeń H512, matryce słownika, narzędzia matematyczne, czytnik dokumentów, lokalne pliki, źródła, daty, pamięć i historię. Przeniesiono 2315 faktów i 2 wpisy źródłowe, zachowując oryginalne oznaczenia. Dawne modele językowe i automaty treningowe nie należą do aktywnego toru. Weryfikacja: 28 testów oraz oddzielna kontrola interfejsu w przeglądarce. Oryginalna pełna historia pozostaje w archiwum.
## 18.10.2026 — porównanie ze starymi testami AI-SI

Wyrywkowa ocena wykazała brak pełnej zgodności funkcjonalnej po migracji. Na 43 próby (obejmujące także ten sam przykład przed i po ręcznym wyborze działu): 18 zgodnych z dawnym oczekiwaniem, w tym 10 prawidłowych zatrzymań; 23 przypadki bez obsługi; 2 różnice dawnych zasad zakresu. Proste wyrażenia: 4/4. Dawne polecenia kalkulatora w zwykłej rozmowie: 0/12. Wybrane wyrażenia po wskazaniu obliczeń: 4/8. Nie przeszły dwa dawne polskie polecenia rachunkowe, trzy zadania dwustopniowe, relacja grafowa i polecenie programistyczne. Poprawne odmowy nie oznaczają rozumienia dodatnich wariantów tych poleceń.

Oryginalne testy plików i źródeł, uruchomione z modułami nowego TSI: 9 przeszło, 1 pominięto z powodu braku możliwości utworzenia dowiązania symbolicznego. Dwa dawne zestawy dokumentów/dat nie miały zachowanych plików wejściowych i nie zostały zaliczone. Ocena nie zmieniała kodu, wag ani progów; użyto odrębnej pamięci próbnej. Archiwalne testy pozostały niezmienione.

Do dalszej adaptacji: odczyt dawnych poleceń naukowych i działań wieloetapowych, aliasy funkcji, brakujące narzędzia oraz dawne relacje i programowanie. Pełny zapis: raport próbki.


## 18.10.2026 — przywrócenie i nauka umiejętności

Przywrócono dawne operacje naukowe, polecenia arytmetyczne PL/EN, plany dwuetapowe, katalog kodu i relacje. Dwa osobne przebiegi treningowe po 500 kroków dały dodatkowy moduł 263 508 parametrów; aktywny wariant ma 901 przykładów treningowych i 82/84 poprawnych klasyfikacji na odłożonej ocenie. Kontroler znaczenia wymaga zgodności operacji i ról przed wykonaniem. Znana regresja: 18/43 → 42/43, braków obsługi 23 → 0. Weryfikacja aplikacji: 62 testy, dodatkowo dawne narzędzia 9 testów i 1 pominięty. Wagi H512, archiwum i dane użytkownika zachowano. Szczegóły i ograniczenia opisuje TSI/docs/RESTORED_SKILLS_2026-10-18.md.


## 2026-10-18 — ogólna warstwa rozmowy

Dodano kontekst intencji i treści, dopytywanie, operacje na tekstach i listach zadań, poprawki, cofanie, reset aktywnego tematu i pytania z cytatem do podanej treści. Próby obejmowały dziedziny pozamatematyczne. W przeglądzie odpowiedzi naprawiono niewidoczną zmianę źródła streszczenia, podwójne powitania, powtórzenia w odczycie notatki i mylenie pytania ogólnego z dawnym kontekstem logicznym. Pełna regresja 86/86, po ostatniej zmianie komunikatów 27/27 ukierunkowanych. 31 wypowiedzi zachowano w dokumentacji. Wagi niezmienione; bez treningu ogólnego generatora. Szczegóły.


## 2026-10-18 — pomoc i pierwszy własny generator języka

Oddzielono dokumentację obsługi od odpowiedzi: wspólny katalog 17 przykładów w panelu i poleceniu pomoc. Wytrenowano od zera własny Transformer 1,8 mln parametrów, bez zewnętrznych wag i prywatnych rozmów. Jakość 0/6 nowych poleceń; kandydat odrzucony, H512 pozostaje aktywny. Zachowano kod, źródła, stan optymalizatora, pełne odpowiedzi i ograniczenia eksperymentu. Zabezpieczono kolejne próby osobnymi katalogami. Raport.


## 2026-10-18 — matryce odmiany, reguł i kontroli znaczenia

Podłączono Morfeusz/SGJP z pełnymi analizami fleksyjnymi zamiast ręcznych końcówek imion. Dodano macierze cech, siedem przypadków, rekcję, uzgodnienia i jawne operacje na macierzach reguł. Zintegrowano je z kontrolerem zdania, słownikiem, dokumentami i pamięcią; zachowano dawny obsługiwany zakres. Dodano kontrolę zgodności ról, określeń, liczby, przeczenia, aspektu, warunku i źródła; wybrane kontrole pisania wskazują pozycje. 167/167 testów, 26 przejrzanych wypowiedzi w 10 rozmowach; test przeglądarki i zapasowego środowiska portable. Generator języka i H512 bez zmian. Szczegóły i ograniczenia.


## 18.10.2026 — dalszy trening aktywnego H512

Przeprowadzono dalszy trening wag aktywnego rdzenia H512, a nie osobnego prototypu generatora. Nowy model: `TSI-NATIVE-H512-P2054186-9deec43d`. Liczba parametrów rdzenia pozostaje 2 054 186; uczono 9225 parametrów odczytu działania i argumentów. Kontekst rekurencyjny, operacje wektorowe, pamięć faktów i moduł logiki pozostają identyczne tensor po tensorze. Współpracujące moduły relacji i kompozycji przypięto do nowej tożsamości rdzenia, zachowując ich wagi.

Zakres treningu: pojedyncze polskie polecenia READ, NOT, AND, OR, XOR, IMPLIES i EQUIV, kolejność argumentów oraz różne sformułowania. Nie jest to trening swobodnych opowiadań ani dowód uniwersalnego rozumienia języka. Matryce fleksji i znaczenia nadal współpracują z narzędziami; ich reguł nie zmieniono podczas tego treningu.

## Dane i wybór wag

672 autorskie przykłady treningowe, 140 deweloperskich, 252 odłożone przykłady oceny. Nazwy argumentów i dosłowne sformułowania nie pokrywają się między tymi trzema częściami; są to warianty siedmiu znanych działań, nie nowe dziedziny. Dodatkowe 168 dawnych poleceń PL i 168 EN służyło powtórkom podczas treningu oraz kontroli utrzymania zachowań — te liczby nie są niezależnym testem generalizacji. Nie użyto prywatnej pamięci ani rozmów użytkownika.

Wykonano 600 kroków. Według zestawu deweloperskiego i kontroli utrzymania zachowań wybrano krok 75; późniejsze kroki nie zostały wdrożone. Zbiór końcowy oceniono po wyborze wag i nie używano go do wyboru kroku. Próg przerwania przy dużym pogorszeniu nie został przekroczony. Zapisano dane, skrypt, wybrane wagi, stan optymalizatora i raport; nie zachowano osobnego stanu każdego kroku.

## Wyniki

| Sprawdzenie | Przed | Po |
|---|---:|---:|
| Nowe sformułowania i nazwy, odłożona ocena | 212/252 | 229/252 |
| Zestaw deweloperski | 127/140 | 140/140 |
| Dawne polecenia PL, powtórki | 149/168 | 166/168 |
| Dawne polecenia EN, powtórki | 149/168 | 166/168 |
| Osobna próba 140 poleceń z krótkimi i dłuższymi nazwami | 128/140 | 130/140 |
| Pełne odpowiedzi przy 1260 kombinacjach poleceń i stanów | 1194/1260 | 1200/1260 |

W kontroli utrzymania wcześniej prawidłowo odczytanych poleceń nie wykazano utraty poprawnych odpowiedzi. Pełne odpowiedzi porównywano ze strukturalnym wykonaniem zamierzonego działania przez dotychczasowy moduł logiki — to kontrola odczytu i kierowania, nie niezależny dowód tabel prawdy. Dla 2048 prób wektorowych maksymalna różnica wyniku wyniosła dokładnie zero.

Pełna regresja aplikacji po podmianie: **167/167 testów**. Panel uruchomiono ponownie; identyfikator modelu wskazuje nowe wagi, a stan pamięci użytkownika pozostał zachowany.

## Przejrzane odpowiedzi i pozostałe błędy

Dla A=prawda i B=fałsz:

- „Proszę obliczyć równoważność A oraz B.” → fałsz, EQUIV, argumenty A i B.
- „Proszę obliczyć koniunkcję A oraz B.” → fałsz, AND, argumenty A i B.
- „Teraz podaj A lub B.” → prawda, OR, argumenty A i B.
- „Jaki wynik ma zaprzeczenie A?” → fałsz, NOT, argument A.
- **Pozostały błąd:** „Proszę obliczyć xor A oraz B.” zostało odczytane jako AND i dało fałsz zamiast prawdy. Zapisano go do następnej rundy nauki, bez ukrywania błędu regułą odpowiedzi.

W odłożonym zbiorze pozostały 23 błędy, w tym 14 przy XOR. Wzrost wyniku nie oznacza bezbłędnego rozumienia wszystkich wariantów. Dodatkowa świeża próba 84 poleceń dała 76 poprawnych odczytów; nie była używana do wyboru wag.

## Cofnięcie i ślady

Poprzednie wagi pozostawiono na miejscu. Kopia konfiguracji do cofnięcia: `backups/before-core-language-training-2026-10-18`. Raporty, pełne odpowiedzi i skrypty tej rundy: `training/core-language-2026-10-18`. Te pliki pozostają lokalne; publicznie publikowany jest tylko opis wyników.


# Uczone składanie pełnych odpowiedzi — 18 października 2026

## Wdrożony wynik

Włączono do rozmowy wytrenowany moduł TSI układający pełne zdania z rozpoznanych fragmentów źródła. To działająca część lokalnego asystenta, odrębna od wcześniejszego odrzuconego prototypu generatora opowiadań. W tej rundzie nie zmieniano wag H512 po poprzednim treningu.

Przykład rzeczywistej odpowiedzi:

- Źródło: „Zieloną książkę Oskarowi przekazuje Alicja.”
- Pytanie: „Komu Alicja przekazuje zieloną książkę?”
- Odpowiedź: „Oskar. Alicja przekazuje zieloną książkę Oskarowi.”, następnie oryginalny cytat.

Wykryta zmiana osoby, koloru lub przeczenia w propozycji odpowiedzi pozostaje odrzucana. Gdy całe zdanie źródłowe jest rozpoznane, kontrola znaczenia może dodatkowo zaproponować pełną wersję zgodną ze źródłem. Nie nadpisuje przy tym tekstu użytkownika.

## Co rzeczywiście jest uczone

Moduł ma **8736 parametrów**: kodowanie cech ról, stan rekurencyjny GRUCell i uczony wybór kolejnego fragmentu przez uwagę. Uczy się kolejności fragmentów i zakończenia zdania. Podczas generowania nie korzysta z gotowej tablicy kolejności ról ani zapisanych odpowiedzi. Treść fragmentów pochodzi z tekstu użytkownika; model nie dopisuje słów spoza źródła. To ograniczone generowanie przez układanie fragmentów, nie swobodny model wiedzy lub opowiadań.

Odmianę i role nadal ustalają Morfeusz oraz jawne matryce. Uczony moduł otrzymuje już oznaczone role — wynik jego treningu nie jest wynikiem samodzielnego odczytu surowego tekstu. Zachowuje istniejące formy fleksyjne, zamiast tworzyć nowe odmiany od zera. To rozdzielenie pozwala osobno kontrolować rozumienie i zapis odpowiedzi.

Przy wyszukiwaniu kolejnego fragmentu model wyklucza powtórne użycie tego samego fragmentu. Próba zakończenia z pominięciem części tekstu jest odrzucana. Dostępne są trzy alternatywne plany; każdy pełny kandydat przechodzi kontrolę zgodności ze źródłem. Brak zatwierdzonego zdania zachowuje dotychczasową odpowiedź z cytatem.

## Trening i pomiar

- 480 autorskich przykładów treningowych, 120 deweloperskich i 240 odłożonych.
- W odłożonej części użyto innych imion, rzeczowników, przymiotników i czasowników; struktury ról pozostają znanego typu.
- 100 kroków treningu; krok 25 wybrano według części deweloperskiej, bez wyboru na końcowym zestawie.
- Odłożone składanie zdań: **240/240 dokładnie zgodnych z oczekiwanym zdaniem**; wszystkie kandydaty przeszły kontrolę znaczenia. Wszystkie odpowiadające pytania były obsługiwane przez istniejący kontroler znaczenia.
- Początkowy, losowy planista: 0/120 na części deweloperskiej; po treningu 120/120.
- Podczas tworzenia treningu 34 niejednoznaczne lub nieobsługiwane propozycje źródeł odłożono osobno; nie są zaliczonymi przykładami. Zestawy deweloperski i końcowy nie wymagały odrzuceń w przyjętym generatorze.
- Pełna regresja aplikacji: **184/184 testów**, 201,18 s, na odrębnej pamięci. Obejmuje dawne funkcje i 17 kontroli pełnych zdań, kontrprzykładów, niejednoznaczności, uszkodzenia wag i kontroli alternatywnych planów.
- Przeglądarka: sześć kolejnych poleceń, pełna odpowiedź, odrzucenie zamienionych ról, poprawka zmienionego koloru, zachowanie przeczenia, Enter i widok 375 px. Bez błędów JavaScript i poziomego przepełnienia.

W testach wychwycono wielką literę pozostającą na przenoszonym przymiotniku; poprawiono jej obsługę na podstawie wybranej analizy gramatycznej. Nazwy własne pozostają zachowane. Konstrukcja „Książki Markowi nie daje Anna” może pozostać niejednoznaczna z powodu analiz nazwy własnej i rzeczownika; nie wymusza się wtedy jednego odczytu.

## Zakres i granice

Obsługiwane jest pojedyncze, w pełni rozpoznane zdanie źródłowe, także z przeczeniem, grupą czasownika modalnego, czasem i miejscem. Odpowiedź może powstać z kilku osobno dopasowanych cytatów, ale moduł nie rozwiązuje jeszcze zaimków między zdaniami ani wielozdaniowych zależności przyczynowych. Warunek, konflikt, nieodczytany fragment lub nieznana konstrukcja nie stają się bezwarunkowym twierdzeniem. Kontrola zgodności ze źródłem nie jest dowodem prawdziwości źródła.

Wynik 240/240 dotyczy kontrolowanego zestawu z podanymi rolami, a nie dowolnej rozmowy po polsku. Swobodne opowiadania i szerokie wyjaśnienia pozostają do rozwinięcia. Prywatnych rozmów ani pamięci użytkownika nie użyto do treningu.

## Ślady i cofnięcie

Dane, wagi, skrypt i pełne odpowiedzi: `training/sentence-language-2026-10-18`. Aktywny model: `artifacts/sentence/active.json`. Kopia wcześniejszych plików i manifest: `backups/before-sentence-training-2026-10-18`. Wycofanie polega na przywróceniu plików z kopii i ponownym uruchomieniu aplikacji; trwałe notatki pozostają niezależne.

(Zrzut historyczny: Przykładowa odpowiedź w panelu, wyłącznie dane demonstracyjne)


# Wektorowe łączenie ról i logika trójstanowa — 18 października 2026

## Działająca funkcja

W tej samej rozmowie wpisz:

```text
Połącz informacje: Zofia daje mapę Irenie. Irena daje mapę Piotrowi.
```

Wynik: **T — potwierdzone dopasowanie ról**, „Zofia → Irena → Piotr”, wraz z dwoma cytatami. Można też podać tekst przez „Przeczytaj:” i potem zapytać „Jak łączą się te informacje?”. W pomocy znajduje się nowy przykład; łącznie jest 27 przykładów.

To pierwszy zakres: zgodność ról w opisach przekazywania przedmiotu, od 2 do 8 rozpoznanych zdań. Nie jest to uniwersalny mechanizm łączenia wszelkiej wiedzy. T dotyczy dopasowania ról i wartości w tekście, nie prawdziwości zdarzeń ani dowodu tożsamości fizycznego przedmiotu. Sam rzeczownik „mapa” w dwóch zdaniach nie dowodzi, że chodzi o ten sam egzemplarz. Wynik nie ustala chronologii ani obecnego właściciela.

## Wektory z zachowaniem ról

Wartości ról są kodowane istniejącym neuronalnym enkoderem wyrazów aktywnego TSI do 96 wymiarów. Cztery role: wykonawca, czynność, obiekt i odbiorca mają oddzielne ortonormalne wektory w macierzy R. V zawiera cztery wektory wartości, a związana reprezentacja ma postać:

**M = Rᵀ V; odzyskanie wartości: V ≈ R M.**

Macierz M ma wymiar 4×96. Ta konstrukcja zachowuje rozdzielenie osoby i przedmiotu, mimo że obie informacje znajdują się w jednej macierzy. Maksymalny błąd numerycznego odzyskania w treningu i ocenach wyniósł około 2,1×10⁻⁷.

Wektor porównania zawiera podobieństwo cosinusowe, logarytm odległości kwadratowej i dwie cechy obecności danych. Wytrenowany komparator MLP ma **259 parametrów** i trzy wyjścia. Uczy się zgodności wartości oraz odróżnienia braku danych od różnicy. Nie uczono tu znaczenia wszystkich wyrazów ani podobieństwa synonimów; różne lemmy pozostają różnymi wartościami. Role nadal wyznaczają matryce i analizator odmiany.

## Logika trójstanowa

Prototypy stanów:

- T = (1,0,0): zgodność potwierdzona w sprawdzanym zakresie.
- F = (0,1,0): rozpoznana niezgodność.
- U = (0,0,1): dane nie wystarczają albo interpretacja jest nierozstrzygnięta.

Komparator zwraca wektor trzech ocen softmax. Nie są one skalibrowanym prawdopodobieństwem prawdziwości informacji o świecie. Niska pewność odczytu jest traktowana jako U.

Istniejący uczony moduł logiki TSI łączy wektory porównania odbiorca–wykonawca, obiekt–obiekt oraz kontekstu operatorem AND. W tej rundzie ponownie sprawdzono 27 kombinacji trzech stanów, bez ponownego uczenia wag logiki. Brak danych nie staje się fałszem: T AND U = U. Rozpoznana niezgodność może rozstrzygnąć połączenie: F AND U = F.

Kontekst pochodzi z jawnych matryc: negacja przekazania wyklucza twierdzenie o dodatnim przekazaniu; możliwość, warunek lub niedopasowane warunki pozostawiają niepewność. Sprzeczne cytaty są zachowywane i oznaczane w analizie, nie uśredniane. Dodatkowe kontrole lemmy, liczby i określeń przedmiotu są oddzielone od ocen sieci. Raport zachowuje surowe odpowiedzi modelu oraz wynik kontroli.

Zatwierdzone dopasowania tworzą macierz sąsiedztwa A. Iloczyn A² pokazuje możliwość złożenia dwóch dopasowań ról między trzema zdaniami. Jest to algebra grafu rozpoznanych relacji, nie dowód przebiegu zdarzeń.

## Trening i pomiar

- 3600 porównań treningowych, 600 deweloperskich i 1200 odłożonych, z rozdzielonym słownictwem.
- 125 kroków, wybór kroku na części deweloperskiej przed odłożoną oceną.
- Odłożone porównania: **1200/1200**, po 400 T, F i U; bez fałszywego T na 800 przykładach F/U.
- Wynik dotyczy porównań zakodowanych wartości ról i masek obecności, nie 1200 dowolnych zadań językowych.
- Natywna logika: **27/27** kombinacji trzech stanów dla potrójnego AND.
- Cała aplikacja: **200/200 testów** na odrębnej pamięci, w tym 16 kontroli nowego przepływu na rzeczywistych zdaniach.
- W przeglądarce: sześć kolejnych poleceń, stan T, różny przedmiot F, możliwość U, złożenie trzech zdań i zachowanie wcześniejszych pełnych odpowiedzi. Enter czyści pole, brak błędów JavaScript i przepełnienia przy szerokości 375 px.

W trakcie przeglądu poprawiono błędne oczekiwanie testowe: „Alicja daje książkę Oskarowi. Marek daje książkę Alicji” dopuszcza strukturalne powiązanie Marek → Alicja → Oskar. Kolejność zapisu nie jest chronologią. Dodano osobny test tego przypadku i test dwóch niezależnych przekazań do tej samej osoby.

Żadne prywatne rozmowy ani notatki nie były materiałem treningowym. Wagi rdzenia H512 i istniejącej logiki nie zostały zmienione w tej rundzie. Wytrenowano i podłączono dodatkowy komparator wektorów, korzystający z aktywnego enkodera. To wdrożony moduł asystenta, odrębny od dawnego odrzuconego prototypu swobodnego generatora.

## Granice i dalsza praca

Nieodczytane zdanie, zaimek wymagający ustalenia osoby, nieznany schemat albo przekroczenie ośmiu zdań wymagają doprecyzowania. Synonimy rzeczowników i tożsamość egzemplarzy przedmiotów nie są rozwiązywane automatycznie. Następne rozszerzenie powinno dotyczyć jawnego powiązania zaimków, identyfikatorów przedmiotów oraz kolejności i warunków zdarzeń, z osobnymi testami błędnych połączeń.

Aktywny komparator: `artifacts/vector_language`. Dane, skrypty i pełne wyniki: `training/vector-language-2026-10-18`. Kopia plików do cofnięcia: `backups/before-vector-language-2026-10-18`. Pamięć użytkownika pozostaje niezależna. Publicznie udostępniamy tylko opis i demonstracyjny zrzut ekranu.

(Zrzut historyczny: Dopasowanie ról T w panelu — dane demonstracyjne)


# Macierz kontekstowo-przyczynowa — 18 października 2026

## Korzystanie w tej samej rozmowie

```text
Macierz przyczynowa: Fakt: pada deszcz. Jeśli pada deszcz, to ulica jest mokra. Deszcz powoduje wzrost poziomu wody.
```

Dostępne są też „Macierz kontekstowo-przyczynowa:” i „Pokaż macierz przyczynową” dla tekstu wcześniej podanego przez „Przeczytaj:”. Nowy przykład dodano do pomocy; obecnie jest 28 przykładów. Nie dodano nowej strony panelu.

Macierz przechowuje osobno przyczyny, reguły warunkowe, kolejność w czasie oraz wnioski zapisane w źródle. Każde pole ma stan T, F albo U oraz trójelementowy wektor. Nieopisane połączenie ma U. Źródłowe cytaty i sprzeczności pozostają zachowane.

## Rozpoznawane konstrukcje

- „A powoduje B”, „A jest przyczyną B” — przyczyna podana w źródle.
- „A nie powoduje B” — jawne zaprzeczenie tej relacji.
- „Ponieważ A, B”, „B, ponieważ A”, „B, bo A”, „A, dlatego B”, „B dlatego, że A” — kierunek przyczyna–skutek z zachowaniem kolejności logicznej.
- „Jeśli A, to B” lub „Jeżeli A, B” — osobna reguła warunkowa, nie automatycznie przyczyna.
- „Najpierw A, potem B”, „A poprzedza B” — kolejność bez dopisywania przyczyny.
- „A, więc B” i „A, zatem B” — osobna warstwa wniosków zapisanych w tekście.
- „Fakt: A”, „Nieprawda: A”, „Nieznane: A” — jawnie podany stan zdania. Zwykłe zdanie staje się faktem tylko w zakresie potwierdzonym przez dotychczasowy kontroler; pozostałe atomy pozostają U.
- „W piątek: …”, „W sobotę: …”, „W biurze: …” — jawnie wydzielone konteksty. Różne konteksty nie są uśredniane ani automatycznie utożsamiane.

Treści A i B są literalnymi zdaniami lub nazwami zdarzeń; nie jest to lista gotowych pełnych zadań. Tożsamość atomów opiera się na tym samym zapisie z pominięciem wielkości liter i zbędnych odstępów. Nie usuwa się polskich znaków. Parafrazy, zaimki i tożsamość zdarzeń nie są tu jeszcze rozwiązywane automatycznie.

## Wnioskowanie i bezpieczeństwo znaczenia

Jeżeli źródło podaje fakt A oraz jawną regułę „Jeśli A, to B”, aktywny uczony moduł logiki TSI łączy wektory antecedentu i reguły przez AND; potwierdzone uruchomienie pozwala wyprowadzić B w granicach tych założeń. Ślad pokazuje aktywacje T/F/U oraz cytowaną regułę.

Fałszywe A nie oznacza fałszywego B. Nieznane A nie potwierdza B. Sama relacja „A powoduje B” nie jest używana jako reguła wystarczająca do B — przyczynę odróżniamy od wystarczającego warunku. Nie dopisujemy bezpośredniej przyczyny A→C tylko z A→B i B→C.

Sprzeczne fakty lub wersje tej samej zależności w tym samym kontekście otrzymują U i zachowują obie wersje. Sprzeczny wniosek nie uruchamia kolejnych reguł. Pytanie nie jest twierdzeniem. „Prawdopodobnie”, „być może” i podobne zastrzeżenia pozostawiają zależność U. Niezgodne nawiasy lub niejednoznaczne zagnieżdżenie zatrzymują potwierdzanie całości.

Macierz opisuje informacje zadeklarowane w źródle, nie dowodzi prawdziwości przyczyn w świecie. Wyprowadzenie zdania o poleceniu nie wykonuje tego polecenia: węzły pozostają danymi.

## Sprawdzenie i zakres

Końcowe testy tej macierzy: **38/38**, 58,01 s. Obejmują kierunki relacji, oddzielne warstwy, brak przyczynowości przy współwystępowaniu, konflikty, konteksty, polskie znaki, niepewność, pytania, nawiasy, limity, natywne wnioskowanie, brak odwracania implikacji, zatrzymanie po sprzeczności i izolację sesji. Wcześniejszy przebieg obejmował 68 testów nowego przepływu oraz wybranych dawnych rozmów, matryc, pełnych odpowiedzi i wektorowego wiązania ról; wszystkie przeszły. Dodatkowo ponowiono trzy testy aktywacji natywnej logiki po poszerzeniu śladu.

W przeglądarce sprawdzono siedem poleceń: nową macierz, brak fałszywej przyczyny, rozdzielenie kontekstów, zablokowanie następstw sprzecznego faktu oraz zachowanie poprzedniego łączenia wektorów i pełnych odpowiedzi. Bez błędów JavaScript i poziomego przepełnienia przy 375 px. Ostatnia pełna regresja przed tą macierzą wynosiła 200/200; nowej wersji nie przypisujemy nieuruchomionego pełnego przebiegu.

Limit to 40 krótkich zdań i 24 węzły; przekroczenia wymagają podziału tekstu, nie obcinania warunków. Obecnie obsługiwane są opisane polskie łączniki i jawne konteksty. Pełne drzewa zdań złożonych oraz angielski czytnik nie zostały jeszcze wdrożone. Docelowo osobne reguły PL/EN mają zasilać tę samą strukturę znaczenia; translator może być pomocą z zachowaniem oryginału.

## Pojemność przy zapominaniu

Zapisano `data/training_capacity_policy.json`. Powtarzalna utrata wcześniej poprawnych przypadków ma uruchamiać kontrolę pojemności odpowiedniego modułu, powiększenie i trening z powtórkami. Dla natywnego H512 zachowano kandydatów szerokości 640, 768 i 1024; wybór wymaga pomiaru. Dla modułów pomocniczych zwiększa się ich własną szerokość, jeśli regresja dotyczy tych modułów. Starsze wagi są zachowywane. Wdrożenie dopiero po potwierdzeniu poprawy i utrzymania wcześniejszych umiejętności. Polityka dotyczy kolejnych jawnie zlecanych treningów; nie włącza samoczynnej wymiany wag podczas rozmowy.

W tym etapie wykorzystano istniejącą logikę; nie trenowano nowych wag ani nie użyto prywatnych rozmów jako materiału. Kopia do cofnięcia: `backups/before-context-causal-2026-10-18`. Wyniki i demonstracja: `docs/context-causal-2026-10-18`.

(Zrzut historyczny: Macierz przyczyn i warunków — dane demonstracyjne)
