import random
import sys

solution = random.randrange(0, 10)
countTries = 1

print("##Guessing Game##")
guess = input("guess the number (range 0-10):")
for i in range(1, 5):
    if int(guess) == solution:
        print("!!!Congratulations!!!")
        print("Your guess is right!!!")
        print("You needed "+str(countTries)+". tries!")
        sys.exit(0)

    print(str(countTries)+". try")
    print("!wrong number!")
    guess = input("guess the number (range 0-10):")
    countTries += 1

print("!wrong number!")
print("You needed "+str(countTries)+". tries and have no try left!")
