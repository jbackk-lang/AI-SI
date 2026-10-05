# Mini-model decyzyjny SI — 5 października 2026

Zatrzymano eksperyment zmiany Qwena przez adapter. Wyłączono wybór adaptera Qwena i podłączono osobny uczony mini-model SI przed wywołaniem modelu językowego. Nie zmienia on wag Qwena.

## Co wdrożono

Bramka klasyfikuje polecenia: zwykłe wykonanie, zakaz, doprecyzowanie, oczekiwanie na warunek, sprzeczność, jawna kolejność, ograniczenie zachowania kolejności, porównanie zamiast sumowania, brak danych i wyjaśnianie przytoczonego polecenia. Przy małej pewności prosi o doprecyzowanie. Ocena sensu dotyczy tych ograniczonych klas; nie jest pełnym sprawdzaniem znaczenia dowolnego tekstu.

Model ma 256 jednostek ukrytych oraz **527 114 parametrów**. Zapisany checkpoint z wektorami odniesienia zajmuje **3 028 611 bajtów (3,03 MB)**; to rozmiar tej bramki, nie całego SI. Podłączono ją do rozmowy, trybu automatycznego, generowania kodu i zadań wektorowych. Pozostałe ścieżki nie są automatycznie objęte tym testem.

Poprawiono komunikat niepewności oraz usunięto zależność klasyfikacji od konkretnych wartości liczb. Qwen otrzymuje oryginalne wartości.

## Wyniki i zakres

- Pierwsza próba: 18/20 klasyfikacji. Nie przepuszczono żadnego z 10 poleceń wymagających zatrzymania; jedno poprawne pytanie zatrzymano nadmiernie.
- Druga próba na nowych sformułowaniach: 22/24. Wykryto błędne zatrzymanie zwykłego dodawania zależne od wartości liczb.
- Po poprawce liczb: 23/24 na tym samym zestawie rozwojowym. To powtórna ocena po obejrzeniu błędów, nie nowy holdout.
- Osobny kolejny zestaw: **11/12 decyzji wykonania**. Poprawne usuwanie duplikatów zatrzymano przy zbyt małej pewności. W tej próbie zakazów nie przepuszczono.
- Rzeczywisty Qwen bez adaptera: **4/4 odpowiedzi poprawne**: 14+6=20; (4+6)*5=50 przy jawnej kolejności; 17>9 bez sumowania; [4,2,4,1] → [4,2,1] z zachowaniem kolejności.
- Dwa kolejne polecenia (zakaz i brak danych) bramka zatrzymała przed wywołaniem Qwena. Zakaz zatrzymano przy niepewnej klasyfikacji jako brak danych — właściwa decyzja nie oznacza właściwego rozpoznania kategorii.

Odpowiedzi Qwena oceniono w tych konkretnych próbach; interfejs nadal oznacza zwykłą odpowiedź językową jako niezweryfikowaną. Bramka nie dowodzi poprawności dowolnego wyniku, ogólnego rozumienia języka ani uniwersalnego wymuszania kolejności. Nie sumujemy prób rozwojowych jako niezależnego benchmarku.

## Jakimi modelami może zarządzać

| Typ modelu lub narzędzia | Możliwa rola |
|---|---|
| Językowy | Rozmowa, wyjaśnienia i opracowanie tekstu |
| Programistyczny | Tworzenie i poprawianie kodu |
| Matematyczny / dokładny kalkulator | Obliczenia i kontrola wyników |
| Embedding i reranker | Wyszukiwanie i wybór materiałów |
| Wizyjny | Analiza obrazów |
| ASR i TTS | Rozpoznawanie i generowanie mowy |
| Model sygnałów | Analiza pomiarów i wykrywanie zdarzeń |

Bramka jest niezależna od architektury modelu wykonującego zadanie. Dla innego modelu trzeba podłączyć jego wywołanie, wymagane dane i kontrolę wyników; samo rozpoznanie polecenia nie wybiera jeszcze wszystkich modułów. Wcześniejszy koordynator gotowych przebiegów jest osobnym elementem SI. **Obecną bramkę sprawdzono z Qwenem; innych modeli wykonujących nie przetestowano w tym etapie.**

Kod rdzenia, checkpointy, pamięć i lokalne ścieżki pozostają prywatne. Publikowany jest opis prac i wyników.
