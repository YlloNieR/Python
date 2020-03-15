# Originalliste
fr = ["Paris", "Lyon", "Marseille", "Bordeaux"]
print("Original: ")
print(fr,"\n")

# Ersetzen eines Elements durch ein Element
fr[2] = "Lens"
print("Element ersetzt:")
print(fr,"\n")

# Ersetzen eines Teillbereiches durch eine Liste
fr[1:3] = ["Nancy", "Metz", "Gap"]
print("Teil ersetzt: ")
print(fr,"\n")

# Entnehmen eines Teilbereiches
del fr[3:]
print("Teil entnommen: ")
print(fr,"\n")

# Ersetzen eines Elements durch eine Liste
fr[0] = ["Paris-Nord", "Paris-Sud"]
print("Elemnt durch Liste ersetzt: ")
print(fr)
