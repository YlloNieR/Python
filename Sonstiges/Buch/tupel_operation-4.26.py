# Der Unterschied zur Liste
# Liste = [],           Tupel = ()
# Liste = veränderbar,  Tupel = nicht veränderbar

# Tupel mit und ohne Klammer
z = (3, 4, -8, 5.5)
print("Tupel 1: ", z)

z = 3, 6, -3
print("Tupel 2: ", z)

# mehrdimensionales Tupel, unterschiedliche Objekte
x = (("Paris", "Fr", 3_500_000), ["Rom", "It", 4_200_000])
print("\nmehrdim. Tupel: ")
print(x)

# Ersetzen
try:
    x[0][0] = "Lyon"    # nicht erlaubt, weil Tupel
except:
    print("\nFehler")

x[1][0] = "Pisa"        # erlaubt, weil Liste
print("\nListenelement ersetzt: ", x[1],"\n")

# Tupel bei der for-Schleife
for i in 4, 5, 12:
    print("i: ", i)

# Zuweisung mit Tupel
x, y = 2, 18
print("\nx: ", x, "y: ", y)
