# SI — aktualizacja 6 października 2026

## Co działa obecnie
W prywatnym interfejsie działa własny mały model językowy SI bez Qwena, kontrola odpowiedzi ze źródła, most sesji, wyuczony wybór trzech strategii oraz polski translator obsługiwanych formatów. Wagi języka nadal trenujemy tylko po angielsku. Starsze konfiguracje z Qwenem, obrazami i wyszukiwaniem opisują wcześniejsze etapy.

## Wyniki i granice
| Próba | Wynik | Co rzeczywiście sprawdzono |
|---|---|---|
| Relacje i warunki | 24/24 | Nowe pary cyfr w tych samych szablonach; 12 relacji i 12 warunków |
| Zmiana form pytań i kolejności zdań | 40/84 → 70/84 | Identyczne zadania przed i po treningu; nowe połączenia sformułowań tylko 10/24 |
| Trening różnych nazw | 19/40 → 32/40 | Znane rodzaje nazw 24/24; całkiem nowe U/V 8/16 |
| Zachowanie wcześniejszych zadań | 89/93 | Powtórzenie wcześniejszego zestawu, nie nowy test |
| Wykorzystanie strategii z mostu | 7/16 → 14/16 | Zamiana nazw z kontrolą pierwotnego źródła; dwie odmowy, zero wypuszczonych błędów w tej próbie |
| Wyuczony wybór strategii | 240/240 | Syntetyczne odłożone stany walidacji; etykiety nauczyciela, nie wymyślanie strategii |
| Polski translator | 10/10 i 5/5 przez interfejs | Jawne reguły obsługiwanych formatów, nie pełne tłumaczenie języka |
| Lokalny słownik | 9/9 i 4/4 przez interfejs | Formy słów i jednoznaczne polecenia; nie definicje |
| Zachowanie języka rozmowy | 10/10 | Sześć nieznanych pytań z rzędu, skrócenie historii, zakaz i jawny angielski |

Nie sumujemy tych prób jako jednego niezależnego benchmarku. Kolejne testy powtórzeniowe są materiałem rozwojowym. Odmowy zapewniane przez walidator nie są poprawnymi odpowiedziami samej sieci. Te wyniki nie dowodzą ogólnego rozumienia języka ani bezpieczeństwa na dowolnych zadaniach.

## Most sesji i strategie
Wspólny lokalny dziennik pozwala odczytać zadanie, postęp, wynik i wybraną strategię innej sesji. Polecenie show sessions oraz przycisk Pokaż sesje udostępniają stan. Sesje nie nadpisują równolegle wag. Most nie jest dowodem samoświadomości.

Mały sterownik wybiera keep, normalize_names lub stop na podstawie ustrukturyzowanego stanu walidacji. Ma 451 parametrów i 4525 bajtów zapisanych wag. Narzędzie zamiany nazw jest jawne; odpowiedź nadal musi zgadzać się z oryginalnym źródłem. W tej próbie nie zmieniano wag języka. Zachowano również nieudany pierwszy test strategii: przykład ponowienia nie trafił do treningu; poprawiono podział danych, a nowy zestaw zawiera każdą strategię w obu częściach.

## Polski i źródła słów
Język odpowiedzi jest ustawiany jawnie, domyślnie polski; nieznane pytania proszą o doprecyzowanie. Translator ma ograniczony zestaw poleceń i formatów źródła. Nie jest pełnym modelem tłumaczeniowym ani treningiem SI po polsku.

Pierwszym lokalnym źródłem form słów jest [SJP.PL — odmiany](https://sjp.pl/sl/odmiany/): 237322 wpisy podstawowe, 4692353 pary forma–lemma, indeks 154550272 bajty (154,55 MB). Zachowano informację o źródle i wybranej licencji CC BY 4.0. To inny serwis niż SJP PWN. Baza nie zawiera pełnych definicji; wieloznaczności nie rozstrzygamy przez wybór pierwszej lemmy. Przykłady: „Opowiedz o pamięci”, „Sprawdź słowo: wartością”.

## Rozmiar i uruchomienie
Aktywne wagi własnego SI zajmują około 6,06 MB, dodatkowy sterownik strategii około 4,5 KB, indeks słownika około 154,55 MB. Są to wybrane składniki, nie gotowy pakiet z Pythonem i bibliotekami. Folder roboczy przed dodaniem indeksu miał 12,14 GB, w tym starsze modele, wyniki i kopie. Nie zmierzono kompletnego przenośnego instalatora ani wymagań na drugim komputerze. Większa liczba neuronów nie była konieczna do opisanych popraw.

## Publikacja
Ten dokument publikuje wyniki i ograniczenia. Rdzeń SI/TIMDR, kod prywatnego silnika, wagi, pamięć, logi sesji i lokalne ścieżki pozostają prywatne. Opisy funkcji nie oznaczają, że sam publiczny klient zawiera silnik. Aktualna runda treningowa jest zakończona; automatyczna kolejka czytania pozostaje wstrzymana.
