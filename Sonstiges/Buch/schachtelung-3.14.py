print('''
1. Wert -2
2. Wert -1
3. Wert 0
4. Wert 1
5. Wert 2
''')
for x in -2, -1, 0, 1, 2:
    if x > 0:
        print(x, "positiv")
    else:
        if x < 0:
            print(x, "negativ")
        else:
            print(x, "gleich 0")
