print("Berechnung des monatlich zu zahlenden Steuerbetrages vom Bruttolohn")


# Berechnung
def steuer(Wert):
    prozentsatz1 = 0.22
    prozentsatz2 = 0.18
    ergebnis1 = bruttolohn * prozentsatz1  # 22%
    ergebnis2 = bruttolohn * prozentsatz2  # 18%

    if bruttolohn > 2500:
        return prozentsatz1*100, ergebnis1
    else:
        return prozentsatz2*100, ergebnis2


# Hauptprogramm
# Ausgabe
for bruttolohn in 1800, 2200, 2500, 2900:
    print("Von", bruttolohn, "EURO ergibt sich bei einem", steuer(bruttolohn)[0],
          "% -iger Versteuerung, ein Steuerbetrag in Höhe von", steuer(bruttolohn)[1], "EURO.")
