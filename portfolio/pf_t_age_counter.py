import tkinter as tk
import datetime
import time
import os


age_counter = tk.Tk()
age_counter.title('Alter Zähler')
age_counter.geometry("400x400+1800+200")


def back():
    age_counter.destroy()

def rebootAgeCounter():
    age_counter.destroy()                  # Beendet jetzige Session
    os.system("pf_t_age_counter.py")  # Startet neue Session

def leereTextfeld():
    ausgabefeld.delete(1.0, tk.END)

def timeNow():
    z = datetime.datetime.now()
    ausgabefeld.insert('end',z)

# Frame 1
rahmenreihe1 = tk.Frame(age_counter)
rahmenreihe1.pack(fill='x', padx=10, ipady=10)

# Frame 2
rahmenreihe2 = tk.Frame(age_counter)
rahmenreihe2.pack(fill='x', padx=10, ipady=10)

# Label 1
labeleingabe = tk.Label(rahmenreihe1, text='Eingabe:')
labeleingabe.pack(side='left')

# Eingabefeld 1
eingabefeld = tk.Entry(rahmenreihe1, width=10)
eingabefeld.pack(side='left')

# Button Zurück
bback = tk.Button(rahmenreihe1, width=10, text="Zurück", command=back)
bback.pack(side="left", padx=10, pady=5)

# Button Count Age
bcountage = tk.Button(rahmenreihe2, text='Count Age', command=timeNow)
bcountage.pack(side='left', padx=10, pady=5)

# Button Lösche Ausgabefeld
bdelete = tk.Button(rahmenreihe2, text='clear', command=leereTextfeld)
bdelete.pack(side='left', padx=10, pady=5)

# Button neustart
bdelete = tk.Button(rahmenreihe2, text='Neustart', command=rebootAgeCounter)
bdelete.pack(side='left', padx=10, pady=5)

# Ausgabefeld 1
x = time.strptime("23 Nov 00", "%d %b %y")
y = time.strptime("30 Nov 00", "%d %b %y")
z = y;"\n";x

ausgabefeld = tk.Text(age_counter,width = 20,)
ausgabefeld.insert('end', z)
ausgabefeld.pack(padx=20, pady=20)





age_counter.mainloop()
