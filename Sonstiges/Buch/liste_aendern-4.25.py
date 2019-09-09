# Originalliste
fr = ["Paris", "Lyon", "Marseille"]
print("Original: ")
print(fr)

# Einsetzten eines Elements
fr.insert(0, "Nantes")
print("\nNach Einsetzen: ")
print(fr)

# Sortieren der Elemente
fr.sort()
print("\nNach Sortieren: ")
print(fr)

# Umdrehen der Liste
fr.reverse()
print("\nNach Umdrehen: ")
print(fr)

# Entfernen eines Elements
fr.remove("Nantes")
print("\nNach Entfernen: ")
print(fr)

# Ein Element am Ende hinzu
fr.append("Paris")
print("\nEin Element hinzu: ")
print(fr)

# Anzahl bestimmter Elemente
print("\nAnzahl Elemente Paris: ", fr.count("Paris"))

# Suchen bestimmter Elemente 
print("Erste Position Paris: ", fr.index("Paris"))
