# Wyjście pamięci i pełna treść — 21 października 2026

## Poprawka działającej aplikacji

Odtworzono utratę dostępu do pierwszego tekstu po wczytaniu drugiego. Źródła rozmowy miały jeden identyfikator; następny tekst stawał się nową aktywną wersją, a wcześniejszy pozostawał wyłącznie w historii bazy. Nie było to usunięcie wag ani zniknięcie zapisu z dysku.

Nowe teksty mają osobne identyfikatory. Korekta i cofnięcie wersjonują wybrane źródło, zachowując pozostałe. Istniejące sesje otrzymują odnośnik do dotychczasowego źródła przed korektą. Nie przywracano hurtowo nieaktywnych wersji, ponieważ część z nich zawiera zastąpione poprawkami informacje. Testy: 13/13 kontroli rejestru, korekt, cofania, starych sesji, resetu i izolacji trwałych notatek. Na działającym panelu wczytano tekst o Annie, potem o Dorocie; pytanie o Annę odnalazło pierwszy tekst. Oba źródła pozostały aktywne. Sprawdzono też korektę i cofnięcie drugiego źródła.

Serwer kolejkuje żądania podczas odczytu i przygotowania odpowiedzi. Nie potwierdzono równoczesnej przebudowy matrycy w tej ścieżce. KHIPU indeksuje tekst dialogu; nie skraca samej odpowiedzi. Samowalidacja dopisuje ocenę. Wybór języka może zmienić odpowiedź, zachowując oryginał w szczegółach.

## Nowa konstrukcja sieci — niewdrożony kandydat

Jeden checkpoint zawiera zachowany H512 z dotychczasowymi matrycami, własny generator i nowe połączenia: **4 958 102 parametry**, w tym **2 344 997 uczonych w tej próbie**; plik **20 031 875 bajtów (20.03 MB)**. Cała treść do 512 tokenów przechodzi przez nową ścieżkę H512. Znane słowa korzystają również z zachowanych wag matrycy słownika. Tekst, odczyt H512 i matryca mają normalizację i uczone udziały; w próbce po treningu około 34% / 33% / 33%. To udział w znormalizowanej reprezentacji, nie udział wiedzy ani dowód poprawności odpowiedzi.

Trening zatrzymano po wzroście błędu rozwojowego 0.407 → 0.599 → 0.887. Zachowano krok 75. Stare wagi pozostały identyczne bitowo; niezależne porównanie 64 zestawów zachowało stare decyzje. Te wyniki nie wykluczają pogorszenia zachowania nowej gałęzi.

| Ten sam nowy test | Poprzedni generator | Kandydat z pełną treścią |
|---|---:|---:|
| Fakty — pełna odpowiedź | 5/16 | 5/16 |
| Definicje — pełna odpowiedź | 0/16 | 0/16 |
| Brak informacji — poprawna odpowiedź | 7/8 | 2/8 |
| Wybór źródła faktów | 15/16 | 16/16 |

Kandydat nie poprawił jakości odpowiedzi i nie zastąpił działającego modelu. Dotychczasowy aktywny checkpoint pozostaje bez zmian.

## Puste impulsy i ślad wyjścia

Zera nie zmieniły wag. Powtórzone niezależne wejścia zerowe dawały ten sam stan. Po wcześniejszym tekście stan GRU pozostawał odróżnialny od startu bez tekstu również po 256 zerowych krokach. To test chwilowego stanu, nie trwałych notatek.

Ślad generowania wykazał dopisywanie tokenów bez nadpisywania wcześniejszych. Dla źródła S2 model skopiował „parasol”, po czym dekoder sam wygenerował S1. Puste wejście otrzymało wybór „brak źródła”, ale dekoder wypisał fragment S1]. To niespójność generowania i wskazania źródła, a nie potwierdzony zapis nowej treści w pamięci.

Usunięto współdzielony bufor stanów pośrednich z nowego modułu. Test A→B→A i osiem wywołań w dwóch wątkach zachowały wyniki. Niezmienne zrzuty źródeł oraz kontrola pochodzenia wykrywają sprzeczne i nieistniejące cytowania; nie zastępują sprawdzenia znaczenia odpowiedzi.

Zmiana jednego przedmiotu przy tej samej liczbie tokenów dawała różne reprezentacje na wejściu, wyjściu H512, odczycie pamięci i po połączeniu gałęzi. Poprawny przedmiot docierał do odpowiedzi. Pomiar czułości nie dowodzi zachowania całego znaczenia.
