# timderSI (TSI) — aktualny stan na 12 października 2026

TSI to lokalny, uczony system wiążący nazwy z wartościami i wykonujący operacje logiki trójstanowej. Rozwijana warstwa językowa rozpoznaje polskie polecenia oraz ich argumenty. Kod, wagi i bazy pozostają lokalnie; to repozytorium udostępnia dokumentację.

## Budowa i parametry

| Część | Architektura | Parametry |
|---|---|---:|
| Pamięć faktów | wspólny znakowy encoder nazw: dwukierunkowy GRU, szerokość 96; uczona adresowana pamięć klucz–wartość; wyjście trójstanowe | 108 725 |
| Logika | embedding sześciu operatorów i MLP 14 → 64 → 64 → 3 | 5 363 |
| Język poleceń | embedding znaków 32; dwukierunkowy GRU po 64 jednostki; siedem klas operacji i cztery granice argumentów | 42 699 |
| **Wybrany zestaw łącznie** | pamięć + logika + język | **156 787** |

Pamięć przyjmuje do ośmiu jawnych faktów, nazwy do 16 znaków oraz wartości `prawda`, `fałsz`, `nieznane`. Warstwa językowa obsługuje wejście do 160 znaków. Fakty są obecnie podawane jako uporządkowane rekordy; naturalny język służy poleceniu o tych faktach.

Konstruktor wykorzystuje rzeczywisty `TIMDRWorkflow` z TIMDR-AI-Core, z zachowaną wersją źródeł i kontraktem konstrukcji. TSI używa GRU i uczonej pamięci adresowanej. Koordynator TIMDR organizuje konstrukcję i walidację; nie przypisujemy tym warstwom równoważności z fizycznymi operatorami TIMDR.

## Sprawdzone możliwości

| Zakres | Wynik | Co sprawdzono |
|---|---:|---|
| Odczyt wartości z pamięci | **2208/2208** | nowe pełne nazwy, 2–8 faktów, trzy wartości, obie kolejności faktów |
| Rozpoznanie braku podobnej nazwy | **455/480** | pytana nazwa nieobecna, różniąca się znakiem od obecnej |
| Złożenia operatorów na wartościach | **10 000/10 000** | świeże rozgałęzione drzewa głębokości 1–5, wartości dwustanowe i trójstanowe |
| Złożenia na faktach wskazywanych nazwą | **240/240** | nowe nazwy, osiem faktów, cztery operandy; część pytań o brakujący fakt |
| Cały przebieg polskiego polecenia | **251/252** | rozpoznanie polecenia i argumentów, odczyt faktów, odpowiedź; 126 znanych form i 126 nowych połączeń zwrotów |

Uczone operatory: negacja, AND, OR, XOR, implikacja i równoważność, według przyjętej logiki trójstanowej. Brak faktu ma stan `nieznane`; negacja nie zmienia go w `prawda` ani `fałsz`.

Wyniki dotyczą podanych zakresów i syntetycznych testów. Wykluczano pełne testowe nazwy z nauki w świeżych próbach; użyte już testy służą później diagnostyce. Referencyjne reguły logiczne tworzą etykiety treningu i testów. Podczas odpowiadania wynik obliczają uczone moduły neuronowe.

## Aktualne ograniczenia języka

Test 251/252 obejmował wąski zakres sformułowań. Szerszy test sześciu form i czterech rodzin nazw ujawnił nadal istotne braki:

| Rodzina nazw | Dokładne rozpoznanie operacji i argumentów | Poprawna odpowiedź |
|---|---:|---:|
| Pojedyncze litery `E`, `F` | 18/378 | 77/378 |
| Podobne nazwy numerowane | 306/378 | 299/378 |
| Polskie nazwy z diakrytyką | 108/378 | 190/378 |
| Polskie nazwy różnej długości | 135/378 | 179/378 |

Poprawna odpowiedź bez poprawnego rozpoznania polecenia może być przypadkowa. Dlatego oba pomiary są raportowane osobno. Warstwa językowa nadal wymaga nauki krótkich nazw, polskich słów i przenoszenia między sformułowaniami. Nie deklarujemy rozumienia dowolnych zdań, swobodnej rozmowy ani zagnieżdżonych poleceń w języku naturalnym. Nie ma jeszcze pełnego uczonego wyboru wielu modułów i oceny ich wyników.

## Ochrona wiedzy i stan prac

Podczas nauki języka pamięć faktów i logika pozostają zamrożone. Ich niezmienione pliki wag potwierdzono sumami SHA-256. Każdy krok treningu jest zapisywany wraz ze stanem optymalizatora i generatorów losowych. Najlepsze wersje są przechowywane osobno; pogarszające się próby nie zastępują ich.

Wariant logiki z 16 wymiarami pamięci pośredniej jest zbudowany i zachowany. W sprawdzonych złożeniach nie wykazał przewagi poprawności nad mniejszym modułem. Nowa wiedza i kolejne moduły mają być weryfikowane przed utrwaleniem w chronionej pamięci.

TSI pozostaje kandydatem lokalnym w rozwoju. Dotychczasowa aplikacja SI i jej starsze wagi są zachowane osobno. Trwa dalsza nauka i monitoring; uruchomienie procesu nie oznacza gotowości całego systemu.

## Możliwe zastosowania po walidacji

Najbliższy zakres zastosowań to lokalna pamięć nazwanych faktów, kontrola reguł z jawnym stanem niepewności oraz niewielki uczony kontroler współpracujący z osobnymi modułami. Testy nie potwierdzają jeszcze niezawodności produkcyjnej ani zastosowań wymagających wysokiej pewności.

## Historia

[Historia procedur, pomiarów i zmian](HISTORIA_SI_2026-10-11.md) pozostaje osobnym dokumentem. README przedstawia aktualny stan i potwierdzone wyniki; wcześniejsze modele oraz przerwane eksperymenty nie są bieżącymi możliwościami TSI.

