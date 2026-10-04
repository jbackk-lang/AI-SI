# AI-SI

SI to eksperymentalny warsztat łączący język, matematykę, programowanie i pracę ze źródłami, inspirowany TIMDR jako punktem wyjścia do budowy sterownika współpracy.

**Publiczne repo zawiera interfejs, integrację, narzędzia treningowe, testy i dokumentację; rdzeń SI/TIMDR, wagi, checkpointy i pamięć użytkownika pozostają prywatne.** [Zakres publikacji](docs/PUBLIC_SCOPE.md).

## Osiągnięcia w skrócie

Poniższe funkcje dotyczą prywatnego silnika i ograniczonych prób rozwojowych; samo pobranie repo nie udostępnia wszystkich modułów.

- **Język:** Qwen zastąpił Bielika w polskiej rozmowie, interpretacji źródeł i generowaniu kodu.
- **Matematyka:** dokładny kalkulator, niezależna walidacja i SymPy obsługują określone działania oraz równania.
- **Programowanie:** SI wybiera sprawdzone przykłady Pythona i testuje wygenerowany kod na podanych przypadkach.
- **Dokumenty:** Embedding i Reranker wybierają materiały przekazywane do interpretacji przez Qwena.
- **Obrazy:** Qwen-VL analizuje obrazy, a odczyt może zasilać kolejne kontrolowane zadanie.
- **Źródła:** dostęp do dozwolonych stron i udostępnionych plików wspiera pracę z materiałami.
- **Pamięć:** zapisane fragmenty źródeł można wyszukiwać i przekazywać do rozmowy.
- **Koordynacja:** własne sieci wybierają gotowe przebiegi współpracy między modułami.
- **Uczenie:** potwierdzone przykłady służą do treningu kandydatów ocenianych pod kątem poprawy i regresji.
- **Kontrola poleceń:** ograniczone walidatory sprawdzają negację, warunki, kolejność i argumenty.
- **Interfejs:** rozmowa i zadania mają osobne panele, a historia rozmów jest zapisywana lokalnie.
- **Audio:** ASR i TTS sprawdzono w małych próbach, lecz dźwięk pozostaje odłączony.

**Wyniki, liczby neuronów, rozmiary wag, historia zmian, ograniczenia i propozycja wdrożenia:** [szczegółowy opis projektu](README_DETAILS.md).

## Uruchomienie

1. Uruchom posiadany prywatny silnik SI zgodnie z jego instrukcją.
2. Uruchom `Uruchom_AI_SI.bat` albo `python run_ui.py` w tym repo.
3. Wskaż adres silnika przez `--backend`; bez działającego silnika interfejs zgłosi brak połączenia.

## Jak oceniać projekt

To prototyp oceniany w niewielkich, kontrolowanych próbach, a nie potwierdzony odpowiednik ogólnych modeli AI.
Odczyt źródła nie oznacza uczenia wag, przejście podanych testów nie gwarantuje poprawności dowolnego programu, a większa liczba neuronów sama nie dowodzi poprawy.
Szczegółowe wyniki i ich zakres pozostają dostępne w [pełnej dokumentacji](README_DETAILS.md).
