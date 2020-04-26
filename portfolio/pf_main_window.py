import tkinter as tk
import os
from tkinter import *
import tkinter.messagebox

main = tk.Tk()
main.title("PyFolio")
# Hauptfenster
status = "main"
# Breite 1000x Höhe 400+ X 1200+ Y 200
main.geometry("260x460+1800+200")  # großer Monitor
# main.geometry("260x460+100+0") # kleiner Monitor


# Funktionen öffne
# Spiele
def openBlackJack():
    main.destroy()
    os.system("pf_g_black_jack.py")  # Startet neue Session


def openRomme():
    main.destroy()
    os.system("pf_g_romme.py")  # Startet neue Session


def openTicTacToe():
    main.destroy()
    os.system("pf_g_tic_tac_toe.py")  # Startet neue Session


# Tools
def openAgeCounter():
    main.destroy()
    os.system("pf_t_age_counter.py")  # Startet neue Session


def openSodokuSolver():
    main.destroy()
    os.system("pf_t_sodoku_solver.py")  # Startet neue Session


def openSystemInfo():
    main.destroy()
    os.system("pf_t_systeminfo.py")  # Startet neue Session


def openTkinterView():
    main.destroy()
    os.system("pf_t_tkinter_views.py")  # Startet neue Session


# andere Projekte
def openDrawWithTurtle():
    main.destroy()
    os.system("pf_otpr_draw_with_turtle.py")  # Startet neue Session


def openLoginSystem():
    main.destroy()
    os.system("pf_otpr_login_system.py")  # Startet neue Session


def openPyExcelReader():
    main.destroy()
    os.system("pf_otpr_py_excel_reader.py")  # Startet neue Session


# Funktionen binnen MAIN Fenster
def theEnd():
    main.destroy()


def rebootMain():
    main.destroy()                  # Beendet jetzige Session
    os.system("pf_main_window.py")  # Startet neue Session


def openTester():
    main.destroy()                  # Beendet jetzige Session
    os.system("pf_m_test.py")  # Startet neue Session

# Menüleiste erzeugen
mBar = tk.Menu(main)
main["menu"] = mBar

# Menü
mGames = tk.Menu(mBar)
mGames["tearoff"] = 0  # Menü nicht abtrennbar
mTools = tk.Menu(mBar)
mTools["tearoff"] = 0  # Menü nicht abtrennbar
motpr = tk.Menu(mBar)


# Menüs
mBar.add_cascade(label="Spiele", menu=mGames)
mBar.add_cascade(label="Tools", menu=mTools)
mBar.add_cascade(label="sonstige Projekte", menu=motpr)


# Untermenü 1 Spiele
mGames.add_command(label="Black Jack", command=openBlackJack)
mGames.add_command(label="Rommé", command=openRomme)
mGames.add_command(label="Tic Tac Toe", command=openTicTacToe)
mGames.add_command(label="Spiel4")

# Untermenü 2 Tools
mTools.add_command(label="Altersrechner", command=openAgeCounter)
mTools.add_command(label="Sudoku Solver", command=openSodokuSolver)
mTools.add_command(label="SystemInfo", command=openSystemInfo)
mTools.add_command(label="tkinter view", command=openTkinterView)
mTools.add_command(label="Tool4")


# Untermenü 3 sontige Projekte
motpr.add_command(label="Turtle Zeichnung", command=openDrawWithTurtle)
motpr.add_command(label="Login System", command=openLoginSystem)
motpr.add_command(label="Py Excel reader", command=openPyExcelReader)
motpr.add_command(label="otpr4")


# Frame 1
rahmenreihe1 = tk.Frame(main)
rahmenreihe1.pack(side='left', anchor="nw")


# Frame 2
rahmenreihe2 = tk.Frame(main)
rahmenreihe2.pack(side='right', anchor="ne", padx=25, pady=3)

# Projektliste
projektListeCheck = ["Sudoku Solver",
                     "System Info",
                     "tkinter view",
                     "Py Excel reader",
                     "Altersrechner",
                     "Login System"]
projektListeNot = ["Black Jack",
                   "Rommé",
                   "Tic Tac Toe",
                   "Turtle Zeichnung"]
CheckVar = [IntVar(),
            IntVar(),
            IntVar(),
            IntVar(),
            IntVar(),
            IntVar(),
            IntVar(),
            IntVar(),
            IntVar(),
            IntVar(),
            IntVar()]

# Checkbutton placed
for i in range(len(projektListeCheck)):
    tk.Checkbutton(rahmenreihe1, text=projektListeCheck[i], variable=CheckVar[i], onvalue=0, offvalue=1).pack(
        anchor="w", padx=0, pady=4)

for i in range(len(projektListeNot)):
    tk.Checkbutton(rahmenreihe1, text=projektListeNot[i], variable=CheckVar[i], onvalue=1, offvalue=0).pack(
        anchor="w", padx=0, pady=4)


# Button neues Fenster
tk.Button(rahmenreihe2, text="Test Button", font='Helvetica 9 bold', fg='#428df5',
          command=openTester).pack(padx=10, pady=5)


# Button beenden
tk.Button(rahmenreihe2, text="Quit", font='Helvetica 9 bold underline', fg='#ff0000',
          command=theEnd).pack(padx=10, pady=5)


# Button Neustart
tk.Button(rahmenreihe2, text="Neustart", font='Helvetica 9 bold ', fg='#32ad59',
          command=rebootMain).pack(padx=10, pady=5)


main.mainloop()
