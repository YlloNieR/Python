# Definition der Funktion
def mittelwert(x, y):
    ergebnis = (x+y) / 2
    return ergebnis


# Hauptprogramm
c = mittelwert(3, 9)  # Zwischenspeicherung des return Wertes der Funktion
print("Mittelwert: ", c)
x = 5
print("Mittelwert: ", mittelwert(x, 4)) # unmittelbare Ausgabe des return Wertes der Funktion
