# Funktion
def volumen(breite, laenge, tiefe, farbe):
    print("Werte: ", breite, laenge, tiefe, farbe)
    erg = breite * laenge * tiefe
    print("Volumen: ", erg, "Farbe: ", farbe)


# Aufrufe
volumen(4, 6, 2, "rot")
volumen(laenge=2, farbe="gelb", tiefe=7, breite=3)
volumen(5, tiefe=2, laenge=8, farbe="blau")

# letzte Zeile ergibt Fehler, 
# weil sobald erster Parameter benannt hier "tiefe=4," 
# dann müssen alles folgenden auch benannt werden Fazit ...laenge=5, farbe="schwarz"...

# volumen(3, tiefe=4, laenge=5, "schwarz")
