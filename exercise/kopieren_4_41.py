# Modul copy
import copy

# Kopie einer Liste, Methode 1
print('''
Kopie einer Liste, Methode 1
x = [23, "hallo", -7.5]
y = []
for i in x:
    y.append(i)
''')
x = [23, "hallo", -7.5]
y = []
for i in x:                 # elemente einzeln kopieren
    y.append(i)
print("dasselbe Objekt: ", x is y)
print("gleicher Inhalt: ", x == y)
print("x = ", x)
print("y = ", y)
print()

# Kopie einer Liste, Methode 2
print('''
Kopie einer Liste, Methode 2
x = [23, ["Berlin", "Hamburg"], -7.5, 12, 67]
y = copy.deepcopy(x)
''')
x = [23, ["Berlin", "Hamburg"], -7.5, 12, 67]
y = copy.deepcopy(x)        # Funktionen zur Tiefenkopie
print("dasselbe Objekt: ", x is y)
print("gleicher Inhalt: ", x == y)
print("x = ", x)
print("y = ", y)
