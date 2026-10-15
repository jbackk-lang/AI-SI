# timderSI (TSI) — aktualny stan projektu

Dokumentacja z 15 października 2026, oparta na ostatnim potwierdzonym stanie z 14 października. Nie wykonano nowych pomiarów modeli 15 października.

TSI jest lokalnym, eksperymentalnym systemem z uczonym rdzeniem wektorowym, chronioną pamięcią i logiką trójstanową oraz modułami poleceń i relacji. Ma wykonawcę jawnych programów wielokrokowych i pierwszy adapter do walidatora matematycznego. Repozytorium publikuje dokumentację; kod, wagi, dane i surowe wyniki pozostają lokalne.

**Praca została zatrzymana na polecenie użytkownika. Automatyzacja ma ostatni zapisany status PAUSED. Cała TSI nie została uznana za gotową.** Raport końcowy odnotowuje brak aktywnego treningu i serwera TSI na porcie 8791. Wybrana wersja wag nie oznacza uruchomionego procesu.

## Obecna budowa

Rdzeń ma szerokość 256, 670 250 parametrów i wybrany checkpoint 10150. Operuje na wektorach 96-elementowych. Sześć przybliżonych operacji to wydłużenie, skrócenie, suma, różnica, środek i przesunięcie cykliczne. Pamięć i logika trójstanowa pozostają chronione przy dołączaniu modułów.

| Wybrany moduł | Parametry | Checkpoint |
|---|---:|---:|
| Rdzeń wektorowy | 670 250 | 10150 |
| Relacja długości | 3 328 | 120 |
| Kompozycja relacji długości | 18 980 | 100 |
| Odczyt ról | 96 | 100 |
| Angielskie polecenia | 14 102 | 200 |
| Kolejność argumentów odejmowania | 13 842 | 100 |
| Relacja kierunku | 3 328 | 100 |

Tabela podaje parametry poszczególnych modułów według identyfikatorów rejestru, bez deklarowania sumy całego systemu.

## Działające możliwości

| Możliwość | Zapisany wynik | Zakres sprawdzenia |
|---|---:|---|
| Relacja długości | 600/600 | nowe pary w ustalonym zakresie; zera oraz skale 0,001 i 4 |
| Relacja kierunku | 800/800 | osobny generator o określonym zakresie |
| Kompozycja relacji długości | 800/800 | osobny test jakościowych relacji |
| Wybór według roli | 900/900 | jawna rola obiektu, operacji lub relacji; rekonstrukcja wektora przybliżona |
| Angielskie polecenia sześciu operacji | 72/72 | odłożone kombinacje znanych słów |
| Kolejność argumentów odejmowania | 36/36 | osobny jawny kontekst zadania |

Zintegrowano przepływ polecenie → role → operacja → relacje. Lokalny wykonawca przyjmuje jawne wektory i listę kroków; wynik kroku może zasilać kolejny. Wykonano przykład suma → skrócenie → odwrócone odejmowanie. Nazwane wyniki stanowią pamięć wykonania zadania, a nie nową wyuczoną pamięć rdzenia.

Pierwszy adapter do **math-validator-3.0** rozwiązał `2*x−4=0`, otrzymał `x=2` i sprawdził podstawienie z resztą zero. Zapisano wykres oraz dziennik zadania. Adapter korzysta z rzeczywistego walidatora. Wybór narzędzia jest jawnie określony w zadaniu; uczone zarządzanie narzędziami nie jest wdrożone. Poprawne podstawienie nie stanowi ogólnego dowodu kompletności rozwiązania.

## Aktualne ograniczenia

Wyniki osobnych modułów nie gwarantują poprawności całego przepływu. W diagnozie 192 rzeczywistych wyników operacji poprawne były **149/192 relacje długości** i **173/192 relacje kierunku**. Problemy obejmują przesunięcie cykliczne i granice kategorii. Zintegrowane relacje są oznaczone jako niezweryfikowane estymaty; dostępne są także rzeczywiste długości i względna zmiana długości.

Obliczenia wektorowe są przybliżone. Nieznane polecenie może zostać przypisane do jednej ze znanych operacji. Nie ma ogólnego czatu, swobodnego parsowania programów, wyuczonego zarządzania narzędziami ani potwierdzonej dokładności relacji przy granicach kategorii. Wyniki na generatorach nie stanowią potwierdzenia niezawodności produkcyjnej.

## Docelowa rola i pozostałe prace

TSI ma zarządzać zadaniami matematycznymi z wykresami oraz współpracować z **math-validator-3.0**, **TIMeDR-MUZ** i **TIMDR-Industrial-Predict**. Pierwszy adapter matematyczny działa; MUZ i Industrial-Predict nie są podłączone.

Po wznowieniu pozostaje integracja rzeczywistych interfejsów, zebranie konkretnych zadań oraz nauka wyboru modułu i strategii. Relacje graniczne wymagają ustalonego kontraktu rozdzielczości. Gotowość należy sprawdzać na całych zadaniach z ochroną wcześniejszych poprawnych zachowań.

## Zasoby i historia

Rejestr obejmuje **467 plików modeli i kopii** oraz **168 plików danych**. Liczba plików nie oznacza liczby niezależnych modułów aktywnego systemu. Zachowano źródła, wybrane wersje, punkty zwrotne i kopie cofnięcia.

[Historia badań, wcześniejsze wersje i raport stanu z 14 października](HISTORIA_SI_2026-10-11.md).

Opis oparto na lokalnym raporcie końcowym, rejestrze modeli i zapisanym wyniku zadania matematycznego. Aktualizacja dokumentacji nie wznawia treningu ani serwera.
