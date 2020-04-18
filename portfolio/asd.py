import tkinter as tk

blackJack = tk.Tk()
blackJack.title('Black Jack')
blackJack.geometry("400x400+1800+200")


def back():
    blackJack.destroy()


rahmenreihe1 = tk.Frame(blackJack)
rahmenreihe1.pack(fill='x', padx=10, ipady=10)
labeleingabe = tk.Label(rahmenreihe1, text='Eingabe:')
labeleingabe.pack(side='left')

eingabe = tk.Entry(rahmenreihe1, width=10)
eingabe.pack(side='left')

bback = tk.Button(rahmenreihe1, width=10, text="Zurück", command=back)
bback.pack(side="left", padx=10, pady=5)

bdelete = tk.Button(blackJack, text='clear')
bdelete.pack(side='bottom', anchor='w', padx=10, pady=5)

text1 = tk.Text(blackJack)
text1.insert('end', "Start Game")
text1.pack(padx=10)


z19 = input("\n Dealer - Möchtest du eine Karte j/n ? ")     
    if z19 == "j":

z19.get()) == 0

blackJack.mainloop()
