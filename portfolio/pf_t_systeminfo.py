import sys
import tkinter as tk


def back():
    systeminfo.destroy()


def systeminfos():
    info1 = sys.argv
    info2 = sys.version
    info3 = sys.addaudithook
    info4 = sys.stdin
    info5 = sys.displayhook
    info6 = sys.stdout
    info7 = sys.stderr
    info8 = sys.platform
    
    lbanzeige = tk.Label(systeminfo, text="")
    lbanzeige.pack()
    
    lbanzeige = tk.Label(systeminfo, text="info1 = sys.argv")
    lbanzeige.pack()
    lbanzeige = tk.Label(systeminfo, text=info1)
    lbanzeige.pack()

    lbanzeige = tk.Label(systeminfo, text="")
    lbanzeige.pack()

    lbanzeige = tk.Label(systeminfo, text="info2 = sys.version")
    lbanzeige.pack()
    lbanzeige = tk.Label(systeminfo, text=info2)
    lbanzeige.pack()

    lbanzeige = tk.Label(systeminfo, text="")
    lbanzeige.pack()

    lbanzeige = tk.Label(systeminfo, text="info3 = sys.addaudithook")
    lbanzeige.pack()
    lbanzeige = tk.Label(systeminfo, text=info3)
    lbanzeige.pack()

    lbanzeige = tk.Label(systeminfo, text="")
    lbanzeige.pack()

    lbanzeige = tk.Label(systeminfo, text="info4 = sys.stdin")
    lbanzeige.pack()
    lbanzeige = tk.Label(systeminfo, text=info4)
    lbanzeige.pack()

    lbanzeige = tk.Label(systeminfo, text="")
    lbanzeige.pack()

    lbanzeige = tk.Label(systeminfo, text="info5 = sys.displayhook")
    lbanzeige.pack()
    lbanzeige = tk.Label(systeminfo, text=info5)
    lbanzeige.pack()

    lbanzeige = tk.Label(systeminfo, text="")
    lbanzeige.pack()

    lbanzeige = tk.Label(systeminfo, text="info6 = sys.stdout")
    lbanzeige.pack()
    lbanzeige = tk.Label(systeminfo, text=info6)
    lbanzeige.pack()

    lbanzeige = tk.Label(systeminfo, text="")
    lbanzeige.pack()

    lbanzeige = tk.Label(systeminfo, text="info7 = sys.stderr")
    lbanzeige.pack()
    lbanzeige = tk.Label(systeminfo, text=info7)
    lbanzeige.pack()

    lbanzeige = tk.Label(systeminfo, text="")
    lbanzeige.pack()

    lbanzeige = tk.Label(systeminfo, text="info8 = sys.platform")
    lbanzeige.pack()
    lbanzeige = tk.Label(systeminfo, text=info8)
    lbanzeige.pack()


systeminfo = tk.Tk()
systeminfo.title("Systeminfo")
systeminfo.geometry("600x800+1400+400")

# Anzeige Label
#lbanzeige = tk.Label(systeminfo, text="test\n info1 = sys.argv\n info2 = sys.version\n info3 = sys.addaudithook")
# lbanzeige.pack()

# Button Hauptfunktion
bsysteminfo = tk.Button(systeminfo, text="get Infos()", command=systeminfos)
bsysteminfo.pack()

# Button Zürück
bsysteminfo = tk.Button(systeminfo, text="Zurück", command=back)
bsysteminfo.pack()
