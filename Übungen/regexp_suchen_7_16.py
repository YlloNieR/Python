# Modul
import re

# 1: Exakter Text
tx = "Haus und Maus und Laus"
print(tx)
erg = re.findall("Maus", tx)
print("1: ", erg)

# 2: Wahl zwischen bestimmten Zeichen
erg = re.findall("[HM]aus", tx)
print("2: ", erg)

# 3: Alle Buchstaben aus Bereich
erg = re.findall("[L-M]aus", tx)
print("3: ", erg)

# 4: Alle Buchstaben nicht aus Bereich
erg = re.findall("[^L-M]aus", tx)
print("4:", erg)

# 5: Belibieges Zeichen
erg = re.findall(".aus", tx)
print("5: ", erg)

# 6: Suchbegriff nur am Anfang des Texts
erg = re.findall("^.aus", tx)
print("6: ", erg)

# 7: Suchbegriff nur am Ende des Textes
erg = re.findall(".aus$", tx)
print("7: ", erg)
print()
