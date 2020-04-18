import tkinter as tk
import tkinter.messagebox

blackJack = tk.Tk()
blackJack.title('Black Jack')
blackJack.geometry("640x800+1800+200")


def back():
    blackJack.destroy()


def clearAusgabe():
    ausgabefeld.delete("1.0", "end")


class Kartendeck:
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 11]

    def diamond(self, RandomKarte):
        blattDiamonds = ["Diamond"]
        if RandomKarte == 0:
            ausgabe = "NULL"
            ausgabefeld.insert('end', ausgabe)
        elif RandomKarte == 1:
            ausgabe = *blattDiamonds, "A"
            index = "\nIndex = "
            rkarte = RandomKarte
            frei = "\n"
            ausgabefeld.insert('end', ausgabe)
            ausgabefeld.insert('end', index)
            ausgabefeld.insert('end', rkarte)
            ausgabefeld.insert('end', frei)
        elif RandomKarte == 11:
            ausgabe = *blattDiamonds, "J"
            index = "\nIndex = "
            rkarte = RandomKarte
            frei = "\n"
            ausgabefeld.insert('end', ausgabe)
            ausgabefeld.insert('end', index)
            ausgabefeld.insert('end', rkarte)
            ausgabefeld.insert('end', frei)
        elif RandomKarte == 12:
            ausgabe = *blattDiamonds, "D"
            index = "\nIndex = "
            rkarte = RandomKarte
            frei = "\n"
            ausgabefeld.insert('end', ausgabe)
            ausgabefeld.insert('end', index)
            ausgabefeld.insert('end', rkarte)
            ausgabefeld.insert('end', frei)
        elif RandomKarte == 13:
            ausgabe = *blattDiamonds, "K"
            index = "\nIndex = "
            rkarte = RandomKarte
            frei = "\n"
            ausgabefeld.insert('end', ausgabe)
            ausgabefeld.insert('end', index)
            ausgabefeld.insert('end', rkarte)
            ausgabefeld.insert('end', frei)
        elif RandomKarte == 14:
            ausgabe = *blattDiamonds, "A"
            index = "\nIndex = "
            rkarte = RandomKarte
            frei = "\n"
            ausgabefeld.insert('end', ausgabe)
            ausgabefeld.insert('end', index)
            ausgabefeld.insert('end', rkarte)
            ausgabefeld.insert('end', frei)
        else:
            ausgabe = *blattDiamonds, self.numbers[RandomKarte]
            index = "\nIndex = "
            rkarte = RandomKarte
            frei = "\n"
            ausgabefeld.insert('end', ausgabe)
            ausgabefeld.insert('end', index)
            ausgabefeld.insert('end', rkarte)
            ausgabefeld.insert('end', frei)

    def hearts(self, RandomKarte):
        blattHearts = ["Heart"]
        if RandomKarte == 0:
            ausgabe = "NULL"
            ausgabefeld.insert('end', ausgabe)
        elif RandomKarte == 1:
            ausgabe = *blattHearts, "A"
            index = "\nIndex = "
            rkarte = RandomKarte
            frei = "\n"
            ausgabefeld.insert('end', ausgabe)
            ausgabefeld.insert('end', index)
            ausgabefeld.insert('end', rkarte)
            ausgabefeld.insert('end', frei)
        elif RandomKarte == 11:
            ausgabe = *blattHearts, "J"
            index = "\nIndex = "
            rkarte = RandomKarte
            frei = "\n"
            ausgabefeld.insert('end', ausgabe)
            ausgabefeld.insert('end', index)
            ausgabefeld.insert('end', rkarte)
            ausgabefeld.insert('end', frei)
        elif RandomKarte == 12:
            ausgabe = *blattHearts, "D"
            index = "\nIndex = "
            rkarte = RandomKarte
            frei = "\n"
            ausgabefeld.insert('end', ausgabe)
            ausgabefeld.insert('end', index)
            ausgabefeld.insert('end', rkarte)
            ausgabefeld.insert('end', frei)
        elif RandomKarte == 13:
            ausgabe = *blattHearts, "K"
            index = "\nIndex = "
            rkarte = RandomKarte
            frei = "\n"
            ausgabefeld.insert('end', ausgabe)
            ausgabefeld.insert('end', index)
            ausgabefeld.insert('end', rkarte)
            ausgabefeld.insert('end', frei)
        elif RandomKarte == 14:
            ausgabe = *blattHearts, "A"
            index = "\nIndex = "
            rkarte = RandomKarte
            frei = "\n"
            ausgabefeld.insert('end', ausgabe)
            ausgabefeld.insert('end', index)
            ausgabefeld.insert('end', rkarte)
            ausgabefeld.insert('end', frei)
        else:
            ausgabe = *blattHearts, self.numbers[RandomKarte]
            index = "\nIndex = "
            rkarte = RandomKarte
            frei = "\n"
            ausgabefeld.insert('end', ausgabe)
            ausgabefeld.insert('end', index)
            ausgabefeld.insert('end', rkarte)
            ausgabefeld.insert('end', frei)

    def spades(self, RandomKarte):
        blattSpades = ["Spade"]
        if RandomKarte == 0:
            ausgabe = "NULL"
            ausgabefeld.insert('end', ausgabe)
        elif RandomKarte == 1:
            ausgabe = *blattSpades, "A"
            index = "\nIndex = "
            rkarte = RandomKarte
            frei = "\n"
            ausgabefeld.insert('end', ausgabe)
            ausgabefeld.insert('end', index)
            ausgabefeld.insert('end', rkarte)
            ausgabefeld.insert('end', frei)
        elif RandomKarte == 11:
            ausgabe = *blattSpades, "J"
            index = "\nIndex = "
            rkarte = RandomKarte
            frei = "\n"
            ausgabefeld.insert('end', ausgabe)
            ausgabefeld.insert('end', index)
            ausgabefeld.insert('end', rkarte)
            ausgabefeld.insert('end', frei)
        elif RandomKarte == 12:
            ausgabe = *blattSpades, "D"
            index = "\nIndex = "
            rkarte = RandomKarte
            frei = "\n"
            ausgabefeld.insert('end', ausgabe)
            ausgabefeld.insert('end', index)
            ausgabefeld.insert('end', rkarte)
            ausgabefeld.insert('end', frei)
        elif RandomKarte == 13:
            ausgabe = *blattSpades, "K"
            index = "\nIndex = "
            rkarte = RandomKarte
            frei = "\n"
            ausgabefeld.insert('end', ausgabe)
            ausgabefeld.insert('end', index)
            ausgabefeld.insert('end', rkarte)
            ausgabefeld.insert('end', frei)
        elif RandomKarte == 14:
            ausgabe = *blattSpades, "A"
            index = "\nIndex = "
            rkarte = RandomKarte
            frei = "\n"
            ausgabefeld.insert('end', ausgabe)
            ausgabefeld.insert('end', index)
            ausgabefeld.insert('end', rkarte)
            ausgabefeld.insert('end', frei)
        else:
            ausgabe = *blattSpades, self.numbers[RandomKarte]
            index = "\nIndex = "
            rkarte = RandomKarte
            frei = "\n"
            ausgabefeld.insert('end', ausgabe)
            ausgabefeld.insert('end', index)
            ausgabefeld.insert('end', rkarte)
            ausgabefeld.insert('end', frei)

    def squares(self, RandomKarte):
        blattSquares = ["Square"]
        if RandomKarte == 0:
            ausgabe = "NULL"
            ausgabefeld.insert('end', ausgabe)
        elif RandomKarte == 1:
            ausgabe = *blattSquares, "A"
            index = "\nIndex = "
            rkarte = RandomKarte
            frei = "\n"
            ausgabefeld.insert('end', ausgabe)
            ausgabefeld.insert('end', index)
            ausgabefeld.insert('end', rkarte)
            ausgabefeld.insert('end', frei)
        elif RandomKarte == 11:
            ausgabe = *blattSquares, "J"
            index = "\nIndex = "
            rkarte = RandomKarte
            frei = "\n"
            ausgabefeld.insert('end', ausgabe)
            ausgabefeld.insert('end', index)
            ausgabefeld.insert('end', rkarte)
            ausgabefeld.insert('end', frei)
        elif RandomKarte == 12:
            ausgabe = *blattSquares, "D"
            index = "\nIndex = "
            rkarte = RandomKarte
            frei = "\n"
            ausgabefeld.insert('end', ausgabe)
            ausgabefeld.insert('end', index)
            ausgabefeld.insert('end', rkarte)
            ausgabefeld.insert('end', frei)
        elif RandomKarte == 13:
            ausgabe = *blattSquares, "K"
            index = "\nIndex = "
            rkarte = RandomKarte
            frei = "\n"
            ausgabefeld.insert('end', ausgabe)
            ausgabefeld.insert('end', index)
            ausgabefeld.insert('end', rkarte)
            ausgabefeld.insert('end', frei)
        elif RandomKarte == 14:
            ausgabe = *blattSquares, "A"
            index = "\nIndex = "
            rkarte = RandomKarte
            frei = "\n"
            ausgabefeld.insert('end', ausgabe)
            ausgabefeld.insert('end', index)
            ausgabefeld.insert('end', rkarte)
            ausgabefeld.insert('end', frei)
        else:
            ausgabe = *blattSquares, self.numbers[RandomKarte]
            index = "\nIndex = "
            rkarte = RandomKarte
            frei = "\n"
            ausgabefeld.insert('end', ausgabe)
            ausgabefeld.insert('end', index)
            ausgabefeld.insert('end', rkarte)
            ausgabefeld.insert('end', frei)

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
    summe = "Summe = "
    Punkte = sum(numbers)
    ausgabe = Punkte
    ausgabefeld.insert('end', summe)
    ausgabefeld.insert('end', ausgabe)
    if Punkte < 21:        
        ausgabe = "\nEine geht noch!\n"
        ausgabefeld.insert('end', ausgabe)

    elif Punkte == 21:
        ausgabe = "\nDer Dealer hat bereits Gewonnen!!\n"
        ausgabefeld.insert('end', ausgabe)
        textfile = open("pf_g_black_jack_speicher_dealer.txt", "w")
        textfile2 = open("pf_g_black_jack_speicher_spieler.txt", "w")
        textfile.close()
        textfile2.close()
        restartGame()

    elif Punkte > 21:
        ausgabe = "\nDer Dealer hat bereits Verloren!\n"
        ausgabefeld.insert('end', ausgabe)
        textfile = open("pf_g_black_jack_speicher_dealer.txt", "w")
        textfile2 = open("pf_g_black_jack_speicher_spieler.txt", "w")
        textfile.close()
        textfile2.close()
        restartGame()


