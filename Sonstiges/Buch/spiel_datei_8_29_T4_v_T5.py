# Funktion Spiel
def spiel():
    # Eingabe des Namens
    name = input("Bitte geben Sie Ihren "
                 "Namen ein (max. 10 Zeichen): ")
    name = name[0:10]

    # Initialisierung Counter Zeit
    richtig = 0
    startzeit = time.time()

    # 5 Aufgaben
    for aufgabe in range(5):
        a = random.randint(10, 30)
        b = random.randint(10, 30)
        c = a + b

        # Eingabe
        try:
            zahl = int(input("Aufgabe "
                             + str(aufgabe+1) + " von 5: "
                             + str(a) + " + " + str(b) + " : "))
            if zahl == c:
                print("*** Richtig ***")
                richtig += 1
            else:
                raise
        except:
            print(" Falsch")

    # Auswertung
    endzeit = time.time()
    differenz = endzeit-startzeit
    print(f"Ergebnis: {richtig:d} von 5 in "
    f"{differenz:.2f} Sekunden", end="")
    if richtig == 5:
        print(", Highscore")
    else:
        print(", leider kein Highscore")
        return

    # Mitten in Liste schreiben
    gefunden = False
    for i in range(len(hs_liste)):
        # Einsetzen in Liste
        if differenz < hs_liste[i][1]:
            hs_liste.insert(i, [name, differenz])
            gefunden= True
            break

    # Ans Ende der Liste schreiben
    if not gefunden:
        hs_liste.append([name, differenz])

    # Highscore-Liste anzeigen
    hs_anzeigen()
