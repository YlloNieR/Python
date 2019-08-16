##Iteration  Kapitel 6
##Multiple assignment
print("##Multiple assignment =\n")
bruce = 5
print("bruce erster Aufruf = ",bruce)
bruce = 7
print("bruce zweiter Aufruf = ",bruce)
a = 2
print("a =",a)
print(" b = a")
b = a
print("  b =",b)
a = 3
print("a =",a,"...also wird a geändert")
print("b =",b,"...b bleibt weiterhin ",b)
##Ende Multiple assignment

print('\n')

##The while statement
print("##The while statement =\n")
print("countdown mit while =")
def countdown(n):
    while n > 0: #solange n größer 0
        print(n) #Zeige jede Zahl an
        n = n-1  #reduziere jede Zahl um 1
    print("Blastoff!") #wenn n größer 0 dann zeige Blastoff! an

countdown(2) #Funktionsaufruf

print("\nsequence mit while = nicht ausgeführt da infinite loop")
def sequence(n):
    while n != 1:  #Loop bis n = 1
        print(n)  #Zeige solange n an
    if n%2 == 0: 
        n = n/2    #dann n/2
    else:          
        n = n*3+1  #ansonsten n mal 3 + 1
print("\nÜbung nLine umschreiben in while")
def nLines(n):
    while n > 0:
        print("a")
        n = n-1

nLines(2)
##Ende The while statement
print('\n')

##Tables
print("##Tables =\n")
import math

Basis = 2.0
Potenz = 8.0
Exponent = "x"
print("Zahlen bestehen aus:\n Basis =",int(Basis),"\n Exponent =",Exponent,"\n Beispiel: ",int(Basis),"hoch",Exponent,"dann ist",Exponent,"ist der Exponent, das Ergebnis ist die Potenz.")
print(" Der Logarithmus ist dann log von",int(Potenz),"zur Basis",int(Basis),".",'\n')
x = 1.0

print("print ( x, /t, math.log(x) )") #Beachte / anders \
print("   x =",x) 
while x < 10.0:
    print(x, '\t', math.log(x))
    x = x + 1.0  # + 1.0 = Potenzwert

print("\nprint ( x, /t, math.log(x)/math.log(2.0) )") #Beachte / anders \
x = 1.0
while x < 100.0:
    print(x, '\t', math.log(x)/math.log(2.0))
    x = x * 2.0  # * 2.0 = Potenzwert

print("\nÜbung log") 
Basis = 2.0
Exponent = 16
while Basis < 65536:
    print(Basis, '\t', math.log(Basis)/math.log(2.0))
    Basis = Basis * 2.0  

print("\nÜbung Schreibweise Tabelle") 
print("\nproduces")
print('\t''\t'"this")
print(3*'\t',"output.")
##Ende Tables

print('\n')

##Two-dimensional tables
print("##Two-dimensional tables =\n")
print("multiplication table for the values from 1 to 6")
i = 1
while i <= 6:                       # @ 7 loop terminates
    print(2*i,end="   ")            # each loop 2*i followed by 3 spaces with end=""
    i = i + 1                       # the value of i increases from 1 to 6, i = counter or loop variable
    print
##Ende Two-dimensional tables

print('\n')

##Encapsulation and generalization
print("##Encapsulation and generalization =\n")
print("\t\t\tMultiplication table")
print("\t\t\t____________________")

def printMultiples(n):
    i = 1
    while i <= n:                       
        print("\t\t",i,'\t',2*i,'\t',3*i,'\t',4*i,'\t',5*i,'\t',6*i)                 
        i = i + 1

print("")

printMultiples(2)

def printMultTable(n):
    i = 1
    while i <= n:
        printMultiples(i)
        i = i + 1

printMultTable(2)

##Ende Encapsulation and generalization
##Ende Iteration

print('\n')

##Strings
##A compound data type
print("##Strings = \n")
print("##A compound data type \n = Typen, die kleinere Teile umfassen, werden als zusammengesetzte Datentypen bezeichnet.")

fruit = "banana"
letter = fruit[1] # Index of the string in integer
print(letter)
##Ende A compound data type

print('\n')
    
