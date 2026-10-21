# AI-SI-TSI — lokalny asystent TSI

**Stan potwierdzony: 21 października 2026.** TSI łączy własne uczone modele, macierze językowe, pamięć dokumentów i narzędzia obliczeniowe. Działa lokalnie. Nie korzysta z wag Bielika ani Qwena.

Repozytorium opisuje projekt. Ta aktualizacja zawiera dokumentację i podgląd panelu; **nie publikuje kodu obecnego TSI, wag, danych treningowych ani dokumentów użytkownika**. Starsze pliki repozytorium dotyczą wcześniejszego AI-SI.

## Co jest dostępne w lokalnej aplikacji

| Obszar | Możliwości i zakres |
|---|---|
| Tekst i dokumenty | Wczytywanie materiału, pytania do źródła, skróty, listy i przygotowanie wiadomości z podanej treści; zakres poleceń jest ograniczony |
| Lokalny słownik | Polski Wikisłownik przez Kaikki: 114 215 różnych haseł, 125 720 wpisów i 1 437 842 powiązania form odmiany. Definicje i przykłady są dostępne offline; nie oznacza to opanowania swobodnej rozmowy przez sieć |
| Konkret z definicji | Uczony wybór rodzaju pytania i jawna matryca relacji odczytują cechę, uczestników oddziaływania, przeznaczenie, skład lub zapisany warunek z aktywnego hasła. Zakres obejmuje rozpoznane konstrukcje; brak jednoznacznego fragmentu powoduje prośbę o doprecyzowanie |
| Pliki | TXT, MD, CSV, PDF, DOCX i DOC oraz wklejanie całej treści; do 10 plików, 8 MB na plik, 32 MB łącznie; DOC wymaga Worda, skany wcześniejszego OCR |
| Pamięć i poprawki | Wersjonowane źródła, korekty i cofanie zmian, trwałe notatki, historia oraz eksport JSON |
| Matematyka | Obsługiwane polecenia arytmetyczne, kalkulator naukowy, równania, pochodne, całki, macierze i wykresy przez narzędzia obliczeniowe |
| Logika T/F/U | Uczony moduł operatorów AND, OR, NOT, IMPLIES i EQUIV; nawiasy, symbole matematyczne i kolejne kroki wyniku; formalne wyrażenia w panelu PL/EN |
| Analiza sygnałów | Serie liczbowe JSON, wykres oraz uczona ocena wybranych trendów, anomalii i okresowości |
| Kontrola odpowiedzi | Ponowienie obsługiwanych obliczeń i sprawdzenie cytatu w zapisanym źródle; brak pełnego audytu dowolnej wypowiedzi |
| Obsługa | Panel PL/EN, Enter wysyła polecenie, Shift+Enter dodaje wiersz, nowa rozmowa i pomoc z przykładami |

Funkcje narzędziowe aplikacji i sprawność generatora tekstu są oceniane osobno. Samo korzystanie z notatek lub prowadzenie rozmowy **nie uruchamia automatycznie treningu wag**.

## Co potwierdzono dla nowego modelu dwupołówkowego

Dwie aktywne połówki przekazują reprezentacje do wspólnego dekodera odpowiedzi. Wcześniejszy wspólny trening objął obie sieci i obie pamięci H512. Ostatni zakończony etap ćwiczył odczyt odpowiedzi przez **400 kroków z powtórkami**; podpowiedź stopniowo wycofano. Osobne macierze odczytu definicji chronią je przed pogorszeniem podczas ćwiczenia faktów.

**Poniższe wyniki dotyczą zapisanych wag bez podpowiedzi. Model nie został jeszcze podmieniony w działających panelach.**

| Sprawdzian | Wynik |
|---|---:|
| Wcześniejsze przypadki ucinania odpowiedzi | **8/8**, przed powtórkami 6/8 |
| Nowy odłożony zestaw krótkich faktów | **24/24**, wcześniej 23/24 |
| Osobny zestaw prostych definicji | **16/16**, zachowany |
| Wszystkie starsze zadania łącznie | **53/85**, wcześniej 49/85 |
| Powtórne wczytanie wag i ponowienie ośmiu przypadków | **8/8** |

