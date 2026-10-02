# AI-SI



Lokalny interfejs SI i narzędzia do eksperymentów z uczeniem programowania. Prywatny silnik korzysta obecnie z Qwena; publiczne narzędzia historycznego treningu Bielika pozostają w repo.



**Repozytorium nie zawiera głównego rdzenia SI/TIMDR ani jego prywatnych algorytmów.** Nie zawiera również wag modeli, checkpointów i pamięci użytkownika. Publikujemy interfejs, integrację, narzędzia treningowe i testy. [Dokładny zakres](docs/PUBLIC_SCOPE.md).



## Narzędzie SymPy i status prac

Lokalny SI obsługuje SymPy oraz ograniczony, regułowy przekład prostych polskich równań. Przykład: „dwa razy x plus trzy równa się jedenaście” daje `x = 4`. **12/12 testów funkcjonalnych przeszło. To dodatek narzędziowy, nie trening ani dowód przewagi TIMDR.** Wagi nie zmieniły się. Dalszy trening został wstrzymany; obecne funkcje pozostają dostępne. [Zakres i ograniczenia](docs/SI_SYMPY_2026-10-02.md). Publikujemy tylko dokumentację tej aktualizacji, bez kodu SI.

## Aktualizacja lokalnego silnika: Qwen i matematyka



Qwen3-4B-Instruct-2507 zastąpił Bielika w prywatnym silniku: rozmowie po polsku, analizie źródeł/plików, generowaniu kodu i przekładzie poleceń matematycznych. Mała próba matematyczna: **Qwen 8/8, Bielik 3/8**; regresja Qwena 8/8. Trzy odmowy realizuje kontrola wejścia, pięć pozostałych zadań bada przekład planu i obliczenie. Dalsze osiem prób funkcjonalnych Qwena przeszło, ale nie jest to szeroki benchmark.



Dwa moduły matematyczne mają po 256 neuronów ukrytych. Wyniki: pojedyncze działania 140/140 i 282/282 regresji; pięć planów dwuetapowych 96/96 i 192/192 regresji. **Podwojenie ze 128 do 256 zachowało wynik, nie wykazało poprawy.** To kontrolowana gramatyka z kalkulatorem i walidatorem, nie pełna nauka matematyki ani izolowany dowód przewagi TIMDR.



Aktywny Qwen: **2,50 GB**, moduły matematyczne razem **4,21 MB**. Bielik zachowany jako nieaktywna kopia (1,70 GB). [Opis, ograniczenia i wyniki](docs/SI_QWEN_MATEMATYKA_2026-10-02.md) · [liczby JSON](docs/SI_QWEN_MATEMATYKA_2026-10-02.json). Ta aktualizacja publikuje wyłącznie dokumentację; kod SI i wagi pozostają lokalnie.



## Wyniki lokalnego SI — 2 października 2026



Uczone rozszerzenie negacji zachowało wcześniejsze umiejętności: **1440/1440 nowych grafów i 720/720 regresji**, w trzech przebiegach na tych samych zestawach. Dokładne narzędzie SI z walidatorem rozwiązało **24/24 nowych rachunków**; Bielik bez adaptera **3/24**. Obliczenia wykonuje narzędzie, nie wyuczona sieć. Badano ograniczoną domenę rozwojową; nie wykazano jeszcze samodzielnego doboru narzędzi ani ogólnej przewagi SI.



