import sys
import urllib.request


# Verbindung zu einer URL
try:
    u = urllib.request.urlopen("http://localhost/Projekte/Python/Sonstiges/Buch/url_lesen_9_1.htm")

except:
    print("Fehler")
    sys.exit(0)

# Liest alle Zeilen in eine Liste
li = u.readlines()

# Schliesst die Verbindung
u.close()

# Ausgabe der Liste
for element in li:
    print(element)
