# Modul
import re

# 11: Wiederholung, beliebig oft
tx = "aa und aba und abba und abbba und aca"
print(tx)
erg = re.findall("ab*a", tx)
print("11: ", erg)

# 12: Wiederholung, 1 oder mehr
erg = re.findall("ab*a", tx)
print("12: ", erg)

# 13: Wiederholung, 0 oder 1
erg = re.findall("ab?a", tx)
print("13: ", erg)

# 14: Wiederholung, m bis n
erg = re.findall("ab{2,3}a", tx)
print("14: ", erg)

# 15: Wiederholung der max. Menge von Zeichen
tx = "aa und aba und abba und aca und addda"
erg = re.findall("a.*a", tx)
print("15: ", erg)

# 16: Wiederholung der min. Menge von Zeichen
erg = re.findall("a.*?a", tx)
print("16: ", erg)