[Opis eksperymentu i komplet wyników w GIA-TIMDR](https://github.com/jbackk-lang/GIA-TIMDR/blob/main/docs/SI_NEGACJA_WALIDACJA_2026-10-02.md). Kod rozszerzenia i kalkulatora SI, checkpointy oraz pamięć pozostają lokalne. Nowy checkpoint negacji: **7,6 KB**; w chwili tej wcześniejszej próby folder zajmował około **1,84 GB**, w tym Bielik **1,70 GB**.



## Uruchomienie interfejsu



1. Uruchom prywatny silnik w sąsiednim folderze `Al-SI`: `Uruchom_SI_w_przegladarce.bat` (port 8771).

2. W tym repo uruchom `Uruchom_AI_SI.bat` albo `python run_ui.py`.

3. Publiczny interfejs otworzy się pod http://127.0.0.1:8780/. Można wybrać inny lokalny silnik przez `--backend http://127.0.0.1:PORT`.



Interfejs obsługuje rozmowę, sprawdzone przykłady i generowanie Pythona z testami, źródła internetowe oraz katalogi/pliki wskazane przez użytkownika. Funkcje te wykonuje osobny lokalny silnik; bez niego interfejs pokaże komunikat o braku połączenia. Domyślna konfiguracja nie przesyła rozmów ani plików do usług AI. Hasło wyszukiwania trafia do Wikipedii; odczyt strony łączy się z jej serwerem.



## Katalogi



| Katalog | Zawartość |

|---|---|

| src/ai_si | Publiczny gateway i integracja modelu językowego |

| web | Okno przeglądarkowe |

| tools/training | Trening adaptera Bielika, bez prywatnego rdzenia |

| tools/testing | Ograniczony tester kodu Python |

| tools/release | Kontrola plików przed publikacją |

| tests | Testy publicznych modułów |

| data/coding_adapter | Mały zbiór ćwiczeń i testów |

| docs | Zakres publikacji, protokół i wyniki |

| scripts | Przygotowanie lokalnego commitu |



## Rozmiar



Aktywny lokalny Qwen Q4_K_M zajmuje **2 497 280 448 bajtów (2,50 GB)**; dwa moduły matematyczne razem **4 212 272 bajty (4,21 MB)**. Nieaktywny Bielik Q8_0 zajmuje **1 699 568 288 bajtów (1,70 GB)**. Wszystkie wagi pozostają poza Git. Publiczne źródła oraz dane pilotażowe są małe; ich dokładny rozmiar podano w końcowym raporcie. Własny rdzeń, pamięć, runtime i środowisko Python są osobnymi składnikami i nie wchodzą do tego repo.



## Historyczny trening programowania z Bielikiem



To trening małego adaptera przy zamrożonej bazie Bielika. Bazę Q8_0 odtwarzamy do bfloat16 w RAM, bez zapisywania drugiej pełnej kopii modelu. Wymagania: `pip install -r requirements-training.txt`. Ustaw `SI_MODEL_PATH` na istniejący plik GGUF i `SI_LLAMA_SERVER` na oficjalny llama-server.exe. Następnie uruchom `python tools/training/prepare_runtime.py` i `python tools/training/run_bielik_coding_adapter.py`.



[Protokół](docs/BIELIK_CODING_PROTOCOL.md) · [Wynik](docs/TRAINING_RESULT.md). Pilot obejmuje 12 przykładów treningowych, 6 zadań końcowych i 3 krótkie kontrole polskiego. Nie jest benchmarkiem ogólnej inteligencji. Kod testujemy w ograniczonym podzbiorze języka; nie jest to uniwersalny bezpieczny wykonawca dowolnych skryptów.



## Testy i publikacja



W PowerShell ustaw `$env:PYTHONPATH="src;tools/testing"`, a potem uruchom `python -m unittest discover -s tests -v`. Przed commitem: `python tools/release/prepare_commit.py`. Pomocnik Python działa także przy wyłączonych skryptach PowerShell, zachowuje początkową historię GitHub i sprawdza pliki. Nie wykonuje commitu ani push. Przy ostrzeżeniu o właścicielu repo dodaj wyjątek tylko dla tego katalogu: `git config --global --add safe.directory C:/Users/jback/Downloads/a/AI-SI-git`.



Historia dotychczasowego prywatnego projektu pozostaje w Al-SI. To publiczna część integracyjna; nie kopiujemy historii ani kodu głównego rdzenia. Nie dołączono licencji do prywatnego rdzenia i nie sugerujemy praw do zewnętrznych wag innych niż licencja ich producenta.



## Wynik wcześniejszego pilotażu adaptera Bielika



Adapter po korekcie testera: 3/6 → 4/6; dodatkowe zadania: 0/3 → 1/3; krótkie próby polskiego: 2/3 → 2/3. To mała poprawa w eksperymencie, nie pełny asystent programistyczny. Adapter zajmuje 312 800 bajtów i pozostaje poza Git. [Pełny wynik i korekta oceny](docs/TRAINING_RESULT.md).
