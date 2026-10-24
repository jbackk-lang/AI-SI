# Pamięć TSI — stan 24 października 2026

## Aplikacja

Do istniejącego panelu TSI podłączono inkubator pamięci. Wagi działającego modelu pozostały te same; dużego modelu badawczego nie podstawiono przy tej operacji. Pamięć jest lokalna i rozdzielona według profili przeglądarki. Nowa rozmowa zmienia historię bieżącego dialogu, zachowując zapisane informacje.

Zapis obejmuje źródło użytkownika, temat, pochodzenie oraz stan informacji. Rozpoznana spójna wypowiedź użytkownika nie jest automatycznie uznawana za fakt o świecie. Nierozstrzygnięta treść może zostać przywołana jako dokładny cytat. Odpowiedzi modelu nie są w tym trybie obserwacjami do zapisu.

Początkowy limit wynosi 10 000 wpisów i 64 MiB treści; może rosnąć do 200 000 wpisów i 1 GiB treści. To limity logiczne, bez rezerwowania od razu takiej przestrzeni. Fizyczna baza z indeksami zajmuje dodatkowe miejsce. Po osiągnięciu limitu nie nadpisuje się po cichu starszych źródeł.

Tematy mają powiązania przez wspólne obiekty. Dostępne są wybór kontekstu, uśpienie i zamknięcie tematu, jawne rozstrzyganie sprzeczności, cofanie jednej lub dwóch decyzji, pauza zapisu i odczytu, eksport oraz potwierdzane wyczyszczenie. Wątpliwość dotycząca kontekstu powoduje pytanie do użytkownika. Zamknięty temat wymaga ponownego otwarcia.

## Sprawdziany na danych przykładowych

| Zakres | Wynik |
|---|---:|
| Zapis, trwałość, profile, konflikty, cofanie, rozmiar i równoległe zapisy | 18/18 |
| Trzy informacje przywołane po nowej rozmowie w aplikacji | 3/3 |
| Integracja HTTP: nowa rozmowa, pamięć, korekty, pauza, tematy i ochrona żądań | 20/20 |
| Powtarzane pytania po nowej rozmowie: przed / po | 0/15 → 15/15 |
| Wyszukiwanie w bazie 50 000 przykładowych wpisów | 60/60 |

Trzy informacje dotyczyły kolorów plecaków i położenia klucza. To ograniczona próba przywoływania podanych źródeł, nie sprawdzian dowolnej rozmowy.

## Czasy odpowiedzi

Pełne lokalne żądanie HTTP, 15 próbek na wariant: mediana **207,872 → 214,525 ms**, p95 **248,870 → 403,770 ms**. Obejmuje aplikację, JSON i lokalne połączenie; bez renderowania przeglądarki. W tej próbie poprawił się dostęp do informacji, a pełna odpowiedź nie przyspieszyła. Przy tak małej liczbie próbek p95 jest bardzo wrażliwe na pojedyncze opóźnienie.

Samo wyszukiwanie w niezmienionej bazie 50 000 wpisów, 60 zapytań: mediana **1066,448 → 14,206 ms**, p95 **1771,614 → 61,333 ms**. Poprawka wybiera najpierw rzadsze słowa z indeksu. Ten pomiar nie obejmuje analizy językowej, generowania ani HTTP.

## Osobny trening językowy

Wytrenowano czytnik ról czasowych i dopasowano do niego oba enkodery, pamięć H512 oraz generator. Sześć macierzy reguł pozostało bez zmian. Pytania wymagające wcześniejszej informacji: **5/12 → 7/12**. Próby stanu i zakresu danych: **28/28**. Chronione odpowiedzi: **56/56**. W rozmowach dwóch i trzech tur wynik ścisłego porównania wyniósł **7/8**; w pozostałym przypadku odpowiedź była krótsza i zachowała sens. Tych wyników nie należy sumować.

Wybrany wspólny zapis badawczy: **23 542 811 parametrów**, około **94,67 MB**. Osobny czytnik i środowisko wykonawcze nie są w tej liczbie uwzględnione. Model nie osiągnął wymaganego poziomu swobodnej rozmowy. Pamięć źródeł w aplikacji jest odrębna od tego treningu.

## Odniesienia i dalsza integracja

Przyjęto duże archiwum oraz niewielką porcję źródeł dobieraną do pytania. Tematy nie są odizolowanymi silosami. Obecny odczyt korzysta z indeksu tekstowego, odmiany słów i jawnych relacji; nie wdrożono tu wyszukiwania przez wektory semantyczne.

Punkty odniesienia: [MemGPT](https://arxiv.org/abs/2310.08560), [bloki pamięci Letta](https://docs.letta.com/v1-sdk/memory/memory-blocks), [pamięć LangGraph](https://docs.langchain.com/oss/python/concepts/memory), [LongMemEval](https://arxiv.org/abs/2410.10813), [zarządzanie kontekstem Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).

Adaptacja nowej pamięci do MUZ i walidatora jest kolejnym etapem. Docelowo walidator ma prowadzić naukę z podpowiedziami i kontrolą kroków; samo podłączenie pamięci nie stanowi potwierdzenia tej umiejętności. Osobne README zostaną zaktualizowane po testach integracji. Automatyczne uczenie wag z internetu pozostaje wyłączone.