##Length
print("##Length = \n")
fruit = "banana"
print("fruit = banana\n")
print("   len(fruit) = ",len(fruit))
length = len(fruit)
x = length
print("   length = len(fruit) \n    length = ",x)
last = fruit[length - 1]
x = last
print("   last = fruit[ length - 1 ] \n    last = ",x)
##Ende Length

print('\n')
    
##Traversal and the for loop
print("##Traversal and the for loop = \nprocesses start at the beginning, select each character in turn, do something to it and continue until the end.")
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

print("\nÜbung Traversal Vorwärts Funktion")
def TraversalV(Wort):
    index = 0
    
    while index < len(Wort):
        buchstabe = Wort[index]
        print(buchstabe)
        index = index + 1
        
TraversalV("asd")

print("\nÜbung Traversal Rückwärts Funktion")
def TraversalR(Wort):
    index = -1
    
    while -index < len(Wort)+1:
        buchstabe = Wort[index]
        print(buchstabe)
        index = index - 1

TraversalR("asd")

fruit="fruit"
print("\nfor loop")
for char in fruit:
    print(char)

print('\n')
print("Prefix + suffix liste Jack & Quack")

prefixes = "NOPQ"
suffix = "ack"
letter = prefixes[0]

for letter in prefixes:
    if letter in ("Q","O"):
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)
##Ende Traversal and the for loop

print('\n')

##String slices
print("##String slices = A segment of a string is called a slice.\n")
s = "Peter, Paul, and Mary"
print("s = Peter, Paul, and Mary")
print("s[0:5]")
print("Der Nullte bis fünfte Buchstabe sind: ",s[0:5])
##Ende String slices

print('\n')

##String comparison
print("##String comparison = ")
ErsterBuchstabeDesWortes = "banana"
print('\n')

if ErsterBuchstabeDesWortes == "banana":
    print("ausgewähltes Wort " + ErsterBuchstabeDesWortes + ", beginnt mit dem selben Buchstaben wie banana")
print('\n')

ErsterBuchstabeDesWortes = "dsa"
if ErsterBuchstabeDesWortes < "banana":
    print("ausgewähltes Wort " + ErsterBuchstabeDesWortes + ", beginnt mit einem Buchstaben welcher alphabetisch nach b von banana kommt")
elif ErsterBuchstabeDesWortes > "banana":
    print("ausgewähltes Wort " + ErsterBuchstabeDesWortes + ", beginnt mit einem Buchstaben welcher alphabetisch nach b von banana kommt")
else:
    print("ausgewähltes Wort " + ErsterBuchstabeDesWortes + ", beginnt mit dem selben Buchstaben wie banana")

#You should be aware, though, that Python does not handle upper- and lowercase
#letters the same way that people do. All the uppercase letters come before all
#the lowercase letters.

##Ende String comparison

print('\n')

##Strings are immutable
print("##Strings are immutable =")
greeting = "Hello, world!"
newGreeting = 'J' + greeting[1:]
print(newGreeting)
print("The solution here is to concatenate a new first letter onto a slice of greeting.")
##Ende Strings are immutable

print('\n')

##A find function
print("##A find function = ")
print("Finde den Buchstaben im Wort \n")

Wort = "asdaa"
Buchstabe = "a"
index = 5
print("gesuchtes Wort = ",Wort)
print("gesuchter Buchtstabe = ",Buchstabe,"\n")

#Suche ob der Buchstabe im Wort vorhanden ist mit while
def find(Wort, Buchstabe):
    index = 0
    while index < len(Wort):
        if Wort[index] == Buchstabe:
            return index
        else: 
            index = index + 1
            return -1

print("Ist in derm Wort ",Wort," der Buchstabe ",Buchstabe," enthalten? ...mit while")

if find(Wort, Buchstabe) == 0:
    x = "Ja"
else:
    x = "Nein"
print("Ergebis =",x)

print("\nÜbung A find function\n")

#Suche wie oft kommt der Buchstabe im Wort vor mit while

def BuchstabenSuche(Wort,Buchstabe):
    count=0
    for BuchstabenSuche in Wort:
        if Buchstabe == BuchstabenSuche:
            count = count + 1
    return count

print("Wie oft kommt der Buchstabe ",Buchstabe," vor =",BuchstabenSuche(Wort,Buchstabe),"...mit while","\n")


