import random
print("Kopfrechnen")


# Aufgabe
def aufgabe():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    erg = a + b
    print("Die Aufgabe: ", a, "+", b)
    return erg


# Kommentar
def kommentar(eingabezahl, ergebnis): #die Werte eingabezahl und ergebnis werden an die Funktion übermittelt
    if eingabezahl == ergebnis:
        print(eingabezahl, "ist richtig")
    else:
        print(eingabezahl, "ist falsch")


# Zufallsgenerator
random.seed()

# Aufgabe
c = aufgabe()

# Schleife und Anzahl initialisieren
zahl = c + 1  # Vorbesetzung der VAR zahl für while Schleife damit sie mindestens einmal läuft
versuch = 0  # Vorbesetzung mit 0 dient der Aufzählung

# Schleife mit while
while zahl != c:
    # Anzahl Versuche
    versuch = versuch + 1

    # Eingabe mit Umwandlung
    print("Bitte eine ganze Zahl eingeben: ")
    z = input()

    # Versuch einer Umwandlung
    try:
        zahl = int(z)
    except:
        # Falls Umwandlung nicht erflgreich
        print("Sie haben keine ganze Zahl eingegeben!")
        # Schleife unmittelbar fortsetzen
        continue

    # Kommentar
    kommentar(zahl, c)

    # Verzweigung
    if zahl == c:
        print(zahl, "ist richtig")
        # Abbruch der Schleife
    else:
        print(zahl, "ist falsch")

# Ergebnis ausgeben
print("Ergebnis: ", c)
# Versuche ausgeben
print("Anzahl Versuche: ", versuch)
