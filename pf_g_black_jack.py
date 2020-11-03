import tkinter as tk
import os
import tkinter.messagebox

blackJack = tk.Tk()
blackJack.title('Black Jack')
blackJack.geometry("400x400+1800+200")  # großer Monitor
# blackJack.geometry("400x400+100+0") # kleiner Monitor

class asd:
    zahl = 42
    string = "Zeichenkette"

    def do_something(self):         # self = argument, was sagt innerhalb dieser Klasse
        pass

instanz = asd() 



def back():
    blackJack.destroy()
    os.system("pf_main_window.py")    # Startet neue Session


def rebootMain():
    blackJack.destroy()                  # Beendet jetzige Session
    os.system("pf_g_black_jack.py")  # Startet neue Session

def starteSpiel():
    if eingabefeldSpielername == "":
        tk.messagebox.showinfo(title="Spielername",
                               message="Geben Sie bitte erst einen Spielernamen ein!")
    else:
        eingabefeldSpielername.config(state='disabled')
        bstartGame.config(state='disabled')


# Frame 1
rahmenreihe1 = tk.Frame(blackJack)
rahmenreihe1.pack(fill='x', padx=10, ipady=10)

# Frame 2
rahmenreihe2 = tk.Frame(blackJack)
rahmenreihe2.pack(fill='x', padx=10, ipady=10)

# Label 1
labeleingabeSpielername = tk.Label(rahmenreihe1, text='Spielername:')
labeleingabeSpielername.pack(side='left')

# Eingabefeld 1
eingabefeldSpielername = tk.Entry(rahmenreihe1, width=10)
eingabefeldSpielername.pack(side='left')

# Button Zurück
bback = tk.Button(rahmenreihe1, width=10, text="Zurück", command=back)
bback.pack(side="left", padx=10, pady=5)

# Button Reboot
breboot = tk.Button(rahmenreihe1, width=10, text="Neustart", command=rebootMain)
breboot.pack(side="left", padx=10, pady=5)

# Button Starte
bstartGame = tk.Button(rahmenreihe2, width=10, font="Helvetica 10 bold",
                   text="Starte Spiel", command=starteSpiel)
bstartGame.pack(side="left", padx=10, pady=5)

# Button Noch eine
boneMore = tk.Button(rahmenreihe2, width=10, font="Helvetica 10 bold",
                   fg="#09750b", text="+Karte", command=starteSpiel)
boneMore.pack(side="left", padx=10, pady=5)

# Button Keine Mehr
bkeineKarte = tk.Button(rahmenreihe2, width=15, font="Helvetica 10 bold",
                   fg="#b81307", text="Keine Karte mehr", command=starteSpiel)
bkeineKarte.pack(side="left", padx=10, pady=5)


# Button Lösche Ausgabefeld
bdelete = tk.Button(blackJack, text='clear')
bdelete.pack(side='bottom', anchor='w', padx=10, pady=5)

# Ausgabefeld 1
ausgabefeld = tk.Text(blackJack)
ausgabefeld.insert('end', "Start Game")
ausgabefeld.pack(padx=10)


blackJack.mainloop()
