print("\n\n\t Black Jack")
'''
312 Karten
52 Blatt 13 Karten
K, Q, J

Croupier
bis zu sieben Spieler 

'''
print("")

class Kartendeck:
    numbers = [0,1,2,3,4,5,6,7,8,9,10,10,10,10,10,11]

    def diamond(self,RandomKarte):
        blattDiamonds = ["Diamond"]
        if RandomKarte == 0:
            print("NULL")
        elif RandomKarte == 1:
            print(*blattDiamonds, "A", ", Index =", RandomKarte)
        elif RandomKarte == 11:
            print(*blattDiamonds, "J", ", Index =", RandomKarte)
        elif RandomKarte == 12:
            print(*blattDiamonds, "Q", ", Index =", RandomKarte)
        elif RandomKarte == 13:   
            print(*blattDiamonds, "K", ", Index =", RandomKarte)
        elif RandomKarte == 14:   
            print(*blattDiamonds, "A", ", Index =", RandomKarte)
        else:
            print(*blattDiamonds, self.numbers[RandomKarte], ", Index =", RandomKarte)

    def hearts(self,RandomKarte):
        blattHearts = ["Heart"]
        if RandomKarte == 0:
            print("NULL")
        elif RandomKarte == 1:
            print(*blattHearts, "A", ", Index =", RandomKarte)
        elif RandomKarte == 11:
            print(*blattHearts, "J", ", Index =", RandomKarte)
        elif RandomKarte == 12:
            print(*blattHearts, "Q", ", Index =", RandomKarte)
        elif RandomKarte == 13:   
            print(*blattHearts, "K", ", Index =", RandomKarte)
        elif RandomKarte == 14:   
            print(*blattHearts, "A", ", Index =", RandomKarte)
        else:
            print(*blattHearts, self.numbers[RandomKarte], ", Index =", RandomKarte)

    def spades(self,RandomKarte):
        blattSpades = ["Spade"]
        if RandomKarte == 0:
            print("NULL")
        elif RandomKarte == 1:
            print(*blattSpades, "A", ", Index =", RandomKarte)
        elif RandomKarte == 11:
            print(*blattSpades, "J", ", Index =", RandomKarte)
        elif RandomKarte == 12:
            print(*blattSpades, "Q", ", Index =", RandomKarte)
        elif RandomKarte == 13:   
            print(*blattSpades, "K", ", Index =", RandomKarte)
        elif RandomKarte == 14:   
            print(*blattSpades, "A", ", Index =", RandomKarte)
        else:
            print(*blattSpades, self.numbers[RandomKarte], ", Index =", RandomKarte)

    def squares(self,RandomKarte):
        blattSquares = ["Square"]    
        if RandomKarte == 0:
            print("NULL")
        elif RandomKarte == 1:
            print(*blattSquares, "A", ", Index =", RandomKarte)
        elif RandomKarte == 11:
            print(*blattSquares, "J", ", Index =", RandomKarte)
        elif RandomKarte == 12:
            print(*blattSquares, "Q", ", Index =", RandomKarte)
        elif RandomKarte == 13:   
            print(*blattSquares, "K", ", Index =", RandomKarte)
        elif RandomKarte == 14:   
            print(*blattSquares, "A", ", Index =", RandomKarte)
        else:
            print(*blattSquares, self.numbers[RandomKarte], ", Index =", RandomKarte)       

    def kartenzug(self):
        global WertRandomKarte
        from random import randint
        Kartenstapel = randint(1, 4)
        RandomKarte = randint(1, 15)
        if Kartenstapel == 1:
            self.diamond(RandomKarte)
        elif Kartenstapel == 2:
            self.hearts(RandomKarte)
        elif Kartenstapel == 3:
            self.spades(RandomKarte)
        elif Kartenstapel == 4:
            self.squares(RandomKarte)
        WertRandomKarte = RandomKarte
    
    def get_list(self):    
        global Punkte    
        self.kartenzug()
        if WertRandomKarte < 10:
            Punkte = WertRandomKarte
        elif WertRandomKarte == 11 or 12 or 13:
            Punkte = 10

