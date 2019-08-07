zeilen = [] 

with open ("pwdata.txt", "rt") as textfile: 
    for zeile in textfile:
        zeilen.append(zeile)

print(len(zeilen))
print(str(zeilen[1])[20:30])

print("Ergebnis= ")

def Checker(y):
    index = 0
    a = len(y)+19
    x = str(zeilen[index])[20:a]
    
    while index < len(zeilen):
        if x == y:
            return index
        else: 
            index = index + 1
            return 1

y = ""
print(Checker(y))

print("y = super ... ",y)



#if Checker(y) == 