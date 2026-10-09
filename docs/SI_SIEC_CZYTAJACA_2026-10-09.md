# Sieć czytająca SI — 9 października 2026

## Po co

Wyuczone wzorce (np. „( [DATA] –”, „ur. [DATA]”) czytają tylko zapisy, które SI już zna. Gdy zdanie jest zbudowane inaczej, wzorzec milczy. Sieć czytająca uzupełnia wzorce bez Qwena: sama ocenia, który zapis daty albo liczby w artykule odpowiada na pytanie.

## Jak się uczy

- **Nauczyciel:** Wikidane jako sędzia. Każde hasło z pamięci podręcznej nauki daje przykład: pytanie o fakt, zdania artykułu, wszystkie zapisy dat lub liczb (kandydaci) i informacja, który kandydat zgadza się z Wikidanymi. Gdy żaden się nie zgadza, poprawną odpowiedzią jest „nie ma tu odpowiedzi”.
- **Cechy:** słowa wokół kandydata (do 6 z każdej strony), ich połączenie z rodzajem pytania, kształt zapisu (pełna data, miesiąc i rok, sam rok, liczba), numer zdania, obecność słowa pytania w zdaniu. Cechy są haszowane do 2^20 kubełków.
- **Sieć:** suma wektorów cech → ReLU → wynik dla każdego kandydata i osobny wynik „brak odpowiedzi”; softmax po kandydatach jednego pytania.
- **Automat rośnięcia:** start od 8 neuronów ukrytych, potem 16 itd.; większa sieć zostaje tylko wtedy, gdy podnosi trafność na walidacji o więcej niż 0,5 punktu. Zatrzymał się na 8 — większa nie czytała lepiej.
- **Próg pewności:** wybrany na walidacji tak, by błędnych odczytów było nie więcej niż 1% (0,92).
- **Rozmiar:** zostają tylko cechy widziane co najmniej 25 razy, zapisane w połowie precyzji — 1,5 MB.
- Zamrożone hasła testowe nie były używane do uczenia ani do wyboru progu.

## Gdzie działa

Tylko tam, gdzie wzorce nie znalazły odpowiedzi, i tylko powyżej progu: w pętli nauki z Wikipedii i przy pytaniach o fakty w czacie. Odpowiedź sieci jest nadal jednym źródłem — potwierdzenie wymaga zgody z drugim źródłem (Wikidane). Bez modelu albo bez biblioteki torch SI działa jak wcześniej.

## Wyniki

| Test | Same wzorce | Wzorce + sieć |
|---|---|---|
| Zamrożone hasła angielskie (215 pytań): poprawnie | 83 | 91 |
| … błędy czytania | 0 | 0 |
| Zamrożony test pytań w czacie, angielski (126): potwierdzone | 68 | 76 |
| Zamrożony test pytań w czacie, polski (126): potwierdzone | 70 | 78 |
| … „źródła różne” (en / pl) | 5 / 5 | 5 / 5 |

Nowe potwierdzenia: głównie daty urodzenia i śmierci zapisane w nietypowych zdaniach oraz daty założenia.

## Czego jeszcze nie ma

- Model tylko dla angielskiej Wikipedii; polskiego jeszcze nie uczyłam.
- Sieć nie douczy się sama z nowych sprawdzeń — na razie uczona raz.
