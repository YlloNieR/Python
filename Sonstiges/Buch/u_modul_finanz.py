# Berechnung
def steuer(Wert):
    prozentsatz1 = 0.22
    prozentsatz2 = 0.18
    ergebnis1 = Wert * prozentsatz1  # 22%
    ergebnis2 = Wert * prozentsatz2  # 18%
    if Wert > 2500:
        return Wert, prozentsatz1*100, ergebnis1
    else:
        return Wert, prozentsatz2*100, ergebnis2
