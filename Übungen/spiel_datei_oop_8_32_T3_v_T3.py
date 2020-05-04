# Klasse "Highscore"
class Highscore:
    # Liste aus Datei lesen
    def __init__(self):
        self.liste = []
        if not glob.glob("spiel_datei_oop_highscore.csv"):
            return
        d = open("spiel_datei_oop_highscore.csv")
        zeile = d.readline()
        while(zeile):
            teil = zeile.split(";")
            name = teil[0]
            zeit = teil[1][0:len(teil[1])-1]
            zeit = zeit.replace(",", ".")
            self.liste.append([name, float(zeit)])
            zeile = d.readline()
        d.close()

    # Liste ändern
    def aendern(self, name, zeit):
        # Mitten in Liste schreiben
        gefunden = False
        for i in range(len(self.liste)):
            # Einsetzen in Liste
            if zeit < self.liste[i][1]:
                self.liste.insert(i, [name, zeit])
                gefunden = True
                break

        # Ans Ende der Liste schreiben
        if not gefunden:
            self.liste.append([name, zeit])

    # Liste ändern, in Datei speichern
    def speichern(self, name, zeit):
        self.aendern(name, zeit)
        d = open("spiel_datei_oop_highscore.csv", "w")
        for element in self.liste:
            name = element[0]
            zeit = str(element[1]).replace(".", ",")
            d.write(name + ";" + zeit + "\n")
        d.close()

    # Liste anzeigen
    def __str__(self):
        # Highscore nicht vorhanden
        if not self.liste:
            return "Keine Highscores vorhanden"

        # Ausgabe Highscore
        ausgabe = " P. Name         Zeit\n"
        for i in range(len(self.liste)):
            ausgabe += f"{i+1:2d}. {self.liste[i][0]:10}" \
                f"{self.liste[i][1]:5.2f} sec\n"
            if i >= 9:
                break
        return ausgabe