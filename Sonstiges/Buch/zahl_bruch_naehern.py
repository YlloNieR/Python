# Import des Moduls
import fractions

# untersuchte Zahl
x = 1.84953
print("Zahl: ",5*"\t", x)

# als bruch
b3 = fractions.Fraction(x)
print("Fraction: ",4*"\t", b3)

# approximiert
b4 = b3.limit_denominator(100)
print("Approximiert auf Nenner max. 100: ","\t", b4)

# Genauigkeit
wert = b4.numerator / b4.denominator
print("Wert: ",5*"\t", wert)
print("rel. Fehler: ",4*"\t", abs((x-wert)/x))
