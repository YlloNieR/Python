import random


# Definition der Klassen


class Spiel:
    def __init__(self):
        # Start des Spiels
        random.seed()
        self.richtig = 0

        # Anzahl bestimmen
        self.anzahl = -1
        while self.anzahl < 0 or self.anzahl > 10:
            try:
                print("Wie viele Aufgaben (1 bis 10): ")
                self.anzahl = int(input())
            except:
                continue

    def spielen(self):
        # Spielablauf
        for i in range(1, self.anzahl+1):
            a = Aufgabe(i, self.anzahl)
            print(a)
            self.richtig += a.beantworten()

    def __str__(self):
        # Ergebnis
        return "Richtig: " + str(self.richtig) \
            + " von " + str(self.anzahl)


# Hauptprogramm
s = Spiel()
s.spielen()
print(s)
