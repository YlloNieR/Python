# Liste
li = [8, 2, 5, 5, 5]
print("Liste: ", li)

# Set / Mengen , Unterschied zu Listen = Jedes Element existiert nur einmal siehe nach for-Schleife
s1 = set([8, 2, 5, 5, 5])
print("Set: ", s1)
print("Anzahl: ", len(s1))

# Elemente
for x in s1:
    print("Element: ", x)
if 5 in s1:
    print("5 ist enthalten")
