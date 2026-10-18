# TSI — czytnik i odpowiedzi PL/EN, 18 października 2026

## Działa w panelu rozmowy

1. `Read: Anna has a map but Piotr does not have a book.`
2. `Does Piotr have a book?`
3. Odpowiedź: **No. Piotr does not have a book.**, z cytatem.

Można także podać `Przeczytaj: Anna nie ma samochodu.`, a następnie `Does Anna have a car?`. Odpowiedź będzie po angielsku; cytat pozostanie po polsku. Odwrotny kierunek też działa: `Read: Anna has an umbrella.`, potem `Czy Anna ma parasol?`.

## Zakres

Angielski adapter rozpoznaje pełne, pojedyncze nazwy osób oraz `has`, `does not have`, `doesn't have`, spójniki `and`, `but`, `or` i warunek `if …, then …` (także standardowy wariant z przecinkiem bez `then`). Pytania mają postać `Does [nazwa] have [przedmiot]?`. Rzeczowniki policzalne są pojedyncze z właściwym `a`/`an`; `water` i `coffee` występują bez przedimka.

Kontrolowany słownik obejmuje **29 angielskich haseł i 27 wspólnych pojęć**. Nie jest to pełny słownik angielski. `bike` i `bicycle` oraz `parcel` i `package` są jawnymi aliasami. Przekład jest ograniczony do tego słownika, nie jest ogólnym translatorem. Nazwy osób pozostają identyfikatorami: nie utożsamiamy automatycznie Jana z Johnem. Zgodność kategorii przedmiotu nie ustala tożsamości fizycznego egzemplarza.

Zaimki, liczba mnoga, nieznane rzeczowniki, opuszczone podmioty i `the` wymagające odniesienia do konkretnego obiektu kończą się doprecyzowaniem. Nie usuwamy `the`, aby przypadkiem nie zmienić sensu na `a`. Limity odczytu pozostają takie jak dla PL: 6 zdań, 6 par osoba–przedmiot, 12 członów atomowych i głębokość 4.

Odpowiedzi w tym module są tworzone regułami gramatycznymi z pytania i potwierdzonego stanu, a nie swobodnym generatorem. Obsługa EN dotyczy czytania kontekstu i pytań o posiadanie; pozostałe funkcje i elementy panelu nie są przez tę zmianę w całości przetłumaczone.

## Wspólny mechanizm

Oddzielne reguły PL i EN prowadzą do tych samych identyfikatorów ról i pojęć. Dalej działa wspólne drzewo logiczne, audyt, macierz ról i istniejący transformer. Negacja, alternatywa i warunek zachowują znaczenie w obu językach. Cytaty oraz pozycje fragmentów pozostają zgodne z oryginałem. Model nie został ponownie wytrenowany: nowy adapter przekazuje mu obsługiwaną reprezentację. Wagi rdzenia i transformera pozostały bez zmian.

## Sprawdzenie

- Pełna regresja po dodaniu EN: **290/290**.
- Końcowe testy interakcji i granic EN, także po doprecyzowaniu zaimków i `the`: **28/28**.
- Kontrola **1536/1536 wariantów językowych**: 384 EN, 384 PL, 384 tekst PL/pytanie EN, 384 tekst EN/pytanie PL. Są to równoważne scenariusze w różnych językach, nie 1536 niezależnych problemów ani pomiar dowolnej znajomości języka.
- Wszystkie hasła słownika: **116/116 prób** potwierdzenia, zaprzeczenia, braku informacji i sprzeczności.
- Próby HTTP: pełne odpowiedzi, zachowanie sesji oraz oryginalnych cytatów w obu kierunkach.

Raporty: `docs/english-context-2026-10-18`. Poprzedni kod: `backups/before-english-context-2026-10-18`. Brak uczenia w tle. Dalsze etapy to kontrolowane odniesienia zaimkowe, konkretne obiekty i rozszerzanie słownika z testami zachowania wcześniejszych odpowiedzi.

## Kontrolowany słownik

| EN | Wspólne hasło |
|---|---|
| map | mapa |
| book | książka |
| bag | torba |
| parcel | paczka |
| package | paczka |
| newspaper | gazeta |
| key | klucz |
| ticket | bilet |
| notebook | zeszyt |
| car | samochód |
| bicycle | rower |
| bike | rower |
| phone | telefon |
| computer | komputer |
| umbrella | parasol |
| backpack | plecak |
| letter | list |
| document | dokument |
| table | stół |
| chair | krzesło |
| cup | kubek |
| pen | długopis |
| pencil | ołówek |
| apple | jabłko |
| orange | pomarańcza |
| watch | zegarek |
| ball | piłka |
| water | woda |
| coffee | kawa |
