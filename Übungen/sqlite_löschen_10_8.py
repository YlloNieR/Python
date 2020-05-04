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
sql = "DELETE FROM personen " \
      "WHERE personalnummer = 81343 "
cursor.execute(sql)
connection.commit()

# Nachher
ausgabe()

# Verbidnung beenden
connection.close()