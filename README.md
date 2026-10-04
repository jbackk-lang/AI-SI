# AI-SI

SI to eksperymentalny warsztat łączący język, matematykę, programowanie i analizę materiałów źródłowych. Własne małe sieci wybierają działania oraz przebiegi współpracy, a specjalistyczne modele i narzędzia wykonują zadania. Inspiracją projektu jest TIMDR jako punkt wyjścia do budowy sterownika.

**To repo publikuje interfejs, integrację, narzędzia treningowe, testy i opis wyników. Nie publikuje rdzenia SI/TIMDR, prywatnych algorytmów, wag, checkpointów ani pamięci użytkownika.** [Zakres publikacji](docs/PUBLIC_SCOPE.md).

## Co obecnie działa

Stan rozwojowy: **4 października 2026**. Poniższy opis dotyczy prywatnego silnika; samo pobranie publicznego repo nie zapewnia jego wszystkich funkcji.

- Rozmowa po polsku i generowanie kodu przez **Qwen3-4B-Instruct-2507**, który zastąpił Bielika.
- Kontrolowana matematyka, dokładny kalkulator, walidator i SymPy dla obsługiwanych równań.
- Dobór sprawdzonych przykładów Pythona oraz osobna ścieżka generowania programu i sprawdzania podanych przypadków.
- Wyszukiwanie znaczeniowe przez **Embedding**, ocena trafności przez **Reranker**, interpretacja przez Qwena.
- Analiza obrazów przez Qwen-VL, wymagająca oceny poprawności odczytu.
- Odczyt wskazanych stron i plików udostępnionych przez użytkownika. Obsługiwane źródła internetowe: Python, MDN, Wikipedia, NASA, GitHub oraz SJP PWN. Nie jest to dostęp do dowolnej strony.
- Uczony koordynator wybierający gotowe przebiegi współpracy. Aktualnie ma **5120 neuronów ukrytych**.
- Kontrolowane uczenie intencji z potwierdzonych przykładów i odrzucanie kandydatów, które nie przechodzą testów.

ASR, analiza dźwięku i TTS zostały podłączone i sprawdzone w ograniczonych próbach, ale **dźwięk jest obecnie odłączony na polecenie użytkownika**. Jego pliki zachowano.

[Szczegóły aktualnego stanu](docs/SI_STAN_2026-10-03.md) · [Podsumowanie wyników JSON](docs/SI_WYNIKI_2026-10-03.json).

## Jak moduły współpracują

| Zadanie | Przebieg |
|---|---|
| Obsługiwany rachunek | Matematyka → niezależna walidacja |
| Znany przykład programu | Dobór programu → sprawdzony przykład |
| Nowy program z przypadkami testowymi | Qwen → kontrola kodu → testy |
| Pytanie o dokumenty | Embedding → Reranker → Qwen |
| Pytanie o stronę | Czytnik internetowy → Qwen |
| Obraz | Qwen-VL → przegląd wyniku |
| Optymalizacja arytmetyczna | Warianty działania → kontrola zgodności → porównanie |

Wykonano również dwie próby przekazywania danych między tymi przebiegami:

1. Obraz z liczbą **42** → porównanie odczytu ze znaną wartością testową → dodanie 8 → sprawdzony wynik **50**.
2. Dokument o silni → Embedding i Reranker → wyjaśnienie Qwena → przekazanie wyjaśnienia do generowania programu → testy **0→1, 5→120, 7→5040**. Wszystkie trzy przeszły.

W tych próbach eksperyment określał kolejność podzadań, a koordynator wybierał ścieżkę każdego podzadania. **Nie wykazano jeszcze samodzielnego tworzenia nowych globalnych planów.** Przekazanie dokumentu nie dowodzi, że Qwen potrzebował go do zadania, które mógł znać wcześniej.

## Co oznacza samouczenie i samonaprawa

Przykład trafia do kontrolowanego uczenia dopiero po sprawdzeniu. Kandydat jest oceniany oddzielnie; zła zmiana nie powinna zastępować aktywnej wersji. Sam opis obrazu, transkrypcja, odpowiedź językowa lub odczyt Wikipedii nie są potwierdzonymi faktami treningowymi.

