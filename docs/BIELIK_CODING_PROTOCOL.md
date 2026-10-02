# Trening adaptera Bielika — protokół pilotażowy

Cel: generowanie nowych funkcji Python, zamiast dobierania gotowych przykładów.

Bazą jest istniejący publiczny Bielik-1.5B-v3.0-Instruct Q8_0 (1 699 568 288 bajtów). Oficjalne pliki Transformers wymagają dostępu przez konto, więc ich nie pobrano. Przekształcamy już udostępnione GGUF do bfloat16 w pamięci RAM, wykorzystując mapowania Transformers i strumieniowo ładując pojedyncze tensory. Nie zapisujemy pełnej zdekwantowanej kopii.

12 przykładów treningowych, 6 innych zadań końcowych z przypadkami wykonania i 3 krótkie próby polskiego. Dane utworzono przed treningiem. To mały pilot autora, nie publiczny niezależny benchmark ani dowód ogólnej kompetencji. Zadania końcowe obejmują nowe specyfikacje i kombinacje operacji; część pojęć pokrywa się z treningiem.

Seed42; LoRA rank4, alpha8; q_proj/v_proj w warstwach 28–31; 3 epoki, lr0.0003. Maksymalnie 900 sekund na kroki treningu i przerwanie przy mniej niż 0,5 GiB wolnej pamięci. Odtworzenie, pomiary i eksport nie wchodzą do tego limitu. Aktualizowane są tylko wagi adaptera. Sumę kontrolną pliku bazowego porównujemy przed i po.

Pomiar przed i po wykonuje ten sam lokalny llama.cpp, ten sam Q8_0, te same prompty, temperature0 i limit160 tokenów kodu /32 tokenów polskiego. Po treningu adapter musi przejść zapis, odczyt oraz eksport GGUF. Polskie próby oceniają tylko obecność oczekiwanego słowa; nie mierzą szerokiej znajomości języka. Kod musi przejść wszystkie zadeklarowane przypadki danego zadania.

Ograniczony tester przyjmuje tylko pojedynczą funkcję solve, prosty AST i wybrane metody/builtins. Brak importów i dostępu do plików. Osobny proces ma limit czasu i pamięci (Windows Job Object: 512 MB, 2 sekundy CPU; limit ścienny 5 sekund). To filtr dla ćwiczeń, nie uniwersalny bezpieczny executor dowolnego Pythona. Przetestowano poprawny kod, błędy, próbę otwarcia pliku, nieskończoną pętlę i nadmierną alokację.

Pierwszy pomiar przerwano przed treningiem, ponieważ filtr odrzucił poprawne x**2. Poprawiono obsługę małych stałych potęg i ponowiono baseline; pierwszy raport zachowano jako ABORTED_CHECKER_CORRECTION_BEFORE_TRAINING. Hash poprawionego testera jest zapisany w planie. Nie zmieniono na tej podstawie danych treningowych ani hiperparametrów.

Przyjęcie: więcej w pełni poprawnych zadań końcowych i nie mniej zaliczonych prób polskiego. W przeciwnym razie adapter pozostaje kandydatem nieaktywnym. Przyjęty adapter nadal wymaga szerokiej dalszej walidacji. Podłączenie do rozmowy wymaga zgodności ścieżki, statusu, wyników i checksumów adaptera/bazy.

Plan, dane i odpowiedzi: artifacts/bielik_coding_adapter/<przebieg>/plan.json, dataset.json, report.json. Narzędzia i wersje: tool_manifest.json. Uruchomienie treningu: python tools/training/run_bielik_coding_adapter.py.
