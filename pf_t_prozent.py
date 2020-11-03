import tkinter as tk
import os


prozent_rechner = tk.Tk()
var = tk.IntVar()
prozent_rechner.title('Prozent Rechner')
prozent_rechner.geometry("400x800+1800+200")  # großer Monitor
# prozent_rechner.geometry("400x400+100+0") # kleiner Monitor


def back():
    prozent_rechner.destroy()
    os.system("pf_main_window.py")    # Startet neue Session


def rebootProzentRechner():
    prozent_rechner.destroy()                   # Beendet jetzige Session
    os.system("pf_t_prozent.py")        # Startet neue Session


def leereTextfeld():
    eingabeWertA.delete(first=0, last=10)
    eingabeWertB.delete(first=0, last=10)
    ausgabefeld.delete(1.0, tk.END)


def berechneProzent():
    if var.get() == 0:
        ausgabefeld.insert('end', "Bitte Wähle was du berechnen willst:\n")
        ausgabefeld.insert('end', "Grundwert\n")
        ausgabefeld.insert('end', "Prozentsatz\n")
        ausgabefeld.insert('end', "Prozent\n")
    try:
        if var.get() == 1:
            ausgabefeld.insert('end', "berechne Grundwert...\n")
            W = int(eingabeWertA.get())
            p = int(eingabeWertB.get())
            G = float((W*100)/p)
            ausgabefeld.insert('end', "Grundwert = ")
            ausgabefeld.insert('end', G)

        if var.get() == 2:
            ausgabefeld.insert('end', "berechne Prozentsatz...\n")
            W = int(eingabeWertA.get())
            G = int(eingabeWertB.get())
            p = float((W*100)/G)
            ausgabefeld.insert('end', "Prozentsatz = ")
            ausgabefeld.insert('end', p)

        if var.get() == 3:
            ausgabefeld.insert('end', "berechne Prozent...\n")
            G = int(eingabeWertA.get())
            p = int(eingabeWertB.get())
            W = float((G*p)/100)
            ausgabefeld.insert('end', "Prozent = ")
            ausgabefeld.insert('end', W)
            ausgabefeld.insert('end', "%")
        ausgabefeld.insert('end', "\n")
    except ValueError:
        ausgabefeld.insert('end', "\nDu musst Wert A und B eingeben!!!\n")


# Frame 1
rahmenreihe1 = tk.Frame(prozent_rechner)
rahmenreihe1.pack(fill='x', padx=10, ipady=5)

# Frame 2
rahmenreihe2 = tk.Frame(prozent_rechner)
rahmenreihe2.pack(fill='x', padx=10, ipady=5)

# Frame 3
rahmenreihe3 = tk.Frame(prozent_rechner)
rahmenreihe3.pack(fill='x', padx=10, ipady=5)

# Frame 4
rahmenreihe4 = tk.Frame(prozent_rechner)
rahmenreihe4.pack(fill='x', padx=10, ipady=5)

# Frame 5
rahmenreihe5 = tk.Frame(prozent_rechner)
rahmenreihe5.pack(fill='x', padx=10, ipady=5)

# Frame 6
rahmenreihe6 = tk.Frame(prozent_rechner)
rahmenreihe6.pack(fill='x', padx=10, ipady=5)

# Frame 7
rahmenreihe7 = tk.Frame(prozent_rechner)
rahmenreihe7.pack(fill='x', padx=10, ipady=5)

# Label 1 Eingabe
labeleingabe = tk.Label(rahmenreihe1, text='Wert A: ')
labeleingabe.pack(side='left')

# Eingabefeld 1 Wert
eingabeWertA = tk.Entry(rahmenreihe1, width=10)
eingabeWertA.pack(side='left')

# Button 1 Zurück
bback = tk.Button(rahmenreihe1, width=10, text="Zurück", command=back)
bback.pack(side="left", padx=10, pady=5)

# Label 2
labeleingabe = tk.Label(rahmenreihe2, text='Wert B: ')
labeleingabe.pack(side='left')

# Eingabefeld 2 Wert B
eingabeWertB = tk.Entry(rahmenreihe2, width=10)
eingabeWertB.pack(side='left')

# Button neustart
breboot = tk.Button(rahmenreihe2, text='Neustart',
                    command=rebootProzentRechner)
breboot.pack(side='left', padx=10, pady=5)

# Radiobutton Grundwert
radioGrundwert = tk.Radiobutton(
    rahmenreihe4, text='-> Grundwert berechnen, A = W | B = p', variable=var, value=1)
radioGrundwert.pack(side="left")

# Radiobutton Prozentsatz
radioProzentsatz = tk.Radiobutton(
    rahmenreihe5, text='-> Prozentsatz berechnen, A = W | B = G', variable=var, value=2)
radioProzentsatz.pack(side="left")

# Radiobutton Prozent
radioProzent = tk.Radiobutton(
    rahmenreihe6, text='-> Prozent berechnen, A = G | B = p', variable=var, value=3)
radioProzent.pack(side="left")

# Button berechne
bBerechne = tk.Button(rahmenreihe7, text='Berechne', command=berechneProzent)
bBerechne.pack(side='left', padx=10, pady=5)

# Button Lösche Ausgabefeld
bdelete = tk.Button(rahmenreihe7, text='Clear', command=leereTextfeld)
bdelete.pack(side='left', padx=10, pady=5)

# Ausgabefeld
ausgabefeld = tk.Text(prozent_rechner)
ausgabefeld.pack(padx=20, pady=20)


prozent_rechner.mainloop()
