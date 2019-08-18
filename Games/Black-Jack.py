print("\t Black Jack")
'''
312 Karten
52 Blatt 13 Karten
K, Q, J

Croupier
bis zu sieben Spieler 

'''
print("")

class Kartendeck:
    numbers = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
    blattDiamonds = ["Diamond"]
    blattHearts = ["Heart"]
    blattSpades = ["Spade"]
    blattSquares = ["Square"]
    check = 0

    def diamond(self):
        for i in self.numbers:
            print(*self.blattDiamonds,self.numbers[self.check])
            self.check += 1
                            

    def hearts(self):
        for i in self.numbers:
            print(*self.blattHearts,self.numbers[self.check])
            self.check += 1

    def spades(self):
        for i in self.numbers:
            print(*self.blattSpades,self.numbers[self.check])
            self.check += 1

    def squares(self):
        for i in self.numbers:
            print(*self.blattSquares,self.numbers[self.check])
            self.check += 1


class Spieler:
    def __init__(self, Nummer):
        self.Nummer = Nummer


print(Kartendeck().diamond())

