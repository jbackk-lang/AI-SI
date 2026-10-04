# Zamknięcie etapu: generalizacja i uporządkowane przebiegi SI

4 października 2026 r.

## Wykonane zmiany

Wdrożono ograniczony parser poleceń „najpierw … potem … następnie …” oraz „first … then … next …”. Obsługuje dwa lub trzy kroki wśród czterech operacji na listach: łączenie podlist, usuwanie powtórzeń z zachowaniem kolejności, zliczanie wystąpień i podział na grupy. Parser odczytuje kolejność, a własny wytrenowany adapter SI rozpoznaje operacje poszczególnych kroków.

Wynik poprzedniego kroku stanowi wejście następnego. Operacje przetwarzają dane w pamięci; nie zmieniają plików ani innych zasobów. Jeżeli krok jest zakazany, niejasny lub otrzymuje nieobsługiwany typ danych, cały przebieg zwraca wstrzymanie bez wyniku częściowego. Kroki wcześniejsze mogą zostać obliczone w pamięci podczas sprawdzania przebiegu.

Poprawiono również dwie wąskie reguły zakresu polecenia: ograniczenie „nie przestawiając elementów” przy zachowaniu pierwszych wystąpień oraz dopuszczenie pustych podlist przy łączeniu. Rzeczywiste zakazy i nierozstrzygnięte warunki pozostają blokowane. Nie zmieniano wag podczas tych prac.

## Zapisane wyniki

| Próba | Wynik | Co sprawdzono |
|---|---:|---|
| Nowe sformułowania i dane na zamrożonych wagach | 21/24 | Pierwsza ocena nowych tekstów: 13/16 działań oraz 8/8 wstrzymań, bez Qwena i bez treningu. |
| Zakres negacji i obsługa pustych podlist | 4/4 | Dwa poprawne wykonania i dwa poprawne wstrzymania po korekcie reguł. |
| Pierwsze przebiegi dwukrokowe | 5/5 | Trzy wykonania i dwa wstrzymania, w tym polskie i angielskie polecenia. |
| Nowe kombinacje dwóch działań | 8/8 | Sześć wykonań i dwa wstrzymania dla niezgodnego wyniku pośredniego. |
| Przebiegi trzyetapowe | 6/6 | Cztery wykonania i dwa wstrzymania przy niejasnym lub zakazanym końcowym kroku. |
| Kontrola wcześniejszych zadań po poprawce reguł i integracji dwóch kroków | 121/121 | Zapisany zestaw rozwojowy, bez treningu i Qwena. |
| Kontrola poprzednich przebiegów po dodaniu trzeciego kroku | 5/5 | Ponownie sprawdzono wcześniejsze próby dwukrokowe. |

W teście generalizacji trzy jasne polecenia zostały wstrzymane: jedno przez sieć, dwa przez zbyt szerokie reguły warunków i negacji. Następnie poprawiono zakres tych reguł. Nie przypisujemy początkowemu testowi nowego wyniku 24/24: po obejrzeniu wyników ten zestaw staje się materiałem rozwojowym, a nie kolejnym niezależnym holdoutem.

Próby są małe, przygotowane przez autora prac i częściowo ponawiane. Nie należy sumować ich jako jednego niezależnego benchmarku. Wyniki dotyczą ograniczonego języka poleceń i operacji na listach; nie sprawdzają ogólnego planowania ani całej współpracy modułów.

## Przykład działającego przebiegu

Polecenie: „Najpierw spłaszcz listę list, potem usuń powtórzenia bez zmiany kolejności, następnie podziel listę na grupy po dwa”.

Wejście: `[[3,1],[3,2],[4,1]]`.

Przebieg: `[3,1,3,2,4,1]` → `[3,1,2,4]` → `[[3,1],[2,4]]`.

Odwrócenie kolejności może zmienić zgodność typów: „usuń powtórzenia → zlicz” działa, natomiast „zlicz → usuń powtórzenia” zostaje wstrzymane, ponieważ obecna operacja usuwania powtórzeń nie obsługuje rekordów zliczeń.

## Stan etapu

Etap poprawiania adaptera oraz dodawania przebiegów do trzech kroków zamknięto. SI jest narzędziem do pracy w opisanym zakresie. Dalsze poprawki mają wynikać z konkretnych problemów podczas używania, a nie z ciągłego rozszerzania liczby kroków.

Własne wagi adaptera są trwale zapisane i mogą być trenowane przez lokalny mechanizm z oceną regresji. W przeprowadzonych pracach diagnozę oraz przykłady przygotowywał autor, a trening, ocena i warunkowa podmiana wykonywały się automatycznie. Nie wykazano jeszcze samodzielnego doboru całej nauki przez SI. Parser kolejności, reguły ochronne i deterministyczne operacje są odrębne od sieci.

## Publikacja

Dokument opisuje prace i wyniki. Prywatny kod SI/TIMDR, wagi, checkpointy, pamięć i prywatne ścieżki pozostają poza publicznym repozytorium.
