# SI: własny język i pamięć — 5 października 2026

## Co wdrożono

Własny mały GPT oparty na implementacji nanoGPT oraz trenowany klasyfikator tematu, bez wywoływania Qwena w nowej rozmowie. Obecny trening obejmuje wyłącznie angielski. Wdrożony wariant uzyskał 18/18 odpowiedzi na ograniczonym zestawie nowych pytań; zakres obejmuje dziewięć tematów i z góry określone znaczenia odpowiedzi, nie ogólne rozumienie języka.

Do interfejsu podłączono historię bieżącej rozmowy oraz jawny regułowy kontroler ostatniego pewnie rozpoznanego tematu. Proste odwołania it/its/this/that korzystają z tematu; pusta historia powoduje prośbę o doprecyzowanie. Niepewna wiadomość nie kasuje poprzedniego tematu. Kontrola wykonawcza: 9/9, obejmująca sześć tematów, pustą historię, niepewną wiadomość i zmianę tematu. Potwierdzono przesyłanie historii przez działające API. To pomoc programowa, nie wyuczona ogólna zdolność rozwiązywania odniesień. Wagi nie zmieniły się przy dodaniu pamięci.

Nowy widok ma rozmowę z własnym SI i osobną ocenę polecenia. Dawne opcje usunięto z tego widoku; nie oznacza to usunięcia wszystkich historycznych plików. Kolejka automatycznego czytania pozostaje wstrzymana.

## Rozwój i testy kolejnych wag

| Wariant | Nowe pytania: poprawne | Poprawne ponad progiem pewności |
|---|---:|---:|
| Osobna sieć rodzaju pytania | 15/20 | 7/20 |
| Trzy niezależne sieci | 10/20 | 6/20 |
| Dalszy trening angielskiego kontekstu | 20/26 | 20/26 |

Każdy wiersz dotyczy innego zestawu, więc nie jest to bezpośrednie porównanie jakości. W ostatnim treningu poprzednio obejrzane pytania wykorzystano jako dane rozwojowe i oceniono osobny, zapisany przed treningiem zestaw. Zachowano 18/18 rozpoznań wcześniejszych tematów. Pytania dzielą szablony pomiędzy tematami; 26 przypadków nie stanowi 26 niezależnych typów problemów. Testy te przekazują poprzedni temat jako dane i nie zastępują pełnej rozmowy wieloturowej.

Nowych kandydatów nie wdrożono. Pozostaje sześć błędów w ostatniej próbie, a pamięć regułowa nie dowodzi naprawy błędów w wagach. Ostatni kandydat: 1 050 862 parametrów, 4 216 773 bajty wag. Wdrożone GPT i klasyfikator: 854 537 parametrów, 4 754 288 bajtów checkpointów. Różne struktury zapisów wyjaśniają różnicę rozmiaru. Nie są to liczby neuronów ani rozmiary całego systemu.

Dodano diagnostyczny odczyt kanałów Lambda/tau/rho/J ze stanów własnego GPT. To eksperymentalne mapowanie, nie potwierdzony walidator poprawności; sprawdzono skończoność odczytów i zgodność tekstu z obserwacją i bez niej.

## Kiedy polski

Następny etap to zamrożony test angielskich rozmów wieloturowych: utrzymanie i zmiana tematu, brak kontekstu oraz niejednoznaczność. Polski można następnie wprowadzić pilotażowo na osobnych danych i ocenić wpływ na angielski. Nie ustalono terminu ani gwarancji opanowania języka. Obecnie nie trenujemy polskich przykładów.

Kod rdzenia, wagi, checkpointy, pamięć, logi rozmów i prywatne ścieżki pozostają poza tym zapisem. Dokumentacja nie udostępnia samodzielnego modelu ani nie dowodzi ogólnego samouczenia.
