import tkinter as tk
import os
from datetime import datetime
import tkinter.messagebox
from tkinter import *

loginSystem = tk.Tk()
loginSystem.title('Login System')
loginSystem.geometry("280x480+1800+200")  # großer Monitor
# loginSystem.geometry("280x480+100+0") # kleiner Monitor


status = "login"


def back():
    if status == "login":
        loginSystem.destroy()
        os.system("pf_main_window.py")    # Startet neue Session


def rebootLoginSystem():
    if status == "login":
        loginSystem.destroy()                   # Beendet jetzige Session
        os.system("pf_otpr_login_system.py")    # Startet neue Session


def deleteEntries():
    if status == "login":
        eingabeUsername.delete(first=0, last=100)
        eingabePasswort.delete(first=0, last=100)


def tesdat():
    if status == "login":
        eingabeUsername.insert('end', "Admin")
        eingabePasswort.insert('end', "1234")


def checkUsername():
    if status == "login":
        global usern
        usern = eingabeUsername.get()                       # hole Username
        # ertselle data Liste (leer)
        data = []
        import csv
        with open("pf_otpr_login_system.csv") as csvfile:   # öffne csv anschließend VAR csvfile
            reader = csv.reader(csvfile)                    #
            for row in reader:
                data.append(row)
        # print(data)
        # suche in 3. Tabelle = User
        col = [x[3] for x in data]
        # print(col.index(usern))
        if usern in col:
            for x in range(0, len(data)):
                if usern == data[x][3]:
                    return True


def checkPWD():
    if status == "login":
        global pwd
        pwd = eingabePasswort.get()
        # ertselle data Liste (leer)
        data = []
        import csv
        with open("pf_otpr_login_system.csv") as csvfile:   # öffne csv anschließend VAR csvfile
            reader = csv.reader(csvfile)                    #
            for row in reader:
                data.append(row)
        # suche in 3. Tabelle = User
        col = [x[4] for x in data]
        if pwd in col:
            for x in range(0, len(data)):
                if pwd == data[x][4]:
                    return True


def pwdUsernVergl():
    if status == "login":
        usern = eingabeUsername.get()                       # hole Username
        pwd = eingabePasswort.get()
        # ertselle data Liste (leer)
        data = []
        import csv
        with open("pf_otpr_login_system.csv") as csvfile:   # öffne csv anschließend VAR csvfile
            reader = csv.reader(csvfile)                    #
            for row in reader:
                data.append(row)

        try:
            # suche in 3. Tabelle = User
            col1 = [x[3] for x in data]
            checkinstanz1 = col1.index(usern)

            col2 = [x[4] for x in data]
            checkinstanz2 = col2[checkinstanz1]
            if checkinstanz2 == pwd:
                return True

        except:
            pass

        # print(usern)
        # print(pwd)
        # print(checkinstanz1)
        # print(checkinstanz2)


def loggedIn():
    global status, loggedIn, img1, img2
    if status != "login":
        return
    status = "loggedIn"
    loggedIn = tk.Toplevel(loginSystem)
    loggedIn.title('logged In')
    loggedIn.geometry("280x280+1800+200")  # großer Monitor
    # loggedIn.geometry("280x480+100+0") # kleiner Monitor

    rahmenreihe = tk.Frame(loggedIn)
    rahmenreihe.pack()
    tk.Button(loggedIn, text="Zurück", command=quitloggedIn).pack(
        side="left", anchor="nw", padx=5, pady=5)

    img1 = PhotoImage(file="img_beer.png")

    lb1 = tk.Label(loggedIn, image=img1)
    lb1.pack(padx=5, pady=5)
    lb2 = tk.Label(loggedIn, font="Helvetica 16 bold",
                   fg="#09750b", text="You Are Logged In")  # grün
    lb2.pack(padx=5, pady=5)


def checkUSER_PWD():
    if status == "login":
        usern = eingabeUsername.get()                       # hole Username
        pwd = eingabePasswort.get()                         # hole Passwort

        if usern == "":
            tk.messagebox.showerror(title="Login", message="Username fehlt!")
        else:
            if pwd == "":
                tk.messagebox.showerror(
                    title="Login", message="Passwort fehlt!")
            else:
                if checkUsername == True:
                    tk.messagebox.showerror(
                        title="Login", message="Username und Passwort stimmen nicht überein!")
                else:
                    if checkPWD == True:
                        tk.messagebox.showerror(
                            title="Login", message="Username und Passwort stimmen nicht überein!")
                    else:
                        if pwdUsernVergl() == True:
                            disableEntries()
                            loggedIn()
                            enterLogin()
                        else:
                            tk.messagebox.showerror(
                                title="Login", message="Username und Passwort stimmen nicht überein!")


