# Definition der Klasse Fahrzeug
class Fahrzeug:
    def __init__(self, bez, ge):
        # Konstruktormethode
        self.bezeichnung = bez
        self.geschwindigkeit = ge

    def __str__(self):
        # Ausgabemethode
        # liefert Strings
        return self.bezeichnung + " " \
            + str(self.geschwindigkeit) + "km/h"

    def __repr__(self):
        # Info-Methode
        # liefert abrufbare Informationen
        return "Objekt " + self.bezeichnung \
            + " der Klasse Fahrzeug"


# Objekte der Klasse Fahrzeug erzeugen
opel = Fahrzeug("Opel Admiral", 40)
volvo = Fahrzeug("Volvo Amazon", 45)

# Objekte ausgeben
print(opel)
print(volvo)

# Informationen zu Objekt
print(repr(opel))
print(repr(volvo))
