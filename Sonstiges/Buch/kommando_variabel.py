import sys
summe = 0

try:
    for i in sys.argv[1:]:
        # Bei sys.argv handelt es sich um eine Liste, dass erste Element darf nicht in die Rechnung mit einfließen
        # sys.arg[0] = Name des Programms
        summe += float(i)
    print("Ergebnis: ", summe)
except:
    print("Parameterfehler!")
