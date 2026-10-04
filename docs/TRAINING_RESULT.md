# Adapter Bielika: wynik pilotażu — 2 października 2026

Wytrenowano 77 824 parametry LoRA przy zamrożonej bazie, 20 kroków na 12 przykładach. Zatrzymano dalsze kroki po osiągnięciu zaplanowanego limitu 900 sekund; nie wykonano pełnych 3 epok. To częściowy trening CPU, nie zakończony duży kurs programowania.

| Pomiar | Baza | Adapter |
|---|---:|---:|
| 6 zadań końcowych, tester po dopuszczeniu przecięcia zbiorów | 3/6 | 4/6 |
| 3 dodatkowe zadania sanity, zapisane przed ich porównaniem | 0/3 | 1/3 |
| 3 krótkie kontrole polskiego | 2/3 | 2/3 |

Pierwszy końcowy raport miał 3/6 → 3/6, bo filtr odrzucił poprawne `set(a) & set(b)`. Zachowano go bez zmian. Następnie rozszerzono bezpieczny podzbiór testera o BitAnd i przeliczono TE SAME zapisane odpowiedzi, bez ponownego uczenia. To korekta oceny po obejrzeniu wyników, więc nie przedstawiamy jej jako całkowicie nienaruszonego prerejestrowanego pomiaru. Dodatkowe trzy zadania nie posłużyły do treningu ani zmiany parametrów, lecz pozostają małym autorskim testem, nie zewnętrznym benchmarkiem.

Adapter poprawił generację poprawnego przecięcia list oraz zliczania liczb ujemnych. Nadal zwraca nieprawidłowy kierunek rotacji listy, potrafi zamiast kodu wygenerować pozorne wywołanie funkcji i niekompletne odpowiedzi. Wynik 2/3 prób polskiego dotyczy tylko krótkich oczekiwanych słów, nie ogólnej jakości języka. Nie wykazano szerokiej kompetencji programistycznej, uniwersalnego braku regresji ani przewagi rdzenia TIMDR.

Zapis i ponowny odczyt wag sprawdzono dokładnie. LoRA_B, początkowo zerowe, mają niezerowe normy. Plik bazowy zachował SHA256. Adapter jest przyjęty wyłącznie jako WARIANT EKSPERYMENTALNY, na podstawie małego pilotażu. Lokalny silnik po restarcie może go załadować z chronionego manifestu; stan eksperymentalny pozostaje jawny. Publiczny repozytorium nie zawiera tych wag ani prywatnego rdzenia.

## Rozmiary

- Bazowy Bielik Q8_0: **1 699 568 288 bajtów (1,70 GB)**.
- Adapter używany przez llama.cpp: **312 800 bajtów (~313 KB)**.
- Katalog zapisu treningowego adaptera: **319 716 bajtów**, również poza Git.
- Pełna kopia zdekwantowanych wag NIE została zapisana; istniała tylko w RAM. Próbki RSS po krokach treningowych były rzędu 3,7 GB; to nie pomiar szczytowego zużycia całego systemu.

Prywatne odpowiedzi i szczegółowy raport: artifacts/bielik_coding_adapter/20261002T111414112658Z/report.json (oryginalny), rechecked_report.json (przeliczony), fresh_validation_report.json. Dane pilotażowe i narzędzia testera znajdują się w publicznej części repo. Pozostawiono wszystkie nieudane wyniki.
