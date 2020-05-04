# Kopie einer Zahl
print("Zahl: ")
x = 12.5
y = x
print("dasselbe Onjekt: ", x is y)
y = 15.8
print("dasselbe Objekt: ", x is y)
print("gleicher Inhalt: ", x == y)
print()

# Kopie eines Strings
print("String: ")
x = "Robinson"
y = x
print("dasselbe Objekt: ", x is y)
y = "Freitag"
print("dasselbe Objekt: ", x is y)
print("gleicher Inhalt: ", x == y)
print()

# Zweite Referenz auf einer Liste
print("Liste: ")
x = [23, "hallo", -7.5]
print("x Ausgangswert", x)
print("y Ausgangswert", y)
y = x
print("y = x, y -> ", y)
print("dasselbe Objekt: ", x is y)
print()
print("y[1] = Welt -> y = ", y)
y[1] = "welt"
print("dasselbe Objekt: ", x is y)
print("x = ", x)
print("y = ", y)
