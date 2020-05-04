# Definition der Klasse Fahrzeug


class Fahrzeug:
    def __init__(self, bez, ge):
        # Konstruktormethode
        self.bezeichnung = bez
        self.geschwindigkeit = ge

    def beschleunigen(self, wert):
        # eigene Methode
        self.geschwindigkeit += wert

    def __str__(self):
        # Ausgabemethode
        return self.bezeichnung + " " \
            + str(self.geschwindigkeit) + " km/h"

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

# Definition der Klasse LKW


class LKW(Fahrzeug):
    def __init__(self, bez, ge, la):
        Fahrzeug.__init__(self, bez, ge)
        self.ladung = la

    def __str__(self):
        return Fahrzeug.__str__(self) + " " \
            + str(self.ladung) + " Tonnen Ladung"

    def beladen(self, wert):
        self.ladung += wert

    def entladen(self, wert):
        self.ladung -= wert

# Definition der Klasse Lieferwagen


class Lieferwagen(PKW, LKW):
    def __init__(self, bez, ge, ins, la):
        PKW.__init__(self, bez, ge, ins)
        LKW.__init__(self, bez, ge, la)

    def __str__(self):
        return PKW.__str__(self) + "\n" \
            + LKW.__str__(self)


# Objekt der abgeleiteten Klasse Lieferwagen erzeugen
toyota = Lieferwagen("Toyota Allround", 0, 0, 0)
toyota.einsteigen(2)
toyota.beladen(3.5)
toyota.beschleunigen(30)
print(toyota)
