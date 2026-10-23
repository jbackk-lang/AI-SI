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

## 23 października 2026 — dalsze utrwalanie po pięciu etapach

Trening kontynuowano z ostatnich wytrenowanych wag, z mniejszym tempem aktualizacji. Co krok powracano do utraconych odpowiedzi, a zestaw ochronny rozszerzono ze 109 do **117**: dodano osiem nowych poprawnych przypadków. Starsze parametry pozostały zamrożone; uczyły się dodane warstwy.

| Aktualizacje | Zachowane ze 117 | Zachowane z pierwotnych 109 | Logika | Znane godziny |
|---|---:|---:|---:|---:|
| 8 | 106/117 | 104/109 | 44/69 | 15/40 |
| 16 | 109/117 | 107/109 | 46/69 | 15/40 |

Nowe opisy czasu, nieużywane w treningu tej serii: **0/16**. Wynik końcowy T/F/U: **T 20/23**, **F 0/19**, **U 26/27**.

Zachowano wcześniejszy przyjęty zapis; kolejne wytrenowane wagi pozostają materiałem do dalszych badań. Panel, MUZ i walidator nie zostały podmienione. Internetowy trening wag pozostaje wyłączony. **Nie osiągnął wymaganego poziomu.**

## 23 października 2026 — równy udział stanów w całych powtórkach

Audyt poprzedniej serii wykazał nierówny udział stanów po dodaniu materiału ochronnego: **T 46, F 22, U 65** ekspozycji logicznych. Wyrównano cały dobór przykładów, łącznie z powtórkami. Kolejne osiem aktualizacji zawierało dokładnie **T 32, F 32, U 32** ekspozycje. Liczby potwierdzono z faktycznie użytych partii.

Po dodatkowym treningu: **109/118** zachowanych odpowiedzi, w tym **100/109** z pierwotnego zestawu i **48/48** podstawowych. Logika **51/69**; T **16/23**, F **12/19**, U **23/27**. Znane godziny **15/40**, nowe opisy **0/16**.

Najnowszy zapis zachowano do dalszych badań, bez zastąpienia wcześniejszych przyjętych wag. **Nie osiągnął wymaganego poziomu.** Bez podmiany panelu, MUZ i walidatora.