#Suche ob der Buchstabe im Wort vorhanden ist mit for loop
def BuchstabenSucheVorhanden(Wort,Buchstabe):
    count=0
    for BuchstabenSuche in Wort:
        if Buchstabe == BuchstabenSuche:
            return BuchstabenSuche

if BuchstabenSucheVorhanden(Wort,Buchstabe) == Buchstabe:           
    x = "Ja"
else:
    x = "Nein"

print("kommt der Buchstabe ",Buchstabe," vor? ",x,"...mit for loop")

#Suche wie oft der Buchstabe im Wort vorhanden ist mit for loop
def BuchstabenSucheAnzahl(Wort,Buchstabe):
    count=0
    for BuchstabenSuche in Wort:
        if Buchstabe == BuchstabenSuche:
            count = count + 1
    return count

print("Wie oft kommt der Buchstabe vor =",BuchstabenSucheAnzahl(Wort,Buchstabe)," mal. ...mit for loop")

##Ende A find function

print('\n')
    
##Looping and counting
print("##Looping and counting = \n")
Wort = "banana"
letter = "n"
print("Wort = ",Wort)
print("letter = ",letter)

print("\nZähle im Wort",Wort,"wie viele a enthalten sind:")

count = 0
for Buchstabe in Wort:
    if Buchstabe == "a":
        count = count + 1
print(count)
        
print("\nÜbung Looping and counting1 = \nAs an exercise, encapsulate this code in a function named countLetters, and generalize it so that it accepts the string and the letter as parameters. \n")


def countLetters(Wort,letter):
    count = 0
    for Buchstabe in Wort:
        if Buchstabe == letter:
            count = count + 1
    return count
            
print("Zähle im Wort",Wort,"wie viele a enthalten sind:",countLetters(Wort,letter))
##Ende Looping and counting

print('\n')
    
##The string module
print("##The string module = \n")
import string
fruit = "banana"
index = str.find(fruit, "a") 
index2 = str.find(fruit, "na") 
index3 = str.find(fruit, "na",3) 
index4 = str.find("bob", "b", 1, 2)

print("strg.find(fruit, a, 1, 2\n")
print("strg = String Modul Aktiviert \n .find = find Modul aktiviert \n (fruit = Bennenung der Variabel, \n a = suche nach a, \n 1 = start at array 1 with find, \n 2 = not including")

print("\nfruit =",fruit,"\n")
print("index   =",index,"zeigt Arraystelle von erstem a von ", fruit,"an = 1")
print("index 2 =",index2,"zeigt substrings wie 2x na von ", fruit,"an")
print("index 3 =",index3,"Suche in Fruit, also banana na ab array nr 3 = 1 von ", fruit,"und addiere 3")
print("index 4 =",index4,"Suche bob im Bereich array 1 bis 2 (= ob) = nicht vorhanden, 2 = not including, return -1")
##Ende The string module

print('\n')

##Character classification
print("##Character classification = \n")
import string
x = "fruit"
y = "123"
index = x.lower()
index2 = x.upper()
index3 = x.isdigit()
index4 = y.isdigit()

print(index,"\t ... x.lower() schreib alles klein")
print(index2,"\t ... x.upper() schreib alles groß")
print(index3,"\t ... x.isdigit() besteht es nur aus Zahlen")
print(index4,"\t ... y.isdigit() besteht es nur aus Zahlen")

print("\nAs an exercise, discuss which version of isLower you think will be fastest. Can you think of other reasons besides speed to prefer one or the other?")

# first string
firstString = "PYTHON IS AWESOME!"

# second string
secondString = "PyThOn Is AwEsOmE!"

if(firstString.lower() == secondString.lower()):
    print("\nThe strings are same.")
else:
    print("The strings are not same.")

ch = "FRsIT"

def isLower(ch):
    return str.islower(ch)

def isLowers(ch):
    return ch in str.lower(ch)

def isLowerst(ch):
    return "a" <= ch <= "z"


print(isLower(ch))
print(isLowers(ch))
print(isLowerst(ch))

##Ende Character classification
##Ende String

print('\n')

##Lists
##List values
print("##List values = \n")
list1 = list(range(1,10))
print(list1)
##Ende ##List values

print('\n')
    
##Accessing elements
print("Accessing elements = \n")
numbers = list(range(1,10))
#
print("list1 = numbers(range(1,10))")
print(numbers)
#
print('\n',"list1[1] =")
print(numbers[1])
#
print('\n',"list1[6] =")
print(numbers[6])

