# TIMDR w języku TSI — 24 października 2026

Dodano aktywną kontrolę tworzenia odpowiedzi. Metoda porównuje znaczenie z macierzą źródła, a następnie może zawęzić dopuszczalne kontynuacje lub poszerzyć poszukiwanie kolejnej propozycji. Jest to badane rozszerzenie językowe TIMDR.

## Co działa

- **Role i negacja:** kontrola wykonawcy, odbiorcy, obiektu i przeczenia względem odczytanych ramek.
- **Dynamika:** stan początkowy → operacja → kolejny stan. Zachowywane są niezależne kopie stanów, role czasu, jednostki i pochodzenie zdarzeń. Zmiana jednej informacji nie nadpisuje innych.
- **Niepewność:** brak danych, niejednoznaczny odczyt lub sprzeczny warunek nie otrzymuje potwierdzenia poprawności.
- **Struktura i rytm:** zmiany długości zdań, powtórzenia, nawiasy i nietypowe serie interpunkcji. Liczby, wzory i długie słowa same w sobie nie są błędami.
- **Łączna ocena:** błąd znaczenia blokuje wysoką ocenę; przy nierozstrzygniętej semantyce wynik łączny pozostaje nieznany. Wynik stylistyczny jest osobną, nieskalibrowaną heurystyką, nie prawdopodobieństwem prawdy.

## TSI korzysta z metody podczas generowania

W aplikacji podłączono kontrolę do istniejącego uczonego generatora kolejności fraz. Sprawdza propozycję wobec macierzy; gdy pierwsze poszukiwanie nie daje poprawnego zdania, rozszerza zakres kolejnych propozycji. Każda musi zachować także przypadki, modyfikatory i warunki sprawdzane przez dotychczasowy czytnik. Wyniki kontroli są dostępne w danych odpowiedzi i śladzie generowania.

W badanym wspólnym modelu językowym kontroler może ograniczyć wybór tokenów do form zgodnych z macierzą. Sieć nadal oblicza oceny i wybiera emitowane tokeny. Kontroler sprawdza gotową odpowiedź ponownie; niezweryfikowana próba poprawy nie zastępuje wcześniejszej odpowiedzi. Wartości dozwolonej wypowiedzi pochodzą z jawnych danych, nie z etykiety testowej.

Przykład dynamiczny: początkowa godzina `10`, operacja `+2`, pytanie o stan po zmianie daje `12`, a pytanie o poprzedni stan — `10`. Przesunięcie `−2` daje `8`. Jawnie zanegowane działanie nie zmienia stanu, nieznane działanie pozostawia wynik nierozstrzygnięty, a niezgodność jednostek blokuje potwierdzenie.

## Wyniki

| Próba | Przed kontrolą | Z kontrolą |
|---|---:|---:|
| Nowe opisy zadań o czasie, z dostarczoną macierzą zdarzeń | 0/16 | **16/16** |
| Wybrane wcześniejsze zadania o czasie, bez podpowiedzi w poleceniu | 3/4 | **4/4** |
| Przesunięcia czasu oraz role i negacja — rzeczywiste generowanie | — | **6/6** |
| Wcześniejsze odpowiedzi poza przekierowaną logiką, ponowna kontrola | — | **105/105 identycznych** |
| Panel HTTP, kontrola porównawcza | — | **8/8 odpowiedzi zachowanych**, 16 żądań |

Sama informacja zwrotna „popraw błąd”, bez ograniczenia generowania macierzą, wcześniej dała **0/8** na części nowych zadań i zachowała **3/4** wcześniejszych. Aktywna kontrola generowania poprawiła wynik badanego systemu. Nie aktualizowano wag.

Dodatkowo przeszło **41 kontroli semantycznych i pętli poprawy**, **9 kontroli struktury** i **8 kontroli przejść stanu**. Pierwszy pomiar rzeczywistego polskiego czytnika dał **5/7**. Późniejsza poprawka odmiany i kontekstu źródła podniosła tę próbę do **7/7**, z 116/116 kontrolami przypisania ról. [Dalsza przebudowa zdań](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/ROZMOWA_I_SKLADNIA_TSI_2026-10-24.md).

## Zakres wdrożenia

Panel korzysta z kontroli uczonego generatora fraz i diagnostyki odpowiedzi. Ograniczanie tokenów dużego modelu oraz jawne macierze dynamiczne sprawdzono w środowisku badawczym. Nowych wag dużego modelu nie podmieniano w panelu, MUZ ani walidatorze. Portable nie przebudowano w tym etapie.

**Wynik 16/16 dotyczy generowania z poprawnie dostarczoną macierzą zdarzeń.** Swobodny odczyt dowolnego opisu oraz automatyczne ustalenie wszystkich jego znaczeń pozostają do rozwinięcia. Sam swobodny dekoder zachowuje dotychczasową ocenę logiki **49/69**; ogólna sprawność językowa nie osiągnęła wymaganego poziomu.
