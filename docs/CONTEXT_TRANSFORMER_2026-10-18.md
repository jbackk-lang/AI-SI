# Transformer kontekstu TSI — 18 października 2026

## Stan wdrożenia

W zwykłej rozmowie działa dodatkowy uczony transformer kontekstu: **266 391 parametrów, szerokość 128, 4 głowy uwagi, 2 warstwy**. Dotychczasowy rdzeń H512 / 2 054 186 parametrów pozostaje aktywny. To rozszerzenie, nie pełna wymiana rdzenia i nie generator swobodnej prozy.

Przykład dwóch kolejnych wiadomości:

1. `Przeczytaj: Marek nie ma samochodu. Anna ma mapę.`
2. `Czy Marek ma samochód?`

Odpowiedź rozróżnia T (potwierdzenie), F (zaprzeczenie) i U (brak lub sprzeczność), zachowuje cytaty. Szczegóły zawierają przewidywanie sieci, niezależny audyt i ślad diagnostyczny. Nowe imiona i przedmioty korzystają ze słownika odmiany, nie z listy słów treningowych.

## Architektura i granice

Adapter przyjmuje 1–6 prostych zdań w kolejności osoba–ma–przedmiot oraz pytanie „Czy osoba ma przedmiot?”. Osoba jest rozpoznanym imieniem/nazwiskiem w mianowniku liczby pojedynczej; przedmiot rzeczownikiem w bierniku, przy negacji w dopełniaczu. Nie rozstrzyga tożsamości osób o jednakowym imieniu. Koniunkcje, zdania złożone, modalność, przestawny szyk i dodatkowe warunki nie są po cichu pomijane: nowy moduł odstępuje, pozostawiając dotychczasową obsługę.

Wejście sieci to macierz czterech jawnych kanałów: zgodność osoby z pytaniem, zgodność przedmiotu, twierdzenie, przeczenie. Zgodność i odmianę podaje adapter; sieć uczy się agregacji i rozstrzygnięcia. Nie jest to wynik samodzielnego odczytu dowolnego języka. Zachowano polskie znaki w lematach.

Encoder ma kodowanie pozycji, maskę dopełnienia, opcjonalną maskę przyczynową i zachowany gradient. Ślad jest osobny dla żądania. Diagnostyka mierzy zmiany wektorów przed końcową normalizacją. Jej próg nie jest skalibrowanym detektorem błędu rozumowania; status jest eksploracyjny. Projekcja META nie była trenowana i nie wyznacza faz stabilna/krytyczna. G i K nie zostały dopisane jako pozorne implementacje.

## Trening i weryfikacja

- Syntetyczne dane: 2400 treningowych, 320 walidacyjnych i 640 odłożonych; bez danych prywatnych.
- Odczyt tokenów: **306/640**, kandydat odrzucony.
- Macierz ról: **640/640**; wybrano krok 50 na walidacji. Nowe połączenia osób i przedmiotów, wspólne słownictwo i struktura; możliwe powtórzenia struktur macierzy między zbiorami.
- Dodatkowy losowy stres: **512/512** poprawnych przewidywań sieci, 0 przejść na audyt.
- Końcowe testy techniczne i adaptera: **33**, błędy: 0 + 0.
- Regresja zmienionej rozmowy, pytań, składania zdań i pomocy: **65**, błędy: 0 + 0.
- Pełna regresja poprzedniego stanu: 237/238. Jeden przypadek sprawdzania warunków nie zwrócił śladu wyprowadzenia; osobne powtórzenie po zakończeniu treningu przeszło 1/1. Przyczyna pierwszego niepowodzenia nie została jednoznacznie ustalona. Nie przedstawiamy tego przebiegu jako 238/238.

Wynik jest dowodem działania w tym ograniczonym zadaniu, nie dowodem ogólnego rozumienia języka ani walidacją całego formalizmu TIMDR. Audyt potrafi powstrzymać celowo błędne przewidywanie modelu. Czytanie zdań złożonych i generowanie pozostają następnymi zadaniami.

Dodatkowe sprawdzenie po wdrożeniu: **972/972 prób** — 252 przypadki z nowymi słowami, zmienioną osobą, negacją, powtórzeniami i sprzecznościami oraz wszystkie **720 kolejności sześciu faktów**. Permutacje sprawdzają odporność na kolejność, nie stanowią 720 niezależnych zadań językowych. Wagi nie były zmieniane.

## Pojemność i powrót

Zachowano politykę zwiększania pojemności przy powtarzalnym zapominaniu. Nie mylimy braku nowej umiejętności z utratą starej. Konfiguracja umożliwia większe warianty, w tym 512/8 głów/6 warstw/FFN 2048; ten duży wariant nie został wytrenowany. Nie ma automatycznego uczenia podczas używania.

Poprzedni kod zachowano w `backups/before-context-transformer-2026-10-18`. Manifest wymienia zmienione i dodane pliki. Wagi starego rdzenia i pamięć użytkownika nie zostały zmienione. Raporty, dane syntetyczne, skrypty i oba checkpointy są w `training/context-transformer-2026-10-18`.
