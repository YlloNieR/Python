# Klasse "Spiel":
class Spiel:
    def __init__(self):
        # Start des Spiels
        random.seed()
        self.richtig = 0
        self.anzahl = 5
        s = input("Bitte geben Sie Ihren "
                  "Namen ein (max. 10 Zeichen): ")
        self.spieler = s[0:10]

    def spielen(self):
        # Spielablauf
        for i in range(1, self.anzahl+1):
            a = Aufgabe(i, self.anzahl)
            print(a)
            self.richtig += a.beantworten()

    def messen(self, start):
        # Zeitmessung
        if start:
            self.startzeit = time.time()
        else:
            endzeit = time.time()
            self.zeit = endzeit - self.startzeit

    def __str__(self):
        # Ergebnis
        ausgabe = f"Richtig: {self.richtig:d} von " \
            f" {self.anzahl:d} in " \
            f"{self.zeit:.2f} Sekunden"
        if self.richtig == self.anzahl:
            ausgabe += ", Highscore"
            hs = Highscore()
            hs.speichern(self.spieler, self.zeit)
            print(hs)
        else:
            ausgabe += ", leider kein Highscore"
        return ausgabe