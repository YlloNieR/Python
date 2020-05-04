print("range mit 3, 11, 3")
for i in range(3, 11, 3):
    print("Zahl: ", i, "Quadrat: ", i*i)

print('''
range nur mit 3! 11 und 3 fehlen
somit wird 0 als untere Grenze festgesetzt
und 3 wird als obere Grenze festgesetzt
''')
for i in range(3):
    print("Zahl: ", i, "Quadrat: ", i*i)
