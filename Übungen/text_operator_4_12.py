# Operatoren + und *
t1 = "Teil 1"
t2 = "Teil 2"
tgesamt = t1 + ", " + t2
t3 = "-0000-"
t4 = "***"
tlinie = t4 + t3 * 3 + t4
print(tgesamt)
print(tlinie)

# Operator in und not
tname = "Robinson Crusoe"
print("Text: ", tname)

if "b" in tname:
    print("b: ist enthalten")

if "p" not in tname:
    print("p: ist nicht enthalten")
