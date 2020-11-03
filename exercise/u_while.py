print("Bitte geben Sie die Maße an welche in cm umgerechnet werden soll an:")
a = input()
eingabe = int(a)
print("Von welcher Einheit aus wollen Sie in cm umrechnen:")
einheit = input()

while einheit != "Inch":  # != bedeutet ist nicht gleich oder auch "not equal to"
    print("Bitte versuchen Sie eine andere Einheit:")
    einheit = input()

print(eingabe, "Inch, sind", eingabe*2.54, "cm")
