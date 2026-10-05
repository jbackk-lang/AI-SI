# AI-SI

## Historia ostatnich dni — stan na 5 października 2026

| Data | Wykonane prace i zapisane wyniki |
|---|---|
| **3 października** | Cztery główne moduły po 1024 neurony i koordynator 5120; kontrola współpracy 52/52. Rozwijano pamięć źródeł, dostęp do lokalnych repozytoriów, dobór materiałów i kontrolę planów. Audio odłączono. |
| **4 października** | Wdrożono własny adapter list z trwałą korektą wag: odtworzenie 121/121 znanych zadań. Pierwszy test nowych poleceń: 21/24. Poprawiono reguły zakresu i wdrożono dwa oraz trzy kroki; próby 5/5, 8/8 i 6/6. Rozdzielono rozmowę i zadania, dodano historię rozmów oraz opis rozmiaru, wymagań i możliwości GPU. |
| **5 października** | Wznowiono kolejkę materiałów z priorytetem potwierdzonej potrzeby lub losowym wyborem niepobranego tematu. Dodano i naprawiono panel logu, uruchomiono interfejs. Uporządkowano 157 plików prywatnego folderu; 12 testów przeszło. Przywrócono historię i linki dokumentacji. |

W kolejce pobrano dotąd **Machine learning**, **Program synthesis** oraz **Working memory**. Są zapisanymi materiałami: zrozumienie nie zostało potwierdzone, wagi nie zmieniły się podczas pobierania. Wyniki treningu i przebiegów dotyczą opisanych prób; nie sumujemy powtórzonych zadań jako niezależnych testów.

[Pełna wcześniejsza historia](README_DETAILS.md) · [Wagi: 4 października](docs/SI_WAGI_2026-10-04.md) · [Przebiegi: 4 października](docs/SI_PRZEBIEGI_2026-10-04.md).


SI to eksperymentalny warsztat łączący język, matematykę, programowanie i pracę ze źródłami, inspirowany TIMDR jako punktem wyjścia do budowy sterownika współpracy.

**Publiczne repo zawiera interfejs, integrację, narzędzia treningowe, testy i dokumentację; rdzeń SI/TIMDR, wagi, checkpointy i pamięć użytkownika pozostają prywatne.** [Zakres publikacji](docs/PUBLIC_SCOPE.md).

## Osiągnięcia w skrócie

Poniższe funkcje dotyczą prywatnego silnika i ograniczonych prób rozwojowych; samo pobranie repo nie udostępnia wszystkich modułów.

- **Język:** Qwen zastąpił Bielika w polskiej rozmowie, interpretacji źródeł i generowaniu kodu.
- **Matematyka:** dokładny kalkulator, niezależna walidacja i SymPy obsługują określone działania oraz równania.
- **Programowanie:** SI wybiera sprawdzone przykłady Pythona i testuje wygenerowany kod na podanych przypadkach.
- **Dokumenty:** Embedding i Reranker wybierają materiały przekazywane do interpretacji przez Qwena.
- **Obrazy:** Qwen-VL analizuje obrazy, a odczyt może zasilać kolejne kontrolowane zadanie.
- **Źródła:** dostęp do dozwolonych stron i udostępnionych plików wspiera pracę z materiałami.
- **Pamięć:** zapisane fragmenty źródeł można wyszukiwać i przekazywać do rozmowy.
- **Koordynacja:** własne sieci wybierają gotowe przebiegi współpracy między modułami.
- **Uczenie:** własne wagi adaptera SI są trenowane, oceniane i warunkowo wdrażane, a ostatnią poprawkę odtworzono jako 121/121 znanych zadań z udziałem jawnych reguł.
- **Kontrola poleceń:** parser kolejności i własny adapter SI wykonują ograniczone przebiegi dwóch lub trzech operacji na listach, z kontrolą zakazów i danych pośrednich.
- **Interfejs:** rozmowa i zadania mają osobne panele, a historia rozmów jest zapisywana lokalnie.
- **Audio:** ASR i TTS sprawdzono w małych próbach, lecz dźwięk pozostaje odłączony.

**Wyniki, liczby neuronów, rozmiary wag, historia zmian, ograniczenia i propozycja wdrożenia:** [szczegółowy opis projektu](README_DETAILS.md).

[Aktualizacja uczenia własnych wag — 4 października 2026](docs/SI_WAGI_2026-10-04.md).

