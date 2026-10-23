# Utrwalanie TSI — 24 października 2026


## 24 października 2026 — utrwalanie odczytu źródła

Wykonano osiem aktualizacji od ostatnich wytrenowanych wag. Utrzymano równą liczbę ekspozycji logicznych wraz z powtórkami: **T 32, F 32, U 32**. Uczenie uwagi na właściwy wynik ze źródła objęło również materiał ochronny. Zmniejszono tempo aktualizacji i powtarzano utracone fakty. Enkodery i cztery starsze warstwy dekodera pozostały zamrożone; trenowano osiem dodanych warstw.

Kontrola zapisanych i ponownie wczytanych wag: **113/124** zachowanych odpowiedzi, **104/109** z pierwotnego zestawu, **48/48** podstawowych. Logika **49/69**, znane godziny **16/40**, nowe opisy czasu **0/16**.

Rozkład logiki: **T 16/23**, **F 7/19**, **U 26/27**.

Sprawdzono hipotezę o wymuszaniu dwóch stanów na aktywnej ścieżce: T/F/U mają osobne tokeny w obu tokenizerach, ich reprezentacje w obu enkoderach są różne, a dekoder wybiera z pełnego słownika. Niezależnie zweryfikowano 69 wyników tablic reguł. Nie stwierdzono twardej zamiany U na T/F w tych punktach. Błędne odpowiedzi dla oczekiwanego F: osiem T i cztery U; dla oczekiwanego U: jedno T.

Zachowano nowe wagi do dalszych badań; przyjęty wcześniej zapis pozostaje bez zmian. **Nie osiągnął wymaganego poziomu.** Bez wdrożenia nowych wag do panelu, MUZ i walidatora. Trening internetowy pozostaje wyłączony.
