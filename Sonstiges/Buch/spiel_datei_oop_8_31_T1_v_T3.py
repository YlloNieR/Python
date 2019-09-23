import random
import time
import glob

# Hauptprogramm
while True:
    # Hauptprogramm, Auswahl
    try:
        menu = int(input("Bitte eingeben "
                         "(0: Ende, 1: Highscores, 2: Spielen): "))
    except:
        print("Falsche Eingabe")
        continue

    # Anlegen eines Objektes oder Ende
    if menu == 0:
        break
    elif menu == 1:
        hs = Highscore()
        print(hs)
    elif menu == 2:
        s = Spiel()
        s.messen(True)
        s.spielen()
        s.messen(False)
        print(s)
    else:
