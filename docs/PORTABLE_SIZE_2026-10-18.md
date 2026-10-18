# Pełny zakres portable — pomiar 18 października 2026

Pomiar obejmuje kod TSI, modele, słowniki, materiały lokalne, współdzielony silnik matematyczny, aktualne środowisko bibliotek i bazową instalację Python 3.12. Jest to **budżet rozmiaru przed zbudowaniem paczki**, a nie rozmiar gotowego, przetestowanego portable.

| Składnik | Rozmiar plików |
|---|---:|
| TSI z kodem i materiałami lokalnymi | 267,55 MB |
| Współdzielony silnik i validator z kodem | 1649,48 MB |
| Obecne środowisko bibliotek Python | 1296,02 MB |
| Bazowa instalacja Python | 677,81 MB |
| **Łącznie przed kompresją** | **3890,86 MB (3.62 GiB)** |

MB = 1 000 000 bajtów. Pominięto historię Git i pamięci podręczne Pythona/testów. Pozostałe materiały robocze, treningowe i kopie wewnątrz tych katalogów są uwzględnione. Pomiar nie obejmuje folderów spoza wskazanych czterech składników ani przeglądarki i systemu Windows.

To konserwatywny wariant z całym obecnym środowiskiem bibliotek, również tymi potencjalnie zbędnymi. Po wybraniu tylko wymaganych zależności paczka może być mniejsza. Rozmiar ZIP będzie znany po jej zbudowaniu. Nie jest to zużycie RAM.

Samo skopiowanie obecnego venv nie tworzy portable: zawiera ono odwołanie do zainstalowanego Pythona. Trzeba przygotować przenośny interpreter, względne ścieżki i przetestować uruchomienie na czystym komputerze. Przy wydawaniu paczki należy rozpocząć z pustą historią rozmów i bez prywatnych dokumentów; powyższy pomiar obejmuje obecny stan lokalny, a nie paczkę do publikacji.
