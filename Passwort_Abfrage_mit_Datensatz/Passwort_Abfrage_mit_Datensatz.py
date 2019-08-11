print("Passwort Abfrage mit Datensatz")

def pwErstellen():
    print("Du möchtest also ein Passwort erstellen \n")
    passwortVorhanden = input("neues Passwort eingeben = ")
    passwortEingabe = input("Passwort wiederholen = ")

    if passwortVorhanden == passwortEingabe:
        from time import localtime, strftime
        now = strftime("%Y-%m-%d %H:%M:%S", localtime())
        textfile = open("pwdata.txt","a")
        textfile.write(str(now))
        textfile.write("\t" + passwortEingabe + "\n")    
        textfile.close()
        print("Passwort erfolgreich gespeichert :)")
    else:
        print("Passwörter stimmen nicht überein!")

 

def numberOfPasswords(gesuchtes_Wort):
    with open("pwdata.txt","r") as z:
        nPasswords = sum(1 for gesuchtes_Wort in z)
        print("\tAnzahl der Passwörter = ",nPasswords)    
    z.close()

def listOfTimePassword(gesuchtes_Wort):
    import re
    print("Liste der Treffer:")
    with open("pwdata.txt","r") as y:
        for lin in y:
            if gesuchtes_Wort in lin:
                print("\t\t",lin.rstrip('\r\n'))    #nimmt \n weg
    y.close()

def numberOfHits(gesuchtes_Wort):
    import re
    with open("pwdata.txt","r") as file:
        for line in file:
            if gesuchtes_Wort in line:
                print(line)
            x = 0
            while re.search(gesuchtes_Wort,file.readline()):
                x = x + 1
        print("\tAnzahl der Treffer =", x)
    file.close()

def pwCheck():
    print("Du möchtest also ein Passwort abfragen \n")
    gesuchtes_Wort = input("Welches Passwort soll sich in der pwdata.txt befinden? \n\t= ")
    #numberOfPasswords(gesuchtes_Wort)
    numberOfHits(gesuchtes_Wort)##Hier ist noch ein Fehler drin
    #listOfTimePassword(gesuchtes_Wort) 

breakpoint
'''
def pwCheck():
    print("Du möchtest also ein Passwort abfragen \n")
    passwortVorhanden = input("Welches Passwort soll sich in der pwdata.txt befinden? \n\t= ")
    textfile = open("pwdata.txt", "r")
    if textfile.read() == passwortVorhanden:
        print("Das Passwort ist in der Datenbank gespeichert!")
    else:
        print("Das Passwort ist nicht gespeichert!")
    textfile.close()
'''    

while True:
    try:
        w = input("\tPasswort erstellen [1]\n\tPasswort eingeben [2]\n\t=")
        n = int(w)
        break
    except ValueError:
        print("\nEs nur die oben angegebenen Auswahlmöglichkeiten möglich!\n")
if n == 1:
    pwErstellen()
elif n == 2:
    pwCheck()


