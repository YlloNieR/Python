print("\n\tPasswort Abfrage mit Datensatz\n")

def pwErstellen():
    print("\nDu möchtest also ein Passwort erstellen & der Datenbank hinzufügen\n")
    username = input("Benutzername = ")
    passwortVorhanden = input("neues Passwort eingeben = ")
    passwortEingabe = input("Passwort wiederholen = ")

    if passwortVorhanden == passwortEingabe:
        from time import localtime, strftime
        now = strftime("%Y-%m-%d %H:%M:%S", localtime())
        textfile = open("pwdata.txt","a")
        textfile.write(str(now))
        textfile.write("\t" + username + "\t" + passwortEingabe + "\n")    
        textfile.close()
        print("Passwort erfolgreich gespeichert :)")
    else:
        print("Passwörter stimmen nicht überein!")

def pwCheck():
    print("\n\tDu möchtest also ein Passwort abfragen \n")
    gesuchtes_Wort = input("\tWelcher Benutzer oder welches Passwort soll sich in der pwdata.txt Datenbank befinden? \n\t= ")
    numberOfPasswords(gesuchtes_Wort)
    numberOfHits(gesuchtes_Wort)
    listOfTimePassword(gesuchtes_Wort)  

def numberOfPasswords(gesuchtes_Wort):
    with open("pwdata.txt","r") as z:
        nPasswords = sum(1 for gesuchtes_Wort in z)
        print("\t\nAnzahl der Passwörter = ",nPasswords)    
    z.close()

def listOfTimePassword(gesuchtes_Wort):
    import re
    x = 0
    b = print("\n\tListe der Treffer: \n")
    with open("pwdata.txt","r") as y:
        for lin in y:
            if gesuchtes_Wort in lin:
                a = print("\t\t",lin.rstrip('\r\n'))    #nimmt \n weg
                x = 1
    if x == 1:
        b, a    
    else: 
        print("Keine Treffer!")
    y.close()

def numberOfHits(gesuchtes_Wort):
    import re
    x = 0
    with open("pwdata.txt","r") as file:
        for line in file:            
            if gesuchtes_Wort in line:
                x = x + 1
        if x == 0:
            print("Das Passwort ist nicht gespeichert!")
        else:
            print("\tDas Passwort ist bereits schon",x,"mal in der Datenbank gespeichert!")
    file.close()

breakpoint

while True:
    try:
        w = input("\t[1] neues Passwort der Datenbank hinzufügen\n\t[2] Passwort eingeben & mit Datenbank überprüfen\n\t= ")
        n = int(w)
        break
    except ValueError:
        print("\n\tEs sind nur die oben angegebenen Auswahlmöglichkeiten möglich!\n")
if n == 1:
    pwErstellen()
elif n == 2:
    pwCheck()
elif n in range(3, 100):
    print("\n\tEs sind nur die oben angegebenen Auswahlmöglichkeiten möglich!\n")
    while True:
        try:
            w = input("\tPasswort erstellen [1]\n\tPasswort eingeben [2]\n\t=")
            n = int(w)
            break
        except ValueError:
            print("\n\tEs sind nur die oben angegebenen Auswahlmöglichkeiten möglich!\n")
    if n in range(3, 100):
        print("\n\tVergiss es spiel Tetris Digga!\n")
        

