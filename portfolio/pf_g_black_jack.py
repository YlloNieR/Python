import tkinter as tk

blackJack = tk.Tk()
blackJack.title('Black Jack')
blackJack.geometry("640x800+1800+200")


def back():
    blackJack.destroy()

def clearAusgabe():
    ausgabefeld.delete("1.0", "end")    




class Kartendeck:
    numbers = [0,1,2,3,4,5,6,7,8,9,10,10,10,10,10,11]
    def diamond(self,RandomKarte):        
        blattDiamonds = ["Diamond"]
        if RandomKarte == 0:
            ausgabe="NULL"
            ausgabefeld.insert('end', ausgabe)
        elif RandomKarte == 1:
            ausgabe=*blattDiamonds, "A", ", Index =", RandomKarte, "\n"
            ausgabefeld.insert('end', ausgabe)
        elif RandomKarte == 11:
            ausgabe=*blattDiamonds, "J", ", Index =", RandomKarte, "\n"
            ausgabefeld.insert('end', ausgabe)
        elif RandomKarte == 12:
            ausgabe=*blattDiamonds, "Q", ", Index =", RandomKarte, "\n"
            ausgabefeld.insert('end', ausgabe)
        elif RandomKarte == 13:   
            ausgabe=*blattDiamonds, "K", ", Index =", RandomKarte, "\n"
            ausgabefeld.insert('end', ausgabe)
        elif RandomKarte == 14:   
            ausgabe=*blattDiamonds, "A", ", Index =", RandomKarte, "\n"
            ausgabefeld.insert('end', ausgabe)
        else:
            ausgabe=*blattDiamonds, self.numbers[RandomKarte], ", Index =", RandomKarte, "\n"
            ausgabefeld.insert('end', ausgabe)

    def hearts(self,RandomKarte):        
        blattHearts = ["Heart"]
        if RandomKarte == 0:
            ausgabe="NULL"
            ausgabefeld.insert('end', ausgabe)
        elif RandomKarte == 1:
            ausgabe=*blattHearts, "A", ", Index =", RandomKarte, "\n"
            ausgabefeld.insert('end', ausgabe)
        elif RandomKarte == 11:
            ausgabe=*blattHearts, "J", ", Index =", RandomKarte, "\n"
            ausgabefeld.insert('end', ausgabe)
        elif RandomKarte == 12:
            ausgabe=*blattHearts, "Q", ", Index =", RandomKarte, "\n"
            ausgabefeld.insert('end', ausgabe)
        elif RandomKarte == 13:   
            ausgabe=*blattHearts, "K", ", Index =", RandomKarte, "\n"
            ausgabefeld.insert('end', ausgabe)
        elif RandomKarte == 14:   
            ausgabe=*blattHearts, "A", ", Index =", RandomKarte, "\n"
            ausgabefeld.insert('end', ausgabe)
        else:
            ausgabe=*blattHearts, self.numbers[RandomKarte], ", Index =", RandomKarte, "\n"
            ausgabefeld.insert('end', ausgabe)

    def spades(self,RandomKarte):        
        blattSpades = ["Spade"]
        if RandomKarte == 0:
            ausgabe="NULL"
            ausgabefeld.insert('end', ausgabe)
        elif RandomKarte == 1:
            ausgabe=*blattSpades, "A", ", Index =", RandomKarte, "\n"
            ausgabefeld.insert('end', ausgabe)
        elif RandomKarte == 11:
            ausgabe=*blattSpades, "J", ", Index =", RandomKarte, "\n"
            ausgabefeld.insert('end', ausgabe)
        elif RandomKarte == 12:
            ausgabe=*blattSpades, "Q", ", Index =", RandomKarte, "\n"
            ausgabefeld.insert('end', ausgabe)
        elif RandomKarte == 13:   
            ausgabe=*blattSpades, "K", ", Index =", RandomKarte, "\n"
            ausgabefeld.insert('end', ausgabe)
        elif RandomKarte == 14:   
            ausgabe=*blattSpades, "A", ", Index =", RandomKarte, "\n"
            ausgabefeld.insert('end', ausgabe)
        else:
            ausgabe=*blattSpades, self.numbers[RandomKarte], ", Index =", RandomKarte, "\n"
            ausgabefeld.insert('end', ausgabe)

    def squares(self,RandomKarte):
        blattSquares = ["Square"]    
        if RandomKarte == 0:
            ausgabe="NULL"
            ausgabefeld.insert('end', ausgabe)
        elif RandomKarte == 1:
            ausgabe=*blattSquares, "A", ", Index =", RandomKarte, "\n"
            ausgabefeld.insert('end', ausgabe)
        elif RandomKarte == 11:
            ausgabe=*blattSquares, "J", ", Index =", RandomKarte, "\n"
            ausgabefeld.insert('end', ausgabe)
        elif RandomKarte == 12:
            ausgabe=*blattSquares, "Q", ", Index =", RandomKarte, "\n"
            ausgabefeld.insert('end', ausgabe)
        elif RandomKarte == 13:   
            ausgabe=*blattSquares, "K", ", Index =", RandomKarte, "\n"
            ausgabefeld.insert('end', ausgabe)
        elif RandomKarte == 14:   
            ausgabe=*blattSquares, "A", ", Index =", RandomKarte, "\n"
            ausgabefeld.insert('end', ausgabe)
        else:
            ausgabe=*blattSquares, self.numbers[RandomKarte], ", Index =", RandomKarte, "\n"
            ausgabefeld.insert('end', ausgabe)  

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
    infile = open('pf_g_black_jack_speicher_dealer.txt', 'r')
    numbers = [int(line) for line in infile.readlines()]
    Punkte = sum(numbers)
    ausgabe=Punkte
    ausgabefeld.insert('end', ausgabe)
    if Punkte < 21:
        ausgabe="\tEine geht noch!\n"
        ausgabefeld.insert('end', ausgabe)
        
    elif Punkte == 21:
        ausgabe="\tDer Dealer hat bereits Gewonnen!!\n"
        ausgabefeld.insert('end', ausgabe)
        textfile = open("pf_g_black_jack_speicher_dealer.txt","w")
        textfile2 = open("pf_g_black_jack_speicher_spieler.txt","w")
        textfile.close()
        textfile2.close()
        restartGame()

    elif Punkte > 21:
        ausgabe="\tDer Dealer hat bereits Verloren!\n"
        ausgabefeld.insert('end', ausgabe)
        textfile = open("pf_g_black_jack_speicher_dealer.txt","w")
        textfile2 = open("pf_g_black_jack_speicher_spieler.txt","w")
        textfile.close()
        textfile2.close()
        restartGame()


