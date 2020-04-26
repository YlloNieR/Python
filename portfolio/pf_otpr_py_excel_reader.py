import tkinter as tk
import tkinter.messagebox
import os
import csv


pyExcelReader = tk.Tk()
pyExcelReader.title('Excel Reader')
pyExcelReader.geometry("450x400+1800+200")  # großer Monitor
# pyExcelReader.geometry("450x400+100+0") # kleiner Monitor


def back():
    pyExcelReader.destroy()
    os.system("pf_main_window.py")    # Startet neue Session


def rebootPyExRead():
    pyExcelReader.destroy()                  # Beendet jetzige Session
    os.system("pf_otpr_py_excel_reader.py")  # Startet neue Session


def emptyEntryField():
    eingabefeldVorname.delete(first=0, last=100)
    eingabefeldNachname.delete(first=0, last=100)
    eingabefeldWohnort.delete(first=0, last=100)


def newLabel():
    labelausgabe = tk.Label(rahmenreihe4, text='Result:')
    labelausgabe.pack(side='left')


def clearResult():
    ausgabefeld.delete(1.0, tk.END)
    ausgabefeld.insert('end', "Results: \n")


def testEntries():
    eingabefeldVorname.insert(0, "Torsten")
    eingabefeldNachname.insert(0, "Schmid")
    eingabefeldWohnort.insert(0, "Rodeck")


def accessTryCSV():
    try:
        csv = open("pf_otpr_py_excel_reader_file.csv")
        textYES = 'Dateizugriff erfolgreich!\n'
        ausgabefeld.insert('end', textYES)
    except:
        textNOT = 'Dateizugriff nicht erfolgreich!\n'
        ausgabefeld.insert('end', textNOT)


def writeCSV():
    csv = open("pf_otpr_py_excel_reader_file.csv",
               "a")  # a erweitern um Eintrag
    VornameCSV = eingabefeldVorname.get()
    NachnameCSV = eingabefeldNachname.get()
    WohnortCSV = eingabefeldWohnort.get()
    eckigeKlauf = "["
    eckigeKlzu = "]"
    apostroph = "'"
    komma = ","
    neueZeile = "\n"
    if VornameCSV == "":
        tkinter.messagebox.showinfo(
            "Hinweis zur Eingabe", "Eintrag in Vorname fehlt!")
        #textWHAT = 'Eintrag in Vorname fehlt!\n'
        #ausgabefeld.insert('end', textWHAT)
    else:
        if NachnameCSV == "":
            tkinter.messagebox.showinfo(
                "Hinweis zur Eingabe", "Eintrag in Nachname fehlt!")
            #textWHAT = 'Eintrag in Nachname fehlt!\n'
            #ausgabefeld.insert('end', textWHAT)
        else:
            if WohnortCSV == "":
                tkinter.messagebox.showinfo(
                    "Hinweis zur Eingabe", "Eintrag in Wohnort fehlt!")
                #textWHAT = 'Eintrag in Wohnort fehlt!\n'
                #ausgabefeld.insert('end', textWHAT)
            else:
                csv.write(eckigeKlauf)  # [
                csv.write(apostroph)  # '
                csv.write(VornameCSV)  # albert
                csv.write(apostroph)  # '
                csv.write(komma)  # ,
                csv.write(apostroph)  # '
                csv.write(NachnameCSV)  # einstein
                csv.write(apostroph)  # '
                csv.write(komma)  # ,
                csv.write(apostroph)  # '
                csv.write(WohnortCSV)  # Wien
                csv.write(apostroph)  # '
                csv.write(eckigeKlzu)  # ]
                csv.write(neueZeile)  # \n


