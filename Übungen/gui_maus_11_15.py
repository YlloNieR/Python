import tkinter


def ende():
    main.destroy()


def mlinks(e):
    lbanz["text"] = "linke Maustaste"


def mrechts(e):
    lbanz["text"] = "rechte Maustaste"


def mstrglinks(e):
    lbanz["text"] = "Strg-Taste und linke Maustaste"


def maltlinks(e):
    lbanz["text"] = "Alt-Taste und linke Maustaste"


def mshiftlinks(e):
    lbanz["text"] = "Shift-Taste und linke Maustaste"


def mlinkslos(e):
    lbanz["text"] = "linke Maustaste losgelassen"


def mbetreten(e):
    lbanz["text"] = "Schaltfläche betreten"


def mverlassen(e):
    lbanz["text"] = "Schaltfläche verlassen"


def mbewegt(e):
    lbanz["text"] = \
        "Koordinaten: x=" + str(e.x) + ", y=" + str(e.y)


main = tkinter.Tk()

# Label mit Events
im = tkinter.PhotoImage(file="c:/xampp/htdocs/Projekte/Python/Sonstiges/Buch/img_Animated_rack_and_pinion.gif")
lbm = tkinter.Label(main, image=im)
lbm.bind("<Button 1>", mlinks)
lbm.bind("<Button 3>", mrechts)
lbm.bind("<Control-Button 1>", mstrglinks)
lbm.bind("<Alt-Button 1>", maltlinks)
lbm.bind("<Shift-Button 1>", mshiftlinks)
lbm.bind("<ButtonRelease 1>", mlinkslos)
lbm.bind("<Motion>", mbewegt)
lbm.pack()

# Anzeigelabel
lbanz = tkinter.Label(main, width=35)
lbanz.pack()

# Schaltfläche Ende, mit Events
bende = tkinter.Button(main, text="Ende",
                       command=ende)

bende.bind("<Enter>", mbetreten)
bende.bind("<Leave>", mverlassen)
bende.pack()

main.mainloop()