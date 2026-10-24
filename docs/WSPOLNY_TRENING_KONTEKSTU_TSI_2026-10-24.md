# Wspólny trening enkoderów i generatora — 24 października 2026

## Aktualny wynik

Enkodery H512 uczą się teraz razem z generatorem. Wybrany zapis zachowuje **56/56 chronionych odpowiedzi**: 48 dawnych i osiem poznanych w poprzednim etapie.

W rozpoznawaniu odpowiedzi po wcześniejszej wiadomości wynik wspólnego wariantu wzrósł z **2/56 do 8/56** na przykładach nauki. Na ośmiu odłożonych kombinacjach: **0/8 → 1/8**. Poprawny nowy dialog:

> Użytkownik: Dzień dobry.  
> TSI: Dzień dobry! W czym mogę pomóc?  
> Użytkownik: Dziękuję.  
> TSI: Proszę bardzo.

Ta kombinacja dwóch wiadomości była odłożona, a pojedyncze sformułowania należały do znanego zestawu. Próba sprawdza nowe połączenie kontekstu, nie nowy słownik.

**Swobodna rozmowa nadal nie osiągnęła wymaganego poziomu.** Domyślnych wag aplikacji, walidatora i MUZ nie podmieniono. Wybrany zapis służy dalszemu wspólnemu treningowi.

## Porównanie trzech sposobów treningu

Wszystkie warianty zaczynały od tego samego zapisu i korzystały z tych samych 56 uczonych kombinacji oraz ośmiu odłożonych. Pytania odłożone nie uczestniczyły w obliczaniu straty ani wyborze punktu wag wewnątrz przebiegu.

| Uczone części | Wybrany krok | Uczone rozmowy | Nowe kombinacje | Zachowane odpowiedzi |
|---|---:|---:|---:|---:|
| Dodane warstwy generatora i warstwa wyjściowa | 30 | 13/56 | 0/8 | 56/56 |
| Cały generator | 30 | 13/56 | 0/8 | 56/56 |
| **Oba enkodery i cały generator** | **10** | **8/56** | **1/8** | **56/56** |

Wspólny trening wykonuje więcej obliczeń na aktualizację; liczby kroków są różne. Wynik na uczonych rozmowach nie zastępuje wyniku nowych kombinacji. Do dalszej nauki zachowano wariant wspólny z pierwszą poprawną pełną odpowiedzią w odłożonym dialogu. To porównanie rozwojowe na małym zestawie, a nie szeroka ocena języka.

## Dlaczego wcześniej enkodery pozostawały zamrożone

Był to wybór ochronny: utrzymać wcześniej wyuczone odpowiedzi podczas uruchamiania generatora. Nie jest to wymóg konstrukcji TSI. Takie ustawienie uniemożliwiało enkoderom zmianę sposobu reprezentowania nowych kontekstów.

W obecnym wariancie oba enkodery oraz pamięci H512 otrzymują gradient z błędu odpowiedzi generatora. Krok uczenia enkoderów wynosi 0,000001, a wcześniejszych warstw generatora 0,000005; pozostałe warstwy mają większy krok. Wskaźniki tokenów mogą być zapamiętywane, ale reprezentacje ukryte podczas nauki są obliczane ponownie po zmianie wag.

## Sprawdzony przepływ uczenia

Przed optymalizacją sprawdzono niezerowe gradienty obu enkoderów, obu pamięci H512 i generatora w rzeczywistej ścieżce treningu. Po zapisaniu wybranego punktu potwierdzono zmiany wag:

- oba enkodery zawierają zmienione tensory;
- w pamięci H512 każdego z nich zmieniło się osiem tensorów;
- **sześć macierzy reguł pozostało dokładnie bez zmian**;
- odczyt całej zapisanej sieci potwierdził **56/56** chronionych odpowiedzi.

Wspólny plik zawiera aktualne wagi enkoderów i generatora, dzięki czemu odtwarzany model korzysta z ich zgodnego kompletu. Sieć nadal ma **23 542 811 parametrów**; wybrany plik wag zajmuje **94.67 MB**. To plik modelu, nie rozmiar całego portable.

## Kontrola regresji

Przy 10. głównej aktualizacji zachowano 48/48 dawnych i 8/8 nowych odpowiedzi. Próba po 15. aktualizacji pogorszyła wyniki do 46/48 oraz 7/8. Do dalszych testów wybrano wcześniejszy zapis; gorszy również zachowano jako artefakt badawczy.

Chroniony zestaw oraz uczone rozmowy sprawdzano w trakcie nauki. Nowe kombinacje oceniono po zamknięciu wyboru wag. Odpowiedzi w tych próbach wygenerowała sieć; nie zastępował ich wzorzec zadania ani solver. Pętla internetowego uczenia wag pozostaje wyłączona.

Następny cel to poprawa odpowiedzi w nowych kontekstach przy dalszej ochronie 56 dotychczasowych odpowiedzi. Kod, wagi i dane pozostają lokalnie; repozytorium publikuje wyniki.