print('\n',"a loop variable as a list index = ")
horsemen = ("war", "famine", "pestilence", "death")
i = 0
while i > 4: 
    print(horsemen[i])
    i += 1
##Ende Accessing elements

print('\n')

##List length
print("##List length = \n")
horsemen = ("war", "famine", "pestilence", "death")
l = 2
while l < len(horsemen):
    print(horsemen[l])
    l = l + 1

print("\nAs an exercise, write a loop that traverses the previous list and prints the length of each element. What happens if you send an integer to len?")

u = ['spam!', 'Text', ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]

def listendurchlauf(u):
    i = 0
    while i < len(u):
        print("Das Element ",u[i],"von u beträgt",len (u[i]),"Stellen.")
        i = i + 1        

print("\n",u,"\n")
print(listendurchlauf (u))
##Ende List length

print(" = \n")
##List membership
print("##List membership = \n")

print("For Loop List enthält alle Teiler von 3 bis 20\n")
for number in range(20):
    if number % 3 == 0:
        print(number)

print("\n")
print("For Loop List fügt Dinge die ich gerne esse mit meiner Aussage zusammen\n")
for fruit in ["banana", "apple", "quince"]:
    print("I like to eat " + fruit + "s!")

##Ende List membership

print('\n')

##List operations
print("##List operation = \n")

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(a,"+",b," = ",c)
print("[0] * 4"," = ",[0] * 4)
print("[1, 2, 3] * 3"," = ",[1, 2, 3] * 3)

##Ende List operations

print('\n')

##List slices
print("##List slices = \n")
print("thislist = ['a', 'b', 'c', 'd', 'e', 'f'] = ")
thislist = ['a', 'b', 'c', 'd', 'e', 'f']
print("print ( thislist [ 1 : 3 ] ) = ")
print(thislist[1:3])
print("print ( thislist [ : 4 ] ) = ")
print(thislist[:4])
print("print ( thislist [ 3 : ] ) = ")
print(thislist[3:])
print("print ( thislist [ : ] ) = ")
print(thislist[:])

##Ende List slices

print('\n')

##Lists are mutable
print("##Lists are mutable = \n")

fruit = ["banana", "apple", "quince"]
print("fruit = [banana, apple, quince] ")
fruit[0] = "pear"
print("fruit[0] = pear")
fruit[-1] = "orange"
print("fruit[-1] = orange\n")

print(fruit)

thislist = ["a", "b", "c", "d", "e", "f"]
print("thislist = [a, b, c, d, e, f] ")

thislist[1:3] = ["x", "y"]
print("thislist [ 1 : 3 ] = [x, y]")

print(thislist)
##Ende Lists are mutable

print('\n')

##List deletion
print("##List deletion = \n")

a = ["one", "two", "three"]
print("a = [one, two, three]\n")

print("print(a)\n")
print(a)
print("del a[1]\n")
del a[1]
print("print(a)")
print(a)
print("thislist = [a, b , c , d , e , f ]")
thislist = ["a", "b", "c", "d", "e", "f"]
print("del thislist [ 1 : 5 ]\n")
del thislist[1:5]
print("print ( thislist )\n")
print(thislist)

##EndeList deletion

print('\n')

##Objects and values

print("##Objects and values = \n")
print("An object is something a variable can refer to.")
a = "banana"
b = "banana"
print("a = ",a)
print("b = ",b)

print("\nidentifier von a =",a," = ", id(a))
print("\nidentifier von b =",b," = ", id(b)," da gleich wie a beudetet das gleiches object")

a = [1,2,3]
print("\na enthält Liste wie folgt",a," der identifier dazu", id(a))
b = [1,2,3]
print("\na enthält Liste wie folgt",b," der identifier dazu", id(b)," da Nicht gleich wie a beudetet das sind unterschiedliche objects")

##Ende Objects and values

print('\n')

##Cloning lists

print("##Cloning lists = \n")
print("to clone a list")

a = [1, 2, 3]
print("a = [1, 2, 3]")
b = a[:]
print("b = a [ : ]")
print("damit ist b von a gelcont worden")
print("b = ",b)

##Ende Cloning lists

print('\n')

##List parameters
print("##List parameters = \n")

