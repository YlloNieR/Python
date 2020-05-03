import random

farbsymbole = ("Kreuz", "Pik", "Herz", "Karo")
ränge = ("Zwei", "Drei", "Vier", "Fünf", "Sechs", "Sieben",
         "Acht", "Neun", "Zehn", "Bube", "Dame", "König", "Ass")
werte = {"Zwei": 2, "Drei": 3, "Vier": 4, "Fünf": 5, "Sechs": 6, "Sieben": 7,
         "Acht": 8, "Neun": 9, "Zehn": 10, "Bube": 10, "Dame": 10, "König": 10, "Ass": 11}

spielen = True


class Karte:
    def __init__(self, farbsymbol, rang):
        self.farbsymbol = farbsymbol
        self.rang = rang

    def __str__(self):
        return self.farbsymbol + " " + self.rang


class Kartendeck:

    def __init__(self):
        self.Kartendeck = []  # starte mit einer leere Liste
        for farbsymbol in farbsymbole:
            for rang in ränge:
                # bildet Karten objekt und fügt diese in eine Liste
                self.Kartendeck.append(Karte(farbsymbol, rang))

    def __str__(self):
        Kartendeck_comp = ''  # start mit einem leeren string
        for Karte in self.Kartendeck:
            # fügt jedes Kartenobjekt dem Ausgabe string hinzu
            Kartendeck_comp += '\n' + Karte.__str__()
        return "Das Kartendeck hat:" + Kartendeck_comp

    def mischen(self):
        random.shuffle(self.Kartendeck)

    def deal(self):
        einzel_karte = self.Kartendeck.pop()  # entfernt Karte
        return einzel_karte


class Hand:
    def __init__(self):
        self.Karten = []  # start with an empty list as we did in the Deck class
        self.wert = 0  # start with zero value
        self.asse = 0  # fügt eine Eigenschaft hinzu um Asse zu verfolgen

    def füge_hinzu_karte(self, Karte):
        self.Karten.append(Karte)
        self.wert += werte[Karte.rang]
        if Karte.rang == "Ass":
            self.asse += 1  # fügt eins hinzu self.asse

    def auf_ass_einstellen(self):
        while self.wert > 21 and self.asse:
            self.wert -= 10
            self.aces -= 1


class Chips:
    def __init__(self):
        self.gesamt = 100  # Das kann zum Standardwert gesetzt werden oder unterstützt den Benutzer
        self.gebot = 0

    def gewinnen_gebot(self):
        self.gesamt += self.gebot

    def verlieren_gebot(self):
        self.gesamt -+ self.gebot

def chips_nehmen(Chips):
    while True:
        try:
            Chips.gebot = int(input('Wieviele Chips möchtest du setzen?'))
        except ValueError:
            print("Leider muss ein Gebot ein Integer sein!")
        else:
            if Chips.gebot > Chips.gesamt:
                print(
                    "Leider kannst du das nicht bieten, deine Chips: ", Chips.gesamt)
            else:
                break

def schlagen(Kartendeck, Hand):
    Hand.füge_hinzu_karte(Kartendeck.deal())
    Hand.auf_ass_einstellen()

def schlagen_oder_aufstehen(Kartendeck, Hand):
    global spielen  # um zu kontrollieren einn darauffolgende while Schleife

    while True:
        x = input(
            "Möchten Sie eine Revanche oder das Spiel verlassen? geben Sie 'r' oder 'v' ein: ")

        if x[0].lower() == 'r':
            # schlagen Funktion bereits definiert
            schlagen(Kartendeck, Hand)

        elif x[0].lower() == 'v':
            print("Spieler bleibt. Der Dealer spielt.")
            spielen = False

        else:
            print("Bitte versuchen Sie es nochmal!")
            continue
        break

def zeige_einige(Spieler, Dealer):
    print("\nDealer's Hand:")
    print(" <Karte versteckt>")
    print("", Dealer.Karten[1])
    print("\Spieler's Hand:", *Dealer.Karten, sep="\n ")

