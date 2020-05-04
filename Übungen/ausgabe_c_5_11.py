# Zahl mit Nachkommastellen
x = 100/7
y = 2/7

print("Zahlen: ", x, ", ", y)
print()

# Die Zeichekette dient als Objekt
# auf das die Funktion format() angewendet wird
print("Format f, Standard:     %f %f %f" % (x, x, y))
print("Format f, nach Komma:   %.25f" % (x))
print("Format f, gesamt:     %15.10f" % (x))
print()

# Format e, Ausgabe einer Variable im Exponentialformat, 3.e = 3 Kommastellen
print("Format e, Standard:     %e" % (x))
print("Format e, nach Komma:   %.3e" % (x))
print("Format e, gesamt:    %12.3e" % (x))
print()

# Format %, Ausgabe in Prozentformat
print("Format %%, Standard:    %f%%" % (y*100))
print("Format %%, nach Komma:   %.3f%%" % (y*100))
print("Format %%, gesamt:  %12.3f%%" % (y*100))
