# TSI — kontekst zdań złożonych, 18 października 2026

Aktualizacja: dodano ograniczony czytnik i odpowiedzi EN. [Aktualny zakres PL/EN](ENGLISH_CONTEXT_2026-10-18.md).


## Działa w zwykłej rozmowie

1. `Przeczytaj: Anna nie ma mapy, ale Piotr ma książkę.`
2. `Czy Anna ma mapę?`

Odpowiedź: zaprzeczenie z cytatem. Obsługiwane są `i`, `oraz`, `ale`, `lecz`, `lub` i jawne `jeśli …, to …` / `jeżeli …, to …`. Każdy człon musi mieć pełny podmiot oraz konstrukcję osoba–ma–przedmiot, ewentualnie z `nie`. Przypadki i lematy pochodzą z istniejącego słownika.

Przykłady kontroli:

| Źródło | Pytanie | Wynik |
|---|---|---|
| Anna ma mapę lub Piotr ma mapę. | Czy Anna ma mapę? | U — żadna możliwość nie została osobno potwierdzona |
| Anna ma mapę lub Piotr ma mapę. Anna nie ma mapy. | Czy Piotr ma mapę? | T — wynika z obu warunków |
| Jeśli Anna ma mapę, to Piotr ma książkę. | Czy Piotr ma książkę? | U — brak potwierdzenia przesłanki |
| Anna ma mapę. Jeśli Anna ma mapę, to Piotr ma książkę. | Czy Piotr ma książkę? | T |
| Anna ma mapę, ale Anna nie ma mapy. Piotr ma książkę. | Czy Anna ma mapę? | U — sprzeczność |
| To samo źródło | Czy Piotr ma książkę? | T — sprzeczność w niezależnej grupie nie usuwa tego faktu |

## Jak to działa

Rozbudowano czytnik, a nie wagi sieci. Gramatyka tworzy drzewo operatorów oraz atomy z rolami. Krótki solver logiczny sprawdza wszystkie wartościowania w każdej połączonej grupie zależności. T/F oznacza zgodność wszystkich dopuszczalnych modeli; U obejmuje brak rozstrzygnięcia lub sprzeczność. Reguły `jeśli` są interpretowane jako formalne implikacje materialne, a nie dowody przyczyn fizycznych. To osobny odczyt warunków źródła; nie zmiana tabel operatorów logiki natywnego rdzenia.

Sprawdzone stany wracają do macierzy ról. Istniejący wytrenowany transformer porównuje je z pytaniem; niezależny audyt kontroluje jego odpowiedź. Zachowano pełne cytaty, fragmenty atomowe i pozycje znaków. Pusta wiedza nie jest zastępowana fikcyjnym faktem: macierz może zawierać wyłącznie maskowany pusty wiersz.

Limity: 6 zdań, 6 różnych par osoba–przedmiot, 12 członów atomowych, głębokość drzewa 4, 2400 znaków. Niepełne człony (`Anna ma mapę i książkę`), zaimki, przyczynowe `ponieważ`, `albo` i mieszanie `i` z `lub` bez jednoznacznego podziału nie są obsługiwane tym modułem. Żaden nierozpoznany człon nie jest w nim pomijany. Pozostaje dotychczasowa obsługa poza tym zakresem.

## Weryfikacja

- Czytnik i reguły: **22/22 testy**.
- Przygotowany wcześniej materiał: **384/384**, w tym wydzielone 240/240, 48/48 i 96/96. To sprawdzenie znanych rodzajów konstrukcji, nie pomiar dowolnej polszczyzny. Wszystkie przewidywania istniejącej sieci zgadzały się z audytem; bez zmiany wag i bez dodatkowego treningu na tym materiale.
- Pełna regresja aplikacji po zmianie: **264/264**.
- Powtórzenie wcześniejszych prób zachowania odpowiedzi: **972/972**, w tym 720 permutacji kolejności tych samych sześciu faktów.
- Próby przez lokalny interfejs HTTP: potwierdzenie, zaprzeczenie, alternatywa i warunek; sesja i cytaty zachowane.

Poprzedni kod: `backups/before-compound-context-2026-10-18`. Raporty: `docs/compound-context-2026-10-18`. Oryginalny materiał do dalszych prac pozostaje w `training/compound-curriculum-next`. Rdzeń H512 i checkpoint transformera nie zostały zmienione. Brak uczenia w tle.
