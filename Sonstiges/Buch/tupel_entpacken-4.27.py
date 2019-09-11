# 1: Mehrfache Zuweisung
x, y, z = 3, 5.2, "hallo"
print("\nMehrfache zuweisung: ", x, y, z)

# 2: Auswirkungen erst danach
a = 12
b = 15
c = 22
a, b, c = c, a, a+b
print("\nAuswirkung: ", a, b, c)

# 3: Verpacken eines Tupels
p = 3, 4
print("\nVerpackt: ", p)

# 4: Entpacken eines Tupels
m, n = p
print("\nEntpacken: m: ", m, "n: ", n)

# 5: Falsche Zuweisung eines Tupels
try:
    s, t = 3, 4, 12
    print(s, t)
except:
    print("\nFehler")

# 6: Rest in Liste
print("\nRest in Liste")
x, *y, z = 3, 5.2, "hallo", 7.3, 2.9
# x = 3
print("x: ",x)
# y = [5.2, "hallo", 7.3] = Rest Liste
print("y: ",y)
print("z: ",z)

# kein Rest, Liste leer
print("kein Rest, Liste leer")
x, *y, z = 3, 5.2
print("x: ",x)
print("y: ",y)
print("z: ",z)
