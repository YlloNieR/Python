# mehrdimensionale Liste, unterschiedliche Objekte
x = [["Paris", "Fr", 350_000], ["Rom", "It", 4_200_000]]
print(x)

# Teilliste
print(x[0])

# einzelne Elemente
print(x[0][0], "hat", x[0][2], "Einwohner")
print(x[1][0], "hat", x[1][2], "Einwohner")

# Teile von Elementen
print(x[0][1][:1])
