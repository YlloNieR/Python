import sys


# Zugriffsversuch
try:
    d = open("schreiben_8_2.txt", "w")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Schreiben von einzelnen Strings, mit Zeilenende
d.write("Die erste Zeile\n")
for i in range(2, 11, 2):
    d.write(str(i) + " ")
d.write("\n")

# Schließen der Datei
d.close
