# Ziffern
for i in range(48, 58):         # Unicode-Zahlen 48-57 = Ziffern 0-9
    print(chr(i), end="")
print()

# große Buchstaben
for i in range(65, 91):         # Unicode-Zahlen 65-90 = große Buchstaben
    print(chr(i), end="")
print()

# kleine Buchstaben
for i in range(97, 123):        # Unicode-Zahlen 97-122 = kleine Buchstaben
    print(chr(i), end="")
print()

# Codenummern
for z in "Robinson":
    print(ord(z), end=" ")      # Codenummern der Unicode-Zahlen von "Robinson"
print()

# Verschoben
for z in "Robinson":            # Verschlüselung anhand der Umwandlung von Unicode der Codenummern + 1 vom Wort Robinson
    print(chr(ord(z)+1), end="")
