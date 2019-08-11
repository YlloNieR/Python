gesuchtes_Wort = "super"

def numberOfPasswords():
    with open("pwdata.txt","r") as z:
        nPasswords = sum(1 for gesuchtes_Wort in z)
        print("Anzahl der Passwörter = ",nPasswords)    
    z.close()

def listOfTimePassword():
    import re
    print("Liste der Treffer:")
    with open("pwdata.txt","r") as y:
        for lin in y:
            if gesuchtes_Wort in lin:
                print("\t",lin.rstrip('\r\n'))    #nimmt \n weg
    y.close()

def numberOfHits():
    import re
    with open("pwdata.txt","r") as file:
        for line in file:
            if gesuchtes_Wort in line:
                print(line)
            x = 0
            while re.search(gesuchtes_Wort,file.readline()):
                x = x + 1
        print("Anzahl der Treffer =", x)
    file.close()


breakpoint

numberOfPasswords()

numberOfHits()

listOfTimePassword()  









