print("Berechnung des monatlich zu zahlenden Steuerbetrages vom Bruttolohn")


def steuer(bruttolohn):
    prozentsatz1 = 0.22
    prozentsatz2 = 0.18

    if bruttolohn > 2500:
        ergebnis = bruttolohn * prozentsatz1  # 22%
        print("Von", bruttolohn, "EURO ergibt sich bei einem", prozentsatz1*100,
              "% -iger Versteuerung, ein Steuerbetrag in Höhe von", ergebnis, "EURO.")
    else:
        ergebnis = bruttolohn * prozentsatz2  # 18%
        print("Von", bruttolohn, "EURO ergibt sich bei einem", prozentsatz2*100,
              "% -iger Versteuerung, ein Steuerbetrag in Höhe von", ergebnis, "EURO.")


for bruttolohn in 1800, 2200, 2500, 2900:
    steuer(bruttolohn)
