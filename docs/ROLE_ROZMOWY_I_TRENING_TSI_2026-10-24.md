# Role rozmowy i wspólny trening — 24 października 2026

**Zachowano poprzedni model badawczy. Aplikacji i portable nie podmieniono.**

| Próba | Model odniesienia | Wariant ze znacznikami po treningu |
|---|---:|---:|
| Chronione odpowiedzi | 56/56 | 56/56 |
| Porównawcze rozmowy dwóch tur | 1/8 | 0/8 |
| Dodatkowe sekwencje trzech tur | 0/8 | 0/8 |

W formacie ze znacznikami uczone rozmowy uzyskały **5/56 przed treningiem → 8/56 po treningu**. Wcześniejszy format tekstowy miał 8/56. Zmieniono jednocześnie reprezentację rozmowy i sposób uczenia; nie przypisujemy całej różnicy samym znacznikom.

## Co zmieniono

Historyczne wypowiedzi użytkownika i TSI otrzymują odrębne, istniejące w słowniku sieci znaczniki ról. Bieżące polecenie jest ostatnią turą użytkownika. Oba enkodery i generator korzystają z tego samego formatu; format jest zapisany w paczce wag i odtwarzany przy jej wczytaniu. Wejścia pojedynczych pytań zachowano bez zmian. Nie dodano nowych parametrów ani tabeli gotowych odpowiedzi w panelu.

Pierwszy start zatrzymał się przed aktualizacją wag: warstwa słownikowa usuwała specjalne znaczniki przy odtwarzaniu tekstu, a kontrola zgodności odrzucała przesunięte wejście. Naprawiono odczyt znaczników, zachowując ścisłe sprawdzanie identyczności tokenów. Znaczniki nie trafiają do słownika jako zwykłe słowa. Porównanie wszystkich **56 chronionych wejść w obu enkoderach** potwierdziło identyczne wcześniejsze reprezentacje słownikowe. Wszystkie **56 kontekstów** przeszły poprawiony odczyt w obu enkoderach.

Wspólnie trenowano oba enkodery, pamięci H512 i generator, z powtórkami oraz porównywaniem odpowiedzi na bieżące polecenie. Sześć macierzy reguł pozostało zamrożonych. Wykonano 15 głównych aktualizacji; zachowano zapis po 15. Liczba automatycznie cofniętych serii: 1. Cofanie przywracało sieć oraz stan optymalizatora i zmniejszało krok uczenia.

Próby używają znanych sformułowań w innych sekwencjach. Osiem dodatkowych sekwencji trzech tur ustalono przed zakończeniem uczenia; nie użyto ich do treningu ani wyboru kroku. Historia zawiera rzeczywiste odpowiedzi modelu. Zestaw dwóch tur był już wcześniej oceniany i służy porównaniu. Swobodna rozmowa nie osiągnęła wymaganego poziomu.

Model: **23 542 811 parametrów**, **94.67 MB** wspólnych wag, bez całego portable. Internetowa pętla uczenia pozostaje wyłączona. [Poprzednia runda bez znaczników](https://github.com/jbackk-lang/AI-SI-TSI/blob/main/docs/ODROZNIANIE_POLECENIA_OD_HISTORII_2026-10-24.md).