W tych zestawach nie utracono żadnej wcześniej poprawnej odpowiedzi. Liczono pełną odpowiedź, a nie samo wskazanie źródła. Starsze zestawy są testami regresji; nie stanowią nowych, nieznanych modelowi sprawdzianów. Zestawy mogą zawierać warianty tego samego typu zadania.

## Czego model jeszcze nie opanował

Szersze starsze testy pokazują **37/40** na prostych faktach, ale tylko **7/30** na definicjach, **9/13** na rozpoznawaniu braku informacji i **0/2** na swobodnym pisaniu oraz wyjaśnianiu. Dlatego 16/16 prostych definicji nie oznacza opanowania dowolnych pojęć.

Najważniejsze błędy to ucinanie końcówek, powtarzanie fragmentów słów i zdań, wypisywanie niewłaściwej etykiety S1/S2 mimo poprawnego wyboru źródła oraz odpowiadanie na podstawie materiału, który nie zawiera potrzebnej informacji. Nie potwierdzono jeszcze uniwersalnej rozmowy, swobodnego pisania ani samodzielnego uczenia dowolnej wiedzy.

## Jak korzystać

W istniejącej lokalnej instalacji uruchom **URUCHOM_TSI.bat**. Panel jest dostępny pod `http://127.0.0.1:8791/`. **ZATRZYMAJ_TSI.bat** zatrzymuje aplikację. To repozytorium dokumentacyjne nie jest samodzielnym instalatorem aktualnej wersji.

| Przykład | Zastosowanie |
|---|---|
| `Przeczytaj: Anna daje książkę Markowi.` | Dodanie materiału źródłowego |
| `słownik: państwo` lub `słownik: grawitacja` | Odczyt znaczeń z lokalnej bazy, bez pobierania strony |
| `Komu Anna daje książkę?` | Pytanie do podanego tekstu |
| `Zamień Markowi na Ewie` oraz `Cofnij` | Korekta źródła i cofnięcie zmiany |
| `Wyznacz pochodną i całkę: x^2` | Skorzystanie z narzędzi matematycznych |
| `logika: NOT (T AND U) OR F` | Logika trójstanowa: T — prawda, F — fałsz, U — nieznane; wynik z krokami |
| `zapamiętaj: termin = piątek` | Trwała notatka |
| `nowy temat` | Rozpoczęcie nowego kontekstu rozmowy |

## Rozmiar i sprzęt

Lokalna baza słownikowa zajmuje **157 716 480 B (150,4 MiB)**. Jest zasobem danych, osobnym od wag modeli. Źródło: [polski Wikisłownik przez Kaikki/Wiktextract](https://kaikki.org/dictionary/rawdata.html); odsyłacze do haseł i informację o pochodzeniu zachowano w bazie.

| Zapisany model | Parametry | Plik wag |
|---|---:|---:|
| Wspólny H512 i czytnik w dotychczasowej aplikacji, runtime 0.6.0 | 2 613 105 | 10 587 275 B |
| Dwupołówkowy model po powtórkach i ochronie odczytu definicji | **10 147 343** | **40 944 075 B — 40,94 MB / 39,05 MiB** |

Rozmiar wag nie jest rozmiarem całej instalacji ani zapotrzebowaniem na RAM. Ostatnich testów nie wykonywano na GPU: użyto CPU. Obsługa CUDA/MPS wymaga odpowiedniego sprzętu i środowiska. W tej aktualizacji nie wydano nowej paczki portable.

## Podgląd aplikacji

Zrzuty z 20 października 2026 przedstawiają działający panel i przykładowe dane; nie pokazują wdrożenia nowego modelu dwupołówkowego.

![Rozmowa i polecenia w panelu TSI](https://raw.githubusercontent.com/jbackk-lang/AI-SI-TSI/main/docs/tsi-panel-2026-10-20.png)

![Wczytywanie dokumentów i wklejanie treści](https://raw.githubusercontent.com/jbackk-lang/AI-SI-TSI/main/docs/tsi-documents-2026-10-20.png)

Przebieg integracji, wcześniejsze wyniki, eksperymenty i poprzednie README: **[historia rozwoju TSI](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/HISTORIA_TSI.md)**.

Powiązany projekt: [TSI-math-validator-5](https://github.com/jbackk-lang/TSI-math-validator-5).
