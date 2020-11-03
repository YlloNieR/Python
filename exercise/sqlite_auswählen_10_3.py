import sqlite3

# Verbindung, Cursor
connection = sqlite3.connect("firma_SQLite_10.db")
cursor = connection.cursor()

# SQL-Abfrage
# Einzelne Felder
sql = "SELECT name, vorname FROM personen"
cursor.execute(sql)
print("Zeige mir alle Vornamen der Namen:")
for dsatz in cursor:
    print(dsatz[0], dsatz[1])
print()

# Auswahl mit WHERE-Klausel und Vergleichsoperator
sql = "SELECT * FROM personen " \
    "WHERE gehalt > 3600"
cursor.execute(sql)
print("Gehalt größer als  3600 € bei:")
for dsatz in cursor:
    print(dsatz[0],dsatz[3],dsatz[4])
print()

# Auswahl mit Zeichenkette
sql = "SELECT * FROM personen " \
    "WHERE name = 'Schmitz'"
cursor.execute(sql)
print("Wer heißt Schmitz mit Nachnamen:")
for dsatz in cursor:
    print(dsatz[0],dsatz[1])
print()

# Auswahl mit logischen Opreratoren
sql = "SELECT * FROM personen " \
    "WHERE gehalt >= 3600 AND gehalt <= 3650"
cursor.execute(sql)
print("Gehalt zwischen 3600 € & 3650 € bei:")
for dsatz in cursor:
    print(dsatz[0],dsatz[3],dsatz[4])
print()

# Verbidnung beenden
connection.close()
