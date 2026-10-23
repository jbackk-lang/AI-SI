# Połączenie wyuczonej logiki TSI — 24 października 2026

Naprawiono przekazywanie formalnego zadania do wyuczonej macierzy operatorów. Wcześniej aplikacja obsługiwała krótki zapis `F AND U`, lecz dłuższy opis z tym samym wyrażeniem omijał moduł logiki. Badany generator językowy miał osobną ścieżkę, bez tej macierzy.

Aplikacja korzysta teraz ze wspólnego czytnika wyrażeń i wyuczonego modułu. Badany wariant ma dodatkowo wspólną paczkę wag oraz osobny sposób jej wczytywania, który rzeczywiście wywołuje moduł logiki. Dotychczasowy sposób badania samego dekodera pozostaje dostępny.

| Kontrola | Wynik |
|---|---:|
| Dziewięć bramek, wszystkie wejścia T/F/U | 69/69 |
| Te same zadania, w tym opis z błędną poprzednią odpowiedzią | 138/138 łącznie |
| Wcześniejsze i nowe wyrażenia złożone | 148/148 |
| Wywołania usługi aplikacji PL/EN | 138/138 |
| Pełna obsługa przez HTTP, osobna pamięć testowa | 6/6 |
| Wcześniejsze odpowiedzi poza przekierowaną logiką — identyczna treść i zakończenie | 105/105 |
| Przypadki błędów składni i niejednoznaczności | 7/7 |

Porównanie odpowiedzi wykonano względem zapisu obecnych wag po ostatnim treningu. Dla 105 odpowiedzi sprawdzono każdy token i zakończenie EOS w jednym przebiegu z maską przyczynową; 6 odpowiedzi wygenerowano ponadto lub zamiast tego kolejno od początku. Porównanie nie używa ocen ani odpowiedzi wcześniejszej wersji modelu.

Obsługiwane operatory: BUF, NOT, AND, OR, NAND, NOR, XOR, XNOR/EQUIV, IMPLIES; nawiasy i symbole logiczne. Rozszerzone bramki są składane z wyuczonych operatorów; BUF przekazuje wartość. Parser ustala strukturę wyrażenia, a sieć operatorów oblicza wartości kroków. Podczas tych prób nie korzystano z nauczyciela ani tablicy prawdy do tworzenia odpowiedzi.

Przykład: `Oblicz w logice trójstanowej: F AND U. Moja poprzednia odpowiedź: U. Zweryfikuj ją.` daje **F**. Wskazanie błędnej poprzedniej odpowiedzi nie zastępuje zadania do obliczenia. Przy kilku wyrażeniach, rozpoznanym dodatkowym warunku albo brakującym nawiasie aplikacja prosi o doprecyzowanie.

**Wynik systemu z modułem wynosi 69/69; wynik samego najnowszego dekodera pozostaje 49/69.** To naprawa połączenia, bez nowych aktualizacji wag. Nie zmienia oceny swobodnej rozmowy ani rozumowania o czasie: model językowy nie osiągnął wymaganego poziomu.

Wspólna paczka badawcza zachowuje wagi obu enkoderów, dekodera i 483-parametrowej macierzy operatorów: **23 019 006 parametrów**, **92.57 MB** zapisu bez optymalizatora. Nie zastąpiła przyjętych wag językowych i nie weszła do nowej paczki portable. W lokalnym panelu wdrożono trzy pliki obsługi logiki i zachowano ich kopie; wagi panelu i historia użytkownika pozostały bez zmian.

Zakres odczytu obejmuje formalne wyrażenie wydzielone w poleceniu. Dowolne zdania opisowe, dodatkowe znaczenia językowe i ogólne wnioskowanie wymagają dalszego rozwoju.
