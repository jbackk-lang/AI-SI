# AI-SI

Lokalny interfejs SI, integracja z polskim modelem Bielik i narzędzia do eksperymentów z uczeniem programowania.

**Repozytorium nie zawiera głównego rdzenia SI/TIMDR ani jego prywatnych algorytmów.** Nie zawiera również wag modeli, checkpointów i pamięci użytkownika. Publikujemy interfejs, integrację, narzędzia treningowe i testy. [Dokładny zakres](docs/PUBLIC_SCOPE.md).

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

Wagi Bielika Q8_0 zajmują **1 699 568 288 bajtów (1,70 GB)** i pozostają poza Git. Publiczne źródła oraz dane pilotażowe są małe; ich dokładny rozmiar podano w końcowym raporcie. Własny rdzeń, pamięć, runtime i środowisko Python są osobnymi składnikami i nie wchodzą do tego repo.

## Trening programowania

To trening małego adaptera przy zamrożonej bazie Bielika. Bazę Q8_0 odtwarzamy do bfloat16 w RAM, bez zapisywania drugiej pełnej kopii modelu. Wymagania: `pip install -r requirements-training.txt`. Ustaw `SI_MODEL_PATH` na istniejący plik GGUF i `SI_LLAMA_SERVER` na oficjalny llama-server.exe. Następnie uruchom `python tools/training/prepare_runtime.py` i `python tools/training/run_bielik_coding_adapter.py`.

[Protokół](docs/BIELIK_CODING_PROTOCOL.md) · [Wynik](docs/TRAINING_RESULT.md). Pilot obejmuje 12 przykładów treningowych, 6 zadań końcowych i 3 krótkie kontrole polskiego. Nie jest benchmarkiem ogólnej inteligencji. Kod testujemy w ograniczonym podzbiorze języka; nie jest to uniwersalny bezpieczny wykonawca dowolnych skryptów.

## Testy i publikacja

W PowerShell ustaw `$env:PYTHONPATH="src;tools/testing"`, a potem uruchom `python -m unittest discover -s tests -v`. Przed commitem: `python tools/release/prepare_commit.py`. Pomocnik Python działa także przy wyłączonych skryptach PowerShell, zachowuje początkową historię GitHub i sprawdza pliki. Nie wykonuje commitu ani push. Przy ostrzeżeniu o właścicielu repo dodaj wyjątek tylko dla tego katalogu: `git config --global --add safe.directory C:/Users/jback/Downloads/a/AI-SI`.

Historia dotychczasowego prywatnego projektu pozostaje w Al-SI. To publiczna część integracyjna; nie kopiujemy historii ani kodu głównego rdzenia. Nie dołączono licencji do prywatnego rdzenia i nie sugerujemy praw do zewnętrznych wag innych niż licencja ich producenta.
