import sqlite3

def ausgabe():
    # SQL-Abfrage, senden, Ausgabe
    sql = "SELECT * FROM personen"
    cursor.execute(sql)
    print("...:")
    for dsatz in cursor:
        print(dsatz[0],'|',dsatz[1],'|',dsatz[2],'|',dsatz[3],'|',dsatz[4],'|',dsatz[5])
    print()

# Verbindung, Cursor
connection = sqlite3.connect("firma_SQLite_10.db")
cursor = connection.cursor()

# Vorher
ausgabe()

# Datensatz erzeugen
personalnummer = input("personalnummer: ")
name = input("name: ")
vorname = input("vorname: ")
gehalt = input("gehalt: ")
waehrung = input("währung: ")
geburtstag = input("Geburtstag: ")

sql = "INSERT INTO personen (name, vorname, personalnummer, gehalt, waehrung, geburtstag)" + " values (?, ?, ?, ?, ?, ?)";
cursor.execute(sql, (name, vorname, personalnummer, gehalt, waehrung, geburtstag))
connection.commit()

# Nachher
ausgabe()

# Verbidnung beenden
connection.close()