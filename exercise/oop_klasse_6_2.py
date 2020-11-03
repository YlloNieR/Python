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


# Hauptprogramm Anfang
# Objekte der Klasse Fahrzeug erzeugen
# ist auch Instanzen einer Klasse erzeugen
opel = Fahrzeug()
volvo = Fahrzeug()

# Objektmethoden
volvo.ausgabe()
volvo.beschleunigung(20)
volvo.ausgabe()

# Objekt betrachten
opel.ausgabe()