[Zamknięcie etapu: generalizacja i przebiegi do trzech kroków](docs/SI_PRZEBIEGI_2026-10-04.md).


## Mini-model decyzyjny SI

Osobna bramka SI przed Qwenem ocenia zakaz, kolejność, ograniczenia i brak danych; checkpoint ma **3,03 MB**, a z Qwenem bez adaptera uzyskano **4/4 poprawnych odpowiedzi** w małej próbie.

SI może służyć do wyboru i wywoływania modeli językowych, programistycznych, matematycznych, wyszukujących, wizyjnych, audio i sygnałowych po podłączeniu ich danych oraz kontroli wyników. W tym etapie sprawdzono bramkę tylko z Qwenem; nie zmienia ona jego wag i nie zastępuje walidatora odpowiedzi. Kolejny test decyzji dał **11/12**, z jednym nadmiernym zatrzymaniem poprawnego zadania.

[Szczegóły, historia prób i zakres zarządzania modelami](docs/SI_DECYZJE_2026-10-05.md).

## Uruchomienie

1. Uruchom posiadany prywatny silnik SI zgodnie z jego instrukcją.
2. Uruchom `Uruchom_AI_SI.bat` albo `python run_ui.py` w tym repo.
3. Wskaż adres silnika przez `--backend`; bez działającego silnika interfejs zgłosi brak połączenia.

## Rozmiar, wymagania i GPU

Folder roboczy prywatnego SI zmierzony 4 października 2026 r. zajmował **9,29 GB (8,65 GiB)**, w tym modele, historię treningu i kopie wag; środowisko Python przechowywane osobno nie jest wliczone.

Pakiet do przeniesienia, po pominięciu historii, kopii i starego Bielika, szacujemy na **2,7–3 GB dla SI + Qwen** albo **5,7–6 GB z Embedding, Reranker i obrazami**; audio oraz Python z bibliotekami zwiększają rozmiar. Są to szacunki, nie pomiar gotowego instalatora. Wagi ostatnio trenowanego adaptera poleceń zajmują około **1,05 MB** — to jeden element SI, nie cały rdzeń.

| Wariant | RAM | Procesor | Wolny SSD z bibliotekami |
|---|---|---|---|
| SI + Qwen | 8 GB orientacyjnie; zalecane 16 GB | współczesny 64-bit, około 4 rdzeni | 8–10 GB |
| Z obrazami i wyszukiwaniem | 16 GB orientacyjnie; wygodniej 32 GB | około 6–8 rdzeni | 12–15 GB |

To orientacyjne wymagania dla obecnej konfiguracji Windows, nie minima potwierdzone testami na tych komputerach. Zużycie zależy od kontekstu, bibliotek oraz liczby modułów uruchomionych jednocześnie. Rozmiar plików nie jest zapotrzebowaniem na RAM.

Obecny Qwen uruchamiany jest przez silnik **CPU**. GPU można podłączyć przez backend **CUDA dla NVIDIA** lub **Vulkan dla zgodnych kart AMD/Intel i sterowników**; zobacz [oficjalną dokumentację llama.cpp](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md). Wymaga to odpowiedniej wersji silnika i konfiguracji przenoszenia warstw na GPU, bez ponownego treningu wag. GPU przyspieszy głównie Qwena i większe moduły; mały adapter SI może pozostać na CPU. Obsługa Vulkan w llama.cpp nie oznacza automatycznie przyspieszenia wszystkich modułów Python.

Dla obecnego Qwena karta z **6–8 GB VRAM** daje orientacyjny zapas; dokładne zużycie należy zmierzyć przy wybranym kontekście. Nie zweryfikowano jeszcze gotowego pakietu GPU ani jego wydajności. Przeniesienie na drugi komputer wymaga także zależności, sterowników i konfiguracji ścieżek — samo skopiowanie folderu nie gwarantuje uruchomienia.

## Jak oceniać projekt

To prototyp oceniany w niewielkich, kontrolowanych próbach, a nie potwierdzony odpowiednik ogólnych modeli AI.
Odczyt źródła nie oznacza uczenia wag, przejście podanych testów nie gwarantuje poprawności dowolnego programu, a większa liczba neuronów sama nie dowodzi poprawy.
Szczegółowe wyniki i ich zakres pozostają dostępne w [pełnej dokumentacji](README_DETAILS.md).
