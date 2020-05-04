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

# Definition der Klasse PKW
# Ableitung von Fahrzeug wird in Klammern geschrieben


class PKW(Fahrzeug):
    def __init__(self, bez, ge, ins):
        Fahrzeug.__init__(self, bez, ge)
        self.insassen = ins

    def __str__(self):
        return Fahrzeug.__str__(self) + " " \
            + str(self.insassen) + " Insassen"

    def einsteigen(self, anzahl):
        self.insassen += anzahl

    def aussteigen(self, anzahl):
        self.insassen -= anzahl


# Objekt der abgeleiteten Klasse PKW erzeugen
fiat = PKW("Fiat Marea", 50, 0)

# Eigene Methode anwenden
fiat.einsteigen(3)
fiat.aussteigen(1)

# Geerbte Methode anwenden
fiat.beschleunigen(10)

# Überschriebene Methode anwenden
print(fiat)
