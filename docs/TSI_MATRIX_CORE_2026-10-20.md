# Wspólny moduł matryc TSI 0.5 — 20 października 2026

## Aktualny wynik

Wdrożony checkpoint **TSI-MATRIX-CORE-4ad2089c** zawiera dotychczasowy transformer relacji, słownik pojęć i macierz wymaganych danych jako wagi oraz uczoną warstwę przejść ról. Ma **302 642 parametry łącznie**, w tym **256 parametrów uczonej tablicy przejść**. Macierze słownika i wymagań przeniesiono dokładnie jako stałe wagi; nie są wynikiem uczenia znaczeń nieznanych słów. Wcześniejsze parametry transformera są identyczne bit po bicie.

Moduł współpracuje z aktywnym H512; nie zastępuje go i nie oznacza scalenia wszystkich wag H512 w jedną sieć. Matryce czytnika i transformer są już w jednym checkpointcie. Kod reguł wiązania danych, audyt i solvery pozostają jawne. Notatki i dokumenty pozostają w wersjonowanej bazie danych, z szybkim odczytem i kontrolą źródeł.

## Dlaczego zmieniono strukturę

Wcześniejszy kandydat przewidywał cel, role i wymagane dane niezależnie. Osiągnął 48/84 pełnych zgodności z pięcioma błędnymi akceptacjami i nie został włączony. Aktualny model wiąże wymagane dane bezpośrednio z celem za pomocą wspólnej macierzy. Przejścia między rolą źródła/celu i stanem dodatnim/zanegowanym uczono jako pełną skończoną tablicę reguł, bez zapisywania całych poleceń.

Zachowano niezależne sprawdzenie źródeł, sprzeczności i wyników narzędzi. Nie zastępuje się brakujących danych zgadywaniem.

## Kontrole

- Uczona tablica przejść: 64/64 kombinacje stanu i zdarzenia, minimalne prawdopodobieństwo poprawnej klasy 0,997. To pełna kontrola skończonej tablicy, nie odłożony test językowy.
- Słownik: 1596 form w 18 kategoriach; zgodność wag z macierzą źródłową dla wszystkich form.
- Macierz wymagań: poprawne wszystkie 512 zestawów dziewięciu celów.
- Rozwój i regresje składania poleceń: 265/265. Pierwsze przejście 264/265 ujawniło brak obsługi konstrukcji łącznej „nie tylko…, ale też…”. Po dodaniu ogólnej reguły zestaw ten jest regresją.
- Oddzielny zamrożony sprawdzian kompozycji po poprawkach: **118/118**, w tym 34 polecenia do zatrzymania; **zero błędnych akceptacji**. Obejmuje nowe kompozycje trzech celów oraz role i rodzaje całek. Nie był używany do uczenia ani wyboru checkpointu. To weryfikacja znanych pojęć i jawnych danych, nie pomiar rozumienia dowolnego języka.
- Wcześniejsze zestawy relacji: **960/960, 720/720 i 640/640**.
- Testy modułu: **57/57**. Dotychczasowy przepływ: **32/32**, w tym **24/24 akademickie**, bez wykonania 16 poleceń do odrzucenia.
- Wdrożenie: **12/12**. Rzeczywiste wykonanie siedmiu nowych zadań: **7/7**, w tym obie całki w jednym zadaniu, polecenia PL/EN, sygnał i projekt budżetu na danych syntetycznych.
- Jawne plany matematyki, budżetu i sygnałów z przerwaniem i wznowieniem: **3/3**.
- Działające panele: **8/8** nowych przypadków PL/EN; wcześniejsze kontrole API **7/7**, zabezpieczenia **4/4**. W początkowej próbie procesu panelu wystąpił ogólny błąd uruchomienia czytnika. Po przeładowaniu test ośmiu przypadków przeszedł; przyczyny pierwotnego błędu nie potwierdzono. Dodano lokalną diagnostykę błędów procesu, bez treści żądań.

## Poprawione wiązanie poleceń

Określenie całki jest wiązane z odpowiednim wystąpieniem i zakresem polecenia. Określenie zanegowanej całki nie przechodzi na pozytywny cel. Dwie jawnie wymienione całki mogą być osobnymi krokami. Granice całki oznaczonej nie zmieniają automatycznie osobno wskazanej całki nieoznaczonej.

Przykłady potwierdzone rzeczywistym wykonaniem:

- `Wyznacz całkę oznaczoną oraz całkę nieoznaczoną: x^2; od 0 do 1` → funkcja pierwotna `x**3/3 + C`, całka oznaczona `1/3`.
- `Nie obliczaj całki nieoznaczonej, lecz wyznacz całkę oznaczoną: x^2; od 0 do 1` → `1/3`.
- `Nie obliczaj całki oznaczonej, lecz wyznacz całkę: 2*x` → `x**2 + C`.
- `Nie tylko oblicz pochodną, lecz wyznacz też całkę: x^2` → dwa cele i dwa sprawdzane wyniki.

Niepełne wskazanie „całkę oznaczoną i nieoznaczoną” wymaga doprecyzowania pełnych celów. Nieznane pojęcia, dowolna rozmowa i swobodne wyjaśnianie całych przedmiotów nie są rozstrzygnięte tym sprawdzianem.

Dodatkowo dwa świeże angielskie zadania wykonano od początku w panelu walidatora: **2/2**, z potwierdzonymi dwoma nowymi krokami dla każdego zadania.

## Zapis i odtworzenie

Kopie poprzednich modułów i checkpointów zachowano lokalnie. Starsze niezakwalifikowane eksperymenty pozostają w historii treningów. Nie publikowano kodu ani wag. Paczki portable w tej partii nie zmieniono.
