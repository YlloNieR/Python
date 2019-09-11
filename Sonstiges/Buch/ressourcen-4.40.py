# Ein Objekt, zwei Referenzen
x = 42
# Ein Objekt "42", mit zwei Referenzen x, y auf das eine Objekt
y = 42
print("\nEin Objekt, zwei Referenzen")
print("x: ", x, "y: ", y, "identisch: ", x is y)

# Zweites Objekt
print("\nZweites Objekt")
print("y = 56")
# Zwei Objekte "42,56", mit jeweils einer Referenz x, y
y = 56
print("x: ", x, "y: ", y, "identisch: ", x is y)

# Ressourcen sparen
print("\nRessourcen sparen")
print("y = 42")
# Zurücksetzten des "y Wertes" -> Ein Objekt "42", mit zwei Referenzen x, y auf das eine Objekt
y = 42
print("x: ", x, "y: ", y, "identisch: ", x is y)

# Entfernen, Schritt 1
print("\nEntfernen, Schritt 1")
print("del y")
# Ein Objekt "42", mit einer Referenz x auf das eine Objekt, da y gelöscht
del y
print("x: ", x)

# Entfernen, Schritt 2
print("\nEntfernen, Schritt 2")
print("del x")
# Ein Objekt "42", verliert letzte Referenz x -> x nicht mehr vorhanden -> "Fehler"
del x
try:
    print("x: ", x)
except:
    print("Fehler")
