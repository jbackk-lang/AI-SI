# Rozbudowa modelu i powtórki


## 23 października 2026 — większy model i pięć etapów powtórek

Model rozszerzono z 14 853 139 do **23 018 523 parametrów**, a dekoder z 4 do **12 warstw**. Przy samym rozszerzeniu 98/98 wcześniejszych odpowiedzi i ich logity pozostały identyczne.

Następnie odtworzono pięć zapisanych programów nauczania w kolejności od najstarszego do najnowszego. Powtarzano poprawne etykiety, a nie wcześniejsze błędne wypowiedzi sieci. Oryginalne enkodery i cztery warstwy dekodera były zamrożone; uczyło się osiem dodanych warstw.

| Etap | Aktualizacje łącznie | Zachowane odpowiedzi | Logika ze źródłem |
|---|---:|---:|---:|
| 1/5 | 16 | 107/109 | 45/69 |
| 2/5 | 26 | 106/109 | 45/69 |
| 3/5 | 42 | 104/109 | 45/69 |
| 4/5 | 50 | 105/109 | 48/69 |
| 5/5 | 60 | 102/109 | 46/69 |

Końcowa próba: znane opisy czasu **15/40**, nowe opisy bez podpowiedzi **0/16**. Znany zestaw 40 przykładów był materiałem powtórek. Zestaw nowych opisów nie był materiałem treningu tego eksperymentu.

Nie przyjęto nowych wag: zachowano zapis sprzed powtórek.

**Nie osiągnął wymaganego poziomu.** Model badany nie został wdrożony do panelu, MUZ ani walidatora. Internetowy trening wag pozostaje wyłączony.
