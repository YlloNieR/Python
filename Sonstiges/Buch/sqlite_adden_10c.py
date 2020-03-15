import sqlite3

auswahl = int(input(" \n"
    "Was möchten Sie machen? \n"
    "Beenden \t\t- 0 \n "
    "DB einsehen \t\t- 1 \n "
    "DB Eintrag adden \t- 2 \n "
    "DB Eintrag löschen \t- 3\n "
    "->"))

def anzeigen():
    print()
    import sqlite_anzeigen_10_2 # Anzeigen
    sqlite_anzeigen_10_2    

def adden():
    print()
    import sqlite_adden_10a # Adden
    sqlite_adden_10a

def loeschen():
    print()
    import sqlite_adden_10b # Löschen
    sqlite_adden_10b   

if auswahl == 0:
    exit

elif auswahl == 1:
    anzeigen()    
    
elif auswahl == 2:
    adden()    

elif auswahl == 3:
    loeschen()