def punkteSpieler():
    infile = open('pf_g_black_jack_speicher_spieler.txt', 'r')
    numbers = [int(line) for line in infile.readlines()]
    Punkte = sum(numbers)
    ausgabe=Punkte
    ausgabefeld.insert('end', ausgabe)
    if Punkte < 21:
        ausgabe="\tEine geht noch!\n"
        ausgabefeld.insert('end', ausgabe)
        
    elif Punkte == 21:
        ausgabe="\tDer Spieler hat bereits Gewonnen!!\n"
        ausgabefeld.insert('end', ausgabe)
        textfile = open("pf_g_black_jack_speicher_dealer.txt","w")
        textfile2 = open("pf_g_black_jack_speicher_spieler.txt","w")
        textfile.close()
        textfile2.close()
        restartGame()
        
    elif Punkte > 21:
        ausgabe="\tDer Spieler hat bereits Verloren!\n"
        ausgabefeld.insert('end', ausgabe)
        textfile = open("pf_g_black_jack_speicher_dealer.txt","w")
        textfile2 = open("pf_g_black_jack_speicher_spieler.txt","w")
        textfile.close()
        textfile2.close()
        restartGame()

def ersterZugDealer():
    ausgabefeld.delete("1.0", "end") 
    ausgabe="Der Dealer beginnt seinen ersten Zug ...\n"
    ausgabefeld.insert('end', ausgabe)
    textfile = open("pf_g_black_jack_speicher_dealer.txt","a")
    y = Kartendeck().get_list()
    z = Punkte
    textfile.write(str(z))
    textfile.write("\n")
    textfile.close()
    punkteDealer()
    #spielDealer()

def ersterZugSpieler():
    textfile = open("pf_g_black_jack_speicher_spieler.txt","a")
    y = Kartendeck().get_list()
    z = Punkte
    textfile.write(str(z))
    textfile.write("\n")
    textfile.close()
    punkteSpieler()
        
