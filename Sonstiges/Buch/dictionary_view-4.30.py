# Erzeugung
alter = {"Peter": 31, "Julia": 28, "Werner": 35}

# Werte / values
w = alter.values()
print("values")
print("Anzahl Werte: ", len(w))
for x in w:
    print(x)
if 31 in w:
    print("31 ist enthalten")
alter["Peter"] = 41
if 31 not in w:
    print("31 ist nicht enthalten")
print()

# Schlüssel / Keys = View der Keys des Dictionarys
k = alter.keys()
print("keys")
print("Anzahl Keys: ", len(k))
for x in k:
    print(x)
if "Werner" in k:
    print("Werner ist enthalten")
del alter["Werner"]
if "Werner" not in k:
    print("Werner ist nicht enthalten")
print()

# Elemente / Items = View der Items des Dictionarys
i = alter.items()
print("items")
alter["Franz"]=35
print("Anzahl Items: ", len(i))
for x in i:
    print(x)
if ("Julia", 28) in i:
    print("Julia, 28 ist enthalten")
