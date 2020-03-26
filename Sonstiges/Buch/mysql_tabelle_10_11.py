# Connector importieren
import sys
import mysql.connector

# Verbindung zur Datenbank auf dem Datenbankserver erstellen
try:
    connection = mysql.connector.connect(
        host="localhost", user="root", passwd="", db="firma_10_10")
except:
    print("Keine Verbindung zum Server")
    sys.exit(0)

# Execution-Objekt erzeugen
cursor = connection.cursor()

# Tabelle erzeugen
cursor.execute("CREATE TABLE IF NOT EXISTS  personen"
               "(name VARCHAR(30), vorname VARCHAR(25),"  # max Länge
               "personalnummer INT(11),"
               "gehalt DOUBLE, geburtstag DATE)"  # Double = Zahlen mit Nachkommastellen
               "ENGINE=MyISAM DEFAULT CHARSET=UTF8")
connection.commit()

# Primärschlüssel erzeugen
cursor.execute("ALTER TABLE personen"
               " ADD PRIMARY KEY (personalnummer)")
connection.commit()

# Execution-Objekt schließen
cursor.close

# Verbindung schließen
connection.close()
