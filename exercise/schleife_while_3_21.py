# Zufallsgenerator
import random
random.seed()

# Initialisierung
summe = 0

# while-Schleife
print(
'''
Solange die Summe kleiner als 30 ist, 
nimm eine zufällige Zahl (zzahl)
und summiere diese mit der letzten (summe)
ausgehend von 0

wenn 30 erreicht wird oder überschritten endet while
'''    
)

while summe < 30:
    zzahl = random.randint(1,8)
    summe = summe + zzahl
    print("Zahl: ", zzahl, "Zwischensumme: ", summe)

print("Ende")