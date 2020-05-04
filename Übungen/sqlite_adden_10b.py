import sqlite3

def ausgabe():
    # SQL-Abfrage, senden, Ausgabe
    sql = "SELECT * FROM personen"
    cursor.execute(sql)
    print("...:")
    for dsatz in cursor:
        print(dsatz[0],dsatz[1],dsatz[2],dsatz[3],dsatz[4])
    print()

# Verbindung, Cursor
connection = sqlite3.connect("firma_SQLite_10.db")
cursor = connection.cursor()

# Vorher
ausgabe()

# Datensatz entfernen
personalnummer = int(input('zu löschende personalnummer: '))
sql = "DELETE FROM `personen` WHERE personalnummer = ?"
cursor.execute(sql, (personalnummer,))
connection.commit()

# Nachher
ausgabe()

# Verbidnung beenden
connection.close()