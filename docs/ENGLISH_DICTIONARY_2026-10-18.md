# Słownik angielski TSI — stan 18 października 2026

Wdrożono lokalny zasób WordNet 3.0 i wymowy CMUdict. Zawiera 147 306 haseł, w tym wyrażenia wielowyrazowe. Obecny czytnik zdań o posiadaniu może korzystać z 24 428 rzeczowników z danymi wymowy; 14 039 z nich ma jedno znaczenie i spełnia warunki tego czytnika. Nie oznacza to rozumienia dowolnych zdań angielskich.

Przykład: `Read: Anna has a telescope but John does not have a microscope.` Następnie: `Does John have a microscope?` Odpowiedź: `No. John does not have a microscope.` z cytatem źródła.

Wieloznaczne nowe słowa zachowują tożsamość leksykalną i listę znaczeń. Czytnik nie wybiera arbitralnie pierwszego znaczenia. Przejście między polskim i angielskim opiera się na 27 sprawdzonych powiązaniach pojęć; cały zasób nie jest słownikiem tłumaczącym. Różne pojęcia nadrzędne i podrzędne nie są automatycznie utożsamiane.

Dobór a/an korzysta z wymowy. Nieobsługiwane liczby mnogie i nieznane nazwy otrzymują doprecyzowanie. Dane nie stanowią kompletnego kontrolera gramatyki ani policzalności rzeczowników. Inne części mowy są zindeksowane, lecz obecny czytnik nie interpretuje na tej podstawie dowolnych czasowników i przymiotników.

Zasób zajmuje około 23 MB i działa offline. Wagi rdzenia i transformera nie zostały zmienione; to rozszerzenie słownika, a nie trening sieci. Zachowano licencje obu źródeł obok danych.

Weryfikacja: pełna regresja 315/315; testy angielskiego i słownika 51/51; 800/800 prób na 200 wylosowanych rzeczownikach (twierdzenie, zaprzeczenie, brak osoby, sprzeczność). Są to warianty ograniczonego zadania czytania, nie 800 niezależnych problemów językowych. Sprawdzono również odpowiedzi przez interfejs HTTP.

Źródła: [WordNet w NLTK](https://www.nltk.org/howto/wordnet.html), [CMUdict](https://github.com/cmusphinx/cmudict).
