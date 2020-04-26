import tkinter as tk
import os
import webbrowser

tkinterViews = tk.Tk()
tkinterViews.title('Tkinter Views')
tkinterViews.geometry("550x500+1800+200")  # großer Monitor
# tkinterViews.geometry("550x500+100+0") # kleiner Monitor


def back():
    tkinterViews.destroy()
    import pf_main_window    # Startet neue Session


def reboottkinterViews():
    tkinterViews.destroy()                  # Beendet jetzige Session
    os.system("pf_t_tkinter_views.py")      # Startet neue Session


def openColorPick():
    webbrowser.open("https://www.google.com/search?biw=871&bih=843&sxsrf=ALeKk03ihEQjCNX7mrt27tapA9eK3uw3fg%3A1587317577620&ei=SYucXqrDJcrBgQbCs51A&q=color+pick&oq=color+pick&gs_lcp=CgZwc3ktYWIQAzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQR1AAWABgo8wyaABwBHgAgAEAiAEAkgEAmAEAqgEHZ3dzLXdpeg&sclient=psy-ab&ved=0ahUKEwjqi_DigvXoAhXKYMAKHcJZBwgQ4dUDCAw&uact=5")


# Frame config
rahmenreihe1 = tk.Frame(tkinterViews, bd=5, relief="sunken", bg="#fff000")
rahmenreihe2 = tk.Frame(tkinterViews, bd=1, relief="ridge")
rahmenreihe3 = tk.Frame(tkinterViews, bd=1, relief="sunken")


# Buttons config
b1 = tk.Button(tkinterViews, text='f. x, s. l, a. n(back)',
               fg="#ffff00", bg="#3234a8", command=back)
b2 = tk.Button(tkinterViews, text='f. x, s. l, a. n, py5, px5(reboot)',
               command=reboottkinterViews, font='Helvetica 9 bold underline')
b3 = tk.Button(tkinterViews, text='Color Picker',
               bg="#42f5aa", command=openColorPick)


# Button placed
b1.pack(fill="x", side="top", anchor='n', pady=5, padx=5)


# Label config
l1 = tk.Label(tkinterViews, text='a. n', background='#ff0000')  # rot
l2 = tk.Label(tkinterViews, text='a. e', background='#ffff00')  # gelb
l3 = tk.Label(tkinterViews, text='px5, a. w', background='#00ff00')  # grün

l4 = tk.Label(rahmenreihe1, text='FR1 sunken a. e, py5, px5')
l5 = tk.Label(rahmenreihe1, text='FR1 sunken a. w')

l6 = tk.Label(rahmenreihe2, text='FR2 ridge a. e')
l7 = tk.Label(rahmenreihe2, text='FR2 ridge a. w')

l8 = tk.Label(rahmenreihe3, text='font - Schrift')
l9 = tk.Label(rahmenreihe3, text='height - Höhe')
l10 = tk.Label(rahmenreihe3, text='width - Breite')
l11 = tk.Label(rahmenreihe3, text='relief - Randart')
l12 = tk.Label(rahmenreihe3, text='Image - Bild')
l13 = tk.Label(rahmenreihe3, text='bg - Background color')
l14 = tk.Label(rahmenreihe3, text='fg - Foreground clolor')
l15 = tk.Label(rahmenreihe3, text='anchor - Ausrichtung')

l16 = tk.Label(tkinterViews, text='pl. x=10, y=200',
               background='#ff0000')  # rot
l17 = tk.Label(tkinterViews, text='pl. x=20, y=221',
               background='#ffff00')  # gelb
l18 = tk.Label(tkinterViews, text='pl. x=30, y=242',
               background='#00ff00')  # grün

# Label placed
l1.pack(anchor='n')
l2.pack(anchor='e')
l3.pack(padx=5, anchor='w')

rahmenreihe1.pack(side="right", padx=5)
l4.pack(anchor='e', pady=5, padx=5)
l5.pack(anchor='w')

rahmenreihe2.pack()
l6.pack(anchor='e')
l7.pack(anchor='w')


# Label placed
# x nach rechts, y nach unten
l16.place(x=10, y=200)  # rot
l17.place(x=20, y=221)  # gelb
l18.place(x=30, y=242)  # grün


# Button placed
b2.pack(fill="x", side="left", anchor='s', pady=5, padx=5)
b3.place(x=20, y=285)


# Label placed
rahmenreihe3.pack(side="bottom", anchor='s', pady=5, padx=5)
l8.pack()
l9.pack()
l10.pack()
l11.pack()
l12.pack()
l13.pack()
l14.pack()
l15.pack()


tkinterViews.mainloop()
