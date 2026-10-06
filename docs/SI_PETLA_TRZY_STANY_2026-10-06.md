# Trzy stany, pętla decyzji i powtórka testów SI — 6 października 2026

## Zmiany działającego systemu

Ujednolicono semantyczne decyzje SI: **potwierdzone**, **odrzucone**, **nierozstrzygnięte**. Stan ma określony zakres: potwierdzenie wyboru modułu nie oznacza potwierdzenia prawdziwości odpowiedzi. Jest to organizacja sterowania programowego, nie sprzętowa konwersja całej sieci na logikę trójwartościową.

Dodano ograniczoną pętlę: **brak danych → odczyt jawnych faktów użytkownika z historii → ponowna ocena**. Dotyczy prostych pytań o wartości urządzeń. Wykonuje jedną ponowną ocenę po znalezieniu nowej informacji; zatrzymuje się przy sprzeczności, braku materiału lub zakazie. Nie traktuje wcześniejszych domysłów asystenta jako dowodów. Pętla nie jest automatycznym treningiem wag.

Do rozmowy podłączono lekką arytmetykę z kontrolą wyniku, wyszukiwanie zapisanych źródeł oraz wyuczony wybór katalogowych przykładów kodu z kontrolą składni. Kontrola składni nie dowodzi poprawności działania programu; zapis pamięci nie jest zewnętrznym potwierdzeniem faktu.

## Powtórka na aktualnej instalacji

| Zakres | Wynik | Interpretacja |
|---|---:|---|
| Język i kontekst | 26/26 | Znane, ograniczone zadania rozwojowe |
| Źródło z kontrolerem | 32/32 | Obejmuje pomoc normalizacji i walidacji; brak błędnie potwierdzonych odpowiedzi |
| Sam model na tych 32 zadaniach | 19/32 | Oddzielny wynik własnej sieci, bez pomocy kontrolera |
| Pętla decyzji | 5/5 | Odzyskanie danych, brak danych, sprzeczność, ignorowanie domysłu asystenta i zakaz |
| Pętla w polskiej rozmowie | 2/2 | Pytanie o brakującą wartość i odzyskanie jej z historii |
| Integracja trzech stanów | 13/13 | Kontrola rozróżnienia stanów i niezmienności czynnych wag |
| Trzy stany przez interfejs | 5/5 | Obliczenie, zakaz, błąd wyrażenia, brak danych i niezweryfikowana odpowiedź językowa |

Powtórka nie zmieniała wag. Są to testy znane i rozwojowe, nie nowy niezależny holdout. Nie dowodzą ogólnego rozumienia języka ani poprawności w dowolnej dziedzinie. Nie sumujemy powtórek jako niezależnych sukcesów.

## Próby treningowe zachowane osobno

**Qwen jako nauczyciel przykładów:** pierwszą porcję odrzucono za powtarzanie nazwy obiektu. Po poprawieniu polecenia dwa poprawne przykłady rozszerzono do 192 wariantów liczbowych, a etykiety wyznaczał niezależny parser ograniczonej gramatyki. Trening własnego SI poprawił nowe zadania **19/32 → 21/32**, ale pogorszył wcześniejsze **89/93 → 87/93**. Powtórka odtworzyła oba wyniki. Kandydat nie został wdrożony; Qwen nie był trenowany.

**Trójstanowa sieć oceny:** wytrenowano osobną głowę 7→32→3, 355 parametrów, checkpoint około 4,1 KB. Wejścia opisują dowody i różnicę liczbową, nie gotowy stan. Wynik rozwojowy **768/768** jest silnie niezrównoważony: potwierdzone 2/2, odrzucone 598/598, nierozstrzygnięte 168/168. Niekompletną pierwszą próbę bez przypadków potwierdzonych zachowano, po czym poprawiono podział. Ta nowa głowa pozostaje niewdrożona. Działająca pętla nie korzysta z jej wag; dokładnego walidatora nie zastąpiono przybliżoną siecią.

## Dalsze uczenie

Najpierw potrzebny jest zrównoważony test wszystkich trzech klas, również z bardzo małymi różnicami liczbowymi i wartościami spoza treningu. Następnie nowe angielskie przykłady językowe z niezależnymi etykietami oraz kontrolą zapominania. Wynik surowej sieci należy raportować oddzielnie od kontrolera i narzędzi. Zamrożony test nie trafia do treningu; kandydat nie nadpisuje czynnych wag przed oceną. Szczegółowa instrukcja przekazania pracy kolejnemu agentowi znajduje się wyłącznie w dokumentacji lokalnej.

Publikacja obejmuje ten opis i README, bez kodu prywatnego silnika, checkpointów, danych treningowych, pamięci oraz prywatnych lokalizacji.
