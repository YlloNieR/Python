# Zahl mit Nachkommastellen
x = 100/7
y = 2/7

print("Zahlen: ", x,", ", y)
print()

# Format f, Anzahl der Nachkommastellen, default = 6
print(f"Format f, Standard:     {x:f} {x:f} {y:f}")
print(f"Format f, nach Komma:   {x:.25f}")
print(f"Format f, gesamt:     {x:15.10f}")
print()

# Format e, Ausgabe einer Variable im Exponentialformat, 3.e = 3 Kommastellen
print(f"Format e, Standard:     {x:e}")
print(f"Format e, nach Komma:   {x:.3e}")
print(f"Format e, gesamt:    {x:12.3e}")
print()

# Format %, Ausgabe in Prozentformat
print(f"Format %, Standard:     {y:%}")
print(f"Format %, nach Komma:   {y:.3%}")
print(f"Format %, gesamt:  {y:12.3%}")
