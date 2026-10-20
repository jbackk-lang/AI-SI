# Wspólny model H512 i czytnika — 20 października 2026

W lokalnych aplikacjach zainstalowano TSI-UNIFIED-H512-7573fd65, runtime 0.6.0. Jeden moduł PyTorch i jeden checkpoint zawierają H512, jego pamięć nazw, transformer czytnika, matryce i uczone połączenia.

Czytnik przekazuje swój stan do rzeczywistej warstwy rekurencyjnej H512. Jej odpowiedź wpływa na ocenę dowodów. Działa również kierunek od reprezentacji H512 do transformera. W tej wersji obieg dotyczy czterech jawnych kanałów relacji; nie obejmuje dowolnej rozmowy ani całego systemu narzędzi.

Wytrenowano 147 552 parametry połączeń w 60 krokach. Wagi obu wcześniejszych części zachowano dokładnie. Nie był to wspólny trening wszystkich wag. Stan H512 zmienia się wraz z wejściem czytnika, a wyłączenie sprzężenia zmienia logity odpowiedzi. Nie wykazano wzrostu trafności względem wcześniejszych kompletnych wyników.

Wyniki regresji: 960/960, 720/720 i 640/640; zachowane odpowiedzi dla 140 poleceń językowych i 256 operacji wektorowych; 118/118 planów bez błędnych akceptacji; 512 zestawów wymagań. Są to wcześniej używane zestawy kontrolne, nie nowy test swobodnego języka. Ponowne wczytanie checkpointu odtwarza wyniki bitowo.

Cały model zawiera **2 613 105 parametrów**, a checkpoint zajmuje **10 587 275 bajtów (10.59 MB / 10.10 MiB)**. Wliczona jest również pamięć nazw H512, której nie obejmowała wcześniejsza suma dwóch głównych modułów. Inne modele pomocnicze i trwałe notatki pozostają poza tym checkpointem.

Na tym komputerze działa CPU. Pełny obieg ma ścieżkę tensorów zgodną z urządzeniem; fizycznego GPU nie testowano. Pomiar kontrolny 16 faktów: około 11.6 ms; to wywołanie sieci, a nie czas całej odpowiedzi panelu. Nie deklarujemy przyspieszenia względem poprzedniego czytnika.

Solvery, kontrola wyniku, pamięć dokumentów i narzędzia budżetowe pozostają osobnymi elementami aplikacji. Dotychczasowe ścieżki językowe H512 są zachowane; zainstalowanie wspólnego modelu nie oznacza konsolidacji wszystkich procesów aplikacji. Poprzedni pakiet zachowano lokalnie do cofnięcia wdrożenia. Paczki portable w tej partii nie przebudowano.
