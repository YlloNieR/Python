##A find function
print("##A find function = ")
print("Finde den Buchstaben im Wort \n")

Wort = "asdaa"
Buchstabe = "a"
index = 5
print("gesuchtes Wort = ",Wort)
print("gesuchter Buchtstabe = ",Buchstabe,"\n")

print("\nÜbung 1 A find function = \nAs an exercise, modify the find function so that it takes a third parameter, the index in the string where it should start looking. \n")
#Suche mit beginn ab index als while Schleife
def find(Wort, Buchstabe, index):
    count=0
    while index < len(Wort):
        if Wort[index] == Buchstabe:
            if Buchstabe == BuchstabenSuche:
                count = count + 1
                return index
            else: 
                index = index + 1
                return -1
            return count
    
print("Wie oft kommt der Buchstabe ",Buchstabe," ab dem index = ",index," = ", find(Wort, Buchstabe, index),"\n")

print("\nÜbung 2 Looping and counting1 = \nAs an exercise, encapsulate this code in a function named countLetters, and generalize it so that it accepts the string and the letter as parameters. \n")

###################################
print("\nAs an exercise, generate a random number between low and high.")

for i in range(2):
    x = random.random()
    x = x*high
    print(x)


print("\nAs an additional exercise, generate a random integer between low and high, including both end points.")

 