print("numbers = [1,2,3]")
numbers = [1,2,3]

print("numbers = ", numbers)
print("def head(list): \n \treturn list[0]")
def head(list):
    return list[0]

print("print ( head ( numbers ) ) = ",head(numbers))
##Ende List parameters

print('\n')

##Nested lists
print("##Nested lists = \n")

thislist = ["hello", 2.0,5, [10, 20]]
print("thislist = [hello, 2.0,5, [10, 20]]")
print("print(thislist[3])")
print(thislist[3])
print("elt = thislist[3] \tdelete part 1")
elt = thislist[3]
print("elt [0] \t\t\tdelete part 2")
elt [0]
print("print(thislist)")
print("\n", thislist)

print("\nkombinieren der Teile [3] und [1] aus this list:")
print("print(thislist[3][1]) =", thislist[3][1])
##Ende Nested lists

print('\n')

##Matrixes

print("##Matrixes = \n")
print("Matrixes = [ [ 1, 2 , 3 ] , [ 4 ,5 , 6 ] , [ 7 , 8 , 9 ] ] = ")
Matrixes = [[1,2,3],[4,5,6],[7,8,9]]
print("\nprint ( Matrixes [ 1 ] ) = ")
print(Matrixes[1])
print("\nMatrixes [ 1 ] [ 1 ] = ")
print(Matrixes[1][1])

##Ende Matrixes

print('\n')

##Strings and lists

print("##Strings and lists = \n")
import string
print("song = The rain in Spain...")
song = "The rain in Spain..."
print("print(song)")
print(song,"\n")
print("print(str.split(song)")
print(str.split(song),"\n")
print("print(str.split(song, ai))")
print(str.split(song, "ai"))
print("\n join function")
print("thislist = [ The , rain , in , Spain ]")
thislist = ["The","rain","in","Spain"]
print("s = *  * \t\t... Malzeichen sind eigentlich Gänsefüßchen")
s = " "
print("print(thislist)")
print(thislist)
print("print(s.join(thislist))")
print(s.join(thislist))

##Ende Strings and lists
##Ende Lists

print('\n')

##Tuples
##Mutability and tuples

print("##Mutability and tuples = \n")
thisTuple = ("a","b","c","d","e")
print("thistuple = ", thisTuple)

t1 = ("a",)
print("Die Klasse von [ t1 = (a , ) ] = ",type(t1))
t2 = ("a")
print("Die Klasse von [ t2 = (a ) ] = ",type(t2))

##Ende Mutability and tuples

print('\n')

##Tuples as return values
print("##Tuples as return values = \n")
def swap(x,y):
    return y,x

print("swap",swap(2,3))
##Ende Tuples as return values

print('\n')

##Random numbers
print("##Random numbers = \n")
import random

for i in range(10):
    x = random.random()
    print(x)
    
##Ende Random numbers

print('\n')

##List of random numbers
print("##List of random numbers = \n")

def randomList(n):
    s = [0] * n
    for i in range(n):
        s[i] = random.random()
    return s

##Ende List of random numbers
##Ende Tuples

print('\n')

##Dictionaries
print("##Dictionaries = \n")

eng2sp = {}                 #first assignment
eng2sp["one"] = "uno"       #second assignment
eng2sp["two"] = "dos"

print(eng2sp)
eng2sp = {"one":"uno","two":"dos","three":"tres"}
print("\n",eng2sp)

print("\n",eng2sp["two"])

##Ende Dictionaries

print("\n")

##Dictionary operations

inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
print(inventory)
print ("\nLöschen aus dem Inventar\n")
del inventory["pears"]
print(inventory)
{"oranges": 525, "apples": 430, "bananas": 312}
print("Wieviele Sorten sind im Inventar = ",len(inventory))

##Ende Dictionary operations

print("\n")

##Dictionary methods
print("##Dictionary methods = \n")

print("eng2sp.keys() = ",eng2sp.keys())
print("eng2sp.items() = ",eng2sp.items())

##Ende Dictionary methods
##Dictionary

print("\n")

##Files and exceptions
##Beginn des Kapitel ohne Namen
print("\b Each file is identified by a unique name")
print("\b or a combination of a file name and a directory name")
print("\nOpening a file creates a file object. The variable f refers to the new file object.")

print("f refers to the new file object = ")

