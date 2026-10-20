# Trening czytania źródeł i rozmowy — 21 października 2026

## Zakres

Własny autoregresyjny transformer: 3 warstwy, szerokość 192, 4 głowy, 512 tokenów, 1 826 496 parametrów. Bez zewnętrznych wag. Trening generatora jest osobny od działającego H512. Materiał obejmuje autorskie dialogi i krótkie definicje Wikidata (CC0), z oddzieleniem pojęć między zbiorami. Nie użyto prywatnej historii rozmów ani kopiowanych artykułów MathWorld.

## Wyniki

1002 przykłady treningowe, 60 rozwojowych, 98 testowych. Po 250 krokach strata rozwojowa generatora spadła z 6.971 do 2.591. Na odłożonych danych: fakty 0/18 pełnych odpowiedzi, definicje 0/50, brak informacji 25/25. Poprawny znacznik źródła nie wystarczał: 9/18 i 22/50 odpowiednio. Swobodne odpowiedzi pozostały niewystarczające.

Dodano eksperymentalną uczoną warstwę kopiowania 73 921 parametrów (razem 1 900 417). W wariancie v3, po 300 krokach, strata rozwojowa spadła z 1.311 do 0.532. Jednak swobodne generowanie na sprawdzonych przykładach rozwojowych nadal skracało „Tomasz ma gazetę” do „Tomasz”, myliło definicję algebry z sąsiednim źródłem i powtarzało fragmenty. Ten wariant nie ma jeszcze końcowej oceny odłożonego zbioru; samego spadku straty nie traktujemy jako poprawy rozmowy.

## Decyzja i dalsza praca

Żaden z tych kandydatów nie został wdrożony. Następna kontrola porównuje przewidywanie z podanym poprawnym początkiem odpowiedzi ze swobodnym generowaniem, a także zachowanie osoby, czynności, obiektu i źródła. Warunkiem wdrożenia jest poprawność pełnej odpowiedzi i zachowanie wcześniejszych umiejętności, nie tylko niższa strata treningowa. Aktywny zintegrowany rdzeń pozostaje bez zmian.

## Diagnostyka odpowiedzi swobodnej

Na trzech rozwojowych pytaniach o posiadany przedmiot, przy podawaniu modelowi prawidłowego początku, zgodność kolejnego tokenu wyniosła 84.6%, 88.2% i 93.8%. Pełne odpowiedzi samodzielne: 0/3. Pierwszy błąd zastępował „ma” kropką lub znakiem zapytania. Przy trzech definicjach zgodność tokenów wynosiła 75.8–83.3%, a pełne odpowiedzi 0/3; pojawiały się pomyłki źródła i powtórzenia. To próbki rozwojowe, nie nowy wynik całego testu.

Uruchomiono wariant ograniczający uczoną uwagę kopiującą do dostarczonego materiału, z wyłączeniem treści pytania. Pytanie pozostaje wejściem transformera. Celem jest sprawdzenie, czy kopiowanie znaków z pytania powoduje przedwczesne urywanie faktu. Bez zmiany działającej aplikacji.

## Wynik wariantu v4

300 kroków uczonej uwagi ograniczonej do materiału źródłowego, bez zmiany wag generatora. Strata rozwojowa 1.242 → 0.479. Na tych samych próbkach rozwojowych pełne odpowiedzi o fakty poprawiły się z 0/3 do 1/3; definicje 0/3, brak informacji 3/3, swobodny dialog 0/2. Poprawna odpowiedź: „Zofia ma bilet. [S2]”. Nadal wystąpiły ucięte zdania, uszkodzone słowa, powtórzenia i wybór niewłaściwego źródła. Są to wyniki małej próbki rozwojowej, nie ocena ogólnej trafności.

Wariant v4 również nie został wdrożony. Dalszy etap wymaga poprawy wyboru właściwego źródła i treningu dekodera, z oceną samodzielnie wygenerowanych pełnych odpowiedzi. Trening samej uwagi przy zamrożonym słabym generatorze nie wystarczył. Zbiór odłożony pozostaje poza treningiem.
