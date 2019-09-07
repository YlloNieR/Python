print("\tCalculator Game")
import random

#Aufgabe und Variablen
a = random.randint(1,100)

c = random.randint(1,100)


def aufgabe():
    print("Wieviel ist",a,"+",c,"? ")
    eingabe = int(input("Eingabe: "))
    ergebnis = a + c
    if eingabe == ergebnis:
        print("korrekt")
        exit
        
    
aufgabe()