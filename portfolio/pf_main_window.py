import tkinter as tk

main = tk.Tk()
# Hauptfenster
status = "main"
# Breite 1000x Höhe 400+ X 1200+ Y 200
main.geometry("1000x700+1200+200")
main.title("PyFolio")

# Funktion beenden
def theEnd():
    main.destroy()

# Erzeugt neues Fenster mit Schaltfläche Ende
def openSodokuSolver():
    import pf_t_sodoku_solver

def openSystemInfo():
    import pf_t_systeminfo






# Menüleiste erzeugen
mBar = tk.Menu(main)
main["menu"] = mBar

# Menü
mGames = tk.Menu(mBar)
mGames["tearoff"] = 0 # Menü nicht abtrennbar
mTools = tk.Menu(mBar)
mTools["tearoff"] = 0 # Menü nicht abtrennbar

# Menüs
mBar.add_cascade(label="Spiele", menu=mGames)
mBar.add_cascade(label="Tools", menu=mTools)

# Untermenü 1
mGames.add_command(label="Spiel1")
mGames.add_command(label="Spiel2")
mGames.add_command(label="Spiel3")
mGames.add_command(label="Spiel4")

# Untermenü 2
mTools.add_command(label="Sudoku Solver", command=openSodokuSolver)
mTools.add_command(label="SystemInfo", command=openSystemInfo)
mTools.add_command(label="Tool3")
mTools.add_command(label="Tool4")


# Button neues Fenster
tk.Button(main, text="Neu").pack()

# Button beenden
bTheEnd = tk.Button(main, text="Quit", command=theEnd)
bTheEnd.pack()


main.mainloop()