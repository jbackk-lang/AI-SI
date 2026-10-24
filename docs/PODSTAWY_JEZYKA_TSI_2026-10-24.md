# Podstawy generowania języka TSI — 24 października 2026

## Wynik bieżącego etapu

Wybrany nowy zapis wag generuje poprawnie **8/8 znanych pełnych odpowiedzi** i zachowuje **48/48 dawnych odpowiedzi**. Razem tworzą **56/56** chronionych przykładów. Generowanie jest natywne: podczas tych ośmiu prób nie stosowano gotowych odpowiedzi w obsłudze poleceń ani ograniczania tokenów listą dopuszczalnych zdań.

Przykłady rzeczywistych odpowiedzi:

- „Cześć!” → **„Cześć! O czym chcesz porozmawiać?”**
- „Opisz deszcz w dwóch prostych zdaniach.” → **„Deszcz stukał o parapet. Ulica powoli pustoszała.”** Drugiego sformułowania polecenia nie było w treningu.

| Próba | Wynik |
|---|---:|
| Osiem znanych ćwiczeń, pojedyncza wiadomość, pełna odpowiedź | **8/8**, przed etapem 0/8 |
| Wcześniejszy chroniony zestaw | **48/48** |
| Cztery nowe proste sformułowania, ręczna ocena sensu | **2/4** |
| Nowe proste sformułowania, identyczność z jedną referencyjną wersją tekstu | 1/4 |
| Osiemnaście nowych zdań z rolami i przeczeniem | **0/18** |
| Wcześniejsza wieloturowa próba: dwie znane wypowiedzi | **1/2**, poprzednio 0/2 |
| Ta sama wieloturowa próba: cztery nowe wypowiedzi | **1/4**, bez zmiany; godzina wymagała korekty macierzowej |

Ocena 2/4 dopuszcza poprawną inną treść wypowiedzi. Odpowiedź o deszczu spełnia polecenie mimo różnicy względem jednego przykładowego rozwiązania. Osiemnaście prób gramatycznych należy do kolejnego etapu; wybrany zapis opanował na razie początkowe osiem ćwiczeń.

**Swobodna wieloturowa rozmowa nadal nie osiągnęła wymaganego poziomu.** Nowych wag nie podmieniono w domyślnym panelu, MUZ ani walidatorze.

## Co zmieniono w sieci

W badanym wariancie rozdzielono współdzieloną dotąd macierz słownika wejściowego i warstwę wyjściową. Początkowo obie zawierały dokładnie te same wartości. Przed treningiem potwierdzono **48/48 dawnych odpowiedzi oraz zerową różnicę logitów** względem modelu wyjściowego.

Uczyły się warstwa wyjściowa oraz dodane warstwy dekodera 4–11 z uwagą krzyżową. Słownik wejściowy, oba enkodery, pierwotne warstwy dekodera 0–3 i macierze reguł pozostały zamrożone. Kontrola zapisanych wag potwierdziła, że zmieniła się macierz wyjściowa, a wymienione stare części zachowały wartości.

Wariant ma **23 542 811 parametrów**, o **524 288** więcej od poprzedniego wspólnego modelu. Jego wybrany plik wag zajmuje **94666793 B — 94.67 MB**. To wspólny plik enkoderów i dekodera; czytnik i środowisko uruchomieniowe są oddzielne. Nie jest to rozmiar całego portable.

Zmiany danych, etapowania i warstwy wyjściowej zastosowano razem. Wynik nie rozdziela ich indywidualnego wpływu.

## Zbiór i przebieg nauki

Przygotowano lokalnie **514 przykładów nauki oraz 22 odłożone próby**: 8 krótkich odpowiedzi, 486 ćwiczeń opartych na 162 sprawdzonych rodzinach zdań i 20 wcześniejszych przykładów autorskich. Zadania gramatyczne obejmują wykonawcę, czynność, przedmiot, odbiorcę, odmianę i przeczenie. Powiązane warianty jednego zdania nie przecinają podziału na naukę i próby. To rodziny ćwiczeń syntetycznych, a nie 514 różnych tematów rozmowy.

Początkowo uczono ośmiu podstaw. Wynik pełnych ścieżek generowania rósł: **0/8 → 2/8 → 3/8 → 5/8 → 8/8**. Po osiągnięciu kompletu sprawdzono później rzeczywiste, swobodnie wygenerowane odpowiedzi, bez podstawiania wzorca.

Po 50 głównych aktualizacjach i trzech korektach chronionego zestawu osiągnięto 8/8 oraz 48/48. Po dołączeniu trudniejszych przykładów przy 60. aktualizacji wynik spadł do 5/8 i 47/48. Ten zapis odłożono; do oceny oraz następnych prób wybrano wcześniejszy zapis 8/8 i 48/48. Wszystkie artefakty zachowano.

Pierwszy start tego wariantu zatrzymał się przed pierwszą aktualizacją wag na błędzie przekazywania tensorów trybu odczytu do funkcji treningowej. Poprawiono przekazywanie, zachowano nieudany start i uruchomiono oddzielny przebieg. Powyższe wyniki pochodzą z poprawionego przebiegu.

## Następny problem: historia rozmowy

Pytanie „Mam ochotę pogadać.” osobno daje poprawną odpowiedź. Po poprzedzającym powitaniu ta sama wiadomość powoduje uszkodzoną wypowiedź. Użyto tych samych wag; podczas rozmowy nie wykonywano treningu ani nie usuwano historii przez limit kontekstu. Zmienił się pełny kontekst wejścia.

Przygotowano **56 kombinacji krótkich rozmów i 8 odłożonych kombinacji**. Ich odpowiedzi wynikają z opanowanych ćwiczeń, ale pojawiają się po różnych wcześniejszych wypowiedziach. Nowe osiem opanowanych odpowiedzi dołączono do 48 starych, tworząc ochronę 56/56. Dalszy sterownik uwzględnia ten rozszerzony zestaw w powtórkach, aby przejście do nowego etapu nie usuwało świeżo poznanych odpowiedzi. W chwili zamknięcia tego etapu nauki na nowych kombinacjach jeszcze nie przeprowadzono. Dalszy wspólny trening opisuje [kolejny raport](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/WSPOLNY_TRENING_KONTEKSTU_TSI_2026-10-24.md).

Pętla internetowego uczenia wag pozostaje wyłączona. Kod, wagi i zbiory treningowe pozostają lokalnie; repozytorium publikuje ten opis i wyniki.
