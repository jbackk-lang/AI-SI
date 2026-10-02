# Lokalna SI: matematyka i podmiana modułu językowego — 2 października 2026

Ten raport opisuje prywatny silnik. Nie zawiera jego kodu, wag, checkpointów, pamięci ani danych użytkownika. Publiczny interfejs nie otrzymał w tej aktualizacji nowych funkcji kodowych; opisujemy zmiany wykonane lokalnie. [Zestawienie liczb](SI_QWEN_MATEMATYKA_2026-10-02.json).

## Co zmieniono

Dodano wyuczone odczytywanie ograniczonych poleceń rachunkowych i pięć planów dwuetapowych, w tym resztę z zakupów. Sieć wybiera działanie/plan, kontrolowana gramatyka sprawdza zgodność, dokładny kalkulator wykonuje rachunek, a osobny walidator kontroluje wartość wyrażenia. Nie jest to swobodne rozumienie matematyki ani dowodzenie.

Warstwę każdego z dwóch modułów zwiększono ze 128 do 256 neuronów. Nie oznacza to 256 neuronów całego modelu językowego. Czytnik ma 526 086 parametrów, planowanie 525 829. Wersje 128 i 256 mają identyczne wyniki na tym porównaniu; większa pojemność nie dała wykazanej poprawy.

| Moduł 256 | Nowe wartości w znanych sformułowaniach | Regresja | Błędne zaakceptowane odpowiedzi |
|---|---:|---:|---:|
| Pojedyncze działania | 140/140 | 282/282 | 0 |
| Pięć planów dwuetapowych | 96/96 | 192/192 | 0 |

Nowość tej próby dotyczy liczb, nie całkowicie nowego języka. Przypadki odmów były ponownie wykorzystane. Jeden seed treningu; nie jest to niezależny szeroki holdout. Proste reguły także rozwiązują kontrolowane plany — wynik nie izoluje przewagi rdzenia TIMDR.

## Qwen zamiast Bielika

Porównano ten sam prompt, temperaturę zero, limit 96 tokenów i identyczny most matematyczny. Lokalny Qwen3-4B-Instruct-2507 Q4_K_M: 8/8 nowych zadań, w tym 5/5 poprawnych planów i obliczeń. Bielik Q8_0: 3/8, w tym 0/5 poprawnych planów. Regresja Qwena: 8/8. Zero błędnych zaakceptowanych odpowiedzi.

Trzy odmowy w każdym zestawie wykonuje kontrola wejścia przed modelem. Nie są dowodem, że sam Qwen rozumie negację i rozpoznaje wszystkie braki danych. Pięć zadań obliczeniowych to mała próba integracji w znanej gramatyce. Różne kwantyzacje ograniczają interpretację porównania.

Następnie Qwen przeszedł 8/8 prób funkcjonalnych: krótki polski opis, imię z historii, liczba ze źródła, brak odpowiedzi w źródle, trzy funkcje Python sprawdzone podanymi testami (suma, duplikaty z zachowaniem kolejności, palindrom) i regresja matematyczna. To nie szeroki benchmark rozmowy/programowania ani gwarancja odporności na instrukcje w źródłach. Dodatkowo przeszło osiem testów integracji i modułów.

Qwen jest teraz domyślną warstwą językową prywatnego interfejsu: rozmowa, źródła/pliki, generowanie kodu i matematyka. Jeden wspólny proces ładuje wagi. Nie trenowano wag Qwena. Adapter Bielika nie jest używany z Qwenem. Bielik pozostaje lokalnie jako nieaktywna kopia. Historyczne publiczne narzędzia treningowe Bielika pozostają w repo; ta aktualizacja dokumentacyjna ich nie zmienia.

## Rozmiar i ograniczenia

| Składnik | Bajty | Rozmiar dziesiętny |
|---|---:|---:|
| Aktywny Qwen Q4_K_M | 2 497 280 448 | 2,50 GB |
| Dwa moduły matematyczne 256 | 4 212 272 | 4,21 MB |
| Nieaktywny Bielik | 1 699 568 288 | 1,70 GB |
| Oba zachowane modele językowe | 4 196 848 736 | 4,20 GB |

Cały folder prywatnej SI orientacyjnie około 4,34 GB plus kolejne artefakty; nie jest to dokładny nowy pomiar katalogu. Pierwsze polecenie Qwena w próbie matematycznej trwało około 80 sekund na CPU, w tym około 72 sekundy przetwarzania wspólnego promptu. Kolejne wywołania mogą korzystać z cache; nie jest to uniwersalny benchmark szybkości.

Swobodne historyjki, ukryte założenia, równania, geometria, dowody, podatki i rabaty pozostają poza potwierdzonym zakresem modułów matematycznych. Odpowiedzi rozmowy i interpretacje źródeł pozostają odpowiedziami modelu. Walidator sprawdza rachunek, nie prawdziwość wszystkich faktów ani sens dowolnego zadania.

## Pochodzenie modelu

Bazowy model: [Qwen/Qwen3-4B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507). Pobrana społecznościowa konwersja GGUF: [lmstudio-community/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/lmstudio-community/Qwen3-4B-Instruct-2507-GGUF), plik Q4_K_M. SHA256 pobranych wag zweryfikowano: `8cdb57cbb880d313736a9bc4e3d3d2485f145b5e19cf33783746e753e82641fc`. Wagi pozostają poza Git.
