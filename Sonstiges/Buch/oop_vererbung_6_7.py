# Funktion dient der Vererbung auf nächste Datei
# Definition der Klasse Fahrzeug
class Fahrzeug:
    def __init__(self, bez, ge):
        # Konstruktormethode
        self.bezeichnung = bez
        # Eigenschaft 1
        self.geschwindigkeit = ge
        # Eigenschaft 2

    def beschleunigen(self, wert):
        # eigene Methode
        self.geschwindigkeit += wert

    def __str__(self):
        # Ausgabemethode
        return self.bezeichnung + " " \
            + str(self.geschwindigkeit) + "km/h"