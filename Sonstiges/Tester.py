import tkinter

main = tkinter.Tk()

def ende():
    main.destroy()

lst = []

for r in range(0,3):
    z = int(tkinter.Entry(width=6))
    z.grid(row=r, column=1)
    


def test():
    lbanz["text"] = "Ergebnis: " + lst.append(z)
    
btest = tkinter.Button(main, text = "Test", command = test)
btest.grid(row=6, column=2)

# Anzeigelabel
lbanz = tkinter.Label(main, text="Ergebnis: ")
lbanz.grid(row=7, column=2)

# Schaltfläche Ende
bende = tkinter.Button(main, text = "Ende", command = ende)
bende.grid(row=8, column=2)

main.mainloop()