Docelowy cykl samonaprawy: **niezaliczone zadanie → diagnoza rodzaju braku → dobór danych lub narzędzia → próba naprawy → ponowny test → zachowanie tylko sprawdzonej zmiany**. Niepewność sieci sama nie dowodzi braku wiedzy.

Ostatnia diagnostyka dotyczy rzeczywistych niepowodzeń rozpoznawania poleceń programistycznych. Brak doboru programu nie oznacza, że nie znamy jego algorytmu: może wymagać lepszego rozpoznania sformułowania, a nie czytania kolejnego artykułu. Uzupełnianie dowolnych braków i ogólne autonomiczne samouczenie pozostają celem rozwojowym.

## Rozmiar

Wartości dziesiętne: MB = milion bajtów, GB = miliard bajtów. Rozmiar wag nie jest rozmiarem całego środowiska ani wymaganą ilością RAM.

### Aktualna liczba neuronów własnych sieci

| Aktywna sieć | Neurony ukryte | Parametry |
|---|---:|---:|
| Czytnik matematyczny | 1 024 | 2 104 326 |
| Planer matematyczny | 1 024 | 2 103 301 |
| Programowanie | 1 024 | 4 206 603 |
| Most intencji | 1 024 | 2 103 301 |
| Koordynator współpracy | 5 120 | 10 542 090 |
| **Łącznie** | **9 216** | **21 059 621** |

**Mamy łącznie 9 216 neuronów ukrytych w pięciu własnych głównych sieciach.** Liczba 5120 dotyczy samego koordynatora; cztery pozostałe moduły dodają 4096. To suma warstw różnych sieci, nie szerokość jednej warstwy. Wymiary sprawdzono bezpośrednio w aktywnych checkpointach 3 października 2026. Nie wliczamy wejść, wyjść, nieaktywnych eksperymentów ani gotowych modeli Qwen, Embedding, Reranker i Qwen-VL.


| Składnik | Rozmiar wag |
|---|---:|
| Qwen językowy, wersja Q4_K_M | 2,50 GB |
| Embedding, Reranker, Qwen-VL i jego projektor | około 3,40 GB |
| Zachowany, obecnie odłączony ASR | około 486 MB |
| Cztery własne główne moduły po 1024 neurony | 42,09 MB |
| Koordynator współpracy: 5120 neuronów | 42,17 MB |
| Własne główne moduły wraz z koordynatorem | **84,27 MB** |

Zestaw wymienionych głównych wag wraz z zachowanym ASR zajmuje około **6,47 GB**. Biblioteki, środowisko, wyniki, wcześniejsze checkpointy i kopie modeli zajmują dodatkowe miejsce. Własne główne sieci mają łącznie około **21,06 mln parametrów**, w tym koordynator **10,54 mln**. Parametry to wagi i współczynniki sieci, a nie liczba neuronów. Gotowe modele Qwen są osobnymi składnikami.

## Ograniczenia

Wyniki pochodzą z niewielkich, kontrolowanych prób. Część sprawdzianów używa znanych szablonów z nowymi wartościami. Nie wykazaliśmy równorzędności z ogólnymi modelami AI, przewagi TIMDR we wszystkich zadaniach ani samodzielnego nauczenia pełnej matematyki czy programowania.

Więcej neuronów zwiększa pojemność, ale nie zastępuje danych, informacji zwrotnej i poprawnego planowania. W ostatniej próbie zarówno koordynator 1024, jak i 5120 uzyskały **52/52**. Powiększenie nie wykazało poprawy trafności na tym zestawie.

Testy kodu sprawdzają wskazane przypadki i ograniczony podzbiór języka. Nie stanowią gwarancji poprawności ani uniwersalnego bezpiecznego wykonawcy dowolnych skryptów. Trafność dokumentu nie oznacza jego prawdziwości, a odpowiedź na podstawie źródła pozostaje interpretacją wymagającą kontroli.

## Uruchomienie publicznego interfejsu

1. Uruchom posiadany prywatny silnik SI zgodnie z jego instrukcją.
2. W tym repo uruchom `Uruchom_AI_SI.bat` albo `python run_ui.py`.
3. Interfejs korzysta z adresu silnika skonfigurowanego przez `--backend`. Bez uruchomionego silnika zgłosi brak połączenia.

