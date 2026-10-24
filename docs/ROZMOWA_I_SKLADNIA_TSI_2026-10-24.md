# Rozmowa TSI i obsługa zdań — 24 października 2026

## Co wdrożono

W lokalnym panelu poprawiono podział zdań przy skrótach, inicjałach, liczbach dziesiętnych i końcowej interpunkcji. Ten sam podział obsługuje czytnik znaczenia, analizę TIMDR i operacje na tekście. Kontrola: **24/24**; oba tokenizery zachowały zapis tekstów bez zmian: **54/54**.

Poprzedni czytnik odrzucał spójniki, wymagał jednego orzeczenia i ograniczał analizowane zdanie do 16 tokenów. Generator fraz wymagał jednej relacji. Przebudowano analizę całych zdań: jawne człony otrzymują osobne wiersze macierzy oraz powiązania łączenia, kontrastu i przyczyny. Limit techniczny dla jednego członu wynosi obecnie 96 tokenów; istnieją także ograniczenia złożoności analizy przypadków. Nie jest to pełna składnia dowolnego polskiego tekstu.

Obsługiwane są m.in. jawne konstrukcje z „i”, „oraz”, „ale”, „a”, „bo”, „ponieważ”, „więc”. Każdy człon musi zostać rozpoznany. Alternatywy, nieodczytane człony i niejednoznaczne pominięcie wykonawcy pozostają nierozstrzygnięte; nie dopisuje się za nie faktów. Odrzucona wersja „bo” → „więc” sprawdza także kierunek przyczyny.

Generator fraz może ułożyć kilka członów lub zdań, zachowując role, przeczenia i powiązania. Przykład rzeczywistego wyniku: **„Anna daje książkę Markowi, ale Ewa nie daje klucza Piotrowi.”** To uczenie kolejności zweryfikowanych fraz źródłowych, odrębne od swobodnego generatora rozmowy.

| Sprawdzian wdrożonych poprawek | Wynik |
|---|---:|
| Zdania złożone i rozpoznawanie przypadków nierozstrzygniętych | 15/15 |
| Wcześniejsze kontrole przypisania ról | 116/116 |
| Wcześniejsze kontrole zgodności znaczenia | 13/13 |
| Generowanie wieloczłonowych odpowiedzi z podanego źródła | 4/4 |
| Poprawianie całego zdania, negacji i przyczyny przez API panelu | 3/3 |

Wcześniejszy błąd odmiany oraz niejednoznacznych nazw rozwiązuje się w kontekście danego źródła. Dawna próba semantyczna **5/7** osiąga **7/7** po tej poprawce. Kontekstu nie przenosi się między niezależnymi źródłami.

## Swobodna rozmowa — aktualny stan

**Nie osiągnął wymaganego poziomu.** Rzeczywista próba starej aplikacji objęła 12 tur: 9 odmów obsługi, 8 powtórzonych odpowiedzi, dwa nietrafione odwołania do Wikipedii i jedno nietrafione wyszukanie dokumentu. Średni czas wynosił 1,913 s.

Przygotowano osobny wariant: uczony odczyt wiadomości → stan rozmowy → macierz → natywny generator → kontrola TIMDR. Fakty mogą pochodzić wyłącznie od użytkownika; odpowiedzi sieci nie stają się dowodami. Stan zachowuje kolejne wersje czasu, negację i niepewność. Nieodczytana zmiana nie certyfikuje starego terminu. Wariant korzysta z istniejącego panelu w osobnym procesie i osobnej pamięci, bez automatycznego wyszukiwania internetowego.

Kontrole przepływu stanu: 9/9; osobny serwer przez HTTP: 4/4. Te kontrole potwierdzają połączenie elementów, a nie jakość języka. Uczony czytnik osiągnął **8/17** na nowych sformułowaniach.

Pierwszy trening: 112 przykładów, 52 aktualizacje, 47/48 zachowanych wcześniejszych odpowiedzi. Pełna rozmowa z tym generatorem nadal dawała błędne godziny, niepowiązane wypowiedzi i uszkodzone słowa; średnio 16,908 s na turę. **Wag nie przyjęto.** Przyjęty wcześniej zapis pozostaje zachowany.

## Czy odpowiedzi były ucinane?

