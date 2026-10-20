# Rozmiar modeli, sprzęt i wznowienie — 20 października 2026

## Parametry i pliki

| Składnik | Parametry | Plik wag, MB | Plik wag, MiB |
|---|---:|---:|---:|
| Aktywny językowy H512 | 2 054 186 | 8.55 | 8.15 |
| Wspólny transformer i matryce czytnika | 302 642 | 1.32 | 1.26 |
| Suma tych dwóch modułów | 2 356 828 | 9.87 | 9.41 |

Liczbę zapisanych wag H512 sprawdzono z checkpointem. Suma nie obejmuje wszystkich dodatkowych modeli pomocniczych. Rozmiar plików obejmuje także metadane checkpointu; nie oznacza zużycia RAM ani VRAM. Liczba parametrów nie jest limitem liczby notatek ani miarą samodzielności.

Cały lokalny katalog aplikacji TSI w chwili pomiaru: **432.31 MB / 412.29 MiB**, **1216 plików**. Obejmuje kod, modele, słowniki, dane, historię treningów, kopie i runtime. Współdzielony Python poza tym katalogiem nie jest wliczony. To pomiar plików, nie aktualnej gotowej paczki portable ani zajętych klastrów systemu plików.

## Automatyczny dobór sprzętu

Wspólny czytnik wykrywa urządzenia udostępnione przez PyTorch: CPU, CUDA albo MPS. Mierzy reprezentatywne obliczenie i wybiera urządzenie oraz 1, 2 lub do 4 wątków CPU według wyniku. Profil jest pamiętany do doby i unieważniany po zmianie modelu, środowiska lub wykrytych możliwości. Po błędzie dostępnego akceleratora możliwy jest powrót na CPU.

Na sprawdzonym komputerze: **Intel HD Graphics**, **PyTorch 2.14.0+cpu**, CUDA niedostępna. Obecnie wykorzystywany jest CPU. Nie instalowano innego backendu i nie potwierdzono działania na fizycznym GPU. H512 i solvery dokładne pozostają na CPU; automatyczny wybór urządzenia dotyczy wspólnego czytnika neuronowego. Macierze oraz wagi pozostają float32, bez zmiany checkpointu.

Kontrole: 9/9 sprzętu/cache/fallbacku na CPU, 57/57 testów modułu i zachowane zbiory 960/960, 720/720, 640/640. Dostępność GPU w kodzie jest warunkowa; testy CPU nie są certyfikacją akceleratora.

## Kontrolowane ponowienie procesu

Panel walidatora może ponowić start procesu czytnika jeden raz po awarii, niepoprawnym transporcie albo potencjalnie przejściowym błędzie dostępu do plików. Obie próby dzielą łączny limit 45 sekund. Błędne dane, prośba o doprecyzowanie i niepotwierdzony wynik nie są automatycznie wykonywane ponownie. Po wyczerpaniu limitu błąd pozostaje widoczny. To nie jest bezwarunkowe odświeżanie strony ani reset rozmowy.

Przeszło 13/13 prób ponowienia i kontrola rzeczywistego wznowienia: dwie próby procesu, dwa wykonane kroki łącznie, bez powtórzenia ukończonego kroku. Dziennik lokalny nie zapisuje treści żądania ani dokumentu. Ponowienie nie zastępuje naprawy trwałego problemu z zapisem.

## Zmiana nazwy i kontrola końcowa

Lokalna aplikacja: AI-SI-TSI; lokalna kopia dokumentacji: AI-SI-TSI-git. Adres repozytorium: https://github.com/jbackk-lang/AI-SI-TSI. Zaktualizowano aktywne odwołania między modułami. Po przeładowaniu przeszły 3/3 kontrole: panel ogólny, czytnik walidatora i odtworzenie raportu. W próbach wdrożenia występowały też błędy dostępu do zapisu, których nie zawsze usuwało ponowienie; nie uznaje się ich trwałej przyczyny za ustaloną. Ponowienie pozostaje ograniczone, a po dwóch niepowodzeniach zwraca błąd.
