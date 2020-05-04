import sqlite3

# Verbindung, Cursor
connection = sqlite3.connect("firma_SQLite_10.db")
cursor = connection.cursor()

# Eingabe Name
eingabe = input("Bitte den gesuchten Namen eingeben: ")
sql = "SELECT * FROM personen WHERE name  LIKE ?"
cursor.execute(sql, (eingabe,))
print("unter dem gesuchten Namen ",eingabe," wurden folgende Einträge gefunden:")
for dsatz in cursor:
    print(dsatz[0],dsatz[1])
print()

# Eingabe Teile des Namens
eingabe2 = input("Bitte den gesuchten Namensteil eingeben: ")
sql = "SELECT * FROM personen WHERE name  LIKE ?"
eingabe2 = '%' + eingabe2 + '%'
cursor.execute(sql, (eingabe2,))
print("unter dem gesuchten Namensteil ",eingabe2," wurden folgende Einträge gefunden:")
for dsatz in cursor:
    print(dsatz[0],dsatz[1])
print()

# Verbidnung beenden
connection.close()