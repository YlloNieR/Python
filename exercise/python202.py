#!/bin/python3
import sys
from datetime import datetime


# Print String
print("\n#Strings and things")
print("""Hello world
a multi line string""")
print('This is '+'Strings and things')
print("\n") # new line

# Maths
print("#Maths time:")
print("\tad ", 50 + 50)
print("\tsubtract ", 50-50)
print("\tmultiply ",50 * 50)
print("\tdivide ", 50 / 50)
print("\tPEMDAS ",50 + 50 * 50 / 50)
print("\tmodulo ",50 % 6)
print("\tnumber without leftovers", 50 // 6)
print("\n") # new line

# Variables & Methods
print("#Variables & Methods")
print("Fun with variables and methods:")
quote = "All is fair in love and war"
print("\tlength ",len(quote))
print("\tuppercase ",quote.upper())
print("\tlowercase ",quote.upper())
print("\tquote.title ",quote.title())
print("\n") # new line
print("Variables\n")
name = "Heath"
age = 29 # int(29)
gpa = 3.7 # float(3.7) 
print("\t",int(age))
print("\t",int(212.2))
print("\nMy Name is " + name + " and I am " + str(age) + "years old")
print("\n") # new line
age += 1
print("\t",age)
birthday = 1
age+= birthday
print("\t",age)

# Functions
print("\n","#Now, some functions")
def who_am_i():
	name2 = "Health"
	age2 = 29
	print("\nMy Name is " + name2 + " and I am " + str(age2) + "years old")

who_am_i()

# adding in parameters
print("\n","#adding in parameters")
def add_one_hundred(num):
	print(num + 100)

add_one_hundred(100)

# add mutltiple parameters
print("\n","#add mutltiple parameters")
def multiple_parameters(x,y):
	return x * y

print(multiple_parameters(7,7))

# square root
print("\n","#square root")
def square_root(x):
	return x ** .5

print(square_root(64))

# Boolean expressions (True or False)
print("\n","#Boolean expressions (True or False)")
bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))

#Relational and Boolean Operators 
print("\n","# Relational and Boolean Operators")
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

print(greater_than, less_than, greater_than_equal_to, less_than_equal_to)

test_and = (7 > 5) and (6 < 7)
test_or = (7 > 5) or (5 < 7)
test_not = True

print(test_and)

print("\n")

#Conditional Statements
print("\n","# Conditional Statements:")
def soda(money):
	if money >= 2:
		return "You've got yourself a soda!"
	else:
		return "No soda for u"

print("du hast 3 € ->",soda(3))
print("du hast 1 € ->",soda(1))


def alcohol(age,money):
	if(age >= 21) and (money >= 5):
		return "We're getting tipsy"
	elif(age >= 21) and (money < 5):
		return "come back with more money"
	elif(age < 21) and (money >= 5):
		return "nice try, kid"
	else:
		return "You're too poor and too young"

print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(14,5))
print(alcohol(20,4))

#List
print("\n","# List")
print("lists have brackets:")
movies = ["when Harry met Sally","The Hangover","the Perks of Being Wallflower","The Exorcist"]

print("movie n= ",len(movies))
print("movie 1:",movies[0])
print("movie 1-3:",movies[0:2])
print("movie from 2:",movies[1:])
print("movie until 3:",movies[:2])
print("movie until -1:",movies[-1])
print("movie n= ",len(movies))
print("movie 1-3:",movies[0:2])

movies.append("Jaws")
print("movie added Jaws ",movies,"\n")

movies.pop(1)
print("movie poped Jaws ",movies,"\n")

movies = ["when Harry met Sally","The Hangover","the Perks of Being Wallflower","The Exorcist"]
person = ["Health", "Jake", "Leah", "Jeff"]

combined = zip(movies, person)
print(list(combined),"\n")

#Tuples 
print("\n","# Tuples")
print("Tuples have a parentheses and cannot change = immutable")
grades = ("A","B","C","D","F")
print(grades[1])

#Loops
print("\n","# Loops")
print("For loops - start to finish of iterate")
vegetables = ["cucumber","spanish", "cabbage"]
for x in vegetables:
	print(x)

#While loops
print("\n","# While loops")
print("Execute as long as true")
i = 1
while i <= 10:
	print(i)
	i += 1

#Dictionaries
print("Dictionaries are keys and values")
drinks = {"White Russian":7,"Old Fashion":10,"Lemon Drop":8,"Butterfly Nipple":8}
print(drinks)

employees = {"Finance": ["Bob","Linda","Tina"], "IT":["Gene","Louise","Teddy"], "HR":["Jimmy Jr.","Mort"]}
print(employees)

employees ['Legal'] = ["Mr. Frond"] #add new key:value pair
print(employees)

employees.update({"Sales": ["Andie","Ollie"]})
print(employees)

drinks['White Russian'] = 8
print(drinks)

print(drinks.get("White Russian"))
print(drinks.get("Martini"))
drinks.update({"Martini":7})
print(drinks.get("Martini"))




print(datetime.now())

def new_line():
	print("\n")

my_name = "Health"

print(my_name[0])
print(my_name[-1])
print(my_name[3])
print(my_name[:2])
print(my_name[3:])

sentence = "This is a sentence."

print(sentence[:4])
print(sentence[-9:-1])
print(sentence.split())

print("A" in "Apple")
letter = "a"
word = "Apple"

print(letter.lower() in word.lower())



