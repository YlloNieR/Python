import tkinter as tk

dTurtle = tk.Tk()
dTurtle.title('Turtle Zeichnung')
dTurtle.geometry("200x200+1800+200") # großer Monitor
# dTurtle.geometry("200x200+100+0") # kleiner Monitor



def back():
    dTurtle.destroy()

def rebootMain():
    main.destroy()                  # Beendet jetzige Session
    os.system("pf_main_window.py")  # Startet neue Session

# Frame 1
rahmenreihe1 = tk.Frame(dTurtle)
rahmenreihe1.pack(fill='x', padx=10, ipady=10)

# Label 1
labeleingabe = tk.Label(rahmenreihe1, text='Eingabe:')
labeleingabe.pack(side='left')

# Eingabefeld 1
eingabefeld = tk.Entry(rahmenreihe1, width=10)
eingabefeld.pack(side='left')

# Button Zurück
bback = tk.Button(rahmenreihe1, width=10, text="Zurück", command=back)
bback.pack(side="left", padx=10, pady=5)

# Button Lösche Ausgabefeld
bdelete = tk.Button(dTurtle, text='clear')
bdelete.pack(side='bottom', anchor='w', padx=10, pady=5)

# Ausgabefeld 1
ausgabefeld = tk.Text(dTurtle)
ausgabefeld.insert('end', "Start Game")
ausgabefeld.pack(padx=10)



dTurtle.mainloop()
