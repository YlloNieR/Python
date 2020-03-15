import os
import sys
import sqlite3

# Existenz feststellen
if os.path.exists("firma_SQLite_10.db"):
    print("Datei bereits vorhanden")
    sys.exit(0)

# Verbindung zur Datenbank erzeugen
connection = sqlite3.connect("firma_SQLite_10.db")

# Datensatz-Cursor erzeugen
cursor = connection.cursor()

# Tabelle erzeugen
sql = "CREATE TABLE personen(" \
    "name TEXT, " \
    "vorname TEXT, " \
    "personalnummer INTEGER PRIMARY KEY, " \
    "gehalt REAL, " \
    "waehrung TEXT, " \
    "geburtstag TEXT)"
cursor.execute(sql)

# Datensatz erzeugen
sql = "INSERT INTO personen VALUES('Maier', " \
    "'Hans', 6714, 3500.00,'€', '15.03.1962')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeuegen
sql = "INSERT INTO personen VALUES('Schmitz', " \
    "'Peter', 81343, 3750.00,'€', '12.04.1958')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeuegen
sql = "INSERT INTO personen VALUES('Mertens', " \
    "'Julia', 2297, 3621.50,'€', '30.12.1959')"
cursor.execute(sql)
connection.commit()

# Verbindung beenden
connection.close()
