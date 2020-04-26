import sys
import tkinter as tk

testinfo = tk.Tk()
testinfo.title("Test")
testinfo.geometry("200x200+1800+200")  # großer Monitor
# testinfo.geometry("200x200+100+0") # kleiner Monitor


def back():
    testinfo.destroy()
    import pf_main_window    # Startet neue Session


def tester():
    eingabe.delete(0, 10)
    ausgabefeld.delete(0, 10)


rahmenreihe1 = tk.Frame(testinfo, relief="sunken")
rahmenreihe2 = tk.Frame(testinfo, relief="sunken")
rahmenreihe3 = tk.Frame(testinfo, relief="sunken")
rahmenreihe4 = tk.Frame(testinfo, relief="sunken")

rahmenreihe1.pack(anchor="nw")
rahmenreihe2.pack(anchor="nw")
rahmenreihe3.pack(anchor="nw")
rahmenreihe4.pack(anchor="w")

eingabe = tk.Entry(rahmenreihe4, width=10)
eingabe.pack(side="left")
eingabe.insert("end", "test")
ausgabefeld = tk.Entry(rahmenreihe4, width=10)
ausgabefeld.pack(side="left")
ausgabefeld.insert("end", "test")


z1 = tk.Entry(rahmenreihe1, width=2)
z2 = tk.Entry(rahmenreihe1, width=2)
z3 = tk.Entry(rahmenreihe1, width=2)
z4 = tk.Entry(rahmenreihe2, width=2)
z5 = tk.Entry(rahmenreihe2, width=2)
z6 = tk.Entry(rahmenreihe2, width=2)
z7 = tk.Entry(rahmenreihe3, width=2)
z8 = tk.Entry(rahmenreihe3, width=2)
z9 = tk.Entry(rahmenreihe3, width=2)

z1.insert(0, '1')
z2.insert(0, '2')
z3.insert(0, '3')
z4.insert(0, '4')
z5.insert(0, '5')
z6.insert(0, '6')
z7.insert(0, '7')
z8.insert(0, '8')
z9.insert(0, '9')

z1.pack(side="left")
z2.pack(side="left")
z3.pack(side="left")

z4.pack(side="left")
z5.pack(side="left")
z6.pack(side="left")

z7.pack(side="left")
z8.pack(side="left")
z9.pack(side="left")

# Button Hauptfunktion
btestinfo = tk.Button(testinfo, text="Tester", command=tester)
btestinfo.pack(side="bottom")

# Button Zürück
btestinfo = tk.Button(testinfo, text="Zurück", command=back)
btestinfo.pack(side="bottom")

testinfo.mainloop()
