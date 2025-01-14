Opis techniczny projektu: Symulator Szyfrowania Tekstu

1. Cel projektu
Aplikacja webowa umożliwiająca szyfrowanie i odszyfrowywanie tekstu za pomocą trzech popularnych algorytmów:

Szyfr Cezara – podstawowe przesunięcie liter w alfabecie.
Szyfr Vigenère’a – metoda oparta na kluczu tekstowym.
Base64 – kodowanie danych w formacie tekstowym.
Aplikacja pozwala użytkownikowi na interakcję poprzez przyjazny interfejs, a wyniki są generowane dynamicznie.

2. Struktura projektu
Backend: Flask (Python) – obsługuje logikę szyfrowania i deszyfrowania, przyjmuje dane od użytkownika i zwraca wyniki.
Frontend: HTML, CSS, JavaScript – odpowiada za interakcję z użytkownikiem, wysyłanie żądań do backendu oraz wyświetlanie wyników.
Technologie wspierające:
fetch – do komunikacji frontend-backend.
JSON – do przesyłania danych między frontendem a backendem.
3. Funkcjonalności
Wybór algorytmu szyfrowania:
Użytkownik wybiera jeden z dostępnych algorytmów z listy rozwijanej.
Wprowadzanie danych:
Użytkownik wprowadza tekst do zaszyfrowania/odszyfrowania oraz opcjonalny klucz (dla Cezara i Vigenère’a).
Przycisk akcji:
Dwa przyciski umożliwiają wykonanie szyfrowania lub deszyfrowania.
Wynik:
Po przetworzeniu żądania wynik wyświetla się w dedykowanej sekcji.
4. Frontend
HTML:

Formularz zawierający pola tekstowe (tekst do przetworzenia, klucz) oraz listę rozwijaną do wyboru algorytmu.
Przycisk „Zaszyfruj” oraz „Odszyfruj”.
Sekcja wyników, która dynamicznie wyświetla rezultat operacji.
CSS:

Stylizacja formularza i strony, zapewniająca nowoczesny wygląd i responsywność.
Elementy są zorganizowane w kontenerze z zaokrąglonymi rogami i lekkim cieniem.
JavaScript:

Obsługuje wysyłanie żądań do backendu za pomocą fetch.
Przechwytuje błędy i wyświetla komunikaty w przypadku problemów.

5. Backend
Framework: Flask
Endpointy:
POST /encrypt – przyjmuje dane wejściowe (tekst, algorytm, klucz) i zwraca zaszyfrowany tekst.
POST /decrypt – przyjmuje dane wejściowe i zwraca odszyfrowany tekst.
Logika szyfrowania:
Zaimplementowana w pomocniczych funkcjach w Pythonie.
Obsługuje walidację kluczy i różne algorytmy szyfrowania.

7. Przepływ danych
Użytkownik wprowadza dane w formularzu i klika „Zaszyfruj” lub „Odszyfruj”.
JavaScript wysyła dane do backendu za pomocą fetch w formacie JSON.
Backend przetwarza dane i odsyła odpowiedź z wynikiem szyfrowania/odszyfrowania.
Wynik jest wyświetlany w sekcji „Wynik”.

9. Problemy i rozwiązania
Brak połączenia z backendem: Backend musi być uruchomiony, a aplikacja otwarta pod adresem serwera (http://127.0.0.1:5000/), a nie bezpośrednio z pliku lokalnego.
Obsługa błędów: Wbudowane mechanizmy w JavaScript informują użytkownika o problemach z połączeniem lub serwerem.

11. Możliwe rozszerzenia
Dodanie obsługi zaawansowanych algorytmów (np. AES, RSA).
Możliwość przesyłania plików do zaszyfrowania.
Wizualizacja procesu szyfrowania (np. animacje przesunięć liter).
Lokalizacja aplikacji na różne języki.
