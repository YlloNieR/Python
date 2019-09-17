# Definition der Klasse Fahrzeug


# Eigenschaft
class Fahrzeug:
    geschwindigkeit = 0
# Methode

    def beschleunigung(self, wert):
        self.geschwindigkeit += wert
# Methode

    def ausgabe(self):
        print("Geschwindigkeit: ", self.geschwindigkeit)
