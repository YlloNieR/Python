x = 12
y = 15
z = 20
print("x: ", x)
print("y: ", y)
print("z: ", z)

# Bedinung 1 - UND
if x < y and x < z:
    print("x ist die kleinste Zahl")

# Bedinung 2 - ODER
if y > x or y > z:
    print("y ist nicht die kleinste Zahl")

# Bedinung 3 - NICHT
if not y < x:
    print("y ist nicht kleiner als x")
