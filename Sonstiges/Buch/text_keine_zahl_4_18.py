# Fehler abfangen
x = "15.3p"

print("Zeichenkette lautet wie folgt: x = ", x)
print("Zeichenkette wird nun mit 2 mutlipliziert, Resultat =")


try:
    x = float(x)
    print(x*2)
except:
    print("\tZeichenkette kann nicht umgewandelt werden")
