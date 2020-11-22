# 1. part of exercise
str = "name"

print("Hello, World")
print("Hello, ",str)
print("")

# 2. part of exercise
name = input("Hallo wie ist ihr Name?")
print("Hallo ",name)

zahl1 = int(5)
print("Hier sollte 5 stehen:\n",zahl1)

zahl2 = int(7)
print("Hier steht 7:\n",zahl2)

zahl3 = 12
print("Hier steht 12:\n",zahl3)

ergebnis = zahl1 - zahl2
print("Hier steht das Ergebnis von zahl1 - zahl2 (-2):\n",ergebnis)

zahl4 = float(1.5)
#double does not exist
print("Hier steht eine Kommazahl(float) 1.5:\n",zahl4)
print("Hier wird der Kommazahl der Rest abgeschnitten:\n",int(zahl4))

c = 'F'
print("Hier steht ein F [in ",type(c),"]\n",c)

motivation = "5 lines to go"
print(motivation)

wahrheitswert = bool(ergebnis < zahl3)
print("Ist das Ergebnis kleiner als zahl3?",wahrheitswert)

print("Gut gemacht")