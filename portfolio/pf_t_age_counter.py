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
    age_counter.destroy()                   # Beendet jetzige Session
    os.system("pf_t_age_counter.py")        # Startet neue Session


def leereTextfeld():
    eingabeAlter.delete(first=0, last=10)
    eingabeGeburtstagDD.delete(first=0, last=10)
    eingabeGeburtstagMM.delete(first=0, last=10)
    eingabeGeburtstagYY.delete(first=0, last=10)
    ausgabefeld.delete(1.0, tk.END)
    heutigertag


def testdats():
    eingabeAlter.insert('end', "12")
    eingabeGeburtstagDD.insert('end', "12")
    eingabeGeburtstagMM.insert('end', "12")
    eingabeGeburtstagYY.insert('end', "1212")


def heutigertag():
    now = datetime.datetime.today()
    tag = now.now
    a = now.date

    c = now.hour
    d = now.month
    uhrzeit = now.hour
    jahr = now.year

    neueZeile = "\n"
    heute1 = "Heute ist der "
    heute2date = now.day, ".", d, ".", jahr
    heute3 = " um {} Uhr.".format(uhrzeit)

    ausgabefeld = tk.Text(age_counter)
    ausgabefeld.insert('end', heute1)
    ausgabefeld.insert('end', heute2date)
    ausgabefeld.insert('end', heute3)


def countAge():
    jahreEingabe = eingabeAlter.get()
    jahr = now.year

    # t = datetime.datetime.today()           # Alternative Eingabe
    neueZeile = "\n"

    if jahreEingabe == "":
        ausgabefeld.insert('end', neueZeile)
        ausgabefeld.insert('end', neueZeile)
        ausgabefeld.insert('end', "Kein Alter für Person A angegeben!")

    else:
        alter = str(int(jahr)-int(jahreEingabe))
        textGeburtsjahr = "Die Person A ist im Jahr {} geboren.".format(alter)
        ausgabefeld.insert('end', neueZeile)
        ausgabefeld.insert('end', neueZeile)
        ausgabefeld.insert('end', textGeburtsjahr)

    if eingabeGeburtstagYY.get() == "":
        ausgabefeld.insert('end', neueZeile)
        ausgabefeld.insert('end', neueZeile)
        ausgabefeld.insert('end', "Kein Geburtstag für Person B angegeben!")

    else:
        a = datetime.date(int(eingabeGeburtstagYY.get()), int(
            eingabeGeburtstagMM.get()), int(eingabeGeburtstagDD.get()))
        b = datetime.date(int(now.year), int(now.month), int(now.day))
        c = b-a
        alterMitGeburtstag = round((c.days / 365), 2)
        textGeburtstag = "Die Person B ist {} Jahre alt.".format(
            alterMitGeburtstag)
        ausgabefeld.insert('end', neueZeile)
        ausgabefeld.insert('end', neueZeile)
        ausgabefeld.insert('end', textGeburtstag)


# Frame 1
rahmenreihe1 = tk.Frame(age_counter)
rahmenreihe1.pack(fill='x', padx=10, ipady=5)

# Frame 2
rahmenreihe2 = tk.Frame(age_counter)
rahmenreihe2.pack(fill='x', padx=10, ipady=5)

# Frame 3
rahmenreihe3 = tk.Frame(age_counter)
rahmenreihe3.pack(fill='x', padx=10, ipady=5)

# Label 1 Alter
labeleingabe = tk.Label(rahmenreihe1, text='Alter Person A: ')
labeleingabe.pack(side='left')

# Eingabefeld 1 Alter in Jahren
eingabeAlter = tk.Entry(rahmenreihe1, width=10)
eingabeAlter.pack(side='left')

# Button 1 Zurück
bback = tk.Button(rahmenreihe1, width=10, text="Zurück", command=back)
bback.pack(side="left", padx=10, pady=5)

# Label 2
labeleingabe = tk.Label(rahmenreihe2, text='Geburtstag Person B: ')
labeleingabe.pack(side='left')

# Eingabefeld 2 Geburtstag
eingabeGeburtstagDD = tk.Entry(rahmenreihe2, width=2)
eingabeGeburtstagDD.pack(side='left')
tk.Label(rahmenreihe2, text='-').pack(side='left')
eingabeGeburtstagMM = tk.Entry(rahmenreihe2, width=2)
eingabeGeburtstagMM.pack(side='left')
tk.Label(rahmenreihe2, text='-').pack(side='left')
eingabeGeburtstagYY = tk.Entry(rahmenreihe2, width=4)
eingabeGeburtstagYY.pack(side='left')

# Button Count Age
bcountage = tk.Button(rahmenreihe3, text='Count Age', command=countAge)
bcountage.pack(side='left', padx=10, pady=5)

# Button Lösche Ausgabefeld
bdelete = tk.Button(rahmenreihe3, text='Clear', command=leereTextfeld)
bdelete.pack(side='left', padx=10, pady=5)

# Button neustart
breboot = tk.Button(rahmenreihe3, text='Neustart', command=rebootAgeCounter)
breboot.pack(side='left', padx=10, pady=5)

# Button Testdaten
btestdat = tk.Button(rahmenreihe3, text='Testdaten', command=testdats)
btestdat.pack(side='left', padx=10, pady=5)

# Ausgabefeld 1
now = datetime.datetime.today()
tag = now.now
a = now.date

c = now.hour
d = now.month
uhrzeit = now.hour
jahr = now.year

neueZeile = "\n"
heute1 = "Heute ist der "
heute2date = now.day, ".", d, ".", jahr
heute3 = " um {} Uhr.".format(uhrzeit)

ausgabefeld = tk.Text(age_counter)
ausgabefeld.insert('end', heute1)
ausgabefeld.insert('end', heute2date)
ausgabefeld.insert('end', heute3)

ausgabefeld.pack(padx=20, pady=20, fill='x')

heutigertag

age_counter.mainloop()
