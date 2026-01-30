# projekt_bazy

## 1. stworzenie lokalnej bazy 
  - ściągnij mariadb: https://mariadb.org/download/ - ustaw 'haslo_maslo67' jako hasło dla użytkownika 
  - wpisz do konsoli: `mysql -u root -p` (przy błędzie spróbuj zmienić 'mysql' na ścieżkę do mysql.exe)
  - konsola, znak zachęty wygląda inaczej: `MariaDB [(none)]>`, teraz wpisać: `CREATE DATABASE AiBtcQuantLandia;` (UWAGA: pamiętać o średniku na końcu)

## 2. połączenie się z bazą: 
### po staremu ('add new connction' w vsc) i tutaj:
- database: AiBtcQuantLandia
- username: root
- zapyta się o hasło przy łączeniu
### przez pythona: gotowy bloczek kodu:
```
import mysql.connector
con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haslo_maslo67",
    database = "AiBtcQuantLandia"
)
```
## 3. tworzenie tabel: 
uruchomić plik 'pierwsza_tabela.sql' na połączeniu z bazą