def countRows():
    with open("pf_otpr_login_system.csv") as csv:
        nRows = sum(1 for row in csv)


def disableEntries():
    eingabeUsername.config(state='disabled')
    eingabePasswort.config(state='disabled')


def enableEntries():
    eingabeUsername.config(state='normal')
    eingabePasswort.config(state='normal')


def register():
    global status, registry, regUsername, regPassword, regPassword2, labelErfolg
    disableEntries()
    if status != "login":
        return
    status = "registry"
    registry = tk.Toplevel(loginSystem)
    registry.title('Registrierung')
    registry.geometry("260x210+1800+200")  # großer Monitor
    # registry.geometry("260x210+100+0") # kleiner Monitor

    rahmenreiheREG1 = tk.Frame(registry)
    rahmenreiheREG2 = tk.Frame(registry)
    rahmenreiheREG3 = tk.Frame(registry)
    rahmenreiheREG4 = tk.Frame(registry)
    rahmenreiheREG5 = tk.Frame(registry)
    rahmenreiheREG6 = tk.Frame(registry)

    rahmenreiheREG1.pack(ipady=5)
    rahmenreiheREG2.pack(ipady=5)
    rahmenreiheREG3.pack(ipady=5)
    rahmenreiheREG4.pack(ipady=5)
    rahmenreiheREG5.pack(ipady=5)
    rahmenreiheREG6.pack(ipady=5)

    tk.Button(rahmenreiheREG1, text="Zurück",
              command=quitRegister).pack(side="left")

    regUsername = tk.Entry(rahmenreiheREG2)
    regUsername.pack(side="right")
    tk.Label(rahmenreiheREG2, text='Username:').pack(side='right')

    regPassword = tk.Entry(rahmenreiheREG3)
    regPassword.pack(side="right")
    tk.Label(rahmenreiheREG3, text='Passwort:').pack(side='right')

    regPassword2 = tk.Entry(rahmenreiheREG4)
    regPassword2.pack(side="right")
    tk.Label(rahmenreiheREG4, text='Passwort wiederholen:').pack(side='right')

    tk.Button(rahmenreiheREG5, text="Register",
              command=enterRegistry).pack(side="left")

    labelErfolg = tk.Label(rahmenreiheREG6, font="Times 10 bold",
                           text='Sie wurden erfolgreich registriert :D', fg="#29d40f")


def quitRegister():
    global status
    registry.destroy()
    status = "login"
    enableEntries()


def checkRegUsername():
    # ertselle data Liste (leer)
    data = []
    import csv
    with open("pf_otpr_login_system.csv") as csvfile:   # öffne csv anschließend VAR csvfile
        reader = csv.reader(csvfile)                    #
        for row in reader:
            data.append(row)
    # suche in 3. Tabelle = User
    col = [x[3] for x in data]
    if ruser in col:
        for x in range(0, len(data)):
            if ruser == data[x][3]:
                return True


def enterRegistry():
    global ruser
    status = "registry"
    csv = open("pf_otpr_login_system.csv", "a")
    datum = datetime.today().strftime('%Y.%m.%d')
    uhrzeit = datetime.now().strftime("%H:%M:%S")
    komma = ","
    nLine = "\n"
    ruser = regUsername.get()
    rpw = regPassword.get()
    rpw2 = regPassword2.get()

    if ruser == "":
        tk.messagebox.showinfo(title="Registrierung",
                               message="Bitte geben Sie einen Nutzernamen ein!")
    else:
        if checkRegUsername() == True:
            tk.messagebox.showerror(
                title="Registrierung", message="Leider ist der Nutzername bereits vergeben!")
        else:
            if rpw == "":
                tk.messagebox.showinfo(
                    title="Registrierung", message="Bitte geben Sie das Passwort ein das Sie verwenden möchten!")
            else:
                if rpw2 == "":
                    tk.messagebox.showinfo(
                        title="Registrierung", message="Bitte wiederholen Sie die Passworteingabe!")
                else:
                    if rpw != rpw2:
                        tk.messagebox.showerror(
                            title="Registrierung", message="Passwörter stimmen nicht überein!")
                    else:
                        # csv.write("Datum,Uhrzeit,Event,Username,Passwort\n")
                        csv.write(datum)
                        csv.write(komma)
                        csv.write(uhrzeit)
                        csv.write(komma)
                        csv.write("Registrierung")
                        csv.write(komma)
                        csv.write(ruser)
                        csv.write(komma)
                        csv.write(rpw)
                        csv.write(nLine)
                        labelErfolg.pack(side='bottom')

    csv.close()


