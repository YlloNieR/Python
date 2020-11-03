# Beispiel
test = "Das ist ein Beispielsatz"
print("Text: \t\t", test)

# Anzahl Suchtexte
such = "ei"
zo = '"'
suchPlus = zo + such + zo
anz = test.count(such)
print("\ncount: \t\tDer String", suchPlus, "kommt", anz, "Mal vor\n")


# Erste Position des Suchtextes
nextpos = test.rfind(such)
print("find 2: \tEin weiteres Mal kommt",
      suchPlus, "an Position", nextpos, "vor\n")

# letzte Position des Suchtextes
# Suche mit rfind() ergibt die letzte Position vom Suchtext im analysierten Bereich

endpos = test.rfind(such)
print("rfind: \t\tzum letzten Mal kommt",
      suchPlus, "an Position", endpos, "vor\n")

# Suchtext nicht gefunden
such = "am"
zo = '"'
suchPlus = zo + such + zo
pos = test.find(such)
if pos == -1:
    print("find 3: \t", suchPlus, "wird nicht im Beispieltext gefunden\n")
else:
    print("find 3: \t", suchPlus, "an Position", pos, "gefunden\n")

# Suche mit find() ergibt Position vom Suchtext im analysierten Bereich
such = "Beispiel"
zo = '"'
suchPlus = zo + such + zo
pos = test.find(such)
print("find 3: \t", suchPlus, "an Position", pos, "gefunden\n")

# Ersetzen von Text
test = test.replace("ist", "war")
test2 = "Das ist ein Beispielsatz"
print("Original: \t", test2)
print("replace: \t", test, '-> es wurde "ist" durch "war" ersetzt')
