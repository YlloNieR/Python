import tkinter as tk
import os
from datetime import datetime
import tkinter.messagebox
loginSystem = tk.Tk()
loginSystem.title('Login System')
loginSystem.geometry("280x280+1800+200")

status = "login"


def back():
    if status == "login":
        loginSystem.destroy()

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
        eingabeUsername.insert('end',"Admin")
        eingabePasswort.insert('end',"1234")

def checkPWD():
    if status == "login":
        usern = eingabeUsername.get()
        pwd = eingabePasswort.get()
        csv = open("pf_otpr_login_system.csv", "r")
        data =[]
        import csv
        with open("pf_otpr_login_system.csv") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
        #print(data)

        col = [x[3] for x in data]

        if usern in col:
            for x in range(0,len(data)):
                if usern == data[x][3]:
                    print(data[x])
        else:
            print("Name doesn't exist")

        
        labelausgabe = tk.Label(rahmenreihe6, text="asd") #lcsv[2]
        labelausgabe.pack(side="left")

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
    registry.geometry("260x210+1900+300")

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

    tk.Button(rahmenreiheREG1, text="Zurück", command=quitRegister).pack(side="left")
    
    regUsername = tk.Entry(rahmenreiheREG2)
    regUsername.pack(side="right")
    tk.Label(rahmenreiheREG2, text='Username:').pack(side='right')
    
    regPassword = tk.Entry(rahmenreiheREG3)
    regPassword.pack(side="right")
    tk.Label(rahmenreiheREG3, text='Passwort:').pack(side='right')

    regPassword2 = tk.Entry(rahmenreiheREG4)
    regPassword2.pack(side="right")
    tk.Label(rahmenreiheREG4, text='Passwort wiederholen:').pack(side='right')

    tk.Button(rahmenreiheREG5, text="Register", command=enterRegistry).pack(side="left")
    
    labelErfolg = tk.Label(rahmenreiheREG6, font="Times 10 bold", text='Sie wurden erfolgreich registriert :D', fg="#29d40f")


def quitRegister():
    global status
    registry.destroy()
    status = "login"
    enableEntries()

def enterRegistry():
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
        tk.messagebox.showinfo(title="Registrierung",message="Bitte geben Sie einen Nutzernamen ein!")
    else:
        if rpw == "":
            tk.messagebox.showinfo(title="Registrierung",message="Bitte geben Sie das Passwort ein das Sie verwenden möchten!")
        else: 
            if rpw2 == "":
                tk.messagebox.showinfo(title="Registrierung",message="Bitte wiederholen Sie die Passworteingabe!")
            else:
                if rpw != rpw2:
                    tk.messagebox.showerror(title="Registrierung", message="Passwörter stimmen nicht überein!")        
                else:
                    #csv.write("Datum,Uhrzeit,Event,Username,Passwort\n")
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
brebootLoginSystem = tk.Button(rahmenreihe1, width=10, text="Neustart", command=rebootLoginSystem)
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
bCheckPassword = tk.Button(rahmenreihe4, text="PasswordCheck", command=checkPWD)
bCheckPassword.pack(side="left",anchor="nw", padx=10, pady=5)

# Button Lösche Ausgabefeld
bdelete = tk.Button(rahmenreihe4, text='clear', command=deleteEntries)
bdelete.pack(side='left', anchor='nw', padx=10, pady=5)

# Button Testdat
btestDat = tk.Button(rahmenreihe4, text='Testdat', command=tesdat)
btestDat.pack(side='left', anchor='nw', padx=10, pady=5)

# Button Registrierung
bRegistrierung = tk.Button(rahmenreihe5, text='Registrierung', command=register)
bRegistrierung.pack(side='right', padx=10)

# Label 2 Result
labelausgabe = tk.Label(rahmenreihe6, text="Result: ")
labelausgabe.pack(side="left")


loginSystem.mainloop()
