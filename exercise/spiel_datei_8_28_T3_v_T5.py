# Funktion Highscore schreiben
def hs_schreiben():
    # Zugriff
    d = open("highscore.bin", "wb")
    pickle.dump(hs_liste, d)
    d.close()
