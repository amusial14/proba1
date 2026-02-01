# projekt_bazy

## kroki uruchomienia
### 1. stworzenie lokalnej bazy 
  - ściągnij mariadb: https://mariadb.org/download/ - ustaw 'haslo_maslo67' jako hasło dla użytkownika 
  - wpisz do konsoli: `mysql -u root -p` (przy błędzie spróbuj zmienić 'mysql' na ścieżkę do mysql.exe)
  - konsola, znak zachęty wygląda inaczej: `MariaDB [(none)]>`, teraz wpisać: `CREATE DATABASE AiBtcQuantLandia;` (UWAGA: pamiętać o średniku na końcu)

### 2. wypełnienie bazy i analiza
- puść kod w pliku main.py
- analizę i raport daje jeden plik pod nazwą raport_i_analiza.ipynb: najpierw puszczamy cały plik w vsc, potem eksportujemy do pdf (gyd mamy latexa) lub do html rozwijając te trzy kropki pokazane na zrzucie ekranu poniżej: <img width="1130" height="334" alt="obraz" src="https://github.com/user-attachments/assets/ddd67381-5e27-487d-850a-bfd4b0ca6edd" />

## spis użytych technologii
- Python i dostępne jego pakiety (tworzenie klasy, łączenie skryptów)
- Jupyter Notebook
- Relacyjna baza danych
- język SQL i lokalny serwer mariidb
- integracja sql i pythona
- GitHub (tam "składaliśmy" po kolei nasz projekt)

## lista plików i ich zawartość
- main.py - główny plik, z którego wszystko uruchamiamy w wypełnianiu bazy
- raport_i_analiza.ipynb - daje raport i analizę
- config.py - można tu zmienić parametry używane do wypełniania bazy
- insert.py - wpakowywuje wygenerowane dane do tabel
- szkielet.sql - zawiera szkielet bazy (zapisany w języku sql)
- budowa.py - opisuje klasę Baza (zawiera też metodę czytającą szkielet.sql)
- generators - folder z plikami zawierającymi odpowiednio funkcje generowania danych ((wszystkie z rozszerzeniem py) attractions, costs, employees, generate_dates, guests, incident_type, incidents, inspections, insurance, malfunctions, payments, prices)

## schemat projektu bazy danych:
znajduje się w pliku pt. "schemayt"

## lista zależności funkcyjnych z wyjaśnieniem
1. Tabela attractions: attraction_id -> attraction_name, vr, built_date. Wyjaśnienie: Klucz główny identyfikuje nazwę atrakcji, informację czy posiada VR oraz datę budowy.
2. Tabela inspections: inspection_id -> attraction_id, inspection_date, result. Wyjaśnienie: Numer inspekcji identyfikuje, której atrakcji dotyczyła, kiedy się odbyła i czy ją przeszła.
3. Tabela malfunctions: malfunction_id -> attraction_id, accident_date, fix_date, comment, fix_cost. Wyjaśnienie: Każda awaria ma swój unikalny identyfikator, który pozwala przypisać ją do konkretnej atrakcji, daty naprawy, opisu i kosztu.
4. Tabela guests: guest_id -> first_name, last_name, birth_date. Wyjaśnienie: Klucz główny identyfikuje gościa i daje mu imię, nazwisko, datę urodzenia.
5. Tabela incident_type: incident_type_id -> name, risk_level. Wyjaśnienie: Typ incydentu ma przypisaną nazwę i poziom ryzyka.
6. Tabela insurance: insurance_id -> name, coverage_amount. Wyjaśnienie: Każde ubezpieczenie ma swoją nazwę i określony limit pokrycia.
7. Tabela guest_insurance: {guest_id, insurance_id}. Wyjaśnienie: To tabela łącznikowa. Złożony klucz główny służy jedynie do powiązania gościa z ubezpieczeniem.
8. Tabela incidents: incident_id -> incident_type_id, guest_id, attraction_id, incident_date, description. Wyjaśnienie: Każdy incydent jest unikalny i przypisany do konkretnego typu, gościa, atrakcji oraz daty.
9. Tabela costs: cost_id -> cost_type, amount, how_often, attraction_id. Wyjaśnienie: Identyfikator kosztu określa jego rodzaj, kwotę, okresowość, oraz atrakcję, której dotyczy.
10. Tabela payments: payment_id -> payment_date, amount, guest_id. Wyjaśnienie: Każda płatność ma przypisaną datę, kwotę oraz gościa, który jej dokonał.
11. Tabela employees: employee_id -> first_name, last_name, position, salary, hire_date, attraction_id. Wyjaśnienie: Klucz główny identyfikuje pracownika, imię i nazwisko, jego stanowisko, zarobki, moment zatrudnienia i przy jakiej atrakcji pracuje.
12. Tabela prices: ticket_id -> amount, attraction_id. Wyjaśnienie: Klucz główny identyfikuje klucz, daje mu koszt i do jakiej atrakcji.
13. Tabela payment_ticket: {payment_id, ticket_id}. Wyjaśnienie: To tabela łącznikowa. Złożony klucz główny służy jedynie do powiązania płatności z rodzajem biletu.



## uzasadnienie, że baza jest w EKNF
Każda tabela ma jasno określony klucz główny. Żaden atrybut niekluczowy nie zależy częściowo od klucza – wszystkie atrybuty są albo częścią klucza, albo w pełni zależą od całego klucza. Nie występują nadmiarowe zależności funkcyjne między atrybutami niekluczowymi a częścią klucza. 

## opis, co było najtrudniejsze podczas realizacji projektu
- Patrycja Krzyżostanek: "zacząć, a potem: wyrobić się"

