# Zakres publicznego repozytorium

Użytkownik wybrał publikację interfejsu, integracji oraz narzędzi treningowych. Nie publikujemy prywatnego rdzenia SI/TIMDR.

Publiczne: gateway do lokalnego silnika, HTML interfejsu, adapter integracji Bielika, trening LoRA na publicznej bazie GGUF, ograniczony tester ćwiczeń Python, dane pilotażowe, testy i protokół.

Wyłączone: independent_timdr_core.py, recursive_relation_core.py, deliberative_core.py, confirmed_feedback_learning.py, learned_si_language.py, programming_si.py, si_neural_conversation.py, si_learning_conversation.py, si_bilingual_conversation.py oraz zależne prywatne modele i pamięci. Pełny prywatny serwer si_web_app.py pozostaje w Al-SI.

Duże wagi, checkpointy, tokenizer treningowy, sesje rozmów, ścieżki udostępnionych plików, środowisko Python i runtime nie są częścią publikacji. .gitignore chroni przed przypadkowym dodaniem; check_public.py dodatkowo sprawdza jawny katalog dozwolonych plików i indeks Git. Nie stosujemy git add . bez kontroli.

Publiczny interfejs nie jest pełnym samodzielnym SI. Funkcje rdzenia wymagają osobnego lokalnego silnika. Brak rdzenia jest świadomym ograniczeniem dystrybucji, nie dowodem zamkniętej przewagi albo poprawności TIMDR. Narzędzia treningu adaptera Bielika są odrębne od prywatnego rdzenia.
