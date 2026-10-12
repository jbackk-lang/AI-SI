# AI-SI — sprawdzony stan na 11 października 2026

Eksperymentalny lokalny system: własny uczony rdzeń i osobny tryb narzędziowy. Kod, wagi oraz bazy pozostają lokalnie. Dokumentacja nie jest pakietem instalacyjnym.

## Parametry aktywnego rdzenia

| Parametr | Wartość |
|---|---:|
| Architektura | autoregresyjny Transformer |
| Parametry wraz z głowicami | 1 888 140 |
| Warstwy | 9 |
| Głowice uwagi na warstwę | 4 |
| Wymiar embeddingu | 128 |
| Słownik BPE | 768 tokenów |
| Kontekst | 128 tokenów |
| Dropout treningowy | 0,05 |
| Głowica stanu | 3 wyjścia |
| Głowice pomocnicze | argumenty: 6; operacja: 3 |

Rdzeń generuje tekst z własnych wag, bez kalkulatora, translatora i zewnętrznego modelu podczas odpowiadania. Odpowiedzi wymagają sprawdzenia.

## Potwierdzone testami

- Rdzeń udziela odpowiedzi w krótkich zadaniach z nazwami i stanami prawda/fałsz/nieznane. Aktywny model w wyczerpującym teście trzech nazw numerowanych uzyskał **263/486**. To potwierdza częściową zdolność, nie niezawodne wiązanie zmiennych ani pełną logikę trójstanową.
- Tryb narzędziowy przeszedł **10/10** sprawdzonych zadań obliczeniowych w ostatniej próbie integracyjnej, obejmującej arytmetykę, polskie polecenia, wybraną literówkę, pierwiastek z pi, wyznacznik macierzy i logikę klasyczną. Wynik pochodzi z narzędzi; nie jest wynikiem samodzielnego liczenia przez rdzeń.
- Walidacja składni arytmetycznej sprawdza nawiasy i zgodność drzewa wyrażenia między parserami. Nie stanowi ogólnego dowodu matematycznego ani walidacji topologii geometrycznej.
- Lokalny proces treningowy zapisuje testowe checkpointy, wykonuje powtórki i mierzy wyniki na oddzielnych przykładach. Uruchomienie procesu nie dowodzi skutecznego samouczenia.

## Ograniczenia

Wiązanie kilku nazw z wartościami pozostaje zawodne. Nowe nazwy i zmiana kolejności mogą ujawnić błędy. Tryb modułowy nie wykazał poprawnej integracji nowego rdzenia dla wszystkich pytań o zmienne i role osób. Nie potwierdzono autonomicznego wybierania skutecznych ćwiczeń, skutecznej trwałej nauki z internetu ani samodzielnej naprawy wag. Brak podstaw do deklarowania odczuwanej ciekawości lub świadomości.

## Historia i aktualizacje

[Procedura z 11 października, wyniki, próby w toku i poprzedni README](HISTORIA_SI_2026-10-11.md). [Wcześniejsze szczegóły](README_DETAILS.md).

Po ukończeniu prób wyniki będą dopisywane do historii. Do tego README trafią wyłącznie niezależnie sprawdzone możliwości, z zakresem testu i informacją o aktywacji. Trwające eksperymenty nie są deklarowane jako gotowe funkcje.