def readCSV():
    #csv = open("pf_otpr_py_excel_reader_file.csv")
    #csvInhalt = csv.read()
    # csv.close()
    #ausgabefeld.insert('end', csvInhalt)
    with open('pf_otpr_py_excel_reader_file.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="'")

        for line in csv_reader:
            x = line[1], line[3], line[5]
            ausgabefeld.insert('end', "\n")
            ausgabefeld.insert('end', x)


def clearCSV():
    csv = open("pf_otpr_py_excel_reader_file.csv", "w")
    csv.write("['Vorname','Nachname','Wohnort']\n")
    csv.close()


def countRows():
    with open("pf_otpr_py_excel_reader_file.csv") as csv:
        nRows = sum(1 for row in csv)


def deleteLastEntry():
    import csv
    inputs = open("pf_otpr_py_excel_reader_file.csv")
    all_lines = inputs.readlines()
    all_lines.pop(len(all_lines)-1)
    inputs.close()

    with open("pf_otpr_py_excel_reader_file.csv", "w") as out:
        for line in all_lines:
            out.write(line.strip() + "\n")


# Frame 1
rahmenreihe1 = tk.Frame(pyExcelReader)
rahmenreihe1.pack(fill='x', padx=10, ipady=5)

# Frame 2
rahmenreihe2 = tk.Frame(pyExcelReader)
rahmenreihe2.pack(fill='x', padx=10, ipady=5)

# Frame 3
rahmenreihe3 = tk.Frame(pyExcelReader)
rahmenreihe3.pack(fill='x', padx=10, ipady=5)

# Frame 4
rahmenreihe4 = tk.Frame(pyExcelReader)
rahmenreihe4.pack(fill='x', padx=10, ipady=5)

# Frame 6 (wird von unten gezählt)
rahmenreihe6 = tk.Frame(pyExcelReader)
rahmenreihe6.pack(fill='x', side='bottom', anchor='w', padx=10, ipady=5)

# Frame 5 (wird von unten gezählt)
rahmenreihe5 = tk.Frame(pyExcelReader)
rahmenreihe5.pack(fill='x', side='bottom', anchor='w', padx=10, ipady=5)

# Button Zurück
bback = tk.Button(rahmenreihe1, width=10, text="Zurück", command=back)
bback.pack(side="left", padx=10, pady=5)

# Button Neustart
breboot = tk.Button(rahmenreihe1, width=10,
                    text="Neustart", command=rebootPyExRead)
breboot.pack(side="left", padx=10, pady=5)

# Label 1
labeleingabe = tk.Label(rahmenreihe2, text='Vorname:')
labeleingabe.pack(side='left', padx=10)

# Label 2
labeleingabe = tk.Label(rahmenreihe2, text='Nachname:')
labeleingabe.pack(side='left', padx=10)

# Label 3
labeleingabe = tk.Label(rahmenreihe2, text='Wohnort:')
labeleingabe.pack(side='left', padx=10)

# Eingabefeld 1
eingabefeldVorname = tk.Entry(rahmenreihe3, width=10)
eingabefeldVorname.pack(side='left', padx=10)

# Eingabefeld 2
eingabefeldNachname = tk.Entry(rahmenreihe3, width=10)
eingabefeldNachname.pack(side='left', padx=10)

# Eingabefeld 3
eingabefeldWohnort = tk.Entry(rahmenreihe3, width=10)
eingabefeldWohnort.pack(side='left', padx=10)

# Ausgabefeld 1
ausgabefeld = tk.Text(rahmenreihe4, width=50, height=13)
ausgabefeld.pack(side='left')
ausgabefeld.insert('end', "Results: \n")

# Button Lese csv
bclearResult = tk.Button(rahmenreihe5, fg="#c91c10",
                         text='clear Result', command=clearResult)
bclearResult.pack(side='left')

# Button Lese csv
breadCSV = tk.Button(rahmenreihe5, text='Lese csv', command=readCSV)
breadCSV.pack(side='left', padx=10)

# Button Access möglich
baccessCSV = tk.Button(rahmenreihe5, text='Access csv', command=accessTryCSV)
baccessCSV.pack(side='left', padx=10)

# Button Lösche Eingabefeld
bclearEntries = tk.Button(rahmenreihe6, fg="#c91c10",
                          text='clear Eingabe', command=emptyEntryField)
bclearEntries.pack(side='left', anchor='w', pady=5)

# Button Füge Testergebnisse ein
btestErg = tk.Button(rahmenreihe6, text='Test Eingabe',
                     command=testEntries)  
btestErg.pack(side='left', anchor='w', padx=10, pady=5)

# Button entferne aus csv
bdeletefromCSV = tk.Button(rahmenreihe6, fg="#c91c10", command=deleteLastEntry,
                           font="Times 10 bold", text='- csv')      # rot
bdeletefromCSV.pack(side='right', pady=5)

# Button Füge der CSV hinzu
bpasteToCSV = tk.Button(rahmenreihe6, fg="#169c21",
                        font="Times 10 bold", text='+ csv', command=writeCSV)  # grün
bpasteToCSV.pack(side='right', padx=10, pady=5)

# Button Lösche CSV
bclearCSV = tk.Button(rahmenreihe6, fg="#c91c10", font="Times 10 bold",
                      text='Clear CSV', command=clearCSV)  # grün
bclearCSV.pack(side='right', pady=5)


pyExcelReader.mainloop()
