
##numberOfHits(gesuchtes_Wort)##Hier ist noch ein Fehler drin
gesuchtes_Wort = "asd"

def numberOfHits():
    import re
    x = 0
    with open("pwdata.txt","r") as file:
        for line in file:
            if gesuchtes_Wort in line:
                print(line)
                while re.search(gesuchtes_Wort,file.readline()):
                    x = x + 1
        print("Anzahl der Treffer =", x)
    file.close()

numberOfHits()