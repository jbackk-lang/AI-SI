# AI-SI

Eksperymentalny system inspirowany TIMDR jako punktem wyjścia do budowy sterownika współpracy.

## Aktualny stan — 7 października 2026

Własny mały model językowy SI działa bez Qwena, z kontrolą źródeł, mostem sesji, wyborem strategii i ograniczoną obsługą polskiego; wagi języka trenujemy po angielsku. Zadania słowne są sprawdzane na prawdziwych zadaniach z otwartych zbiorów, a polskie pytania obsługuje maper z katalogiem sprawdzonych zdań.

## Najnowsza aktualizacja — 7 października 2026

- **Most WordNet:** nieznany czasownik w zadaniu słownym jest zamieniany na znany czasownik SI tej samej operacji przez otwarty angielski WordNet, tylko gdy wszystkie znaczenia słowa są zgodne. Nowy test zamrożony przed pracą 208→286/300; 0 błędnych potwierdzeń.
- **Most pytań:** nieznane sformułowanie pytania zamieniane na znane pytanie tej samej klasy. Nowy zamrożony test 247→272/300.
- **Sprawdzian na prawdziwych zadaniach:** na 1730 zadaniach z otwartych zbiorów SVAMP/ASDiv parser trafiał tylko 10%, czyli prawie jak losowanie; mosty działały tylko w świecie własnych szablonów (wynik negatywny).
- **Nowe podejście:** liniowy klasyfikator działania uczony na otwartym MAWPS, wskazówki ról liczb (wynik, stan początkowy, porównanie, grupy) i czytnik kontekstu czytający zadanie słowo po słowie, połączony z modelem ról. Połowa testu nieużywana do strojenia 451→512; w SI prawdziwe zadania 178→944/1730. Odpowiedzi nowego modelu zawsze wymagają potwierdzenia; 0 błędnych potwierdzeń.
- **Polski maper pytań:** katalog sprawdzonych zdań (wzór nauczyciela z 4 października) i czytnik kontekstu po formach SJP.PL. Zamrożony test 44→64/72; „nie rozpoznaję” 21→5, błędne intencje 7→3.
- **Pętla samouczenia:** koordynator nauki dla modułów z automatem rośnięcia pojemności, okienkiem podglądu i podmianą wag tylko po poprawie, z kopią zapasową.
- **Wyniki negatywne:**
  - dane pisane przez Qwena od zera i z przepisania zadań MAWPS nie poprawiły wyniku na straży;
  - więcej neuronów przy cechach bez kolejności słów nie pomogło;
  - kalibracja bezpiecznego potwierdzania nie dała zera błędów (ok. 10%).

[Dokładne wyniki, metody i ograniczenia — 6–7 października](docs/SI_NAUKA_2026-10-06.md). Testy użyte do wyboru wersji są odtąd rozwojowe. [Aktualizacja z 6 października](README_DETAILS.md#aktualizacja--6-października-2026-cały-dzień) jest w historii.

## Osiągnięcia w skrócie

- **Język:** trening własnych wag poprawił wynik z 40/84 do 70/84 na tych samych zadaniach, przy ograniczonym zakresie.
- **Relacje:** następna runda dała 32/40, lecz całkiem nowe nazwy nadal tylko 8/16.
- **Strategie:** mała sieć wybiera zachowanie odpowiedzi, zmianę nazw lub zatrzymanie, uzyskując 240/240 na stanach walidatora.
- **Most sesji:** wspólny dziennik udostępnia stan i sprawdzone strategie, a w małej próbie poprawił wynik z 7/16 do 14/16.
- **Polski:** translator obsługiwanych formatów zachowuje zakazy, liczby i warunki, a język odpowiedzi pozostaje jawnie wybrany.
- **Słownik:** lokalna baza SJP.PL jest pierwszym źródłem odmian słów, obejmując 4,69 mln par forma–lemma.
- **Kontrola:** niepotwierdzone odpowiedzi są zatrzymywane, bez ogólnej gwarancji poprawności.
- **Interfejs:** rozmowa, ocena decyzji i podgląd sesji są oddzielone; audio pozostaje odłączone.
- **Wcześniejsze moduły:** matematykę, programowanie, wyszukiwanie i obrazy opisuje historia ich odrębnych konfiguracji.

[Dokładne wyniki, rozmiary i ograniczenia — 6 października](docs/SI_AKTUALIZACJA_2026-10-06.md) · [Historia i wcześniejsze konfiguracje](README_DETAILS.md).

Aktywne wagi SI: około **6,06 MB** (stan rano 6 października; nowe moduły z 6 października dodają ok. **5 MB**, 1,25 mln parametrów, a z 7 października ok. **2,5 MB**: czytniki kontekstu, klasyfikator działania, mosty i polski maper), sterownik strategii: **4,5 KB**, lokalny indeks słownika: **154,55 MB**; to nie rozmiar kompletnego pakietu z bibliotekami.

## Zakres publicznego repo

Publiczne repo zawiera interfejs, integrację, narzędzia treningowe, testy i dokumentację. **Rdzeń SI/TIMDR, prywatny silnik, wagi, checkpointy i pamięć pozostają prywatne.** Samo pobranie repo nie udostępnia całego silnika. [Zakres publikacji](docs/PUBLIC_SCOPE.md).

## Uruchomienie

Uruchom posiadany prywatny silnik zgodnie z jego instrukcją, następnie klienta przez Uruchom_AI_SI.bat albo python run_ui.py i wskaż backend. Bez silnika klient zgłosi brak połączenia.

Wyniki pochodzą z ograniczonych prób rozwojowych; nie sumujemy ich jako niezależnego benchmarku i nie przedstawiamy jako dowodu ogólnego rozumienia języka.
