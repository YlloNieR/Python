import tkinter as tk
import os

ticTacToe = tk.Tk()
ticTacToe.title('Tic Tac Toe')
ticTacToe.geometry("400x400+1800+200")  # großer Monitor
# ticTacToe.geometry("400x400+100+0")   # kleiner Monitor

x = True

def back():
    ticTacToe.destroy()
    os.system("pf_main_window.py")    # Startet neue Session


def rebootTicTacToe():
    ticTacToe.destroy()                   # Beendet jetzige Session
    os.system("pf_g_tic_tac_toe.py")      # Startet neue Session

def makeAnXA():
    if x == True:    
        btn_A.set(" X ")
        changePlayer()   
    else:
        btn_A.set(" O ")  
    bAcheck.config(state="disabled")
    changePlayer()          
def makeAnXB():
    if x == True:    
        btn_B.set(" X ")
    else:
        btn_B.set(" O ")            
    bBcheck.config(state="disabled")
    changePlayer()
def makeAnXC():        
    btn_C.set(" X ")
    bCcheck.config(state="disabled")
    x = False

def makeAnXD():          
    btn_D.set(" X ")
    bDcheck.config(state="disabled")
    x = False
def makeAnXE():        
    btn_E.set(" X ")
    bEcheck.config(state="disabled")
def makeAnXF():        
    x = False
    btn_F.set(" X ")
    bFcheck.config(state="disabled")

def makeAnXG():        
    btn_G.set(" X ")
    bGcheck.config(state="disabled")
    x = False
def makeAnXH():        
    btn_H.set(" X ")
    bHcheck.config(state="disabled")
    x = False
def makeAnXI():        
    btn_I.set(" X ")
    bIcheck.config(state="disabled")
    x = False


def makeAnOA():        
    btn_A.set(" O ")
    bAcheck.config(state="disabled")
def makeAnOB():        
    btn_B.set(" O ")
    bBcheck.config(state="disabled")
def makeAnOC():        
    btn_C.set(" O ")
    bCcheck.config(state="disabled")

def makeAnOD():          
    btn_D.set(" O ")
    bDcheck.config(state="disabled")
def makeAnOE():        
    btn_E.set(" O ")
    bEcheck.config(state="disabled")
def makeAnOF():        
    btn_F.set(" O ")
    bFcheck.config(state="disabled")

def makeAnOG():        
    btn_G.set(" O ")
    bGcheck.config(state="disabled")
def makeAnOH():        
    btn_H.set(" O ")
    bHcheck.config(state="disabled")
def makeAnOI():        
    btn_I.set(" O ")
    bIcheck.config(state="disabled")

def makeAnCircle():
    btn_none_text.set(" O ")


def changePlayer():
    if x == True:    
        ausgabefeld.insert('end', x)
        return x == False
    else:
        ausgabefeld.insert('end', x)
        return x == True






# Frame 1
rahmenreihe1 = tk.Frame(ticTacToe)
rahmenreihe1.pack(fill='x', padx=10, ipady=10)

# Frame 2 Spiel 1
rahmenreihe2 = tk.Frame(ticTacToe)
rahmenreihe2.pack(fill='x', padx=10)

# Frame 3 Spiel 2
rahmenreihe3 = tk.Frame(ticTacToe)
rahmenreihe3.pack(fill='x', padx=10)

# Frame 4 Spiel 3
rahmenreihe4 = tk.Frame(ticTacToe)
rahmenreihe4.pack(fill='x', padx=10)

# Button Zurück
bback = tk.Button(rahmenreihe1, width=10, text="Zurück", command=back)
bback.pack(side="left", padx=10, pady=5)

# Button Neustart
brestart = tk.Button(rahmenreihe1, width=10,
                     text="Neustart", command=rebootTicTacToe)
brestart.pack(side="left", padx=10, pady=5)

# Button Start Spiel
bStartSpiel = tk.Button(rahmenreihe1, width=10,
                     text="Starte Spiel")
bStartSpiel.pack(side="left", padx=10, pady=5)

# Label 1
#labeleingabe = tk.Label(rahmenreihe1, text='Eingabe:')
# labeleingabe.pack(side='left')
btn_A = tk.StringVar()
btn_B = tk.StringVar()
btn_C = tk.StringVar()

btn_D = tk.StringVar()
btn_E = tk.StringVar()
btn_F = tk.StringVar()

btn_G = tk.StringVar()
btn_H = tk.StringVar()
btn_I = tk.StringVar()

bAcheck = tk.Button(rahmenreihe2, textvariable=btn_A, command=makeAnXA)
bBcheck = tk.Button(rahmenreihe2, textvariable=btn_B, command=makeAnXB)
bCcheck = tk.Button(rahmenreihe2, textvariable=btn_C, command=changePlayer)

bDcheck = tk.Button(rahmenreihe3, textvariable=btn_D, command=changePlayer)
bEcheck = tk.Button(rahmenreihe3, textvariable=btn_E, command=changePlayer)
bFcheck = tk.Button(rahmenreihe3, textvariable=btn_F)

bGcheck = tk.Button(rahmenreihe4, textvariable=btn_G)
bHcheck = tk.Button(rahmenreihe4, textvariable=btn_H)
bIcheck = tk.Button(rahmenreihe4, textvariable=btn_I)

bAcheck.pack(side='left')
bBcheck.pack(side='left')
bCcheck.pack(side='left')

bDcheck.pack(side='left')
bEcheck.pack(side='left')
bFcheck.pack(side='left')

bGcheck.pack(side='left')
bHcheck.pack(side='left')
bIcheck.pack(side='left')


btn_A.set("[  ]")
bAcheck.config(state="normal")
btn_B.set("[  ]")
btn_C.set("[  ]")

btn_D.set("[  ]")
btn_E.set("[  ]")
btn_F.set("[  ]")

btn_G.set("[  ]")
btn_H.set("[  ]")
btn_I.set("[  ]")

# | A | B | C |
# | D | E | F |
# | G | H | I |


# Button Lösche Ausgabefeld
bdelete = tk.Button(ticTacToe, text='clear')
bdelete.pack(side='bottom', anchor='w', padx=10, pady=5)

# Ausgabefeld 1
ausgabefeld = tk.Text(ticTacToe)
ausgabefeld.insert('end', "Start Game")
ausgabefeld.pack(padx=10, pady=10)


ticTacToe.mainloop()