def punkteDealer():
    infile = open('zwischenspeicher1.txt', 'r')
    numbers = [int(line) for line in infile.readlines()]
    Punkte = sum(numbers)
    print(Punkte)
    if Punkte < 21:
        print("\tEine geht noch!")
        
    elif Punkte == 21:
        print("\tDer Dealer hat bereits Gewonnen!!")
        textfile = open("zwischenspeicher1.txt","w")
        textfile2 = open("zwischenspeicher2.txt","w")
        textfile.close()
        textfile2.close()
        exit()

    elif Punkte > 21:
        print("\tDer Dealer hat bereits Verloren!")
        textfile = open("zwischenspeicher1.txt","w")
        textfile2 = open("zwischenspeicher2.txt","w")
        textfile.close()
        textfile2.close()
        exit()


def punkteSpieler():
    infile = open('zwischenspeicher2.txt', 'r')
    numbers = [int(line) for line in infile.readlines()]
    Punkte = sum(numbers)
    print(Punkte)
    if Punkte < 21:
        print("\tEine geht noch!")
        
    elif Punkte == 21:
        print("\tDer Spieler hat bereits Gewonnen!!")
        textfile = open("zwischenspeicher1.txt","w")
        textfile2 = open("zwischenspeicher2.txt","w")
        textfile.close()
        textfile2.close()
        exit()
        
    elif Punkte > 21:
        print("\tDer Spieler hat bereits Verloren!")
        textfile = open("zwischenspeicher1.txt","w")
        textfile2 = open("zwischenspeicher2.txt","w")
        textfile.close()
        textfile2.close()
        exit()

def ersterZugDealer():
    print("Der Dealer beginnt seinen ersten Zug ...")
    textfile = open("zwischenspeicher1.txt","a")
    y = Kartendeck().get_list()
    z = Punkte
    textfile.write(str(z) + "\n")
    textfile.close()
    punkteDealer()
    spielDealer()

def ersterZugSpieler():
    textfile = open("zwischenspeicher2.txt","a")
    y = Kartendeck().get_list()
    z = Punkte
    textfile.write(str(z) + "\n")
    textfile.close()
    punkteSpieler()
        
def spielDealer(): 
    x = input("\n Dealer - Möchtest du eine Karte j/n ? ")     
    if x == "j":
        textfile = open("zwischenspeicher1.txt","a")
        y = Kartendeck().get_list()
        z = Punkte
        textfile.write(str(z) + "\n")
        textfile.close()
        punkteDealer()
        spielDealer()
    else:
        infile = open('zwischenspeicher1.txt', 'r')
        numbers = [int(line) for line in infile.readlines()]
        PunkteDealer = sum(numbers)
        print("\n Punktestand Dealer = ", PunkteDealer,"\n") 
        print("\n Dann ist als nächstes der Spieler dran ... \n")       
        spielSpieler()    

def punkteAll():
    fileDealer = open('zwischenspeicher1.txt', 'r')
    numbers = [int(line) for line in fileDealer.readlines()]
    PunkteDealer = sum(numbers)
    print("\n\tPunktestand Dealer = ", PunkteDealer)
    fileSpieler = open('zwischenspeicher2.txt', 'r')
    numbers = [int(line) for line in fileSpieler.readlines()]
    PunkteSpieler = sum(numbers)
    print("\tPunktestand Spieler = ", PunkteSpieler)

    if PunkteSpieler > PunkteDealer:
        print("\n\tSpieler hat gewonnen!")
    if PunkteSpieler == PunkteDealer:
        print("\n\tSpieler hat gewonnen!")
    elif PunkteSpieler < PunkteDealer:
        print("\n\tDealer hat gewonnen!")


def spielSpieler():
    x = input("\n Spieler - Möchtest du eine Karte j/n ? ")     
    if x == "j":
        textfile = open("zwischenspeicher2.txt","a")
        y = Kartendeck().get_list()
        z = Punkte
        textfile.write(str(z) + "\n")
        textfile.close()
        punkteSpieler()
        spielSpieler()
        
    else:        
        punkteAll()

    z = input("\nerneut Spielen j/n ? ")     

    if z == "j":
        textfile = open("zwischenspeicher1.txt","w")
        textfile2 = open("zwischenspeicher2.txt","w")
        textfile.close()
        textfile2.close()
        spielDealer()
    else:
        textfile = open("zwischenspeicher1.txt","w")
        textfile2 = open("zwischenspeicher2.txt","w")
        textfile.close()
        textfile2.close()
        exit()


ersterZugDealer()