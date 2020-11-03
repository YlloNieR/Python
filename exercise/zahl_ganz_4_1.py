a = 27
print("Dezimal: ", a)
print("\nErkenungspräfix: 0x")
print("Hexadezimal:", hex(a), "1 mal 16 hoch 1 plus b (=11) mal 16 hoch 0")
print("\nErkenungspräfix: 0b")
print("Oktal: ", oct(a), "3 mal 8 hoch 1 plus 3 mal 8 hoch 0")
print("\nErkenungspräfix: 0o")
print("Dual: ", bin(
    a), "1 mal 2 hoch 4 plus 1 mal 2 hoch 3 plus 0 mal 2 hoch 2 plus 1 mal 2 hoch plus 1 mal 2 hoch 0")

b1 = 0x1a
b2 = 12
b3 = 0b101
b4 = 0o67
b = b1 + b2 + b3 + b4

print("Summe aus", b1, "...b1 +", b2, "...b2 +",
      b3, "...b3 +", b4, "...b4 = ", b)
