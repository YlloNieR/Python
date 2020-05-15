import tkinter as tk
import os
import turtle

Bw_camouflage = tk.Tk()
Bw_camouflage.title('Turtle Zeichnung')
Bw_camouflage.geometry("270x225+1800+200")  # großer Monitor
# Bw_camouflage.geometry("270x225+100+0")  # kleiner Monitor

def end():
    Bw_camouflage.destroy()
    turtle.bye()


def back():
    Bw_camouflage.destroy()
    turtle.bye()
    os.system("pf_main_window.py")    # Startet neue Session


def rebootBw_camouflage():
    Bw_camouflage.destroy()                  # Beendet jetzige Session
    turtle.bye()
    os.system("pf_otpr_draw_bw_camouflage.py")  # Startet neue Session

turtle.setheading(0)
# 0 - east
# 90 - north
# 180 - west
# 270 - south

def lookNW():
    turtle.setheading(135) 

def lookW():
    turtle.setheading(180)

def lookSW():
    turtle.setheading(225)

def lookN():
    turtle.setheading(90)

def moveForward():
    turtle.forward(5)

def lookS():
    turtle.setheading(270)

def lookNE():
    turtle.setheading(45)

def lookE():
    turtle.setheading(0)

def lookSE():
    turtle.setheading(310)  

def pic1():
    for i in range(4):
        turtle.forward(25)
        turtle.left(90)
        for i in range(100):
            x = i+2
            turtle.forward(25+x)
            turtle.left(90)
    turtle.done()


def pic2():
    star = turtle.Turtle()

    for i in range(5):
        star.forward(50)
        star.right(144)
    turtle.done()


def pic3():
    painter = turtle.Turtle()
    painter.pencolor("blue")

    for i in range(50):
        painter.forward(50)
        painter.left(123) # Let's go counterclockwise this time 
        
    painter.pencolor("red")
    for i in range(50):
        painter.forward(100)
        painter.left(123)
    turtle.done()


def dreieckerstellen():
    painter = turtle.Turtle()
    for i in range(3):
        painter.forward(50)
        painter.left(120)
    painter.color("red")
    painter.dot(50)


# Frame 1
rahmenreihe1 = tk.Frame(Bw_camouflage)
bback = tk.Button(rahmenreihe1, width=10, text="Zurück", command=back)
bende = tk.Button(rahmenreihe1, text='Ende', command=end)
brebootBw_camouflage = tk.Button(
    rahmenreihe1, text='Neustart', command=rebootBw_camouflage)

rahmenreihe1.pack(fill='x',padx=10)
bback.pack(padx=10, pady=5)
bende.pack(padx=10, pady=5)
brebootBw_camouflage.pack(padx=10, pady=5)



# Button Zurück

# Button Ende

# Button reboot d Turtle

###################################################################################
# Frame 2 Pfeile links
spaltenreiheL = tk.Frame(Bw_camouflage)
spaltenreiheL.pack(fill='y', side="left", padx=5)

# Frame 3 Pfeile Mitte
spaltenreiheM = tk.Frame(Bw_camouflage)
spaltenreiheM.pack(fill='y',side="left", padx=5)

# Frame 4 Pfeile rechts
spaltenreiheR = tk.Frame(Bw_camouflage)
spaltenreiheR.pack(fill='y',side="left", padx=5)

# Button Pfeil
barrowNW = tk.Button(spaltenreiheL, text='↖️',width="6", command=lookNW)
barrowW = tk.Button(spaltenreiheL, text='⬅️',width="6", command=lookW)
barrowSW = tk.Button(spaltenreiheL, text='↙️',width="6", command=lookSW)

barrowN = tk.Button(spaltenreiheM, text='⬆️',width="6", command=lookN)
bmoveForward = tk.Button(spaltenreiheM, text='🐢',width="6", command=moveForward)
barrowS = tk.Button(spaltenreiheM, text='⬇️',width="6", command=lookS)

barrowNE = tk.Button(spaltenreiheR, text='↗️',width="6", command=lookNE)
barrowE = tk.Button(spaltenreiheR, text='➡️',width="6", command=lookE)
barrowSE = tk.Button(spaltenreiheR, text='↘️',width="6", command=lookSE)

barrowNW.pack(padx=5, pady=5)
barrowW.pack(padx=5, pady=5)
barrowSW.pack( padx=5, pady=5)

barrowN.pack(padx=5, pady=5)
bmoveForward.pack(padx=5, pady=5)
barrowS.pack(padx=5, pady=5)

barrowNE.pack(padx=5, pady=5)
barrowE.pack(padx=5, pady=5)
barrowSE.pack(padx=5, pady=5)

# Frame 5 Pfeile rechts
spaltenreihePic = tk.Frame(Bw_camouflage)
spaltenreihePic.pack(fill='y',side="left", padx=5)

bpic1 = tk.Button(spaltenreihePic, text='Dreieck', command=dreieckerstellen, fg="#4287f5")
bpic2 = tk.Button(spaltenreihePic, text='pic2', command=pic2, fg="#a442f5")
bpic3 = tk.Button(spaltenreihePic, text='pic3', command=pic3, fg="#2b6318")

bpic1.pack(padx=5, pady=5)
bpic2.pack(padx=5, pady=5)
bpic3.pack(padx=5, pady=5)

# Frame 5
#rahmenreihe5 = tk.Frame(Bw_camouflage)
#rahmenreihe5.pack(fill='x', padx=10, ipady=10)

# Label 1
#labeleingabe = tk.Label(rahmenreihe1, text='Eingabe:')
# labeleingabe.pack(side='left')

# Eingabefeld 1
#eingabefeld = tk.Entry(rahmenreihe1, width=10)
# eingabefeld.pack(side='left')


Bw_camouflage.mainloop()
