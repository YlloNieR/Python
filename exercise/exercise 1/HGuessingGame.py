import random

# solution = 4
solution = random.randrange(0, 10)
countTries = 1

print("##Guessing Game##")
guess = input("guess the number (range 0-10):")

while int(guess) != solution:
    print(str(countTries)+". try")
    print("!wrong number!")
    guess = input("guess the number (range 0-10):")
    countTries += 1

print("!!!Congratulations!!!")
print("Your guess is right!!!")
print("You needed "+str(countTries)+". tries!")
