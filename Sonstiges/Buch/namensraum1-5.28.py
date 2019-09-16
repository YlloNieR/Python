# Testfunktion
def func():
    try:
        print(x)
    except:
        print("Fehler")


# Hauptprogramm
func()      # bis hier Variabel x im globalen Raum unbekannt
x = 42      # Variabel x global bekannt
func()
