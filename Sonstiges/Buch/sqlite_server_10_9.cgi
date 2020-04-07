#!C:\Users\...\AppData\Local\Programs\Python\Python38-32\python.exe

import sqlite3

# Dokumententyp
print("Content-type: text/html")
print()

# Dokumentenbeginn
print("<!DOCTYPE html><html>")
print("<head><meta charset:'utf8'></head>")
print("<body>")

# Verbindung, Cursor
connection = sqlite3.connect("firma_SQLite_10.db")
cursor = connection.cursor()

# SQL-Abfrage, Absenden, Ergebnis
sql = "SELECT * FROM personen"
cursor.execute(sql)

# Tabellenanfang / -ausgabe des Ergebnisses
print("<table border='1'>")

# Tabellenkopf
print("<tr><td>Name</td><td>Vorname</td>"
      "<td align='right'>PNr.</td>"
      "<td align='right'>Gehalt</td>"
      "<td></td>"
      "<td align='right'>Geburtsdatum</td>"
      "</tr>")

# Tabellenzeile
for dsatz in cursor:
    print("<tr>" + "<td>" + dsatz[0] + "</td>"  # Name
          + "<td>" + dsatz[1] + "</td>"  # Vorname
          + "<td align='right'>" + str(dsatz[2]) + "</td>"  # Personalnummer
          + f"<td align='right'>{dsatz[3]:.2f}</td>"  # Gehalt
          + "<td>" + dsatz[4] + "</td>"  # Währung
          + "<td>" + dsatz[5] + "</td>"  # Geburtstag
          + "</tr>")

# Tabellenende
print("</table>")

# Verbindungen beenden
connection.close()

# Dokumentenende
print("</body>")
print("</html>")