Domyślna integracja korzysta z lokalnych modeli. Wyszukiwanie i odczyt stron łączą się z odpowiednimi serwerami internetowymi. Udostępnianie plików jest osobną funkcją i wymaga wskazania ich przez użytkownika.

## Historia rozwoju SI

### Punkt wyjścia: TIMDR i osobny moduł językowy

TIMDR potraktowano jako inspirację do budowy rdzenia i sterownika współpracy, a nie utożsamienie SI z modelem sygnału radarowego. Rozdzielono rozumienie języka, obliczenia, dobór narzędzi oraz kontrolę wyniku. Kolejne próby rozwijały negację, rozpoznawanie poleceń, matematykę, programowanie i pamięć. Pełnego niezależnego AI zbudowanego od podstaw nie uzyskano.

### Wcześniejszy pilotaż Bielika

Przy zamrożonej bazie trenowano mały adapter na 12 przykładach. Po korekcie testera wynik zmienił się **3/6→4/6**, dodatkowe zadania **0/3→1/3**, a krótkie próby polskiego **2/3→2/3**. Adapter miał 312 800 bajtów. To niewielka poprawa pilotażowa, nie pełny asystent programistyczny. [Protokół](docs/BIELIK_CODING_PROTOCOL.md) · [Wyniki](docs/TRAINING_RESULT.md).

### 2 października: negacja i dokładna walidacja