def zeige_alles(Spieler, Dealer):
    print("\nDealer's Hand:", *Dealer.Karten, sep="\n ")
    print("Dealer's Hand =", Dealer.wert)
    print("\nSpieler's Hand:", *Spieler.Karten, sep="\n ")
    print("\nSpieler's Hand:", Spieler.wert)

def Spieler_Strafen(Spieler, Dealer, Chips):
    print("Spieler Strafe!")
    Chips.verlieren_gebot()

def Spieler_gewinnt(Spieler, Dealer, Chips):
    print("Spieler gewinnt!")
    Chips.gewinnen_gebot()

def Dealer_Strafen(Spieler, Dealer, Chips):
    print("Dealer Strafe!")
    Chips.verlieren_gebot()

def Dealer_gewinnt(Spieler, Dealer, Chips):
    print("Dealer gewinnt!")
    Chips.gewinnen_gebot()

def Gleichstand(Spieler, Dealer):
    print("Dealer und Spieler sind gleich")

while True:
    # Gebe Eröffnungs Statement aus
    print("Willkomen zum Black Jack! Versuch so nah wie mgl. an die 21 heranzukommen ohne darüber hinaus zu kommen!\n\
        Der Dealer gewinnt sobald er 17 erreicht. Asse zählen als 1 oder 11.")

    # Erstelle & Mische das Kartendeck, teile 2 Kartem zu jedem Spieler
    kartendeck = Kartendeck()
    kartendeck.mischen()

    Spieler_Hand = Hand()
    Spieler_Hand.füge_hinzu_karte(kartendeck.deal())
    Spieler_Hand.füge_hinzu_karte(kartendeck.deal())

    Dealer_Hand = Hand()
    Dealer_Hand.füge_hinzu_karte(kartendeck.deal())
    Dealer_Hand.füge_hinzu_karte(kartendeck.deal())

    # Setze die Spielerchips
    Spieler_Chips = Chips()

    # Nach Gebot fragen
    chips_nehmen(Spieler_Chips)

    # Zeige Karten (aber behalte eine Dealer Karte versteckt)
    zeige_einige(Spieler_Hand, Dealer_Hand)

    while spielen:  # wird aus der schlagen_oder_aufstehen Funktion entnommen
        # Fragen ob Revanche oder Verlassen
        schlagen_oder_aufstehen(kartendeck, Spieler_Hand)

        # Zeige Karten (aber behalte eine Dealer Karte versteckt)
        zeige_einige(Spieler_Hand, Dealer_Hand)

        # Wenn Spieler's Runde 21 übersteigt, führe Spieler Strafe aus und brich aus der Schleife aus
        if Spieler_Hand.wert > 21:
            Spieler_Strafen(Spieler_Hand, Dealer_Hand, Spieler_Chips)
            break

    # Wenn Spieler nicht bestraft, spiele Dealer's Runde bis Dealer erreicht 17
    if Spieler_Hand.wert <= 21:

        while Dealer_Hand.wert < 17:
            schlagen(kartendeck, Dealer_Hand)

        # zeige alle Karten
        zeige_alles(Spieler_Hand, Spieler_Hand)

        # Durchlaufe verschiedene Gewinn Szenarien
        if Dealer_Hand.wert > 21:
            Dealer_Strafen(Spieler_Hand, Dealer_Hand, Spieler_Chips)

        elif Dealer_Hand.wert > Spieler_Hand:
            Dealer_gewinnt(Spieler_Hand, Dealer_Hand, Spieler_Chips)

        elif Dealer_Hand.wert > 21:
            Spieler_gewinnt(Spieler_Hand, Dealer_Hand, Spieler_Chips)

        else:
            Gleichstand(Spieler_Hand, Dealer_Hand)

    # Informiere Spieler über seine Chipanzahl
    print("\nSpieler gewinnt mit: ", Spieler_Chips.gesamt)

    # Frage um zu Spielen
    neues_spiel = input("Wollen Sie nochmal spielen? Geben Sie 'J' oder 'N' ein: ")

    if neues_spiel[0].lower() == 'J':
        spielen = True
        continue
    else:
        print("Danke fürs Spielen")
        break

