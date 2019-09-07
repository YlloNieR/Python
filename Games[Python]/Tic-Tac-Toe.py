class Spielbrett:
    def __init__(self):
        self.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]  

    def Zug(self, zelle, spieler):
        if self.gueltiger_Zug(zelle):
            self.state[zelle] = spieler.x_oder_o
            return True
        return False

    def gueltiger_Zug(self, zelle):
        if self.state[zelle] == 0:
            return True
        else:
            return False

    def ueberpruefe_ob_gewonnen(self, spieler):
        s = spieler.x_oder_o
        #win waagerecht
        if self.state[0] == s and self.state[1] == s and self.state[2] == s:
            return True
        elif self.state[3] == s and self.state[4] == s and self.state[5] == s:
            return True
        elif self.state[6] == s and self.state[7] == s and self.state[8] == s:
            return True
        
        #win horizontal
        elif self.state[0] == s and self.state[3] == s and self.state[6] == s:
            return True
        elif self.state[1] == s and self.state[4] == s and self.state[7] == s:
            return True
        elif self.state[2] == s and self.state[5] == s and self.state[8] == s:
            return True

        #win diagonal
        elif self.state[0] == s and self.state[4] == s and self.state[8] == s:
            return True
        elif self.state[2] == s and self.state[4] == s and self.state[6] == s:
            return True

    def spielbrett_ist_Voll(self):
        for i in self.state:
            if i == 0:
                return False
        return True

    def X_Oder_O(self, sign):
        if sign == 0:
            return " "
        elif sign == 1:
            return "X"
        else:
            return "O"

    def zeichne_Spielbrett(self):
        print(" " + self.X_Oder_O(self.state[0]) + " | " + self.X_Oder_O(self.state[1]) + " | " + self.X_Oder_O(self.state[2]) + " \n" + 
              " " + self.X_Oder_O(self.state[3]) + " | " + self.X_Oder_O(self.state[4]) + " | " + self.X_Oder_O(self.state[5]) + " \n" + 
              " " + self.X_Oder_O(self.state[6]) + " | " + self.X_Oder_O(self.state[7]) + " | " + self.X_Oder_O(self.state[8]) + " \n")       


class Spieler:
    def __init__(self, x_oder_o):
        self.x_oder_o = x_oder_o

    
if __name__ == "__main__":
    Spieler_1 = Spieler(1)
    Spieler_2 = Spieler(-1)
    spielbrett = Spielbrett()
    aktive_Spieler = Spieler_1
    while not spielbrett.spielbrett_ist_Voll():
        spielbrett.zeichne_Spielbrett()
        try:
            zelle = int(input("Wo möchtest du deine Markierung machen? [1-9] "))
        except ValueError and IndexError:
            continue
        
        zelle = zelle - 1
        if zelle < 0 and zelle > 8:
            print("Bitte gib eine Nummer zwischen 1 und 9 ein ")
            continue
        if not spielbrett.Zug(zelle, aktive_Spieler):
            print("ungültiger Zug!")
            continue

        if spielbrett.ueberpruefe_ob_gewonnen(aktive_Spieler):
            spielbrett.zeichne_Spielbrett()
            print("Du hast gewonnen! :D")
            break

        if aktive_Spieler == Spieler_1:
            aktive_Spieler = Spieler_2
        else: 
            aktive_Spieler = Spieler_1
    print("Falls bis jetzt keiner gewonnen hat, ist es ein Unetschieden!") #muss noch geändert werden

