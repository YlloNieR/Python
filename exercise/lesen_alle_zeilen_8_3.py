import sys

# Zugriffsversuch
try:
    d = open("lesen_8_4.txt")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Lesen aller Zeiten in eine Liste
allezeilen = d.readlines()

# Schließen der Datei
d.close()

# Ausgabe und Summierung der Listenelemente
summe = 0
for zeile in allezeilen:
    print(zeile, end="")
    summe += float(zeile)

# Ausgabe der Summe
print("Summe: ", summe)
