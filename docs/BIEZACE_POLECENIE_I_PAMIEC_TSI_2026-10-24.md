# Bieżące polecenie i pamięć — 24 października 2026

**Rozdzielenie wejść generatora i enkoderów poprawiło porównawcze rozmowy.** Wariant jest zapisany i uruchamiany lokalnie do dalszych badań. Domyślnego panelu, MUZ, walidatora i portable nie podmieniono.

| Próba | Poprzedni przepływ | Rozdzielone wejścia |
|---|---:|---:|
| Chronione odpowiedzi | 56/56 | 56/56 |
| Porównawcze rozmowy dwóch tur | 1/8 | 8/8 |
| Porównawcze sekwencje trzech tur | 0/8 | 8/8 |

## Jak działa wariant

Oba enkodery nadal otrzymują pełną zachowaną historię razem z bieżącą wiadomością. Generator otrzymuje osobno bieżące polecenie oraz zachowane jawne fakty, a do historii sięga przez uwagę do reprezentacji enkoderów. Nie dokleja całej wcześniejszej rozmowy do własnego prefiksu generowania. Specjalistyczna ścieżka sprawdzania przez macierze TIMDR pozostaje dotychczasowa.

Wagi obu enkoderów i generatora są **dokładnie identyczne** z wcześniejszym wybranym modelem. Nie wykonano tu aktualizacji optymalizatora; poprawa pochodzi ze zmiany przepływu wejść. Nie dodano wyszukiwania gotowej odpowiedzi, nowych aliasów poleceń ani tekstowych zastępników wyniku sieci.

Przykładowa rzeczywista sekwencja:

- „Dzień dobry.” → „Dzień dobry! W czym mogę pomóc?”
- „Napisz jedno zdanie o lesie.” → „W lesie rosną drzewa.”
- „Cześć!” → „Cześć! O czym chcesz porozmawiać?”

Każda kolejna odpowiedź korzystała z rzeczywistych wcześniejszych wypowiedzi tej samej sieci. Kontrola potwierdziła zachowanie historii bez odcinania tur. Porównanie z dodatkowym wariantem, w którym jeden enkoder otrzymywał tylko bieżące polecenie, również dało 8/8 w próbie dwóch tur; wybrano prostszy wariant z pełną historią w obu enkoderach.

## Zakres i dalsza praca

To znane, niezależne od historii polecenia w różnych sekwencjach. Zestawy były wcześniej oceniane; wyniki są porównawcze. Następny etap obejmuje pytania wymagające informacji z wcześniejszych tur oraz nowe sformułowania. Swobodna rozmowa nie osiągnęła wymaganego poziomu.

Dwie poprzedzające rundy wspólnego treningu nie poprawiły odłożonych rozmów: [porównywanie bieżącej i poprzedniej odpowiedzi](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/ODROZNIANIE_POLECENIA_OD_HISTORII_2026-10-24.md) oraz [znaczniki ról i poprawka warstwy słownikowej](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/ROLE_ROZMOWY_I_TRENING_TSI_2026-10-24.md). Ich wag nie przyjęto. Zmiana przepływu korzysta z zachowanych wcześniejszych wag.

Model: **23 542 811 parametrów**, **94.67 MB** wspólnych wag, bez całego portable. Sześć macierzy reguł zachowano. Internetowa pętla uczenia wag pozostaje wyłączona.
