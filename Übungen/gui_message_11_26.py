import tkinter
import tkinter.messagebox

def ende():
    main.destroy()

def msginfo():
    tkinter.messagebox.showinfo \
        ("Info", "Eine Info-Box")

def msgwarning():
    tkinter.messagebox.showwarning \
        ("Warnung", "Eine Wahrnungs-Box")

def msgerror():
    tkinter.messagebox.showerror \
        ("Fehler", "Eine Fehler-Box")

def msgyesno():
    antwort = tkinter.messagebox.askyesno \
        ("Ja / Nein", "Eine Ja / Nein-Box")
    if antwort == 1:
        lbanz["text"] = "Ja"
    else:
        lbanz["text"] = "Nein"

def msgokcancel():
    antwort = tkinter.messagebox.askokcancel \
        ("OK / Abbrechen", "Eine OK / Abbrechen-Box")
    if antwort == 1:
        lbanz["text"] = "OK"
    else:
        lbanz["text"] = "Abbrechen"

def msgretrycancel():
    antwort = tkinter.messagebox.askretrycancel \
        ("Wiederholen / Abbrechen", "Eine Wiederholen / Abbrechen-Box")
    if antwort == 1:
        lbanz["text"] = "Wiederholen"
    else:
        lbanz["text"] = "Abbrechen"

def msgquestion():
    # hier einmal in allgemeiner Technik, ohne Komfort
    msgbox = tkinter.messagebox.Message(main, \
        type = tkinter.messagebox.ABORTRETRYIGNORE, \
        icon= tkinter.messagebox.QUESTION, \
        title="Beenden, Wiederholen oder Ignorieren",
        message="Beenden, Wiederholen oder Ignorieren")
    
    antwort = msgbox.show()

    if antwort == "abort":
        lbanz["text"] = "Beenden"
    elif antwort == "retry":
        lbanz["text"] = "Wiederholen"
    else:
        lbanz["text"] = "Ignorieren"

main = tkinter.Tk()

# Schaltfläche Message Info
binfo = tkinter.Button(main, text="Info", command=msginfo )
binfo.pack()

# Schaltfläche Message Box Warnung
bwarning = tkinter.Button(main, text="Warnung", command=msgwarning )
bwarning.pack()

# Schaltfläche MessageBox Error
berror = tkinter.Button(main, text="Fehler", command=msgyesno )
berror.pack()

# Schaltfläche Message Box Ja/Nein
byesno = tkinter.Button(main, text="Ja / Nein", command=msgyesno)
byesno.pack()

# Schaltfläche Message Box OK / Cancel
bokcancel = tkinter.Button(main, text="OK / Abbrechen", command=msgokcancel)
bokcancel.pack()

# Schaltfläche Message Box Retry / Cancel
bretrycancel = tkinter.Button(main, text="Wiederholen / Abbrechen", command=msgretrycancel)
bretrycancel.pack()

# Schaltfläche Message Box Frage
bquestion = tkinter.Button(main, text="Allgemeine Frage", command=msgquestion)
bquestion.pack()

# Schaltfläche Ende
bende = tkinter.Button(main, text="Ende", command=ende)
bende.pack()

# Anzeigelabel
lbanz = tkinter.Label(main)
lbanz.pack()

main.mainloop()
