import tkinter


# Erzeugt neues Fenster mit Schaltfläche
def fenster():
    global neu
    neu = tkinter.Toplevel(main)
    tkinter.Button(neu, text="Ende", command=endeneu).pack()


# Ende neues Fenster
def endeneu():
    neu.destroy()


# Ende Hauptfenster
def ende():
    main.destroy()


# Hauptfenster
main = tkinter.Tk()
tkinter.Button(main, text="Neu", command=fenster).pack()
tkinter.Button(main, text="Ende", command=ende).pack()

main.mainloop()
