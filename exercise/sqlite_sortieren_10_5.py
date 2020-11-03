import sqlite3

# Verbindung, Cursor
connection = sqlite3.connect("firma_SQLite_10.db")
cursor = connection.cursor()

# Sortierung absteigend
sql = "SELECT * FROM personen ORDER BY gehalt DESC"
cursor.execute(sql)
print("Sortiere Gehalt absteigend (DESCending <-> ASCending):")
for dsatz in cursor:
    print(dsatz[0],dsatz[1],dsatz[3],dsatz[4])
print()

# Sortierung nach mehreren Feldern
sql = "SELECT * FROM personen ORDER BY name, vorname"
cursor.execute(sql)
print("Sortiere nach Nachname absteigend:")
for dsatz in cursor:
    print(dsatz[0],dsatz[1])
print()


# Verbidnung beenden
connection.close()