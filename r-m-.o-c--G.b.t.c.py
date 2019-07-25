print("!ep1 -rep <answer>. \n 25/2 \n You must send !ep1 -rep <reponse> as private message to the bot.")

import math

def GoBackToCollege(number1,number2):
    square_root= math.sqrt(number1)
    multiply= round((square_root*2),2)
    return multiply

number1 = float(input("\n number1 = "))
number2 = float(input("\n number2 = "))
 

print("\n")

a = '/privmsg Candy !ep1 -rep <['
b = str(GoBackToCollege(number1,number2))
c = ']>'
d = sep=''


from tkinter import *
r = Tk()
var = b
r.clipboard_append(a+var+c+d)
r.after(2000, r.destroy)
r.mainloop()