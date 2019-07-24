print("Python-Übungen", '\n',"How to Think Like a Computer Scientist" '\n',"Learning with Python" '\n')
##Variables
print("Variables =",'\n')
x = 17
y = "3.2"
message = "Hello, World!"
z = "1 + 1"

print(x, "=", type(x),'\n')

print(y, "=", type(y),'\n')

print(message, "=", type(message),'\n')

print(z, "=", type(z),'\n')
##Ende Variables

print ('\n')

##Operators and operands
print("Operators and operands =",'\n')
print("+,-,*,/, ** = exponentiation \n examples: \n \n hour = 60 \n minute = 59")
hour = 60
minute = 59
print("\n 20+32 =", 20+32, '\n', "hour-1 =", hour-1, '\n', "hour*60+minute =", hour*60+minute, '\n', "5**2 =", 5**2, "= exponentiation" '\n', "(5+9)*(15-7) =",(5+9)*(15-7), '\n')

print("minute/60 =", minute/60, "= integer division")
print("minute*100/60 =", minute*100/60)
print("int(minute*100/60) = rounded down = ",int(minute*100/60), '\n')

print("3*Fun =", 3*"Fun", '\n' "fun + fun = ""fun"+"fun")

print("comments with #") #Hier ist ein Kopmmentar
##Ende Operators and operands

print ('\n')

##Functions
print("Functions =",'\n')
print("type(32)=", type(32))
print("type= Funktionsname, (32)= argument von der Funktion,",type(32),"= return value or result")

import math
print("math.sqrt(2) / 2.0 =",math.sqrt(2) / 2.0, "= Quadratwurzel von 2 durch 2" )
print ('\n')
##Funktionen definieren
print ("First Line", '\n', "Funktion newLine() = Second Line" )
print ("newLine() =" )

def newLine():
    print("Second Line")
newLine() 
print ('\n')

print ("Funktion threeLine() = Second Line 3 mal untereinander" )
#def threeLines():
#    newLine()
#    newLine()
#    newLine()

#threeLines()
#print ('\n')

#print ("Übung",'\n', "As an exercise, write a function called nineLines that uses threeLines to print nine blank lines. How would you print twentyseven new lines?")
#def threeLines():
#    print("1")
#    print("2")
#    print("3")

#def nineLines():
#    threeLines()
#    threeLines()
#    threeLines()

#def twentysevenNewLines():
#    nineLines()
#    nineLines()
#    nineLines()

#print('\n',"twentysevenNewLines definiert")
#twentysevenNewLines()

print ('\n')

print("def printTwice(bruce):",'\n'"print (bruce, bruce)")
def printTwice(bruce):
    print (bruce, bruce)
print('\n',"printTwice('Spam') =")
printTwice('Spam')

print('\n',"def catTwice(part1, part2):",'\n'"cat = part1 + part2 =")
def catTwice(part1, part2):
    cat = part1 + part2

printTwice('cat')
##Ende Funktionen definieren

print ('\n')

##The modulus operator
print("The modulus operator =",'\n')
print("quotient = int(7 / 3)")
quotient = int(7 / 3)
print ("= ", quotient)

print ('\n'"Rest von 7 / 3")
remainder = 7 % 3
print ("= ", remainder)
##Ende The modulus operator

print ('\n')

##Boolean expressions
print("Boolean expressions =",'\n')
a = (5 == 5)
print("5 == 5 ...", a)

b = 5 == 6
print("5 == 6 ...", b)

print("a =",int(a),", b =",int(b),"a>b = ",a>b)
##Ende Boolean expressions

print ('\n')

##Conditional execution
print("Conditional execution")
c = 5
if c > 0:
    print('yes')

print("if ... FIRST STATEMENT",'\n'"  print(...) ... LAST STATEMENT")
##Ende Conditional execution

print ('\n')

##Alternative execution
print("")
d = 12
if d%2 == 0:
    print("Der Rest von", d,"/2", 'ist even 0') #True
else:
    print(d, 'is odd')
##Ende Alternative execution

print ('\n')

##Chained conditionals
print("Chained conditionals =",'\n')
def compare(d,c):
    if d < c:
        print (d, "is less than", c)
    elif d > c:
        print (d, "is greater than", c)
    else:
        print (d, "and", c, "are equal")

compare(d,c)
print ('\n')

def functionA():
    print ("functionA was called")

def functionB():
    print ("functionB was called")

def functionC():
    print ("functionC was called")

def dispatch(choice):
    if choice == 'A':
        functionA()
    elif choice == 'B':
        functionB()
    elif choice == 'C':
        functionC()
    else:
        print("Invalid choice.")
dispatch("S")
##Ende Chained conditionals

print ('\n')

##The return statement
print("The return statement =",'\n')
import math
f = 14
print("f =",f,"ist nicht kleiner gleich 0 -> return",'\n')

def printLogarithm(f):
    if f <= 0:
        print ("Positive numbers only, please.")
        return #Muss innerhalb einer Funktion sein

    result = math.log(f) #wird ignoriert
    print ("The log of f is", result) #wird ignoriert
##Ende The return statement

print ('\n')

##Recursion
print("Recursion =",'\n')
print("Countdown")
def countdown(n):
    if n == 0:
        print ("Blastoff!")
    else:
        print (n)
        countdown(n-1)

countdown(3)
print("Countdown mit NewLine Funktion")
print ('\n')
def newLine(m):
    if m == 2:
        print ("2")
    else:
        print (m)
        newLine(m+1)

newLine(1)
##Ende Recursion

print ('\n')

##Infinite recursion
print("Infinite recursion =",'\n')

print("def recurse( g ):",'\n',"   recurse( g+1 )",'\n','\n',"recurse(0)",'\n')

#def recurse( g ):
#    recurse( g+1 )
    
#recurse(0)

print("Error:","Traceback (most recent call last):",'\n',"line ..., in <module>",'\n',"line ..., in recurse",'\n',"line ..., in recurse",'\n',"line ..., in recurse",'\n',"[Previous line repeated 993 more times]")

##Ende Infinite recursion

print ('\n')

##Keyboard input
print("Keyboard input =", '\n')
##built-in functions

print("input = raw_input(prompt=message what to input)",'\n')

name = input("What is your name? ")

print (name)

##Ende Keyboard input

print ('\n')

##Fruitful functions
print("Fruitful functions =", '\n')

def absoluteValueN(n):
    if n < 0:
        return -n
    elif n > 0:
        return n

print ("Wenn absoluteValueN = 0 = ", absoluteValueN(0))
print ("Wenn absoluteValueN = 2 = ", absoluteValueN(2),'\n')

print("As an exercise, write a compare function that returns 1 if x > y, 0 if x == y, and -1 if x < y.")

def compare(x1,y1):
    if x1 > y1:
        return 1
    elif x1 == y1:
        return 0
    elif x1 < y1:
        return -1

print("Wenn compare(x1,y1)=(2,12) dann return = ", compare(2,12))
##Ende Fruitful functions

print ('\n')

##
##Ende 

print ('\n')

##
##Ende 

print ('\n')

##
##Ende 

print ('\n')

##
##Ende 

print ('\n')

##
##Ende 

print ('\n')

##
##Ende 