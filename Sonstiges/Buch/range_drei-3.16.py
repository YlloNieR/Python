print('''
 3 gibt Anfang des Bereichs an
11 gibt Ende des Bereichs an
 2 gibt Schrittweise für die Zahl (i) an
''')



for i in range(3, 11, 2):
    print("Zahl: ", i, "Quadrat: ", i*i)

print("\nohne range ist 3, 11, 2 die Abfolge der zu verwendenen Werte")

for i in 3, 11, 2:
    print("Zahl: ", i, "Quadrat: ", i*i)
