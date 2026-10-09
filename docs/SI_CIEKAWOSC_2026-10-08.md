# Ciekawość SI — własne pytania, mapa wiedzy, nauka w tle (8 października 2026)

## Mapa wiedzy
Każdy fakt, który SI sprawdzi w rozmowie albo z własnej ciekawości, trafia na mapę wiedzy. Zapisane są:
- wartość i stan (potwierdzone albo do potwierdzenia);
- wszystkie źródła z ich wartościami;
- kto pytał i kiedy.

Dla każdego hasła mapa zna też jego rodzaj (osoba, miejsce, organizacja, dzieło) i powiązania z Wikidaty. Powiązania to: rodzice, małżonkowie, dzieci, rodzeństwo, nauczyciele, uczniowie, inspiracje, miejsce urodzenia i śmierci, uczelnie, pracodawcy, dzieła, autorzy, założyciele.

„co wiesz o Mikołaju Koperniku?” → co SI sprawdziła, czego jeszcze nie wie i jakie powiązania zna.

## Własne pytania
SI układa sobie kolejkę pytań z czterech miejsc:
1. **Dziury na mapie:** „znam urodzenie, nie znam śmierci”.
2. **Powiązania:** po pytaniu o Newtona ciekawi ją jego nauczyciel i miejsce urodzenia, potem ich powiązania (do dwóch kroków od tematu rozmowy).
3. **Pytania z rozmów, na które nie znała odpowiedzi:** te z dziennika braków mają pierwszeństwo.
4. **Spory źródeł.** Gdy źródła podają różne wartości, SI czyta artykuły i szuka wyjaśnienia:
   - kalendarz juliański i gregoriański;
   - data chrztu zamiast daty urodzenia;
   - zdarzenie w nocy albo dwie możliwe daty;
   - dokładna data nieznana.

   Gdy wartość różni się tylko w jej własnym odczycie Wikipedii, SI rozpoznaje własny błąd czytania i zapisuje go do nauki czytania.

## Nagroda za postęp
- SI wybiera pytania z rodzajów faktów, w których ostatnio szybko się poprawia.
- Rodzaj, w którym 8 prób z rzędu nic nie dało, odkłada.
- Koordynator nauki dostał moduł „ciekawość” i premię za postęp: moduł, który ostatnio poprawia się szybciej niż wcześniej, wybiera częściej.

## W rozmowie
- Gdy źródła się różnią, SI proponuje: „Napisz „sprawdź dlaczego”, a poszukam wyjaśnienia”.
- „sprawdź dlaczego” → wyjaśnienie różnicy z cytatem z artykułu.
- „czego się dowiedziałaś?” → co SI sama sprawdziła, dlaczego ją to zainteresowało i co ciekawi ją teraz.
- Na powitanie SI mówi, ile rzeczy sama sprawdziła od ostatniej rozmowy.

## Nauka w czasie bezczynności
`Uruchom_nauke_w_tle.bat` uruchamia naukę w tle. Gdy komputer stoi bezczynnie 5 minut, SI robi jedną turę nauki: ciekawość albo czytanie Wikipedii. Przycisk „Zatrzymaj naukę” w podglądzie kończy także naukę w tle. `Wlacz_nauke_w_tle_przy_starcie.bat` dodaje ją do autostartu Windows.

## Sprawdzenie przed wdrożeniem
- 1311 tekstów z zamrożonych testów: nowe polecenia nie przechwyciły żadnego.
- Zamrożony test faktów (126 pytań, offline): wynik identyczny.
- Zamrożony test tabel, dokumentów i dat: 0 fałszywych potwierdzeń.
- Pełna pętla (pytania z dziur i powiązań, wyjaśnienie sporu o datę urodzenia Newtona kalendarzem juliańskim, raport „czego się dowiedziałaś?”) sprawdzona na modelu świata bez sieci.

## Pierwsze godziny (8 października, 14:23–15:38)
Bez żadnego pytania z zewnątrz SI zrobiła 42 rundy i zadała sobie 394 pytania. 190 odpowiedzi potwierdziła co najmniej dwoma źródłami. Zaczęła od Kopernika, Skłodowskiej-Curie, Chopina i Uniwersytetu Jagiellońskiego, a po powiązaniach doszła m.in. do rodziny Chopina, nauczycieli muzyki w Lipsku i Londynie oraz francuskich instytucji naukowych. Na mapie wiedzy ma 338 faktów o 277 hasłach.
Spór liczony z dokładnością (sam rok i pełna data z tym samym rokiem to zgoda): 62 prawdziwe spory. W 18 z nich większość źródeł się zgadza, a inna jest tylko wartość, którą SI odczytała z artykułu Wikipedii. Te artykuły trafiają do nauki czytania (np. śmierć Kopernika odczytana z polskiego artykułu jako 1523 zamiast 1543).
Gdy kolejka się wyczerpie, SI zaczyna od hasła z mapy, którego powiązań jeszcze nie zna.

