# Poprawianie literówek i samoobsługa modułów SI — 8 października 2026

## Poprawianie literówek
Gdy SI nie zrozumie wiadomości, sama poprawia literówki słownikiem SJP.PL (4,69 mln form) i odpowiada na poprawioną wersję, pokazując, co zrozumiała:

- „co to jset rakieta?” → „Zrozumiałam: „co to jest rakieta?”” i definicja;
- „olbicz 2+3*4” → „Zrozumiałam: „oblicz 2+3*4”” i wynik 14;
- „co potarfisz?” → lista modułów;
- brakujące polskie znaki: „wyjasnij pamiec”, „swieta w 2026”, „mieszkancow”, „dzis”, „sprawdz”.

Zasady:
- najpierw brakujące polskie znaki (wygrywa wariant z najmniejszą liczbą zmian), potem przestawione sąsiednie litery (najczęstsze przy dysleksji), potem jedna brakująca, nadmiarowa albo zamieniona litera;
- poprawka tylko wtedy, gdy kandydat jest jeden;
- nazwy własne, tekst angielski, ścieżki plików i adresy zostają bez zmian;
- poprawiona wersja jest przyjmowana tylko wtedy, gdy odpowiada na nią konkretny moduł (kalkulator, daty, fakty, tabele, dokumenty, samoobsługa).

## Samoobsługa modułów
- „co potrafisz?”, „jakie masz moduły?”, „pomoc” → lista modułów z przykładowymi poleceniami do skopiowania i stanem ostatniego autotestu (✓/✗).
- „jak działa moduł dat?”, „jak policzyć sumę w tabeli?”, „jak zapytać dokument?” → opis modułu, czytany z jego własnego opisu w kodzie, i przykłady. Nowy moduł z opisem pojawia się na liście sam.
- „sprawdź się”, „autotest” → SI uruchamia zamrożony test tabel, dokumentów i dat, zamrożony test faktów z Wikipedii (offline), sprawdza słownik SJP.PL, pakiety (XLSX, PDF, DOCX, sieci neuronowe) i dostęp do Wikidanych, a potem raportuje każdy punkt jako ✓ albo ✗.
- Gdy SI nie zrozumie krótkiego pytania, które pasuje do modułu, podpowiada brakującą część i poprawny format. Przykład: „Na jak długo zawarto umowę?” → „brakuje ścieżki pliku. Napisz tak: Dokument: C:\dane\umowa.docx. …”.
- Krótkie „święta w 2026” jest rozpoznawane jako pytanie o dni wolne w Polsce.

## Sprawdzenie przed wdrożeniem
- 1311 tekstów z zamrożonych testów SI przepuszczono przez czat:
  - samoobsługa nie przechwyciła żadnego;
  - poprawka literówek nie zmieniła żadnej odpowiedzi;
  - podpowiedź formatu pojawiła się w 2 pytaniach o umowę bez pliku.
- Zamrożony test tabel, dokumentów i dat: 0 fałszywych potwierdzeń.
- Pierwsza wersja poprawiała też tekst angielski („computer” → „komputer”) i przyjmowała ogólne odpowiedzi modelu językowego po poprawce (33 przypadki). Obie rzeczy zablokowano przed wdrożeniem.
