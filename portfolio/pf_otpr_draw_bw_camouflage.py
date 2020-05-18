import tkinter as tk
import os
import turtle

Bw_camouflage = tk.Tk()
Bw_camouflage.title('Turtle Zeichnung')
Bw_camouflage.geometry("300x300+1800+5")  # großer Monitor
# Bw_camouflage.geometry("310x225+50+0")  # kleiner Monitor
turtle.Screen().setup(width=1600,height=1000,startx=1800,starty=360)

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

#turtle.setheading(0)
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
    turtle.setheading(0)
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


def EINS():    
    #turtle.setheading(0)
    # 0 - east
    # 45
    # 90 - north
    # 135
    # 180 - west
    # 225
    # 270 - south
    # 310
    linie = "white"
    colorlisteGreen = ["#383F2D","#444E36","#49563C","#505A35","#54633A","#636F4B","#727655","#75855E"]
    colorlisteBrown = ["#6B5D38","#59502F","#6E5634","#3D351E","#463A22","#433824","#665134","#302917"]
    colorlisteYellow = ["#78744F","#BDB77D","#C6C285","#9A8C5B","#A69965","#4F4B30","#484B30","#CAC989"]

    x = 0
    turtle.color(linie,colorlisteGreen[x])
    turtle.begin_fill()
    for i in range(2):
        turtle.color(linie,colorlisteGreen[x])
        turtle.forward(100)
        turtle.left(120)
    turtle.end_fill()
    turtle.goto(0,0)
    turtle.setheading(60)

    x = x + 1
    turtle.color(linie,colorlisteGreen[x])
    turtle.begin_fill()
    for i in range(2):
        turtle.color(linie,colorlisteGreen[x])
        turtle.forward(100)
        turtle.left(120)
    turtle.end_fill()
    turtle.setheading(120)
    turtle.goto(0,0)

    x = x + 1
    turtle.color(linie,colorlisteGreen[x])
    turtle.begin_fill()
    for i in range(2):
        turtle.color(linie,colorlisteGreen[x])
        turtle.forward(100)
        turtle.left(120)
    turtle.end_fill()
    turtle.goto(0,0)
    turtle.setheading(180)

    x = x + 1
    turtle.color(linie,colorlisteGreen[x])
    turtle.begin_fill()
    for i in range(2):
        turtle.color(linie,colorlisteGreen[x])
        turtle.forward(100)
        turtle.left(120)
    turtle.end_fill()
    turtle.goto(0,0)
    turtle.setheading(240)

    x = x + 1
    turtle.color(linie,colorlisteGreen[x])
    turtle.begin_fill()
    for i in range(2):
        turtle.color(linie,colorlisteGreen[x])
        turtle.forward(100)
        turtle.left(120)
    turtle.end_fill()
    turtle.goto(0,0)
    turtle.setheading(300)

    x = x + 1
    turtle.color(linie,colorlisteGreen[x])
    turtle.begin_fill()
    for i in range(2):
        turtle.color(linie,colorlisteGreen[x])
        turtle.forward(100)
        turtle.left(120)
    turtle.end_fill()
    turtle.goto(0,0)
    turtle.setheading(300)


def ZWEI():
    #turtle.setheading(0)
    # 0 - east
    # 45
    # 90 - north
    # 135
    # 180 - west
    # 225
    # 270 - south
    # 310
    linie = "white"
    colorlisteGreen = ["#383F2D","#444E36","#49563C","#505A35","#54633A","#636F4B","#727655","#75855E"]
    colorlisteBrown = ["#6B5D38","#59502F","#6E5634","#3D351E","#463A22","#433824","#665134","#302917"]
    colorlisteYellow = ["#78744F","#BDB77D","#C6C285","#9A8C5B","#A69965","#4F4B30","#484B30","#CAC989"]

    x = 0
    x = x + 1
    turtle.color(linie,colorlisteBrown[x])
    turtle.begin_fill()
    turtle.forward(100)
    turtle.setheading(0)
    turtle.forward(100)
    turtle.setheading(120)
    turtle.forward(100)
    turtle.setheading(240)
    turtle.forward(100)
    turtle.end_fill()

    

def DREI():
    #turtle.setheading(0)
    # 0 - east
    # 45
    # 90 - north
    # 135
    # 180 - west
    # 225
    # 270 - south
    # 310
    linie = "white"
    colorlisteGreen = ["#626844","#424C34","#373E2C","#546241","#5B6644"]

    turtle.color(linie,colorlisteGreen[0])
    turtle.begin_fill()
    for i in range(2):
        turtle.color(linie,colorlisteGreen[0])
        turtle.forward(100)
        turtle.setheading(120)
    turtle.end_fill()
    turtle.goto(0,0)
    turtle.setheading(60)
        
def allClear():
    turtle.clear()

# Frame 1
rahmenreihe1 = tk.Frame(Bw_camouflage)
bback = tk.Button(rahmenreihe1, width=10, text="Zurück", command=back)
bende = tk.Button(rahmenreihe1, text='Ende', command=end)
brebootBw_camouflage = tk.Button(
    rahmenreihe1, text='Neustart', command=rebootBw_camouflage)
ballClear = tk.Button(
    rahmenreihe1, text='Clear', command=allClear)

rahmenreihe1.pack(fill='x',padx=10)
bback.pack(padx=10, pady=5)
bende.pack(padx=10, pady=5)
brebootBw_camouflage.pack(padx=10, pady=5)
ballClear.pack(padx=10, pady=5)



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

bpic1 = tk.Button(spaltenreihePic, width="6", text='EINS', command=EINS, fg="#4287f5")
bpic2 = tk.Button(spaltenreihePic, text='ZWEI', command=ZWEI, fg="#a442f5")
bpic3 = tk.Button(spaltenreihePic, text='DREI', command=DREI, fg="#2b6318")

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
