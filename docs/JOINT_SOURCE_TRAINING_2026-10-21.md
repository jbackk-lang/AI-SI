# Wspólny trening i przepływ informacji — 21 października 2026

Własny generator i wybór źródła uczono wspólnie: 1 974 338 parametrów, 300 kroków, wybrano krok 275 według zbioru rozwojowego. Wszystkie wagi dekodera były uczone. Aktywny H512 nie był zmieniany. Kandydat nie został wdrożony.

| Zestaw | Fakty — pełna odpowiedź | Definicje — pełna odpowiedź | Brak informacji | Swobodny dialog |
|---|---:|---:|---:|---:|
| Wcześniejszy test | 6/18 | 1/50 | 25/25 | 0/5 |
| Nowy test | 4/16 | 0/16 | 7/8 | nie badano |

Na nowym teście poprawny wybór źródła: fakty 16/16, definicje 8/16, brak źródła 8/8. Wybór materiału i pisanie odpowiedzi są osobnymi problemami. Dodatkowa kontrola uznająca dokładną krótką odpowiedź samym przedmiotem z właściwym cytowaniem daje 6/16 dla faktów; nie zastępuje ustalonej wcześniej miary pełnego zdania. Przykład błędu: wybór S2 poprawny, lecz wygenerowane cytowanie S1. Występują też uszkodzone słowa i mieszanie definicji.

Nowy zestaw 40 przykładów nie uczestniczył w uczeniu ani wyborze wag; wykluczono wcześniejsze pojęcia, osoby/przedmioty i identyczne odpowiedzi pozytywne. Kontrola pakowania 1202 przykładów nie wykryła kopiowania odpowiedzi docelowych do wejścia. Kontrola wcześniejszych umiejętności generatora obejmowała tylko dwa przykłady, więc nie jest szerokim testem regresji. Strata 2.364 → 0.464 obejmuje dodatkowy cel wyboru źródła i nie jest bezpośrednio porównywalna ze starszymi stratami.

## Ograniczenia aktywnej gałęzi oceny faktów

Odczyt kodu potwierdził, że ta gałąź otrzymuje cztery wartości na fakt: zgodność podmiotu i zakresu, zgodność relacji i wartości, pozytywność, negatywność. Pełne brzmienie faktu nie jest jej wejściem. To reprezentacja do oceny zgodności, nie pełna reprezentacja znaczenia tekstu. Pozostałe ścieżki języka i nowy generator mają inne wejścia.

Wymiary połączeń H512 są dopasowane przez warstwy liniowe. Matryce słownika i wymagań są zamrożone. Wkład mostków ogranicza 0.05*tanh. Na 64 syntetycznych zestawach po 8 faktów stosunek RMS mostka do wejścia czytnika wyniósł 0.097%, a bezpośredniego sprzężenia H512 do logitów 0.013%. Wyłączenie mostków nie zmieniło decyzji w tej próbce. Wagi nie były modyfikowane podczas pomiaru.

Pomiar wskazuje mały wkład tych połączeń; nie dowodzi przyczyny błędów nowego generatora, który otrzymuje pełny tekst do 512 tokenów. Następna przebudowa powinna zachować treść obok macierzy relacji oraz kalibrować wkład gałęzi na zadaniach wymagających tej treści. Samo zwiększenie stałej wzmocnienia nie jest sprawdzonym rozwiązaniem.
