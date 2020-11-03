# Nur 1 Bit gesetzt
bit0 = 1            # 0000 0001 = 1
bit3 = 8            # 0000 1000 = 8
print("Nur ein Bit gesetzt", 2*"\t", bin(bit0), bin(bit3))
print("")

# Bitweises AND
a = 5               # 0000 0101 = 5
erg = a & bit0      # 0000 0001 = 1
if erg:
    print("Bitweises AND", 3*"\t", a, "ist ungerade")
print("")

# Bitweises OR
erg = 0             # 0000 0000 = 0
erg = erg | bit0    # 0000 0001 = 1
erg = erg | bit3    # 0000 1001 = 9
print("Bits nacheinander gesetzt: ", "\t", erg, bin(erg))
print("")

# Bitweises Exclusive-OR
a = 21              # 0001 0101 = 21
b = 19              # 0001 0011 = 19
erg = a ^ b         # 0000 0110 = 6
print("Ungleiche Bits: ", 2*"\t", erg, bin(erg))
print("")

# Bitweise Inversion, aus x wird -(x+1)
a = 11              # 0000 1011 = 11
erg = ~a            # 1111 0100 = 484
print("Bitweise Inversion: ", 2*"\t", erg, bin(erg), "\taus x wird -(x+1)")
print("")

# Bitweise schieben
a = 11              # 0000 1011 = 11
erg = a >> 1        # 0000 0101 = 5
print('''0000 1011
um 1 nach rechts geschoben: ''',
      "\t", "0000 0101", "\t", erg, bin(erg))
erg = a << 2        # 0010 1100 = 76
print('''\n0000 1011
Um 2 nach links geschoben: ''',
      "\t", "0010 1100", "\t", erg, bin(erg))
