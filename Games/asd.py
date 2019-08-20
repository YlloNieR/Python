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
                
    def kartenzug(self):
            global WertRandomKarte
            from random import randint
            Kartenstapel = randint(1,1)
            RandomKarte = randint(1, 15)
            if Kartenstapel == 1:
                self.diamond(RandomKarte)
            WertRandomKarte = RandomKarte

    def get_list(self):    
        global Punkte    
        self.kartenzug()
        if WertRandomKarte < 10:
            Punkte = WertRandomKarte
        elif WertRandomKarte == 11 or 12 or 13:
            Punkte = 10

def punkte():
    infile = open('zwischenspeicher.txt', 'r')
    numbers = [int(line) for line in infile.readlines()]
    Punkte = sum(numbers)
    print(Punkte)
    if Punkte < 21:
        print("Eine geht noch!")
        
    elif Punkte == 21:
        print("gewonnen!!")
        
    elif Punkte > 21:
        print("Verloren")
        
    

def Spiel():
    punkte()
    x = input("\nMöchtest du eine Karte j/n ? ")     
    if x == "j":
        textfile = open("zwischenspeicher.txt","a")
        y = Kartendeck().get_list()
        z = Punkte
        textfile.write(str(z) + "\n")
        textfile.close()

    Ende = input("\nEnde j/n ? ")
    if Ende == "j":
        textfile = open("zwischenspeicher.txt","w")
        textfile.close()
    else:
        Spiel()

Spiel()
