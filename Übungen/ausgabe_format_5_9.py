# Zahl mit Nachkommastellen
x = 100/7
y = 2/7

print("Zahlen: ", x,", ", y)
print()

# Die Zeichekette dient als Objekt
# auf das die Funktion format() angewendet wird
print("Format f, Standard:     {0:f} {0:f} {1:f}".format(x,y))
print("Format f, nach Komma:   {0:.25f}".format(x))
print("Format f, gesamt:     {0:15.10f}".format(x))
print()

# Format e, Ausgabe einer Variable im Exponentialformat, 3.e = 3 Kommastellen
print("Format e, Standard:     {0:e}".format(x))
print("Format e, nach Komma:   {0:.3e}".format(x))
print("Format e, gesamt:    {0:12.3e}".format(x))
print()

# Format %, Ausgabe in Prozentformat
print("Format %, Standard:     {0:%}".format(y))
print("Format %, nach Komma:   {0:.3%}".format(y))
print("Format %, gesamt:  {0:12.3%}".format(y))