f = open("test.dat","w")
print("\tf = open(test.dat,w) = ", f)
print("\topen... Öffnet \n\t(test.dat ...diese Datei\t\t\t\t\t\t= object\n\t,w) ...ich will auf / in die Datei write = schreiben \t= Methode")
print("\n CAVE")
print("\t test.dat noch nicht vorhanden ... wird erstellt")
print("\t test.dat schon vorhanden ... wird ersetzt")
print("\n Methodenbeispiele")
print("\tprint f.read(5) ...lies 5 Buchstaben")
print("\tf.close() ...schließt Datei")

#Liste über Argumente und Methode #called ...Dictionaries...for loop #extract
#argument to method, Argument und dessen Kurzbeschreibung
arg2meth = {}                 
arg2meth["   argument"] = "\tmethod" + " ...Kurzbeschreibung\n"
arg2meth["\t  w"] = "\t\twrite" + " ...beschreibt Inhalt"
arg2meth["\t   r"] = "\t\tread" + " ...liest kompletten Inhalt"
arg2meth["\t   "] = "\t\tclose" + " ...schließt Datei"
print("")
print(arg2meth.values())
print("")
print("")

for i,z in zip(arg2meth.keys(),arg2meth.values()):
    print(i,"\t",z)

print("")
#How to copy a file #extract
print("\t#How to copy a file ... siehe Quellcode/backend [copyFile(oldFile, newFile)]\n")

def copyFile(oldFile, newFile):
    f1 = open(oldFile, "r")
    f2 = open(newFile, "w")
    while 1:
        text = f1.read(50)
        if text == "":
            break
        f2.write(text)
        f1.close()
        f2.close()
        return

##Ende Beginn des Kapitel ohne Namen

print("\n")

##Text files
print("##Text files = siehe Quellcode/backend\n")

f = open("test.dat","w")                    #öffnet zum schreiben
f.write("line one\nline two\nline three\n") #schreibt 3 Lines
f.close()                                   #schließt

f = open("test.dat","r")                    #öffnet zum Lesen
print("f.readline() = ",f.readline())          #zeigt Inhalt, aber nur Line one danach wird alles in strings gesetzt
print("f.readlines() = ",f.readlines())        #returns all of the remaining lines as a list of strings
print("f.readline() = ",f.readline())          #readline returns the empty string
print("f.readlines() = ",f.readlines())        #readlines returns the empty list

print("")
#Beschreibungen
#symbol description, Symbol Beschreibung
symDesc = {}
symDesc["Symbol"] = "Beschreibung"
symDesc["\t[]"] = " ... list"
symDesc["\t{}"] = " ... dict"
symDesc["\t()"] = " ... tuple"

for i,z in zip(symDesc.keys(),symDesc.values()):
    print(i,"\t",z)
        
print("")

#methods description, Methoden Beschreibung
methDesc = {}
methDesc["Methode"] = "Beschreibung"
methDesc["\tfilterFile"] = "... makes a copy of oldFile, omitting any lines that begin with #:"

for i,z in zip(methDesc.keys(),methDesc.values()):
    print(i,"\t",z)

print("")
#statement description, Anweisungsbeschreibung
stateDesc = {}
stateDesc["statement"] = "Anweisungsbeschreibung"
stateDesc["\tcontinue"] = "... ends the current iteration of the loop, but continues looping"

for i,z in zip(stateDesc.keys(),stateDesc.values()):
    print(i,"\t",z)
#Ende Beschreibungen

#extract
#line-processing program filterFile makes a copy of oldFile, 
#omitting any lines that begin with #:
def filterFile(oldFile, newFile):
    f1 = open(oldFile, "r")
    f2 = open(newFile, "w")
    while 1:
        text = f1.readline()
        if text == "":
            break
        if text[0] == "#":
            continue
        f2.write(text)
    f1.close()
    f2.close()
    return
##Ende Text files

print("\n")

##Writing variables
print("##Writing variables = \n")
import string

cars = 52
"%d" % cars
print(cars)

asd = "%12f" % 6.1
"%12f" % 6.1
print(asd)

#andere Form der Listen Erstellung mit dict
#export
print("\n \n______________________    \n     Lohnübersicht \n______________________")

wages = {"\n\tmary": 6.23, "\tjoet\t": 5.45, "\tjoshua": 4.25}
for i,z in zip(wages.keys(),wages.values()):
    print(i,"\t",z)
