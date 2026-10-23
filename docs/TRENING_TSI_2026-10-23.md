# Korekta odczytu źródła i kontrola zapominania — 23 października 2026


## 23 października 2026 — korekta klas i odczytu wyniku ze źródła

Wykonano 16 aktualizacji pierwszej próby oraz 8 aktualizacji drugiej. Uczono oba enkodery i dekoder; reguły formalne pozostały zamrożone. Oceniano ponownie wczytane wagi i pełne odpowiedzi sieci, bez podmiany wyniku przez nauczyciela.

| Zapis | Zachowane wcześniejsze odpowiedzi | Tablica źródłowa | T | F | U | Decyzja |
|---|---:|---:|---:|---:|---:|---|
| Próba 1, krok 8 | 89/98 | 50/69 | 12/23 | 11/19 | 27/27 | Odrzucony |
| Próba 1, krok 16 | 92/98 | 45/69 | 15/23 | 4/19 | 26/27 | Odrzucony |
| Próba 2: wyrównanie i uwaga, krok 8 | 92/98 | 49/69 | 15/23 | 7/19 | 27/27 | Odrzucony |

Chronione 98 przykładów obejmuje 48 wcześniejszych odpowiedzi o faktach i języku, 47 poprawnych wyników logiki oraz 3 poprawne opisy czasu. Podwyższenie łącznego wyniku nie wystarcza do przyjęcia zapisu, jeżeli stracił wcześniej poprawne odpowiedzi.

Audyt pierwszej próby wykazał, że po doliczeniu powtórek udział celów wynosił **T 53, F 32, U 58**, mimo równej liczby nowych ćwiczeń. Druga próba wyrównuje łączny nadzorowany błąd klas: liczby przykładów to T 37, F 16, U 42, a wagi błędu dają każdej klasie taki sam łączny udział. Dodatkowo uwagę sieci uczono kierować na fragment „Wynik reguły”, zamiast na same operandy. Tablica jest materiałem źródłowym dla enkoderów; nie zastępuje wyjścia dekodera.

Pierwsza próba pokazała konkretny błąd: odpowiedź F dla `F NOR F`, chociaż źródło podawało T. Poprawa klasy F kosztem poprawnych odpowiedzi T została rozpoznana jako regresja.

Dodatkowy sprawdzian 16 nowych opisów czasu, z innymi pytaniami i liczbami, dał **0/16** dla bezpiecznych wag oraz **0/16** dla drugiej próby. Te sformułowania nie weszły do treningu. Oddzielnie przygotowano program 72 przykładów czasowych; w tym etapie go nie trenowano. Starszy test 3/16 i nowy sprawdzian stanowią odrębne zbiory. Trzy poprawne przykłady starszego zestawu weszły do chronionych powtórek nowych prób.

**Stan przyjęty pozostaje bez zmian:** 48/48 wcześniejszych odpowiedzi, odczyt źródła logicznego 47/69 (T 21/23, F 0/19, U 26/27), starsze parafrazy czasu 3/16. Nowe próby odrzucono. Panel, MUZ, walidator i paczki portable nie otrzymały tych wag. Nauka internetowa pozostaje zatrzymana.