def punkteSpieler():
    infile = open('pf_g_black_jack_speicher_spieler.txt', 'r')
    numbers = [int(line) for line in infile.readlines()]
    Punkte = sum(numbers)
    ausgabe = Punkte
    ausgabefeld.insert('end', ausgabe)
    if Punkte < 21:
        ausgabe = "\nEine geht noch!\n"
        ausgabefeld.insert('end', ausgabe)

    elif Punkte == 21:
        ausgabe = "\nDer Spieler hat bereits Gewonnen!!\n"
        ausgabefeld.insert('end', ausgabe)
        textfile = open("pf_g_black_jack_speicher_dealer.txt", "w")
        textfile2 = open("pf_g_black_jack_speicher_spieler.txt", "w")
        textfile.close()
        textfile2.close()
        restartGame()

    elif Punkte > 21:
        ausgabe = "\nDer Spieler hat bereits Verloren!\n"
        ausgabefeld.insert('end', ausgabe)
        textfile = open("pf_g_black_jack_speicher_dealer.txt", "w")
        textfile2 = open("pf_g_black_jack_speicher_spieler.txt", "w")
        textfile.close()
        textfile2.close()
        restartGame()


def ersterZugDealer():
    ausgabefeld.delete("1.0", "end")
    ausgabe = "Der Dealer beginnt seinen ersten Zug ...\n"
    ausgabefeld.insert('end', ausgabe)
    textfile = open("pf_g_black_jack_speicher_dealer.txt", "a")
    y = Kartendeck().get_list()
    z = Punkte
    textfile.write(str(z))
    textfile.write("\n")
    textfile.close()
    punkteDealer()
    spielDealer()


