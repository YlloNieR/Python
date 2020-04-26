import tkinter as tk

romme = tk.Tk()
romme.title('Rommé')
romme.geometry("400x400+1800+200")  # großer Monitor
# romme.geometry("400x400+100+0") # kleiner Monitor


def back():
    romme.destroy()
    import pf_main_window    # Startet neue Session


def rebootMain():
    main.destroy()                  # Beendet jetzige Session
    os.system("pf_main_window.py")  # Startet neue Session


# Frame 1
rahmenreihe1 = tk.Frame(romme)
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
bdelete = tk.Button(romme, text='clear')
bdelete.pack(side='bottom', anchor='w', padx=10, pady=5)

# Ausgabefeld 1
ausgabefeld = tk.Text(romme)
ausgabefeld.insert('end', "Start Game")
ausgabefeld.pack(padx=10)


romme.mainloop()
