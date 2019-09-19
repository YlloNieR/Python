import sys

# Zugriffsversuch
try:
    d = open("lesen_8_4.txt")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)


# Lesen des gesamten Texts
gesamtertext = d.read()

# Schließen der Datei
d.close()

# Umwandeln in eine Liste, Zerlegung durch split()
zeilenliste = gesamtertext.split(chr(10))

# Summieren und Ausgeben
summe = 0

for zeile in zeilenliste:
    if zeile:
        summe += float(zeile)
    print(zeile)

# Summe ausgeben
print("Summe: ", summe)