Uczone rozszerzenie negacji uzyskało **1440/1440 nowych grafów i 720/720 regresji**, w trzech przebiegach na tych samych zestawach. Dokładne narzędzie z walidatorem rozwiązało **24/24 rachunków**, a Bielik bez adaptera **3/24**. Rachunki wykonuje narzędzie, nie wyuczona sieć. [Opis i wyniki w GIA-TIMDR](https://github.com/jbackk-lang/GIA-TIMDR/blob/main/docs/SI_NEGACJA_WALIDACJA_2026-10-02.md).

### 2 października: przejście na Qwena i wzrost matematyki

Qwen zastąpił Bielika w rozmowie, interpretacji źródeł, generowaniu kodu i przekładzie poleceń matematycznych. Mała próba: **Qwen 8/8, Bielik 3/8**; regresja Qwena **8/8**. Część przypadków bada odmowy realizowane kontrolą wejścia, pozostałe przekład planu i obliczenie. To nie szeroki benchmark modeli.

Podwojenie matematyki ze 128 do 256 neuronów zachowało wyniki: pojedyncze działania **140/140** i **282/282** regresji; pięć planów dwuetapowych **96/96** i **192/192** regresji. Nie wykazano korzyści z samego zwiększenia szerokości. [Opis](docs/SI_QWEN_MATEMATYKA_2026-10-02.md) · [Liczby](docs/SI_QWEN_MATEMATYKA_2026-10-02.json).

### 2 października: SymPy, język i kolejność

Dodano dokładne narzędzie symboliczne oraz ograniczony przekład polskich równań; **12/12 testów funkcjonalnych** przeszło. Przykład „dwa razy x plus trzy równa się jedenaście” daje `x=4`. To narzędzie, nie wyuczona wiedza sieci. Rozwijano też obsługę poleceń z jawną kolejnością i domyślnym porządkiem matematycznym. [Zakres SymPy](docs/SI_SYMPY_2026-10-02.md).

### Dalsze próby: programowanie i relacje modułów

Pozostawiono moduł programowania i ograniczony tester, wyłączając agenta Qwen Code. Rozwijano rozpoznawanie celu, kryterium ulepszenia i relacji język–matematyka–kod. Dodano Embedding, Reranker i obrazy, następnie eksperymentalnie mowę i dźwięk.

### 3 października: cztery własne moduły po 1024

Matematyka zachowała **710/710** wyników łącznie w sprawdzanych blokach; nie wykazano poprawy ponad wcześniejszą wersję. Programowanie trenowane od nowa poprawiło świeżą próbę **20/24→21/24**, ale wprowadziło regresje i zostało odrzucone. Aktywowano poszerzenie zachowujące wcześniejsze wagi i decyzje: **20/24** w tej próbie oraz **6/6** dodatkowych kontroli. Wzrost pojemności nie oznaczał nowej wiedzy ani zmiany tokenizacji.

Most intencji 1024 zachował **16/16** wcześniejszych zadań i poprawił małą świeżą próbę **15/16→16/16**. Nadal jest to ograniczona klasyfikacja celu, nie dowolne planowanie.

### 3 października: Embedding, Reranker, obraz i audio

Małe kontrole: Embedding **4/4**, Reranker **2/2**, obrazy **2/2**, kontrola wejść **4/4**. Rozpoznawanie mowy badano na dwóch syntetycznych wypowiedziach, a parametry audio m.in. na tonie 440 Hz i ciszy. Jedna transkrypcja zmieniła sens działania, mimo zachowania słów i liczb. Nie uzyskano pełnej niezawodności mowy. Audio później odłączono, zachowując modele.

### 3 października: kontrolowane uczenie i odrzucenie kandydata

Po czterech zweryfikowanych działaniach automatycznie uruchomiono trening intencji. Kandydat poprawił wynik **32/36→35/36**, lecz skierował mnożenie 317 przez 223 do ulepszania. Został odrzucony. Matematyka z niezależną kontrolą uzyskała poprawne **70691**. Próba ścieżki ulepszania początkowo tylko prosiła o kryterium.

### 3 października: ograniczony optymalizator

Dodano porównanie poprawnych wariantów arytmetyki. Dla 317×223 wszystkie trzy warianty dały 70691; zwykłe mnożenie wymagało najmniej działań i było szybsze w lokalnym mikropomiarze. Sześć testów optymalizatora i siedem kontroli wcześniejszego cyklu przeszło. Nie powstał ogólny optymalizator programów ani dowód intencji modelu.

### 3 października: koordynator współpracy 1024

Na 288 syntetycznych przykładach nauczono wyboru gotowych przebiegów. Zamrożona próba: **36/36**; część zadań powtarzała szablony z innymi wartościami. Następnie wykonano rzeczywiście sześć ścieżek bez dźwięku: matematykę, dobór programu, generowanie z testami, dokumenty, internet oraz obraz. Ukończenie wywołania nie oznacza weryfikacji całej treści odpowiedzi.

### 3 października: koordynator 5120 i Wikipedia

Warstwę koordynatora zwiększono pięciokrotnie. Pobrano pięć artykułów i przygotowano **40 zadań** wyboru pracy ze źródłem lub dokumentami. Ocena: **23 nowe zadania + 29 wcześniejszych = 52/52**, tyle samo dla wersji 1024 i 5120. Większą wersję aktywowano bez utraty poprawnych decyzji; stare wagi zachowano.

Trzy rzeczywiste zadania źródło→Qwen dotyczyły silni, twierdzenia Pitagorasa i wyszukiwania binarnego. Wszystkie zakończyły się odpowiedziami; jedna była ucięta przez limit długości. Nie trenowano Qwena ani faktów z artykułów.

### 3 października: zadania wymuszające przekazanie danych

Wykonano obraz→matematyka→walidacja oraz dokumenty→Embedding→Reranker→Qwen→program→testy. Szczegóły i ograniczenia tych dwóch prób podano wyżej. Nadal nie oznacza to samodzielnego odkrywania całych przebiegów.

### 3 października: wybór artykułów a wybór braków

Udostępniono dziesięć pobranych artykułów. Qwen, mając pełną listę, wybrał **Backpropagation, Reinforcement learning i Binary search algorithm**. Oddzielna eksperymentalna polityka nowości i niepewności wybrała **Gradient descent, Reinforcement learning i Sorting algorithm**. Wyniki te nie dowodzą zainteresowań ani zidentyfikowanych braków wiedzy.

Na polecenie użytkownika politykę ciekawości wyłączono jako mechanizm samonaprawy. Kierunek dalszych prac to **wybór potwierdzonych braków**, dobór odpowiedniej naprawy oraz ponowna walidacja — zamiast wybierania materiałów na podstawie samej niepewności.

Ponowny sprawdzian wykazał cztery nierozpoznane polecenia w 24-zadaniowej próbie programowania. Próba naprawy jednego z nich wygenerowała program, ale kontrola wykonania odrzuciła użycie niedozwolonej metody. Naprawy nie zapisano, wagi pozostały bez zmian. Odrzucenie przez ograniczony tester nie dowodzi błędu samego algorytmu; trzeba odróżniać braki rozpoznawania, wiedzy oraz możliwości wykonawcy. **Udanej ogólnej samonaprawy jeszcze nie wykazano.**

## Aktualizacja: pamięć, walidacja i wykorzystanie wiedzy — 4 października 2026

### Co wykonano i działa w ograniczonym zakresie

- Podłączono pamięć materiałów źródłowych: zapis fragmentów i adresów, wyszukiwanie pasujących materiałów oraz przekazywanie ich do rozmowy. Zapisane materiały pozostają niezweryfikowanymi źródłami, a nie automatycznie potwierdzonymi faktami.
- Dodano odczyt udostępnionych lokalnych repozytoriów i analizę wybranych plików własnej pamięci oraz wykonawcy. Dostęp do katalogu nie oznacza przeczytania całego repozytorium.
- Dodano ograniczone reguły semantyczne dla zakazu, warunku, doprecyzowania, braku danych i sprzeczności. Obsługiwane przypadki mogą zatrzymać działanie, poprosić o dane, porównać liczby zamiast ich sumowania lub usunąć duplikaty z zachowaniem kolejności.
- Połączono kontrolę kolejności działań z walidacją argumentów: liczby i ich powtórzenia w obsługiwanej matematyce, liczba argumentów i ograniczona kontrola użycia wejść w programie. Są to kontrole o określonym zakresie, nie dowód sensowności dowolnego planu.
- Poprawne przykłady trafiają do bufora kandydatów do późniejszego treningu. Sam zapis do bufora nie uruchamia uczenia wag.
- Uruchomiono sesje wyboru i czytania materiałów z małym obciążeniem procesora, historią wyników i bez nakładania sesji. Dodano wybór rzeczywistych wyników wyszukiwania po błędnym tytule artykułu. Przekroczenia czasu i nietrafione wybory nadal się zdarzają.

### Potwierdzone wyniki ostatnich prób

| Próba | Wynik | Zakres wniosku |
|---|---|---|
| Trening rozpoznawania poleceń programowania | **3/8 → 5/8** na nowej, zamrożonej próbie; bez utraty wcześniej poprawnych decyzji w sprawdzonej regresji | Poprawa małego klasyfikatora intencji; nie trening Qwena |
| Naprawa spłaszczania list po podpowiedzi | **6/6** przypadków | Zapis sprawdzonego programu dla znanego polecenia; nie ogólna samonaprawa |
| Zastosowanie pamięci do dwóch nowych zadań programowania | Bez pamięci **1/2**, z pamięcią **2/2**; po cztery przypadki na zadanie | Mała próba wskazuje użyteczność przykładu zgodnego z wykonawcą |

W porównaniu pamięci oba warianty rozwiązały usuwanie duplikatów z pomijaniem liczb ujemnych. W zadaniu spłaszczania i wyboru pierwszych trzech elementów wariant bez pamięci użył funkcji `isinstance`, której ograniczony tester nie obsługuje; wariant z pamięcią przeszedł wszystkie przypadki. Odrzucenie pierwszego programu nie dowodzi, że jego algorytm jest błędny. Warunki uruchomiono w stałej kolejności, na zaledwie dwóch zadaniach, więc nie jest to szeroki benchmark ani dowód przewagi szybkości.

### Co pozostaje otwarte

Nie wykazano jeszcze ogólnego samodzielnego uczenia, niezawodnego planowania dowolnych zadań ani przenoszenia wiedzy z przeczytanych artykułów do wszystkich modułów. Reguły semantyczne są ograniczone i nie stanowią wyuczonego rozumienia języka. Pamięć sprawdzonych programów, pamięć źródeł i trening wag to różne mechanizmy. Potrzebne są większe, niezależne próby zastosowania wiedzy, kontrola regresji oraz pilotaż integracyjny opisany poniżej.

## Propozycja wdrożenia SI w większym systemie

SI można rozwijać jako moduł współpracujący z większym systemem: rozpoznający zadanie, przygotowujący plan, dobierający narzędzia, korzystający z pamięci i kontrolujący wynik. Jest to propozycja dalszego rozwoju, nie deklaracja gotowości produkcyjnej.

Do przygotowania integracji potrzebne są:

- **Stabilne API** przyjmujące zadanie i dane, a zwracające wynik, źródła oraz status weryfikacji. Brak danych, niepewność i odrzucenie planu powinny być jawnie reprezentowane.
- **Oddzielenie rdzenia od modułu językowego**, aby można było wymienić Qwena bez przebudowy koordynatora SI.
- **Kontrola uprawnień** rozdzielająca odczyt danych, proponowanie zmian i wykonywanie działań.
- **Testy integracyjne na nowych zadaniach** docelowego systemu, z porównaniem identycznych zadań z SI i bez SI. Należy mierzyć poprawność, błędne działania i regresje, nie tylko ukończenie wywołania.
- **Wersjonowanie pamięci i modeli** oraz możliwość powrotu do poprzedniej wersji po pogorszeniu wyników.

Rdzeń SI/TIMDR może pozostać prywatny. Integrator mógłby korzystać z usługi lub pakietu wykonawczego, a publiczne repo zawierałoby dokumentację i interfejs integracji. Takie udostępnienie wymaga osobnego ustalenia warunków; obecna dokumentacja nie udziela licencji na prywatny rdzeń.

**Następny proponowany krok: stabilne API i pilotaż w jednym wybranym zastosowaniu.** Obecne wyniki dotyczą prototypu i ograniczonych prób. Pilotaż powinien sprawdzić rzeczywisty wkład SI oraz wymagania przed szerszym wdrożeniem. Sam odczyt materiałów i zapis pamięci nie oznaczają treningu wag.

## Publiczne pliki i historyczne narzędzia

| Katalog | Zawartość |
|---|---|
| src/ai_si | Publiczny gateway i integracje |
| web | Interfejs przeglądarkowy |
| tools/training | Historyczne narzędzia treningu adapterów |
| tools/testing | Ograniczony tester Pythona |
| tools/release | Kontrola zakresu publikacji |
| tests | Testy publicznych modułów |
| data/coding_adapter | Dane małego pilotażu |
| docs | Protokoły i wcześniejsze wyniki |

Historyczny trening Bielika wymaga `pip install -r requirements-training.txt`, wskazania modelu przez `SI_MODEL_PATH` i runtime przez `SI_LLAMA_SERVER`. Narzędzia: `python tools/training/prepare_runtime.py` oraz `python tools/training/run_bielik_coding_adapter.py`. Nie są treningiem obecnego rdzenia SI.

## Testy i publikacja

W PowerShell ustaw `$env:PYTHONPATH="src;tools/testing"`, następnie uruchom `python -m unittest discover -s tests -v`. Testy publicznego repo nie zastępują testów prywatnego silnika opisanych w historii.

Kontrola publikacji: `python tools/release/prepare_commit.py`. Nie wykonuje commitu ani push. Wagi, rdzeń i prywatne dane pozostają poza repo. Prawa do zewnętrznych modeli wynikają z licencji ich producentów; ten opis nie ustanawia licencji prywatnego rdzenia.

## Aktualizacja interfejsu — 4 października 2026

Lokalny interfejs ma dwa panele: **Rozmowa z SI** oraz **Narzędzia i zadania**. Qwen pełni rolę modułu językowego; odpowiedzi rozmowy są oznaczone jako niezweryfikowane. Narzędzia korzystają z osobnego panelu i pokazują status wyniku. Na wąskim ekranie panele układają się jeden pod drugim.

Po udanym wysłaniu pole wiadomości jest czyszczone. Przycisk **Nowa rozmowa** rozpoczyna nowy kontekst, zachowując poprzednie wpisy w lokalnym archiwum. Zapis rozmów nie jest treningiem wag. Sprawdzono wyświetlanie paneli i działanie przycisku; nie wykryto błędów JavaScript podczas tej kontroli.

Ta aktualizacja dokumentuje prywatną wersję lokalną. Jej kod, archiwum rozmów, pamięć i wagi nie są dołączane do tego commitu.
