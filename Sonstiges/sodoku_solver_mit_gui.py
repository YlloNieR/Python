import tkinter

def quitapp():
    main.destroy()

def solvesodoku():
    pass

main = tkinter.Tk()


# Titel
lbtitel = tkinter.Label(main, text="Sudoku Solver")
lbtitel.grid(row=1, column=0, columnspan=6)


tkinter.Label(main, text="Test").grid(row=2, column=0)

# Beende Applikation
bend = tkinter.Button(main, text="Quit", command=quitapp)
bend.place(relx=0.5, rely=1, anchor="s")

main.mainloop()