def spielDealer(): 
    ausgabe="\n Dealer - Möchtest du eine Karte j/n ?\n"
    ausgabefeld.insert('end', ausgabe)
    x = eingabe.get()  #   
    if x == "j":
        textfile = open("pf_g_black_jack_speicher_dealer.txt","a")
        y = Kartendeck().get_list()
        z = Punkte
        textfile.write(str(z))
        textfile.write("\n")
        textfile.close()
        punkteDealer()
        spielDealer()
    else:
        infile = open('pf_g_black_jack_speicher_dealer.txt', 'r')
        numbers = [int(line) for line in infile.readlines()]
        PunkteDealer = sum(numbers)
        ausgabe="\n Punktestand Dealer = ", PunkteDealer,"\n"
        ausgabefeld.insert('end', ausgabe)
        ausgabe="\n Dann ist als nächstes der Spieler dran ... \n"  
        ausgabefeld.insert('end', ausgabe)   
        spielSpieler()    

def punkteAll():
    fileDealer = open('pf_g_black_jack_speicher_dealer.txt', 'r')
    numbers = [int(line) for line in fileDealer.readlines()]
    PunkteDealer = sum(numbers)
    ausgabe="\n\tPunktestand Dealer = ", PunkteDealer
    ausgabefeld.insert('end', ausgabe)
    fileSpieler = open('pf_g_black_jack_speicher_spieler.txt', 'r')
    numbers = [int(line) for line in fileSpieler.readlines()]
    PunkteSpieler = sum(numbers)
    ausgabe="\tPunktestand Spieler = ", PunkteSpieler
    ausgabefeld.insert('end', ausgabe)

    if PunkteSpieler > PunkteDealer:
        ausgabe="\n\tSpieler hat gewonnen!\n"
        ausgabefeld.insert('end', ausgabe)
    if PunkteSpieler == PunkteDealer:
        ausgabe="\n\tSpieler hat gewonnen!\n"
        ausgabefeld.insert('end', ausgabe)
    elif PunkteSpieler < PunkteDealer:
        ausgabe="\n\tDealer hat gewonnen!\n"
        ausgabefeld.insert('end', ausgabe)


def spielSpieler():
    ausgabe="\n Spieler - Möchtest du eine Karte j/n ?\n"
    ausgabefeld.insert('end', ausgabe)    
    x = eingabe.get()
    if x == "j":
        textfile = open("pf_g_black_jack_speicher_spieler.txt","a")
        y = Kartendeck().get_list()
        z = Punkte
        textfile.write(str(z))
        textfile.write("\n")
        textfile.close()
        punkteSpieler()
        spielSpieler()
        
    else:        
        punkteAll()

def restartGame():
    ausgabe="\nerneut Spielen j/n ?\n"
    ausgabefeld.insert('end', ausgabe)
    z = eingabe.get()  #   

    if z == "j":
        textfile = open("pf_g_black_jack_speicher_dealer.txt","w")
        textfile2 = open("pf_g_black_jack_speicher_spieler.txt","w")
        textfile.close()
        textfile2.close()
        spielDealer()
    else:
        textfile = open("pf_g_black_jack_speicher_dealer.txt","w")
        textfile2 = open("pf_g_black_jack_speicher_spieler.txt","w")
        textfile.close()
        textfile2.close()
        restartGame()



#labeleingabe = tk.Label(rahmenreihe1, text='Eingabe:')
#labeleingabe.pack(side='left')

#eingabe = tk.Entry(rahmenreihe1, width=10)
#eingabe.pack(side='left')

rahmenreihe1 = tk.Frame(blackJack)
rahmenreihe1.pack(side='top', padx=10, pady=5)

bback = tk.Button(rahmenreihe1, width=10, text="Zurück", command=back)
bback.pack(side='top', padx=10, pady=5)

bstart = tk.Button(rahmenreihe1, text='Start/ Weiter', command=ersterZugDealer)
bstart.pack(side='left', padx=5, pady=5)

byes = tk.Button(rahmenreihe1, text='Ja')
byes.pack(side='left', padx=5, pady=5)

bno = tk.Button(rahmenreihe1, text='Nein', command=back)
bno.pack(side='left', padx=5, pady=5)

bdelete = tk.Button(blackJack, text='clear', command=clearAusgabe)
bdelete.pack(side='top', padx=5, pady=5)

#rahmenreihe2 = tk.Frame(blackJack)
#rahmenreihe2.pack(side='left', pady=5)

ausgabefeld = tk.Text(blackJack, height=40)
ausgabefeld.insert('end', "Start Game\n")
ausgabefeld.pack(fill='x',padx=10)

blackJack.mainloop()