## Baza wiedzy
Mapa wiedzy, hasła, kolejka pytań i postęp są w małej bazie SQLite (`knowledge.sqlite`). Zapis jest zwarty: około 340 bajtów na fakt razem z hasłem i jego powiązaniami. Każdy nowy fakt to jeden zapis w bazie. Z bazy korzystają jednocześnie czat i nauka w tle. Dziennik ciekawości po przekroczeniu 2 MB jest pakowany do archiwum.

## Świeże fakty (22:20)
- **Kto teraz pełni urząd:** „Kto jest prezydentem Polski?”, „kto jest premierem Francji?”, „kto jest prezydentem miasta Krakowa?”, „Who is the prime minister of Japan?”. Obecną osobę SI bierze z Wikidanych (wpis bez daty końca), podaje, od kiedy pełni urząd, i potwierdza zdaniem z artykułu Wikipedii o miejscu albo o tej osobie.
- **Fakty, które się zmieniają:** urzędy SI sprawdza ponownie po 30 dniach, liczbę mieszkańców po 180 dniach. Inna wartość to zmiana świata: poprzednia trafia do historii hasła, a raport „czego się dowiedziałaś?” pokazuje „było …, teraz …”.
- **Świeże punkty startu:** raz dziennie SI bierze nowe hasła z bieżących wydarzeń, list niedawnych zgonów i tegorocznych premier (Wikipedia angielska i polska). Najpierw pyta o to, co się zmienia. Potem pyta o osoby, które pełnią urzędy.
- Pytania o rzeczy zmienne mają w wyborze pierwszeństwo przed kolejnymi datami historycznymi.

## Wydarzenia i znudzenie (9 października, 00:55)
- **Wydarzenia:** „Kiedy odbyły się Igrzyska Olimpijskie 2024?”, „Gdzie odbyła się bitwa pod Grunwaldem?”, „When did the 2026 FIFA World Cup take place?”. Datę wydarzenia (albo jego początku) SI bierze z Wikidanych i czyta w artykule wzorcami, których sama się nauczyła; miejsce potwierdza nazwą w artykule o wydarzeniu. Od wydarzenia ciekawią ją: państwo (kto nim rządzi), miejsce, zwycięzca i uczestnicy.
- **Świeże wydarzenia:** codziennie do 80 nowych haseł z bieżących wydarzeń, wydarzeń miesiąca i roku (także w Polsce), niedawnych zgonów i premier. Co najmniej 60% pytań w rundzie dotyczy wydarzeń, rzeczy zmiennych i świeżych haseł.
- **Znudzenie:** gdy SI opanuje rodzaj faktów (12 ostatnich prób średnio co najmniej 0,8), ten rodzaj przestaje ją ciekawić i przechodzi do innego tematu; rodzaje, których jeszcze nie próbowała, dostają premię za nowość.
- Gdy daty wydarzenia nie umie jeszcze wyczytać z artykułu, odsyła ten artykuł do nauki czytania.

## Wiedza z mapy w rozmowie (9 października, 06:20)
- **Odpowiedź z mapy:** gdy fakt jest już na mapie potwierdzony dwoma źródłami, SI odpowiada od razu, bez internetu: „Niemcy — głowa państwa: Frank-Walter Steinmeier. Wiem to z mojej mapy wiedzy: sprawdziłam 2026-10-09, zgodne źródła: Wikidata, Wikipedia en”. Fakty zmienne (urzędy, liczba mieszkańców) bierze z mapy tylko wtedy, gdy są świeże; starsze sprawdza na nowo.
- **Pytania o świat:**
  - „co nowego na świecie?” — wydarzenia z ostatnich 30 dni i zapowiedziane na najbliższe 90;
  - „jakie wybory są w tym miesiącu?”, „jakie wybory będą w listopadzie?”, „jakie trwają wojny?”, „jakie zawody sportowe są w tym roku?”;
  - „co słychać we Francji?” — wydarzenia kraju (po powiązaniu „państwo” z Wikidanych);
  - „co się wydarzy w listopadzie?”.
- **Z kalendarzem:** „kiedy są wybory w Hiszpanii?” → 29 listopada 2026; „ile dni do wyborów w Hiszpanii?” → za 51 dni.
- Każda pozycja ma znak ✓ (potwierdzone) albo ? (do potwierdzenia).