def ersterZugSpieler():
    textfile = open("pf_g_black_jack_speicher_spieler.txt", "a")
    y = Kartendeck().get_list()
    z = Punkte
    textfile.write(str(z))
    textfile.write("\n")
    textfile.close()
    punkteSpieler()


def spielDealer():
    ausgabe = "\nDealer - Möchtest du eine Karte j/n ?\n"
    ausgabefeld.insert('end', ausgabe)
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure',icon = 'warning')
    if MsgBox == 'yes':
        textfile = open("pf_g_black_jack_speicher_dealer.txt", "a")
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
        ausgabe = "\nPunktestand Dealer = "
        ausgabe = PunkteDealer
        ausgabefeld.insert('end', ausgabe)
        ausgabe = "\nDann ist als nächstes der Spieler dran ... \n"
        ausgabefeld.insert('end', ausgabe)
        spielSpieler()


def punkteAll():
    fileDealer = open('pf_g_black_jack_speicher_dealer.txt', 'r')
    numbers = [int(line) for line in fileDealer.readlines()]    
    ausgabe = "\nPunktestand Dealer = "
    PunkteDealer = sum(numbers)
    ausgabefeld.insert('end', ausgabe)
    ausgabefeld.insert('end', PunkteDealer)
    fileSpieler = open('pf_g_black_jack_speicher_spieler.txt', 'r')
    numbers = [int(line) for line in fileSpieler.readlines()]
    ausgabe = "\nPunktestand Spieler = "
    PunkteSpieler = sum(numbers)
    ausgabe = PunkteSpieler
    ausgabefeld.insert('end', ausgabe)

    if PunkteSpieler > PunkteDealer:
        ausgabe = "\nSpieler hat gewonnen!\n"
        ausgabefeld.insert('end', ausgabe)
    if PunkteSpieler == PunkteDealer:
        ausgabe = "\nSpieler hat gewonnen!\n"
        ausgabefeld.insert('end', ausgabe)
    elif PunkteSpieler < PunkteDealer:
        ausgabe = "\nDealer hat gewonnen!\n"
        ausgabefeld.insert('end', ausgabe)