##Ende Writing variables

print("\n")

##Directories
print("##Directories = \n")

print("f = open(D:/Gemeinsam,r)")
print("print(f.readline())")
print("Aasgabe...")
##Ende Directories

print("\n")

##Pickling
print("##Pickling = \n")

import pickle
f = open("test.pck","w")

#to store a data stucture
print("pickle.dump(12.3, f)")
print("pickle.dump([1,2,3], f)")
print("f.close()")
print("\tf = open(’test.pck’,’r’")
print("\tx = pickle.load(f)")
print("\tx")
print("\t\tAusgabe = 12.3")
print("\ntype(x)")
print("\t\t<type ’float’>")
print("\ny = pickle.load(f)")
print("y")
print("\t\tAusgabe = [1, 2, 3]")
print("type(y)")
print("\t\tAusgabe = <type ’list’>")
##Ende Directories

print("\n")
#Exceptions
print("Exceptions = \n")

#Error Fehlermeldungen und Beschreibung
errorReport = {}
errorReport["\tError"] = "\t\t\t\t\t\t\t\tBeschreibung" + 6*"\t" + "e.g."
errorReport["\tZeroDivisionError: integer division or modulo"] = "... created an exception" + 4*"\t" + ">>> print 55/0"
errorReport["\tIndexError: list index out of range"] = 3*"\t" + "... accessing a nonexistent list item" + 2*"\t" + ">>> a = [ ] \n" + 19*"\t" + ">>> print a[5]"
errorReport["\tKeyError: what"] = 4*"\t" + "... accessing a key that isn’t in the dictionary" + 2*"\t" + ">>> b = {} \n" + 19*"\t" + ">>> print b[’what’]"


for i,z in zip(errorReport.keys(),errorReport.values()):
    print(i,"\t",z)

#überprüft ob Datei schon vorhanden ist
def exists(filename):
    try:
        f = open(filename)
        f.close()
        return 1
    except:         #Wenn Error gibt er False zurück
        return 0

#Übung
print("As an exercise, write a function that uses inputNumber to input a number from the keyboard and that handles the BadNumberError exception.")

def inputNumber():
    x = int(input("Gib Nummer = "))
    if x == 17:
        print("BadNumberError"," 17 is a bad number")

##inputNumber() #deaktiviert wegen falscher Fehlermeldung[d.w.f.f.m.]
##Ende Exceptions
##Classes and objects
##User-defined compound types
print("##Classes and objects \n")
print("##User-defined compound types = \n")
import math

class Point: 
    pass

class str: 
    pass

blank = Point()

##Ende User-defined compound types

print("\n")

##Attributes
print("##Attributes = \n")
blank = Point()

#blank refers to a Point object which contains two attributes
blank.x = 3.0
print("\t[blank] = ...\n\t[.] = dot notationdot notation:\n\t[x] = ...\n\t [3.0] = ...")
print("blank.x =",blank.x)
blank.y = 4.0
print("blank.y =",blank.y)
distanceSquared = blank.x * blank.x + blank.y * blank.y
print("\n\tblank.x * blank.x + blank.y * blank.y = distanceSquared = ",distanceSquared)
print("\nblank = ",blank)
print("\nblank id = ",id(blank))    
##Ende Attributes
##Instances as parameters
print("##Instances as parameters \n blank.x == blank.y",blank.x == blank.y)
##Ende Instances as parameters
##Ende Classes and objects
##Ende Files and exceptions
print("\n")

##Classes and functions
print("##Classes and functions")
##Time
print("##Time = ")

class Time:
    pass

time = Time()
time.hours = 11
time.minutes = 59
time.seconds = 30

print("Stunde =",time.hours," Minute = ", time.minutes," Sekunden = ", time.seconds)

print("\nAs an exercise, write a function printTime that takes a Time object as an argument and prints it in the form hours:minutes:seconds.")

def printTime(hh,mm,ss):
    class Time:
        pass
    time = Time()
    time.hh = hh
    time.mm = mm
    time.ss = ss
    print(time.hh,":",time.mm,":",time.ss," Uhr")

printTime(22,13,12)
##Ende Time

##Ende Classes and functions

##Ende Files and exceptions

print("\n")
    
