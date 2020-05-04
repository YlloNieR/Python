print("Berechnung des monatlich zu zahlenden Steuerbetrages vom Bruttolohn")


# Berechnung und Ausgabe
def steuer(w, x, y, z):
    prozentsatz1 = 0.22
    prozentsatz2 = 0.18

    for bruttolohn in w, x, y, z:
        if bruttolohn > 2500:
            ergebnis = bruttolohn * prozentsatz1  # 22%
            print("Von", bruttolohn, "EURO ergibt sich bei einem", prozentsatz1*100,
                  "% -iger Versteuerung, ein Steuerbetrag in Höhe von", ergebnis, "EURO.")
        else:
            ergebnis = bruttolohn * prozentsatz2  # 18%
            print("Von", bruttolohn, "EURO ergibt sich bei einem", prozentsatz2*100,
                  "% -iger Versteuerung, ein Steuerbetrag in Höhe von", ergebnis, "EURO.")


# Hauptprogramm
steuer(1800, 2200, 2500, 2900)