def spielSpieler():
    ausgabe = "\nSpieler - Möchtest du eine Karte j/n ?\n"
    ausgabefeld.insert('end', ausgabe)
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
        textfile = open("pf_g_black_jack_speicher_spieler.txt", "a")
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
    ausgabe = "\nerneut Spielen j/n ?\n"
    ausgabefeld.insert('end', ausgabe)
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure',icon = 'warning')
    if MsgBox == 'yes':
        textfile = open("pf_g_black_jack_speicher_dealer.txt", "w")
        textfile2 = open("pf_g_black_jack_speicher_spieler.txt", "w")
        textfile.close()
        textfile2.close()
        spielDealer()
    else:
        textfile = open("pf_g_black_jack_speicher_dealer.txt", "w")
        textfile2 = open("pf_g_black_jack_speicher_spieler.txt", "w")
        textfile.close()
        textfile2.close()
        restartGame()

my_string_var = tk.StringVar()
my_string_var.set('j')

rahmenreihe1 = tk.Frame(blackJack)
rahmenreihe1.pack(side='top', padx=10, pady=5)

bback = tk.Button(rahmenreihe1, width=10, text="Zurück", command=back)
bback.pack(side='top', padx=10, pady=5)

bstart = tk.Button(rahmenreihe1, text='Start/ Weiter', command=ersterZugDealer)
bstart.pack(side='left', padx=5, pady=5)

byes = tk.Button(rahmenreihe1, text='Ja', textvariable=my_string_var)
byes.pack(side='left', padx=5, pady=5)

bno = tk.Button(rahmenreihe1, text='Nein', command=back)
bno.pack(side='left', padx=5, pady=5)

bdelete = tk.Button(blackJack, text='clear', command=clearAusgabe)
bdelete.pack(side='top', padx=5, pady=5)

ausgabefeld = tk.Text(blackJack, height=40)
ausgabefeld.insert('end', "Start Game\n")
ausgabefeld.pack(fill='x', padx=10)

blackJack.mainloop()
