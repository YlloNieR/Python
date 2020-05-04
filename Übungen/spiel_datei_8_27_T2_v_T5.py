# Funktion Highscore anzeigen
def hs_anzeigen():
    # Highscore nicht vorhanden
    if not hs_liste:
        print("Keine Highscores vorhanden")
        return

    # Ausgabe Highscore
    print(" P. Name         Zeit")
    for i in range(len(hs_liste)):
        print(f"{i+1:2d}. {hs_liste[i][0]:10}"
              f" {hs_liste[i][1]:5.2f} sec")
        if i >= 9:
            break
