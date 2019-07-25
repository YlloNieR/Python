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
print("##A compound data type")



##Ende A compound data type

print('\n')
    

print(" = ")



##Ende String


