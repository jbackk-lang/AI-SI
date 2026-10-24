# Bieżące polecenie i historia — 24 października 2026

**Zachowano poprzedni model badawczy; wynik nie uzasadnia podmiany.**

| Próba | Przed | Po |
|---|---:|---:|
| Chronione odpowiedzi | 56/56 | 56/56 |
| Uczone rozmowy | 8/56 | 9/56 |
| Odłożone kombinacje dwóch tur | 1/8 | 1/8 |
| Dodatkowe rozmowy trzech tur | 0/8 | 0/8 |

Pomiar przed treningiem: w 14 z 56 ćwiczonych kontekstów pierwszy token odpowiedzi odpowiadał poprzedniej odpowiedzi zamiast bieżącej. Poprawnie zaczynały się 23/56 odpowiedzi; w całości poprawnych było 8/56.

Wspólnie uczono oba enkodery, ich pamięci H512 i cały generator. Dla obsługiwanych, niezależnych od historii poleceń zestawiono odpowiedź z historią z poprawną odpowiedzią tej samej sieci bez historii. Dodatkowy składnik błędu rozróżniał bieżącą odpowiedź i odpowiedź z poprzedniej tury w pierwszym miejscu, gdzie ich tokeny się różniły. Nie dodano tabeli gotowych odpowiedzi w panelu ani wyszukiwania odpowiedzi podczas rozmowy.

Materiał podawano równomiernie według bieżących poleceń. Zachowano powtórki wcześniejszych odpowiedzi i zamrożenie sześciu macierzy reguł. Cofnięcie obejmowało oba enkodery, generator oraz stan optymalizatora; po cofnięciu zmniejszano krok uczenia. Liczba odrzuconych serii: **3**. Wykonano **30** głównych aktualizacji; wybrano zapis po **25**.

Osiem dodatkowych rozmów trzech tur ustalono przed zakończeniem treningu. Używają znanych sformułowań w nowych sekwencjach; nie sprawdzają nowego słownictwa. Historia zawiera rzeczywiste odpowiedzi modelu, również błędne; nie podmieniano ich na odpowiedzi nauczyciela. Obu prób końcowych nie używano do aktualizacji wag ani wyboru kroku wewnątrz tej rundy. Zestaw dwóch tur był już oceniany we wcześniejszych rundach, więc jest próbą porównawczą.

Model ma **23 542 811 parametrów**. Wybrany plik wag: **94.67 MB**, bez całego środowiska portable. Swobodna rozmowa nie osiągnęła wymaganego poziomu. Aplikacji, MUZ, walidatora i portable nie podmieniono. Internetowa pętla uczenia wag pozostaje wyłączona.
