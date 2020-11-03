# Modul
import re

# 8: Alle Ziffern aus Bereich
tx = "0172-445633"
print(tx)
erg = re.findall("[0-2]", tx)
print("8: ", erg)

# 9: Alle Zeichen nicht aus Ziffernbereich
erg = re.findall("[^0-2]", tx)
print("9: ", erg)

# 10: Alle Zeichen oder Ziffern, die angegeben sind
erg = re.findall("[047-]", tx)
print("10: ", erg)
print()
