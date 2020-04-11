import tkinter
import tkinter.messagebox   # Öffnet Info Box
from tkinter import *       # erstelle Bilddatei und verkleinere


def quitapp():
    main.destroy()


def solvesodoku():
    # Entry Liste
    enliste = []

    # Entries
    en = tkinter.Entry(main)
    enliste.append(en)

    # Öffnet Info Box
    tkinter.messagebox.showinfo("Lösung", "OK")


# Test
def test():
    eingabe = z.get()
    try:
        zahl = int(eingabe)
        lb["text"] = "Test:" + zahl
    except:
        lb["text"] = "Bitte Zahl eingeben"


main = tkinter.Tk()


# Titel
lbtitel = tkinter.Label(main, text="Sudoku", font='Helvetica 11 bold')
lbtitel.grid(row=0, column=3, columnspan=1)
lbtitel = tkinter.Label(main, text="Solver", font='Helvetica 11 bold')
lbtitel.grid(row=1, column=3, columnspan=1)

# Reihen / Spalten / Eingaben
for r1 in range(2, 5):
    for c1 in range(2, 5):
        fr = tkinter.Frame(main, width=10, height=10, relief="sunken", bd=2)
        fr.grid(row=r1, column=c1)
        for r2 in range(0, 3):
            for c2 in range(0, 3):
                z = tkinter.Entry(fr, width=1)
                z.grid(row=r2, column=c2)


# Beende Applikation
lbfrei1 = tkinter.Label(main, text="")
lbfrei1.grid(row=13, column=2, columnspan=1)


# erstelle Bilddatei und verkleinere
img = PhotoImage(
    file=r"C:\xampp\htdocs\Projekte\Python\Sonstiges\img-check.png")
photoimage = img.subsample(40, 40)

bsolvesodoku = tkinter.Button(main, text='Solve', font='Helvetica 11 bold',
                              image=photoimage, compound=LEFT, command=test)
bsolvesodoku.grid(row=14, column=2, columnspan=3)

lb = tkinter.Label(main, text="Test:")
lb.grid(row=16, column=2, columnspan=3)

lbfrei2 = tkinter.Label(main, text="")
lbfrei2.grid(row=15, column=2, columnspan=1)

bend = tkinter.Button(main, text="Quit", command=quitapp)
bend.grid(row=17, column=2, columnspan=3)


main.mainloop()
