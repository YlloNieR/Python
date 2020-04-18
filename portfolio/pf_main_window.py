import tkinter as tk
import os

main = tk.Tk()
# Hauptfenster
status = "main"
# Breite 1000x Höhe 400+ X 1200+ Y 200
# main.geometry("1000x700+1200+200")
main.geometry("1000x700+1800+200")
main.title("PyFolio")


# Funktionen Bar
def openBlackJack():
    import pf_g_black_jack

def openSodokuSolver():
    main.destroy()
    import pf_t_sodoku_solver


def openSystemInfo():
    import pf_t_systeminfo


def openTester():
    import pf_t_test

# Funktionen binnen Fenster
def theEnd():
    main.destroy()

def rebootMain():
    main.destroy()                  # Beendet jetzige Session
    os.system("pf_main_window.py")  # Startet neue Session


# Menüleiste erzeugen
mBar = tk.Menu(main)
main["menu"] = mBar

# Menü
mGames = tk.Menu(mBar)
mGames["tearoff"] = 0  # Menü nicht abtrennbar
mTools = tk.Menu(mBar)
mTools["tearoff"] = 0  # Menü nicht abtrennbar

# Menüs
mBar.add_cascade(label="Spiele", menu=mGames)
mBar.add_cascade(label="Tools", menu=mTools)

# Untermenü 1
mGames.add_command(label="Black Jack", command=openBlackJack)
mGames.add_command(label="Spiel2")
mGames.add_command(label="Spiel3")
mGames.add_command(label="Spiel4")

# Untermenü 2
mTools.add_command(label="Sudoku Solver", command=openSodokuSolver)
mTools.add_command(label="SystemInfo", command=openSystemInfo)
mTools.add_command(label="Tool3")
mTools.add_command(label="Tool4")


# Button neues Fenster
tk.Button(main, text="Neu", command=openTester).pack()


# Button beenden
bTheEnd = tk.Button(main, text="Quit", command=theEnd)
bTheEnd.pack()
tk.Button(main, text="Neustart", command=rebootMain).pack()


main.mainloop()
