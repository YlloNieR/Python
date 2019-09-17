# Definition der Klasse PKW
# Ableitung von Fahrzeug wird in Klammern geschrieben
class PKW(Fahrzeug):
    def __init__(self, bez,ge,ins):
        Fahrzeug.__init__(self,bez,ge)
        self.insassen = ins
    def __str__(self):
        return Fahrzeug.__str__(self) + " " \
            + str(self.insassen) + " Insassen"
    def einsteigen(self, anzahl):
        self.insassen += anzahl
    def aussteigen(self, anzahl):
        self.insassen -= anzahl