# Set
s = set([8, 15, "x", 8])
print("Set: ", s)
for x in s:
    print(x)

# Frozenset
fs = frozenset([8, 15, "x", 8])
print("\nFrozenset: ", fs)
for x in fs:
    print(x)
try:
    fs.discard("x")
except:
    print("Fehler")
