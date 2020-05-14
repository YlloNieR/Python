import sys
import tkinter as tk
import os

testinfo = tk.Tk()
testinfo.title("Testinfo")
testinfo.geometry("200x400+1800+200")  # großer Monitor
# testinfo.geometry("200x200+100+0") # kleiner Monitor


def back():
    testinfo.destroy()
    os.system("pf_main_window.py")    # Startet neue Session


#def tester():
    #eingabe.delete(0, 10)
    #ausgabefeld.delete(0, 10)

def print_input(*args):
    for entry in entries:
        print(entry.get())

s = tk.Entry(testinfo, bd =5)

entries = [s for _ in range(5)]
for entry in entries:
    entry.pack()




            


def reboottestinfo():
    testinfo.destroy()                   # Beendet jetzige Session
    os.system("pf_m_test.py")             # Startet neue Session


rahmenreihe1 = tk.Frame(testinfo, relief="sunken")
rahmenreihe2 = tk.Frame(testinfo, relief="sunken")
rahmenreihe3 = tk.Frame(testinfo, relief="sunken")
rahmenreihe4 = tk.Frame(testinfo, relief="sunken")

rahmenreihe5 = tk.Frame(testinfo, relief="sunken")
rahmenreihe6 = tk.Frame(testinfo, relief="sunken")
rahmenreihe7 = tk.Frame(testinfo, relief="sunken")


rahmenreihe1.pack(anchor="nw")
rahmenreihe2.pack(anchor="nw")
rahmenreihe3.pack(anchor="nw")
rahmenreihe4.pack(anchor="w")

rahmenreihe5.pack(anchor="w")
rahmenreihe6.pack(anchor="w")
rahmenreihe7.pack(anchor="w")

eingabe = tk.Entry(rahmenreihe4, width=10)
eingabe.pack(side="left", pady=5)
eingabe.insert("end", "test")
ausgabefeld = tk.Entry(rahmenreihe4, width=10)
ausgabefeld.pack(side="left", pady=5)
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

z10 = tk.Entry(rahmenreihe5, width=2)
z11 = tk.Entry(rahmenreihe5, width=2)
z12 = tk.Entry(rahmenreihe5, width=2)
z13 = tk.Entry(rahmenreihe6, width=2)
z14 = tk.Entry(rahmenreihe6, width=2)
z15 = tk.Entry(rahmenreihe6, width=2)
z16 = tk.Entry(rahmenreihe7, width=2)
z17 = tk.Entry(rahmenreihe7, width=2)
z18 = tk.Entry(rahmenreihe7, width=2)

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

z10.pack(side="left")
z11.pack(side="left")
z12.pack(side="left")
z13.pack(side="left")
z14.pack(side="left")
z15.pack(side="left")
z16.pack(side="left")
z17.pack(side="left")
z18.pack(side="left")



# Button Hauptfunktion
btestinfo = tk.Button(testinfo, text="Tester", command=print_input)
btestinfo.pack(side="bottom", pady=5)

# Button Zürück
btestinfo = tk.Button(testinfo, text="Zurück", command=back)
btestinfo.pack(side="bottom", pady=5)

# Button Reboot
bRebootTest = tk.Button(testinfo, text="Neustart", command=reboottestinfo)
bRebootTest.pack(side="bottom", pady=5)

testinfo.mainloop()
