import math

a = 4.75
print("Variable a: ", 3*"\t", a)
print("Quadratwurzel von a:", 2*"\t", math.sqrt(a))
print("Natürlicher Logarithmus von a: \t", math.log(a))
print("e hoch a: ", 3*"\t", math.exp(a))
print("10er-Logarithmus von a: ", "\t", math.log10(a), "a als Exponent")
print("")

# Konstanten
print("Kreiszahl pi: ", 3*"\t", math.pi)
print("Eulersche Zahl e: ", 2*"\t", math.e)
print("")

print("Fakultät von 5: ", 2*"\t", math.factorial(5))
print('''Größter gem Teiler 
von 60 und 135: ''', 2*"\t", math.gcd(60, 135),"greatest common divisor")
print("")

if(math.isclose(3, 2.96, rel_tol=0.01)):
    print("math.isclose(3, 2.96, rel_tol=0.01) = Nahe dran")
else:
    print("math.isclose(3, 2.96, rel_tol=0.01) = Nicht Nahe dran","\t sind Zahlen einander Nahe, relative Toleranz 0.01")

if(math.isclose(3, 2.97, rel_tol=0.01)):
    print("math.isclose(3, 2.97, rel_tol=0.01) = Nahe dran","\t sind Zahlen einander Nahe, relative Toleranz 0.01")
else:
    print("math.isclose(3, 2.97, rel_tol=0.01) = Nicht nahe dran")

if(math.isclose(3, 2.98, abs_tol=0.01)):
    print("math.isclose(3, 2.98, abs_tol=0.01) = Nahe dran")
else:
    print("math.isclose(3, 2.98, abs_tol=0.01) = Nicht nahe dran","\t sind Zahlen einander Nahe, absolute Toleranz 0.01")

if(math.isclose(3, 2.99, abs_tol=0.01)):
    print("math.isclose(3, 2.99, abs_tol=0.01) = Nahe dran","\t sind Zahlen einander Nahe, absolute Toleranz 0.01")
else:
    print("math.isclose(3, 2.99, abs_tol=0.01) = Nicht nahe dran")