import random
print("\tCalculator Game")

# Aufgabe und Variablen
a = random.randint(1, 10)

c = random.randint(1, 10)
versucheN = 1


def aufgabe():
    print("\tWieviel ist", a, "+", c, "? ")
    eingabe = int(input("\tBitte eine Zahl eingeben:\n"))
    ergebnis = a + c

    if eingabe == ergebnis:
        print("\t",eingabe, "ist richtig")
        print("\tAnzahl der Versuche", versucheN)
    else:
        print("\t",eingabe, "ist falsch")
        print("\tErgebnis: ", ergebnis)
        versucheN + 1


aufgabe()
