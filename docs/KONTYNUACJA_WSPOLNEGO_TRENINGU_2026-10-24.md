# Kontynuacja wspólnego treningu — 24 października 2026

**Kontynuacja nie poprawiła rozmowy. Zachowano poprzedni model badawczy.**

| Próba | Przed kontynuacją | Zachowany zapis kontynuacji |
|---|---:|---:|
| Chronione odpowiedzi | 56/56 | 56/56 |
| Uczone rozmowy | 8/56 | 8/56 |
| Odłożone kombinacje rozmów | 1/8 | 0/8 |
| Pierwsza odpowiedź bez historii w odłożonej próbie | 8/8 | 8/8 |

Wykonano dziesięć głównych aktualizacji. Zapis po piątej zachował 56 chronionych odpowiedzi; po dziesiątej wynik spadł do 47/48 dawnych oraz 7/8 nowych. Gorszych wag nie wybrano. Niezależny odczyt zapisu po piątej aktualizacji potwierdził 56/56, ale osiem odłożonych rozmów wykazało pogorszenie z 1/8 do 0/8. Dlatego również ten zapis nie zastępuje wcześniejszego modelu badawczego.

Przykład: po wcześniejszym „Dzień dobry” na „Dziękuję” sieć odpowiedziała „Dzień dobry!.”. Na prośbę o zdanie o lesie po rozmowie powitalnej odpowiedziała „Proszę bardzo.”. Pierwsze odpowiedzi pozostały poprawne, trudność dotyczy wykorzystania historii i aktualnego polecenia.

Oba enkodery oraz generator były trenowane wspólnie. W każdym enkoderze zmieniło się 71 tensorów, w tym osiem tensorów pamięci H512. Sześć macierzy reguł pozostało bez zmian. Sam przepływ gradientów jest potwierdzony; ta runda nie osiągnęła wymaganego poziomu rozmowy.

Domyślnego modelu aplikacji, integracji MUZ i walidatora ani portable nie zmieniono. Pętla internetowego uczenia wag pozostaje wyłączona. Dalsza praca wymaga poprawy rozróżniania aktualnego polecenia i wcześniejszych wypowiedzi, z zachowaniem powtórek oraz kontroli regresji. Model nadal ma 23 542 811 parametrów; wspólny plik wag zajmuje około 94,67 MB, bez całego środowiska portable.
