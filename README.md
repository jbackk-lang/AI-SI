# AI-SI

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23222487.svg)](https://doi.org/10.5281/zenodo.23222487)

Eksperymentalny system inspirowany TIMDR jako punktem wyjścia do budowy sterownika współpracy.

## Aktualny stan — 9 października 2026

Własny mały model językowy SI działa bez Qwena, z kontrolą źródeł, mostem sesji, wyborem strategii i ograniczoną obsługą polskiego; wagi języka trenujemy po angielsku. Zadania słowne są sprawdzane na prawdziwych zadaniach z otwartych zbiorów, a polskie pytania obsługuje maper z katalogiem sprawdzonych zdań.

## Najnowsza aktualizacja — 9 października 2026

- **Fakty w swobodnej rozmowie:** SI sama sprawdza fakty w kilku źródłach: Wikipedii polskiej i angielskiej (czytanej tym, czego nauczyła się w pętli), Wikidanych i Bibliotece Narodowej. Każde źródło jest pokazane z ✓ albo ✗ i adresem. Potwierdza tylko wtedy, gdy zgadzają się co najmniej dwa źródła i żadne nie przeczy. Zamrożony test: 76 ze 126 pytań po angielsku i 78 ze 126 po polsku potwierdzonych.
- **Sieć czytająca (bez Qwena):** mała sieć neuronowa wskazuje w artykule datę albo liczbę odpowiadającą na pytanie o fakt. Uczy się na przykładach ocenionych przez Wikidane jako sędziego; automat rośnięcia zaczyna od 8 neuronów ukrytych i rośnie tylko, gdy rośnie trafność na walidacji (zatrzymał się na 8). Działa tylko tam, gdzie wyuczone wzorce nie znalazły odpowiedzi, i tylko powyżej progu pewności wybranego na walidacji. Zamrożone hasła angielskie 83 → 91 z 215, 0 błędów czytania; model 1,5 MB.
- **Słownik:** „co to jest rakieta?”, „co znaczy …?” → dosłowne znaczenia ze Słownika PWN i Wikisłownika oraz początek hasła z Wikipedii, z adresami.
- **Ciekawość:** gdy SI nie zna odpowiedzi na pytanie o wiedzę, sama szuka w Wikipedii i słowniku („Sama tego nie wiem, ale sprawdziłam…”) i zapisuje brak w dzienniku. Pętla nauki czyta najpierw hasła, o które pytał użytkownik.
- **Jeden koordynator nauki:** nauka z Wikipedii i samopoprawa modułów w jednej pętli; SI wybiera moduł według świeżych braków z rozmów.
- **Dziś i święta:** „jaka dziś data?”, „święta w 2026”, „kiedy Wielkanoc w 2027?” — polskie dni wolne od pracy według ustawy; Wielkanoc liczona dwiema niezależnymi metodami (zgodne dla lat 1583–4099).
- **Poprawianie literówek:** gdy SI nie zrozumie wiadomości, poprawia literówki słownikiem SJP.PL (brakujące polskie znaki, przestawione litery, jedna litera za dużo, za mało lub zamieniona) i pokazuje „Zrozumiałam: …”. Poprawka jest przyjmowana tylko wtedy, gdy na poprawione zdanie odpowiada konkretny moduł.
- **Własne pytania i mapa wiedzy:** SI zapisuje, co sprawdziła, i widzi swoje dziury („znam urodzenie, nie znam śmierci”). Pyta sama o powiązane hasła (nauczyciel, rodzina, miejsce urodzenia, dzieła). Gdy źródła się różnią, szuka wyjaśnienia w artykułach (kalendarz juliański, data chrztu, data nieznana) i rozpoznaje własne błędy czytania. Wybiera to, w czym najszybciej robi postęp. Gdy komputer jest bezczynny, uczy się w tle. W rozmowie: „czego się dowiedziałaś?”, „sprawdź dlaczego”, „co wiesz o …?”.
- **Wiedza o świecie w rozmowie:** „co nowego na świecie?”, „jakie wybory są w tym miesiącu?”, „jakie trwają wojny?”, „co słychać we Francji?”, „ile dni do wyborów w Hiszpanii?” — z mapy wiedzy, którą SI zebrała sama, od razu i bez internetu; fakt potwierdzony na mapie podaje z datą sprawdzenia i źródłami.
- **Samoobsługa modułów:** „co potrafisz?” → lista modułów z przykładami; „jak działa moduł dat?” → opis modułu z jego kodu; „sprawdź się” → SI uruchamia swoje zamrożone testy i sprawdza słownik, pakiety oraz dostęp do źródeł (✓/✗); przy pytaniu bez potrzebnej części (np. bez ścieżki pliku) podpowiada poprawny format.

[Literówki, samoobsługa i Wikisłownik — 8 października](docs/SI_LITEROWKI_I_MODULY_2026-10-08.md) · [Ciekawość, mapa wiedzy, nauka w tle](docs/SI_CIEKAWOSC_2026-10-08.md) · [Sieć czytająca — 9 października](docs/SI_SIEC_CZYTAJACA_2026-10-09.md).

## Aktualizacja — 7 października 2026

- **Most WordNet:** nieznany czasownik w zadaniu słownym jest zamieniany na znany czasownik SI tej samej operacji przez otwarty angielski WordNet, tylko gdy wszystkie znaczenia słowa są zgodne. Nowy test zamrożony przed pracą 208→286/300; 0 błędnych potwierdzeń.
- **Most pytań:** nieznane sformułowanie pytania zamieniane na znane pytanie tej samej klasy. Nowy zamrożony test 247→272/300.
- **Sprawdzian na prawdziwych zadaniach:** na 1730 zadaniach z otwartych zbiorów SVAMP/ASDiv parser trafiał tylko 10%, czyli prawie jak losowanie; mosty działały tylko w świecie własnych szablonów (wynik negatywny).
- **Nowe podejście:** liniowy klasyfikator działania uczony na otwartym MAWPS, wskazówki ról liczb (wynik, stan początkowy, porównanie, grupy) i czytnik kontekstu czytający zadanie słowo po słowie, połączony z modelem ról. Połowa testu nieużywana do strojenia 451→512; w SI prawdziwe zadania 178→944/1730. Odpowiedzi nowego modelu zawsze wymagają potwierdzenia; 0 błędnych potwierdzeń.
- **Polski maper pytań:** katalog sprawdzonych zdań (wzór nauczyciela z 4 października) i czytnik kontekstu po formach SJP.PL. Zamrożony test 44→64/72; „nie rozpoznaję” 21→5, błędne intencje 7→3.
- **Lokalny tłumacz PL→EN:** neuronowy Opus-MT (218 MB, ok. 0,1–0,4 s na zdanie) przed angielskim rdzeniem SI. SI sprawdza, czy liczby i przeczenia przeszły bez zmian. Polskie zadania słowne 24→51/150.
- **Tabele, dokumenty, daty:** nowe moduły liczą na tabelach i arkuszach (CSV, XLSX), odpowiadają na pytania do własnych dokumentów (TXT, MD, DOCX, PDF) z cytatem zdania źródłowego oraz liczą daty i terminy. Każdy wynik jest sprawdzany drugim, niezależnym obliczeniem albo pełnym dopasowaniem pytania do zdania; testy zamrożone przed pisaniem kodu: tabele 15/15, dokumenty 15/16, daty 9/11 (pozostałe poprawnie niepotwierdzone); 0 błędnych potwierdzeń.
- **Nauka z Wikipedii (angielskiej i polskiej):** SI czyta losowe artykuły i sama wybiera, czego się uczy: rodzaj faktu, na którym najwięcej traci, i rodzaj haseł, z których najwięcej się uczy. Wikidata służy tylko jako niezależny sędzia; SI nie zapamiętuje faktów, uczy się czytać — mostów słów („birth” = „born”) i wzorców zapisu dat („( [DATA] –”, „– [DATA]”, „ur. [DATA]”, „zm. [DATA]”). Podmiana tylko po poprawie na zamrożonych hasłach; każdy język ma własną konfigurację; automat rośnięcia poszerza okno wzorców przy zastoju. Zamrożone hasła: angielskie 0 → 77 z 215 pytań, polskie 0 → 87 z 287 (stan 8 października), 0 błędów czytania. Podgląd na żywo z przyciskiem zatrzymania.
- **Pytania o fakty w czacie:** „Kiedy urodził się Mikołaj Kopernik?”, „When did Marie Curie die?” — SI znajduje hasło (polskie pytanie przez polską wyszukiwarkę), wycina odpowiedź z artykułu z cytatem zdania i sprawdza ją w Wikidacie. Potwierdzone tylko przy zgodności obu źródeł; przy różnicy pokazuje obie wartości. Zamrożony test: 62 ze 126 pytań potwierdzonych dwoma źródłami, po polsku i po angielsku.
- **Pętla samouczenia:** koordynator nauki dla modułów z automatem rośnięcia pojemności, okienkiem podglądu i podmianą wag tylko po poprawie, z kopią zapasową.
- **Wyniki negatywne:**
  - dane pisane przez Qwena od zera i z przepisania zadań MAWPS nie poprawiły wyniku na straży;
  - więcej neuronów przy cechach bez kolejności słów nie pomogło;
  - kalibracja bezpiecznego potwierdzania nie dała zera błędów (ok. 10%).

[Dokładne wyniki, metody i ograniczenia — 6–7 października](docs/SI_NAUKA_2026-10-06.md). Testy użyte do wyboru wersji są odtąd rozwojowe. [Aktualizacja z 6 października](README_DETAILS.md#aktualizacja--6-października-2026-cały-dzień) jest w historii.

## Osiągnięcia

SI to mały, lokalny system: kilka własnych sieci po kilkaset tysięcy parametrów oraz dokładne narzędzia. Mówi, gdy czegoś nie jest pewne.

| Obszar | Co potrafi | Wynik na zamrożonym teście |
|---|---|---|
| **Kontrola odpowiedzi** | Trzy stany: potwierdzone / odrzucone / do potwierdzenia. Niepewne odpowiedzi nie są podawane jako fakt | 0 błędnych potwierdzeń w zadaniach słownych, także na 1730 prawdziwych zadaniach |
| **Odpowiedzi ze źródła** | Odczytuje wartości z podanego tekstu, w tym przy mieszanych wzorcach zdań | 96/96 z kontrolerem |
| **Zadania słowne (angielski)** | Proste zadania jednodziałaniowe: rozpoznaje działanie, liczy dokładnym kalkulatorem | Prawdziwe zadania SVAMP/ASDiv: 944/1730 (55%), zawsze z prośbą o potwierdzenie; znane wzory 297/300 |
| **Polskie pytania o SI** | Rozumie różne sformułowania pytań o pamięć, kalkulator, kod, walidację, kolejność kroków i o siebie | 64/72 (wcześniej 44/72) |
| **Polski interfejs** | Translator obsługiwanych formatów zachowuje zakazy, liczby i warunki; lokalny tłumacz neuronowy PL→EN pod kontrolą SI; polskie zadania słowne z prośbą o potwierdzenie | 10/10 i 5/5; polskie zadania słowne 51/150 |
| **Zakazy i brak danych** | „Nie wykonuj” zatrzymuje działanie; przy braku liczby SI prosi o nią | 10/10 (blokada języka), 5/5 (pętla decyzji) |
| **Strategie i most sesji** | Mała sieć wybiera zachowanie odpowiedzi; wspólny dziennik sesji | 240/240 na stanach walidatora; próba 7/16 → 14/16 |
| **Tabele i arkusze** | CSV i XLSX: suma, średnia, największa, najmniejsza, liczba wierszy; filtry („gdzie Region = North”, „w Krakowie”, „w kwietniu”), grupowanie „według kategorii”, kolumny dat; liczenie dokładne i sprawdzane drugim obliczeniem; nieużyte słowo polecenia → prośba o potwierdzenie | 15/15 |
| **Pytania do dokumentów** | TXT, MD, DOCX, PDF, plik lub folder: odpowiedź wycięta z dokumentu z cytatem (plik, akapit, zdanie); czego nie ma w dokumencie — mówi, że nie ma; kilka pasujących miejsc — pokazuje wszystkie | 15/16, brak informacji poprawnie rozpoznany |
| **Daty i terminy** | Różnica dni, data po N dniach/miesiącach/latach, dzień tygodnia, koniec miesiąca wg k.c., termin w weekend; nieistniejąca data odrzucona | 9/11, pozostałe 2 poprawnie niepotwierdzone |
| **Nauka z Wikipedii** | Sama wybiera, czego się uczy; uczy się czytać artykuły po angielsku i po polsku (mosty słów, wzorce zapisu dat); sędzią jest Wikidata; automat rośnięcia, przycisk „Zatrzymaj naukę” | Zamrożone hasła: en 0 → 77/215, pl 0 → 87/287, 0 błędów czytania |
| **Pytania o fakty** | Daty urodzenia, śmierci, wydania i założenia oraz kto teraz pełni urząd (głowa państwa, premier, władze miasta) — z Wikipedii (pl, en), Wikidanych i Biblioteki Narodowej, z cytatem i adresem każdego źródła; przy różnicy pokazuje wszystkie wartości | Zamrożony test: 68/126 po angielsku, 70/126 po polsku, potwierdzone co najmniej dwoma źródłami |
| **Słownik i definicje** | „co to jest X?”, „co znaczy X?” — Słownik PWN, Wikisłownik, początek hasła z Wikipedii | — |
| **Ciekawość** | Gdy nie wie, sama szuka w źródłach i zapisuje brak dla pętli nauki | — |
| **Dziś i święta** | Dzisiejsza data, polskie dni wolne od pracy, Wielkanoc dwiema niezależnymi metodami | 0 rozbieżności metod w latach 1583–4099 |
| **Literówki** | Poprawia literówki i brakujące polskie znaki, gdy nie zrozumie wiadomości; pokazuje „Zrozumiałam: …” | 1311 tekstów z zamrożonych testów: 0 zmienionych odpowiedzi |
| **Samoobsługa modułów** | „co potrafisz?”, „jak działa moduł …?”, „sprawdź się” (autotest ✓/✗), podpowiedź formatu | 1311 tekstów: 0 przechwyconych |
| **Własne pytania** | Mapa wiedzy z dziurami i powiązaniami; pytania z dziur, powiązań, sporów źródeł i świeżych wydarzeń; fakty, które się zmieniają (urzędy, liczba mieszkańców), sprawdza ponownie i zapisuje zmiany; wyjaśnianie sporów; nagroda za postęp; nauka w czasie bezczynności | 1311 tekstów: 0 przechwyconych; test faktów bez zmian |
| **Wiedza o świecie** | Wiadomości, wybory, konflikty, zawody, wydarzenia kraju i miesiąca, ile dni do wydarzenia — z własnej mapy wiedzy | 1311 tekstów: 0 przechwyconych |
| **Odmiana słów** | Lokalna baza SJP.PL (4,69 mln par forma–lemma) jako pierwsze źródło odmian | — |
| **Samouczenie** | Koordynator nauki: przykłady od nauczyciela → sito → automat rośnięcia pojemności → podmiana wag tylko po poprawie | Pierwsze rundy bez podmiany (zabezpieczenie zadziałało) |

Każdy wynik dotyczy opisanego testu.

[Literówki, samoobsługa i Wikisłownik — 8 października](docs/SI_LITEROWKI_I_MODULY_2026-10-08.md) · [Dokładne wyniki — 6 października](docs/SI_AKTUALIZACJA_2026-10-06.md) · [Historia i wcześniejsze konfiguracje](README_DETAILS.md).

Rozmiary — stan 8 października 2026 (zmierzone na plikach, które czat SI wczytuje):

| Składnik | Rozmiar |
|---|---|
| Własne wagi SI (14 plików: model językowy z głowicami tematu, widoku i odniesienia, polski maper i czytnik kontekstu, bramka i głowica trzech stanów, parsery i czytnik zadań słownych, klasyfikator działania, rodziny polskich zadań, sterownik strategii) | **11,20 MB**, **2,81 mln parametrów** |
| Wyuczona wiedza czytania (mosty, wzorce, katalogi zdań; pliki JSON) | **0,37 MB** |
| Lokalny tłumacz PL→EN Opus-MT | **221,6 MB** |
| Lokalny indeks słownika SJP.PL | **154,55 MB** |

To rozmiary składników, nie kompletnego pakietu z Pythonem i bibliotekami.

## Cytowanie

Wydanie zarchiwizowane w Zenodo: **DOI [10.5281/zenodo.23222487](https://doi.org/10.5281/zenodo.23222487)**.

```
Kielich, J. AI-SI. Zenodo. https://doi.org/10.5281/zenodo.23222487
```

## Zakres publicznego repo

Publiczne repo zawiera interfejs, integrację, narzędzia treningowe, testy i dokumentację. **Rdzeń SI/TIMDR, prywatny silnik, wagi, checkpointy i pamięć pozostają prywatne.** Samo pobranie repo nie udostępnia całego silnika. [Zakres publikacji](docs/PUBLIC_SCOPE.md).

## Uruchomienie

Uruchom posiadany prywatny silnik zgodnie z jego instrukcją, następnie klienta przez Uruchom_AI_SI.bat albo python run_ui.py i wskaż backend. Bez silnika klient zgłosi brak połączenia.

Wyniki pochodzą z ograniczonych prób rozwojowych; nie sumujemy ich jako niezależnego benchmarku i nie przedstawiamy jako dowodu ogólnego rozumienia języka.
