import sqlite3

# Verbindung, Cursor
connection = sqlite3.connect("firma_SQLite_10.db")
cursor = connection.cursor()

# SQL-Abfragen
# beliebig viele Zeichen
sql = "SELECT * FROM personen WHERE name LIKE 'm%'"
cursor.execute(sql)
print("Zeige mir alle Personen dessen Name mit m beginnt:")
for dsatz in cursor:
    print(dsatz[0], dsatz[1])
print()

# Beinhaltet ...
sql = "SELECT * FROM personen WHERE name LIKE '%i%'"
cursor.execute(sql)
print("Zeige mir alle Personen dessen Name ein i beinhaltet:")
for dsatz in cursor:
    print(dsatz[0],dsatz[1])
print()

 # Beinhaltet ...
sql = "SELECT * FROM personen WHERE name LIKE '%a%' AND vorname LIKE '%a%'"
cursor.execute(sql)
print("Zeige mir alle Personen dessen Name & Vorname ein a beinhaltet:")
for dsatz in cursor:
    print(dsatz[0],dsatz[1])
print()

# Verbidnung beenden
connection.close()