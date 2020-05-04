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

# Daten auslesen
cursor.execute("SELECT * FROM personen")
result = cursor.fetchall()

# Execution-Objekt schließen
cursor.close

# Verbindung schließen
connection.close()

# Daten ausgeben
for data in result:
    print(str(data[0]) + ", " + str(data[1]) + ", " +
          str(data[2]) + ", " + str(data[3]) + ", " + str(data[4]))
