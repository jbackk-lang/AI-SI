# Trening czytania źródeł i rozmowy — 21 października 2026

## Zakres

Własny autoregresyjny transformer: 3 warstwy, szerokość 192, 4 głowy, 512 tokenów, 1 826 496 parametrów. Bez zewnętrznych wag. Trening generatora jest osobny od działającego H512. Materiał obejmuje autorskie dialogi i krótkie definicje Wikidata (CC0), z oddzieleniem pojęć między zbiorami. Nie użyto prywatnej historii rozmów ani kopiowanych artykułów MathWorld.

## Wyniki

1002 przykłady treningowe, 60 rozwojowych, 98 testowych. Po 250 krokach strata rozwojowa generatora spadła z 6.971 do 2.591. Na odłożonych danych: fakty 0/18 pełnych odpowiedzi, definicje 0/50, brak informacji 25/25. Poprawny znacznik źródła nie wystarczał: 9/18 i 22/50 odpowiednio. Swobodne odpowiedzi pozostały niewystarczające.

Dodano eksperymentalną uczoną warstwę kopiowania 73 921 parametrów (razem 1 900 417). W wariancie v3, po 300 krokach, strata rozwojowa spadła z 1.311 do 0.532. Jednak swobodne generowanie na sprawdzonych przykładach rozwojowych nadal skracało „Tomasz ma gazetę” do „Tomasz”, myliło definicję algebry z sąsiednim źródłem i powtarzało fragmenty. Ten wariant nie ma jeszcze końcowej oceny odłożonego zbioru; samego spadku straty nie traktujemy jako poprawy rozmowy.

## Decyzja i dalsza praca

Żaden z tych kandydatów nie został wdrożony. Następna kontrola porównuje przewidywanie z podanym poprawnym początkiem odpowiedzi ze swobodnym generowaniem, a także zachowanie osoby, czynności, obiektu i źródła. Warunkiem wdrożenia jest poprawność pełnej odpowiedzi i zachowanie wcześniejszych umiejętności, nie tylko niższa strata treningowa. Aktywny zintegrowany rdzeń pozostaje bez zmian.
