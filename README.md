# AI-SI

Eksperymentalny system inspirowany TIMDR jako punktem wyjścia do budowy sterownika współpracy.

## Aktualny stan — 6 października 2026

Własny mały model językowy SI działa bez Qwena, z kontrolą źródeł, mostem sesji, wyborem strategii i ograniczoną obsługą polskiego; wagi języka trenujemy po angielsku.

## Najnowsza aktualizacja — 6 października 2026 (cały dzień)

- **Źródła:** model odpowiedzi ze źródła uczony na mieszanych wzorcach zdań; nowy zamrożony test 33→67/96, regresja 89→92/93, z kontrolerem 96/96 bez błędnych potwierdzeń.
- **Trzy stany tam, gdzie trzeba:** uczona bramka zwalnia powitania i wyjaśnienia z oceny prawdziwości (52/53, bez pominiętej weryfikacji); zakaz daje „zatrzymaj”.
- **Polski:** uczony maper pytań (SJP.PL → intencje) zamiast stałego słownika; niezrozumiane pytania dostają podpowiedź.
- **Zadania słowne:** dwa małe parsery + dokładny kalkulator; most liczby–struktura (zasada odniesienia TIMDR) i pętla z niezależnym sędzią (Qwen rozwiązuje osobno, etykietą jest jedyne zgodne działanie). Nowe szablony zdań 26→145/210; 0 błędnych potwierdzeń dzięki kanałowi znaczenia operacji i kanałowi nowości. Polskie zadania zawsze wymagają potwierdzenia interpretacji.
- **Most WordNet (noc 6/7 października):** nieznany czasownik w zadaniu słownym → forma podstawowa → otwarty angielski WordNet (synonimy i pojęcia nadrzędne) → znany czasownik SI, tylko gdy wszystkie znaczenia wskazują tę samą operację. Bez zmiany wag: nowy test zamrożony przed pracą (24 nieznane czasowniki) 208→286/300, starszy test nowych czasowników 187→276/300; 0 błędnych potwierdzeń.
- **Most pytań (7 października):** nieznane sformułowanie pytania → uczony klasyfikator klasy pytania → znane pytanie tej samej klasy. Nowy test zamrożony przed pracą 247→272/300, nowe ramy zdań 68→97/300, bez strat na pozostałych testach i bez błędnych potwierdzeń.
- **Prawdziwe zadania (7 października):** na 1730 zadaniach z otwartych zbiorów SVAMP/ASDiv parser trafiał tylko 10% (prawie jak losowanie). Nowy liniowy klasyfikator działania uczony na otwartym MAWPS: 49% (czysty pomiar), w SI 178→854/1730; nigdy sam nie potwierdza, 0 błędnych potwierdzeń.
- **Wyniki negatywne:** pętla bez niezależnego odniesienia utrwalała własne błędy; słownik synonimów użyty do podmiany słów pogarszał odpowiedzi; poranna wersja bezpiecznika potwierdzała błędy na nowych zdaniach (naprawione).

[Dokładne wyniki, metody i ograniczenia — 6 października](docs/SI_NAUKA_2026-10-06.md). Testy użyte do wyboru wersji są odtąd rozwojowe.

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

Aktywne wagi SI: około **6,06 MB** (stan rano 6 października; nowe moduły z 6 października dodają ok. **5 MB**, 1,25 mln parametrów), sterownik strategii: **4,5 KB**, lokalny indeks słownika: **154,55 MB**; to nie rozmiar kompletnego pakietu z bibliotekami.

## Zakres publicznego repo

Publiczne repo zawiera interfejs, integrację, narzędzia treningowe, testy i dokumentację. **Rdzeń SI/TIMDR, prywatny silnik, wagi, checkpointy i pamięć pozostają prywatne.** Samo pobranie repo nie udostępnia całego silnika. [Zakres publikacji](docs/PUBLIC_SCOPE.md).

## Uruchomienie

Uruchom posiadany prywatny silnik zgodnie z jego instrukcją, następnie klienta przez Uruchom_AI_SI.bat albo python run_ui.py i wskaż backend. Bez silnika klient zgłosi brak połączenia.

Wyniki pochodzą z ograniczonych prób rozwojowych; nie sumujemy ich jako niezależnego benchmarku i nie przedstawiamy jako dowodu ogólnego rozumienia języka.