def enterLogin():
    status = "loggedIn"
    csv = open("pf_otpr_login_system.csv", "a")
    datum = datetime.today().strftime('%Y.%m.%d')
    uhrzeit = datetime.now().strftime("%H:%M:%S")
    komma = ","
    nLine = "\n"
    usern = eingabeUsername.get()                       # hole Username
    csv.write(datum)
    csv.write(komma)
    csv.write(uhrzeit)
    csv.write(komma)
    csv.write("loggedIn")
    csv.write(komma)
    csv.write(usern)
    csv.write(komma)
    csv.write("loggedIn")
    csv.write(nLine)

def quitloggedIn():
    global status
    loggedIn.destroy()
    status = "login"
    enableEntries()
    csv = open("pf_otpr_login_system.csv", "a")
    datum = datetime.today().strftime('%Y.%m.%d')
    uhrzeit = datetime.now().strftime("%H:%M:%S")
    komma = ","
    nLine = "\n"
    usern = eingabeUsername.get()                       # hole Username
    csv.write(datum)
    csv.write(komma)
    csv.write(uhrzeit)
    csv.write(komma)
    csv.write("loggedOut")
    csv.write(komma)
    csv.write(usern)
    csv.write(komma)
    csv.write("loggedOut")
    csv.write(nLine)

def openCSV():
    os.startfile("pf_otpr_login_system.csv")

# Frame 1
rahmenreihe1 = tk.Frame(loginSystem)
rahmenreihe1.pack(fill='x', padx=10, ipady=10)

# Frame 2
rahmenreihe2 = tk.Frame(loginSystem)
rahmenreihe2.pack(fill='x', padx=10, ipady=10)

# Frame 3
rahmenreihe3 = tk.Frame(loginSystem)
rahmenreihe3.pack(fill='x', padx=10, ipady=10)

# Frame 4
rahmenreihe4 = tk.Frame(loginSystem)
rahmenreihe4.pack(fill='x', padx=10, ipady=10)

# Frame 5
rahmenreihe5 = tk.Frame(loginSystem)
rahmenreihe5.pack(fill='x', padx=10)

# Frame 6
rahmenreihe6 = tk.Frame(loginSystem)
rahmenreihe6.pack(fill='x', padx=10)

# Button Zurück
bback = tk.Button(rahmenreihe1, width=10, text="Zurück", command=back)
bback.pack(side="left", padx=10, pady=5)

# Button Neustart
brebootLoginSystem = tk.Button(
    rahmenreihe1, width=10, text="Neustart", command=rebootLoginSystem)
brebootLoginSystem.pack(side="left", padx=10, pady=5)

# Label 1 Username
labelUsername = tk.Label(rahmenreihe2, text='Username:')
labelUsername.pack(side='left')

# Eingabefeld 1 Username
eingabeUsername = tk.Entry(rahmenreihe2, width=20)
eingabeUsername.pack(side='left')

# Label 2 Passwort
labelPasswort = tk.Label(rahmenreihe3, text='Passwort:')
labelPasswort.pack(side='left')

# Eingabefeld 2 Passwort
eingabePasswort = tk.Entry(rahmenreihe3, width=20, show="*")
eingabePasswort.pack(side='left')

# Button Passwort überprüfung
bCheckPassword = tk.Button(
    rahmenreihe4, text="PasswordCheck", command=checkUSER_PWD)
bCheckPassword.pack(side="left", anchor="nw", padx=10, pady=5)

# Button Lösche Ausgabefeld
bdelete = tk.Button(rahmenreihe4, text='clear', command=deleteEntries)
bdelete.pack(side='left', anchor='nw', padx=10, pady=5)

# Button Testdat
btestDat = tk.Button(rahmenreihe4, text='Testdat', command=tesdat)
btestDat.pack(side='left', anchor='nw', padx=10, pady=5)

# Button Registrierung
bRegistrierung = tk.Button(
    rahmenreihe5, text='Registrierung', command=register)
bRegistrierung.pack(side='right', padx=10)

# Button Öffner CSV
bopenCSV = tk.Button(
    rahmenreihe5, fg="#169c21", font="Times 10 bold", text='CSV', command=openCSV)
bopenCSV.pack(side='right', padx=10)

# Label 2 Result
labelausgabe = tk.Label(rahmenreihe6, text="Result: ")
labelausgabe.pack(side="top")


loginSystem.mainloop()
