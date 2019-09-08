# Import Math
import fractions

# Bruch
z = 12
n = 28
print("Bruch: ", z, "/", n)

# als Fraction
b1 = fractions.Fraction(z, n)
print("Fraction: ", b1, "Fraction = Konstruktor der Klasse Fraction")
print("Z, N:", b1.numerator, ",", b1.denominator)
wert = b1.numerator / b1.denominator
print("Wert: ", wert, "numerator = Zähler, denominator = Nenner")
print()
