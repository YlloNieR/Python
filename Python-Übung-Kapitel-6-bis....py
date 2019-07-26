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
    
##
print(" = \n")

##Ende

print('\n')
    
##
print(" = \n")

##Ende

##Ende String


