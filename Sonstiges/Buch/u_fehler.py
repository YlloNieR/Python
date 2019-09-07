print("Umrechnung von Inch in cm")
# Initialisierung der while-Schleife
fehler = 1

# Schleife bei falscher Eingabe
while fehler == 1:
    # Eingabe
    print("Bitte geben Sie an wieviel Inch Sie in cm umrechnen wollen:")
    z = input()

    # Versuchder Umwandlung
    try:
        inch = int(z)
        print("Ihre Eingabe", inch, "Inch entsprechen", inch*2.54,"cm")
        fehler = 0
    # Fehler bei Umwandlung
    except:
        print("Das kann ich nicht umwandeln, probier es nochmal!")
print("Ende des Programms")