W teście ustawiono 72 tokeny odpowiedzi. Dekoder ma wspólne okno 384 tokenów na wejście i odpowiedź. Wariant rozmowy zachowuje do czterech ostatnich pełnych tur i usuwa starsze pełne tury, aby zmieścić wejście w 220 tokenach; zgłasza liczbę pominiętych tur. Nie mieści dowolnie długiej rozmowy w aktywnym kontekście.

W 12 z 12 odpowiedzi koniec wybrała sama sieć przez znacznik EOS; nie zadziałało ucięcie limitem. Porównanie dwóch tych samych wejść z limitami 72 i 160 dało identyczne tokeny odpowiedzi. Kontrola z limitem 8 pokazała rzeczywiste ucięcie i poprawnie je oznaczyła. Nie wykryto znikających znaków specjalnych podczas dekodowania. Zwiększono domyślny limit nowego wariantu do 160, zachowując granicę kontekstu.

Dodano zapis powodu zatrzymania: EOS sieci, limit odpowiedzi lub limit kontekstu, wraz z liczbą tokenów oraz opcjonalnym dosłownym śladem tokenów. Nie wymusza się dłuższej wypowiedzi przez ignorowanie EOS.

## Dalszy trening

Zrównoważony trening: **67 aktualizacji**, zachowanie **47/48** wcześniejszych odpowiedzi. W ręcznej ocenie pełnych odpowiedzi: **0/2 powtórek** i **1/4 nowych wypowiedzi**; poprawna odpowiedź czasowa wymagała kontroli macierzowej podczas ponownego generowania. Nowych wag nie ustawiono jako domyślnych.

Dobór tematów jest zrównoważony według celu rozmowy. Wcześniej 90 ze 112 przykładów dotyczyło czasu, co nadmiernie eksponowało ten temat. Nowy przebieg uwzględnia powitania, rozmowę, pisanie, nieznane relacje i pytania uzupełniające oraz powtórki 48 dawnych odpowiedzi. Ostatnie cztery tokeny poprawnej odpowiedzi mają nieco większą wagę w funkcji treningowej. Tablice reguł i wcześniejsze wagi pozostają zabezpieczone; internetowy trening wag jest wyłączony.

Warunek przyjęcia: poprawa rzeczywistych nowych rozmów oraz zachowanie wszystkich 48 wcześniejszych odpowiedzi. Sam spadek błędu treningowego nie zastępuje tej oceny. Portable, MUZ i walidatora nie podmieniano w tym etapie.

## Dosłowne odpowiedzi po zrównoważonym treningu

**Powtórka. Użytkownik:** Cześć!

**TSI:** Tożesz porozmawiać?

**Powtórka. Użytkownik:** Mam ochotę pogadać.

**TSI:** T

**Nowe sformułowanie. Użytkownik:** Hej, znajdziesz chwilę na rozmowę o książkach?

**TSI:** Spotkanie jest o 16.

**Nowe sformułowanie. Użytkownik:** Chcę zacząć opowieść o liście znalezionym w szufladzie. Co proponujesz?

**TSI:** Spotkanie jest o 16.

**Nowe sformułowanie. Użytkownik:** Najpierw zebranie miało godzinę 7, a po zmianie 11.

**TSI:** Spotkych odmiane to 17.

**Nowe sformułowanie. Użytkownik:** Jaka jest teraz godzina tego zebrania?

**TSI:** Aktualna godzina to 11.


## Dodatkowa kontrola wejścia treningowego

Znaleziono również rozbieżność przygotowania danych: podczas treningu generator otrzymywał cel oznaczony przez nauczyciela, a podczas rozmowy — wynik uczonego czytnika z progiem akceptacji. Różnica wystąpiła w **39/112** przykładów. Przykładowo poprawnie przewidziane powitanie z niewystarczającą pewnością zmieniało cel przekazywany generatorowi na „other”.

Przygotowanie następnego zbioru poprawiono: wejście generatora i stan buduje teraz rzeczywisty czytnik, tak jak podczas rozmowy. Kontrola zgodności: **112/112**. Oznaczenia nauczyciela służą do równoważenia tematów i oceny, a nie zastępują odczytu sieci na wejściu. Zestaw po poprawce jest przygotowany do następnego treningu; powyższe 67 aktualizacji wykonano jeszcze przed tą zmianą. Próba z prawidłowym oznaczeniem nauczyciela również dawała uszkodzoną odpowiedź, dlatego sama rozbieżność nie wyjaśnia całego problemu generatora.
