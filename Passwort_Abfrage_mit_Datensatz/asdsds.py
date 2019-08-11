file = open("hello.txt","r")
print("ganze File:")
print(file.read())
print("\n Step für Step\n")

#Wieviele Zeilen?
print("#Wieviele Zeilen?")
file = open("hello.txt","r")
zeilenanzahl = sum(1 for row in file)
print(zeilenanzahl)
print("")

#Welches Zeichen ist das erste zu untersuchende Zeichen?
print("#Welches Zeichen ist das erste zu untersuchende Zeichen?")
file = open("hello.txt","r")
f = file.readline()
print(f[20:21])
print("")

#Welches Zeichen ist das letzte der Zeile?
print("#Welches Zeichen ist das letzte der Zeile?")
letztes_Zeichen = len(f)-1
vorletztes_zeichen = len(f)-2
print(f[vorletztes_zeichen:letztes_Zeichen])
print("")

#Match
print("#match")
gesuchtes_Wort = "asd"
print(f[20:letztes_Zeichen])
if gesuchtes_Wort == f[20:letztes_Zeichen]:
    print(True)
else:
    print(False)
print("")

#Aufsplitten der Zeilen?
print("#Aufsplitten der Zeilen?")
file = open("hello.txt","r")
zeile = file.readlines()[zeilenanzahl-1]
print(zeile)


#match and komplett
print("#match and komplett")
if gesuchtes_Wort == f[20:letztes_Zeichen]:
    print(True)


file.readline()
print(file.readline())



''''
file = open("hello.txt","r")
f = file.strip()
Suchwort = "123"
print(f[0:3])
if Suchwort == f[0:3]:
    print(True)


    print("file input\n",file.read(),"\n")
    print(type(file.read()))
    f = bytes(file.read(),'utf-8') #encodierung von String in Bytes
    print("f = ",f)
    gesuchtes_Wort = b"asd"
    
    print(gesuchtes_Wort)
    print(gesuchtes_Wort.split())
    
    #bytes(f.read,encoding='utf8')
    
    index1 = f.find(gesuchtes_Wort)
    print(index1)
    
    
    #data = bytes(Wort)
    #arr = bytearray(Wort)
    
    #print(data.count(gesuchte_Wort))
    '''