##Classes and methods
print("##Classes and methods")
print("##Object-oriented features")
##printTime
print("\n##printTime als Funktion = ")

class Time:
    pass

def printTime(time): #definiert Funktion mit Objekt
    print(str(time.hours),":",str(time.minutes),":",str(time.seconds)," Uhr")

currentTime = Time()
currentTime.hours = 9
currentTime.minutes = 14
currentTime.seconds = 30

print(Time(currentTime))

print("\n##printTime als Methode = ")
#previous method definitions here...
class Time:
    def printTime(time):
        print(str(time.hours),":",str(time.minutes),":",str(time.seconds)," Uhr")   
    pass

currentTime = Time() #definiert Objekt
currentTime.hours = 9
currentTime.minutes = 14
currentTime.seconds = 30

currentTime.printTime()
##Ende printTime

print("\n")
 
##Optional arguments
print("Optional arguments = \n")

def find(str, ch, start=0):
    index = start               #start wird zu index
    while index < len(str):     #solange ausführen bis index kleiner als Länge des Wortes
        if str[index] == ch:    #wenn Buchstabe des Wortes = Buchstabe ist
            return index        #dann gib index zurück bei apple = 1
        index = index + 1       #ansonsten index +1 
    return -1                   #bei azure kein p Ausgabe -1

print("\n ohne Index")
print(find("apple","p"))
print(find("azure","p"))
print("\n mit Index")
print(find("apple","p",1))
print(find("apple","p",2))
print(find("apple","p",3))
##Ende ptional arguments

print("\n")
##The initialization method
print("##The initialization method = \n")
class Time:
    def printTime(time):
        print(str(time.hours),":",str(time.minutes),":",str(time.seconds)," Uhr")   
    pass

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

currentTime = Time(9,14,30)
currentTime.printTime()

currentTime = Time()
currentTime.printTime()

currentTime = Time(9)
currentTime.printTime()

currentTime = Time (9, 14)
currentTime.printTime()

currentTime = Time(seconds = 30, hours = 9)
currentTime.printTime()
##Ende The initialization method

print("\n")

##Points revisited
print("##Points revisited = \n")
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return ( "(" + str(self.x) + "," + str(self.y) + ")")

p = Point(3, 4)
print(str(p))
##Ende Points revisited

print("\n")

##Operator overloading

print("##Operator overloading = \n")
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return ( "(" + str(self.x) + "," + str(self.y) + ")")

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(3, 4)
p2 = Point(5, 7)
p3 = p1 + p2

print('''
p1 = Point(3, 4)
p2 = Point(5, 7)
p3 = p1 + p2
= ''',p3)

print('''\nAs an exercise, add a method sub (self, other) 
that overloads the subtraction operator, and try it out.''')

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return ( "(" + str(self.x) + "," + str(self.y) + ")")

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

    def __divi__(self, other):
        return Point(self.x / other.x, self.y / other.y)

    def __rmul__(self, other):
        return self.x * other.x + self.y * other.y


s1 = Point(3, 4)
s2 = Point(5, 7)
s3 = s1 - s2

print('''
s1 = Point(3, 4)
s2 = Point(5, 7)
s3 = s1 - s2
= ''',s3)

m1 = Point(3, 4)
m2 = Point(5, 7)
m3 = m1 * m2

print('''
m1 = Point(3, 4)
m2 = Point(5, 7)
m3 = m1 * m2
= ''',m3)

d1 = Point(3, 4)
d2 = Point(5, 7)
d3 = d1 * d2

print('''
d1 = Point(3, 4)
d2 = Point(5, 7)
d3 = d1 * d2
= ''',d3)

r1 = Point(3, 4)
r2 = Point(5, 7)
r3 = r1 * r2

print('''
r1 = Point(3, 4)
r2 = Point(5, 7)
r3 = r1 * r2
= ''',d3)

r1 = Point(3, 4)
r2 = Point(5, 7)


print('''
r1 = Point(3, 4)
r2 = Point(5, 7)

r1 * r2 = ''',r1 * r2)
##Operator overloading

print("\n")

##Polymorphism
print("##Polymorphism = \n")
def multadd (x, y, z):
    return x * y + z

print('''multadd(3,2,1) =''', multadd(3,2,1))

##Ende Polymorphism
##Ende Classes and methods