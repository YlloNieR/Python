import tkinter
import numpy as np
from tkinter import *       # erstelle Bilddatei und verkleinere


main = tkinter.Tk()
main.title("Sodoku Solver")
# Breite 1000x Höhe 400+ X 1200+ Y 200
main.geometry("350x310+1800+200")  # großer Monitor
# main.geometry("350x310+100+0") # kleiner Monitor


# Funktionen----Beginn-----
def back():
    main.destroy()
    import pf_main_window


def testergebnisse():
    z1.insert(0, 9)
    z2.insert(0, 6)
    z3.insert(0, 0)
    z4.insert(0, 0)
    z5.insert(0, 8)
    z6.insert(0, 0)
    z7.insert(0, 0)
    z8.insert(0, 7)
    z9.insert(0, 0)
    z10.insert(0, 3)
    z11.insert(0, 1)
    z12.insert(0, 0)
    z13.insert(0, 0)
    z14.insert(0, 0)
    z15.insert(0, 4)
    z16.insert(0, 0)
    z17.insert(0, 0)
    z18.insert(0, 5)
    z19.insert(0, 0)
    z20.insert(0, 0)
    z21.insert(0, 5)
    z22.insert(0, 0)
    z23.insert(0, 0)
    z24.insert(0, 0)
    z25.insert(0, 0)
    z26.insert(0, 0)
    z27.insert(0, 0)
    z28.insert(0, 0)
    z29.insert(0, 0)
    z30.insert(0, 0)
    z31.insert(0, 0)
    z32.insert(0, 0)
    z33.insert(0, 2)
    z34.insert(0, 0)
    z35.insert(0, 8)
    z36.insert(0, 0)
    z37.insert(0, 5)
    z38.insert(0, 0)
    z39.insert(0, 0)
    z40.insert(0, 0)
    z41.insert(0, 1)
    z42.insert(0, 0)
    z43.insert(0, 0)
    z44.insert(0, 0)
    z45.insert(0, 2)
    z46.insert(0, 0)
    z47.insert(0, 7)
    z48.insert(0, 0)
    z49.insert(0, 5)
    z50.insert(0, 0)
    z51.insert(0, 0)
    z52.insert(0, 0)
    z53.insert(0, 0)
    z54.insert(0, 0)
    z55.insert(0, 0)
    z56.insert(0, 0)
    z57.insert(0, 0)
    z58.insert(0, 0)
    z59.insert(0, 0)
    z60.insert(0, 0)
    z61.insert(0, 4)
    z62.insert(0, 0)
    z63.insert(0, 0)
    z64.insert(0, 1)
    z65.insert(0, 0)
    z66.insert(0, 0)
    z67.insert(0, 6)
    z68.insert(0, 0)
    z69.insert(0, 0)
    z70.insert(0, 0)
    z71.insert(0, 3)
    z72.insert(0, 7)
    z73.insert(0, 0)
    z74.insert(0, 3)
    z75.insert(0, 0)
    z76.insert(0, 0)
    z77.insert(0, 9)
    z78.insert(0, 0)
    z79.insert(0, 0)
    z80.insert(0, 5)
    z81.insert(0, 6)


def zellenleeren():
    z1.delete(first=0, last=10)
    z2.delete(first=0, last=10)
    z3.delete(first=0, last=10)
    z4.delete(first=0, last=10)
    z5.delete(first=0, last=10)
    z6.delete(first=0, last=10)
    z7.delete(first=0, last=10)
    z8.delete(first=0, last=10)
    z9.delete(first=0, last=10)
    z10.delete(first=0, last=10)
    z11.delete(first=0, last=10)
    z12.delete(first=0, last=10)
    z13.delete(first=0, last=10)
    z14.delete(first=0, last=10)
    z15.delete(first=0, last=10)
    z16.delete(first=0, last=10)
    z17.delete(first=0, last=10)
    z18.delete(first=0, last=10)
    z19.delete(first=0, last=10)
    z20.delete(first=0, last=10)
    z21.delete(first=0, last=10)
    z22.delete(first=0, last=10)
    z23.delete(first=0, last=10)
    z24.delete(first=0, last=10)
    z25.delete(first=0, last=10)
    z26.delete(first=0, last=10)
    z27.delete(first=0, last=10)
    z28.delete(first=0, last=10)
    z29.delete(first=0, last=10)
    z30.delete(first=0, last=10)
    z31.delete(first=0, last=10)
    z32.delete(first=0, last=10)
    z33.delete(first=0, last=10)
    z34.delete(first=0, last=10)
    z35.delete(first=0, last=10)
    z36.delete(first=0, last=10)
    z37.delete(first=0, last=10)
    z38.delete(first=0, last=10)
    z39.delete(first=0, last=10)
    z40.delete(first=0, last=10)
    z41.delete(first=0, last=10)
    z42.delete(first=0, last=10)
    z43.delete(first=0, last=10)
    z44.delete(first=0, last=10)
    z45.delete(first=0, last=10)
    z46.delete(first=0, last=10)
    z47.delete(first=0, last=10)
    z48.delete(first=0, last=10)
    z49.delete(first=0, last=10)
    z50.delete(first=0, last=10)
    z51.delete(first=0, last=10)
    z52.delete(first=0, last=10)
    z53.delete(first=0, last=10)
    z54.delete(first=0, last=10)
    z55.delete(first=0, last=10)
    z56.delete(first=0, last=10)
    z57.delete(first=0, last=10)
    z58.delete(first=0, last=10)
    z59.delete(first=0, last=10)
    z60.delete(first=0, last=10)
    z61.delete(first=0, last=10)
    z62.delete(first=0, last=10)
    z63.delete(first=0, last=10)
    z64.delete(first=0, last=10)
    z65.delete(first=0, last=10)
    z66.delete(first=0, last=10)
    z67.delete(first=0, last=10)
    z68.delete(first=0, last=10)
    z69.delete(first=0, last=10)
    z70.delete(first=0, last=10)
    z71.delete(first=0, last=10)
    z72.delete(first=0, last=10)
    z73.delete(first=0, last=10)
    z74.delete(first=0, last=10)
    z75.delete(first=0, last=10)
    z76.delete(first=0, last=10)
    z77.delete(first=0, last=10)
    z78.delete(first=0, last=10)
    z79.delete(first=0, last=10)
    z80.delete(first=0, last=10)
    z81.delete(first=0, last=10)
    ergebnisausgabereihe1.delete(first=0, last=100)
    ergebnisausgabereihe2.delete(first=0, last=100)
    ergebnisausgabereihe3.delete(first=0, last=100)
    ergebnisausgabereihe4.delete(first=0, last=100)
    ergebnisausgabereihe5.delete(first=0, last=100)
    ergebnisausgabereihe6.delete(first=0, last=100)
    ergebnisausgabereihe7.delete(first=0, last=100)
    ergebnisausgabereihe8.delete(first=0, last=100)
    ergebnisausgabereihe9.delete(first=0, last=100)


def nullsetztenwennleer():
    # 1. Reihe
    if len(z1.get()) == 0:
        z1.delete(0, tkinter.END)
        z1.insert(0, 0)
    if len(z2.get()) == 0:
        z2.delete(0, tkinter.END)
        z2.insert(0, 0)
    if len(z3.get()) == 0:
        z3.delete(0, tkinter.END)
        z3.insert(0, 0)
    if len(z4.get()) == 0:
        z4.delete(0, tkinter.END)
        z4.insert(0, 0)
    if len(z5.get()) == 0:
        z5.delete(0, tkinter.END)
        z5.insert(0, 0)
    if len(z6.get()) == 0:
        z6.delete(0, tkinter.END)
        z6.insert(0, 0)
    if len(z7.get()) == 0:
        z7.delete(0, tkinter.END)
        z7.insert(0, 0)
    if len(z8.get()) == 0:
        z8.delete(0, tkinter.END)
        z8.insert(0, 0)
    if len(z9.get()) == 0:
        z9.delete(0, tkinter.END)
        z9.insert(0, 0)

    # 2. Reihe
    if len(z10.get()) == 0:
        z10.delete(0, tkinter.END)
        z10.insert(0, 0)
    if len(z11.get()) == 0:
        z11.delete(0, tkinter.END)
        z11.insert(0, 0)
    if len(z12.get()) == 0:
        z12.delete(0, tkinter.END)
        z12.insert(0, 0)
    if len(z13.get()) == 0:
        z13.delete(0, tkinter.END)
        z13.insert(0, 0)
    if len(z14.get()) == 0:
        z14.delete(0, tkinter.END)
        z14.insert(0, 0)
    if len(z15.get()) == 0:
        z15.delete(0, tkinter.END)
        z15.insert(0, 0)
    if len(z16.get()) == 0:
        z16.delete(0, tkinter.END)
        z16.insert(0, 0)
    if len(z17.get()) == 0:
        z17.delete(0, tkinter.END)
        z17.insert(0, 0)
    if len(z18.get()) == 0:
        z18.delete(0, tkinter.END)
        z18.insert(0, 0)

    # 3. Reihe
    if len(z19.get()) == 0:
        z19.delete(0, tkinter.END)
        z19.insert(0, 0)
    if len(z20.get()) == 0:
        z20.delete(0, tkinter.END)
        z20.insert(0, 0)
    if len(z21.get()) == 0:
        z21.delete(0, tkinter.END)
        z21.insert(0, 0)
    if len(z22.get()) == 0:
        z22.delete(0, tkinter.END)
        z22.insert(0, 0)
    if len(z23.get()) == 0:
        z23.delete(0, tkinter.END)
        z23.insert(0, 0)
    if len(z24.get()) == 0:
        z24.delete(0, tkinter.END)
        z24.insert(0, 0)
    if len(z25.get()) == 0:
        z25.delete(0, tkinter.END)
        z25.insert(0, 0)
    if len(z26.get()) == 0:
        z26.delete(0, tkinter.END)
        z26.insert(0, 0)
    if len(z27.get()) == 0:
        z27.delete(0, tkinter.END)
        z27.insert(0, 0)

    # 4. Reihe
    if len(z28.get()) == 0:
        z28.delete(0, tkinter.END)
        z28.insert(0, 0)
    if len(z29.get()) == 0:
        z29.delete(0, tkinter.END)
        z29.insert(0, 0)
    if len(z30.get()) == 0:
        z30.delete(0, tkinter.END)
        z30.insert(0, 0)
    if len(z31.get()) == 0:
        z31.delete(0, tkinter.END)
        z31.insert(0, 0)
    if len(z32.get()) == 0:
        z32.delete(0, tkinter.END)
        z32.insert(0, 0)
    if len(z33.get()) == 0:
        z33.delete(0, tkinter.END)
        z33.insert(0, 0)
    if len(z34.get()) == 0:
        z34.delete(0, tkinter.END)
        z34.insert(0, 0)
    if len(z35.get()) == 0:
        z35.delete(0, tkinter.END)
        z35.insert(0, 0)
    if len(z36.get()) == 0:
        z36.delete(0, tkinter.END)
        z36.insert(0, 0)

    # 5. Reihe
    if len(z37.get()) == 0:
        z37.delete(0, tkinter.END)
        z37.insert(0, 0)
    if len(z38.get()) == 0:
        z38.delete(0, tkinter.END)
        z38.insert(0, 0)
    if len(z39.get()) == 0:
        z39.delete(0, tkinter.END)
        z39.insert(0, 0)
    if len(z40.get()) == 0:
        z40.delete(0, tkinter.END)
        z40.insert(0, 0)
    if len(z41.get()) == 0:
        z41.delete(0, tkinter.END)
        z41.insert(0, 0)
    if len(z42.get()) == 0:
        z42.delete(0, tkinter.END)
        z42.insert(0, 0)
    if len(z43.get()) == 0:
        z43.delete(0, tkinter.END)
        z43.insert(0, 0)
    if len(z44.get()) == 0:
        z44.delete(0, tkinter.END)
        z44.insert(0, 0)
    if len(z45.get()) == 0:
        z45.delete(0, tkinter.END)
        z45.insert(0, 0)

    # 6. Reihe
    if len(z46.get()) == 0:
        z46.delete(0, tkinter.END)
        z46.insert(0, 0)
    if len(z47.get()) == 0:
        z47.delete(0, tkinter.END)
        z47.insert(0, 0)
    if len(z48.get()) == 0:
        z48.delete(0, tkinter.END)
        z48.insert(0, 0)
    if len(z49.get()) == 0:
        z49.delete(0, tkinter.END)
        z49.insert(0, 0)
    if len(z50.get()) == 0:
        z50.delete(0, tkinter.END)
        z50.insert(0, 0)
    if len(z51.get()) == 0:
        z51.delete(0, tkinter.END)
        z51.insert(0, 0)
    if len(z52.get()) == 0:
        z52.delete(0, tkinter.END)
        z52.insert(0, 0)
    if len(z53.get()) == 0:
        z53.delete(0, tkinter.END)
        z53.insert(0, 0)
    if len(z54.get()) == 0:
        z54.delete(0, tkinter.END)
        z54.insert(0, 0)

    # 7. Reihe
    if len(z55.get()) == 0:
        z55.delete(0, tkinter.END)
        z55.insert(0, 0)
    if len(z56.get()) == 0:
        z56.delete(0, tkinter.END)
        z56.insert(0, 0)
    if len(z57.get()) == 0:
        z57.delete(0, tkinter.END)
        z57.insert(0, 0)
    if len(z58.get()) == 0:
        z58.delete(0, tkinter.END)
        z58.insert(0, 0)
    if len(z59.get()) == 0:
        z59.delete(0, tkinter.END)
        z59.insert(0, 0)
    if len(z60.get()) == 0:
        z60.delete(0, tkinter.END)
        z60.insert(0, 0)
    if len(z61.get()) == 0:
        z61.delete(0, tkinter.END)
        z61.insert(0, 0)
    if len(z62.get()) == 0:
        z62.delete(0, tkinter.END)
        z62.insert(0, 0)
    if len(z63.get()) == 0:
        z63.delete(0, tkinter.END)
        z63.insert(0, 0)

    # 8. Reihe
    if len(z64.get()) == 0:
        z64.delete(0, tkinter.END)
        z64.insert(0, 0)
    if len(z65.get()) == 0:
        z65.delete(0, tkinter.END)
        z65.insert(0, 0)
    if len(z66.get()) == 0:
        z66.delete(0, tkinter.END)
        z66.insert(0, 0)
    if len(z67.get()) == 0:
        z67.delete(0, tkinter.END)
        z67.insert(0, 0)
    if len(z68.get()) == 0:
        z68.delete(0, tkinter.END)
        z68.insert(0, 0)
    if len(z69.get()) == 0:
        z69.delete(0, tkinter.END)
        z69.insert(0, 0)
    if len(z70.get()) == 0:
        z70.delete(0, tkinter.END)
        z70.insert(0, 0)
    if len(z71.get()) == 0:
        z71.delete(0, tkinter.END)
        z71.insert(0, 0)
    if len(z72.get()) == 0:
        z72.delete(0, tkinter.END)
        z72.insert(0, 0)

    # 9. Reihe
    if len(z73.get()) == 0:
        z73.delete(0, tkinter.END)
        z73.insert(0, 0)
    if len(z74.get()) == 0:
        z74.delete(0, tkinter.END)
        z74.insert(0, 0)
    if len(z75.get()) == 0:
        z75.delete(0, tkinter.END)
        z75.insert(0, 0)
    if len(z76.get()) == 0:
        z76.delete(0, tkinter.END)
        z76.insert(0, 0)
    if len(z77.get()) == 0:
        z77.delete(0, tkinter.END)
        z77.insert(0, 0)
    if len(z78.get()) == 0:
        z78.delete(0, tkinter.END)
        z78.insert(0, 0)
    if len(z79.get()) == 0:
        z79.delete(0, tkinter.END)
        z79.insert(0, 0)
    if len(z80.get()) == 0:
        z80.delete(0, tkinter.END)
        z80.insert(0, 0)
    if len(z81.get()) == 0:
        z81.delete(0, tkinter.END)
        z81.insert(0, 0)

    anzeigen()


# kann nach test entfernt werden
def anzeigen():
    global grid

    grid = [[int(z1.get()),
             int(z2.get()),
             int(z3.get()),
             int(z4.get()),
             int(z5.get()),
             int(z6.get()),
             int(z7.get()),
             int(z8.get()),
             int(z9.get())], [
            int(z10.get()),
            int(z11.get()),
            int(z12.get()),
            int(z13.get()),
            int(z14.get()),
            int(z15.get()),
            int(z16.get()),
            int(z17.get()),
            int(z18.get())], [
            int(z19.get()),
            int(z20.get()),
            int(z21.get()),
            int(z22.get()),
            int(z23.get()),
            int(z24.get()),
            int(z25.get()),
            int(z26.get()),
            int(z27.get())], [
            int(z28.get()),
            int(z29.get()),
            int(z30.get()),
            int(z31.get()),
            int(z32.get()),
            int(z33.get()),
            int(z34.get()),
            int(z35.get()),
            int(z36.get())], [
            int(z37.get()),
            int(z38.get()),
            int(z39.get()),
            int(z40.get()),
            int(z41.get()),
            int(z42.get()),
            int(z43.get()),
            int(z44.get()),
            int(z45.get())], [
            int(z46.get()),
            int(z47.get()),
            int(z48.get()),
            int(z49.get()),
            int(z50.get()),
            int(z51.get()),
            int(z52.get()),
            int(z53.get()),
            int(z54.get())], [
            int(z55.get()),
            int(z56.get()),
            int(z57.get()),
            int(z58.get()),
            int(z59.get()),
            int(z60.get()),
            int(z61.get()),
            int(z62.get()),
            int(z63.get())], [
            int(z64.get()),
            int(z65.get()),
            int(z66.get()),
            int(z67.get()),
            int(z68.get()),
            int(z69.get()),
            int(z70.get()),
            int(z71.get()),
            int(z72.get())], [
            int(z73.get()),
            int(z74.get()),
            int(z75.get()),
            int(z76.get()),
            int(z77.get()),
            int(z78.get()),
            int(z79.get()),
            int(z80.get()),
            int(z81.get())]]

    solve()


def possible(y, x, n):
    global grid
    for i in range(0, 9):
        if grid[y][i] == n:
            return False
    for i in range(0, 9):
        if grid[i][x] == n:
            return False

    x0 = (x//3)*3
    y0 = (y//3)*3

    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0+i][x0+j] == n:
                return False
    return True


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return

    ergebnisausgabereihe1.insert(1, grid[0:1])
    ergebnisausgabereihe2.insert(1, grid[1:2])
    ergebnisausgabereihe3.insert(1, grid[2:3])
    ergebnisausgabereihe4.insert(1, grid[3:4])
    ergebnisausgabereihe5.insert(1, grid[4:5])
    ergebnisausgabereihe6.insert(1, grid[5:6])
    ergebnisausgabereihe7.insert(1, grid[6:7])
    ergebnisausgabereihe8.insert(1, grid[7:8])
    ergebnisausgabereihe9.insert(1, grid[8:9])

    input("More?")


# Funktionen----Ende-----
# 1. Reihe
z1 = tkinter.Entry(width=2)
z2 = tkinter.Entry(width=2)
z3 = tkinter.Entry(width=2)
z4 = tkinter.Entry(width=2)
z5 = tkinter.Entry(width=2)
z6 = tkinter.Entry(width=2)
z7 = tkinter.Entry(width=2)
z8 = tkinter.Entry(width=2)
z9 = tkinter.Entry(width=2)

z1.grid(row=1, column=1)
z2.grid(row=1, column=2)
z3.grid(row=1, column=3)
z4.grid(row=1, column=4)
z5.grid(row=1, column=5)
z6.grid(row=1, column=6)
z7.grid(row=1, column=7)
z8.grid(row=1, column=8)
z9.grid(row=1, column=9)

# 2. Reihe
z10 = tkinter.Entry(width=2)
z11 = tkinter.Entry(width=2)
z12 = tkinter.Entry(width=2)
z13 = tkinter.Entry(width=2)
z14 = tkinter.Entry(width=2)
z15 = tkinter.Entry(width=2)
z16 = tkinter.Entry(width=2)
z17 = tkinter.Entry(width=2)
z18 = tkinter.Entry(width=2)

z10.grid(row=2, column=1)
z11.grid(row=2, column=2)
z12.grid(row=2, column=3)
z13.grid(row=2, column=4)
z14.grid(row=2, column=5)
z15.grid(row=2, column=6)
z16.grid(row=2, column=7)
z17.grid(row=2, column=8)
z18.grid(row=2, column=9)

# 3. Reihe
z19 = tkinter.Entry(width=2)
z20 = tkinter.Entry(width=2)
z21 = tkinter.Entry(width=2)
z22 = tkinter.Entry(width=2)
z23 = tkinter.Entry(width=2)
z24 = tkinter.Entry(width=2)
z25 = tkinter.Entry(width=2)
z26 = tkinter.Entry(width=2)
z27 = tkinter.Entry(width=2)

z19.grid(row=3, column=1)
z20.grid(row=3, column=2)
z21.grid(row=3, column=3)
z22.grid(row=3, column=4)
z23.grid(row=3, column=5)
z24.grid(row=3, column=6)
z25.grid(row=3, column=7)
z26.grid(row=3, column=8)
z27.grid(row=3, column=9)

# 4. Reihe
z28 = tkinter.Entry(width=2)
z29 = tkinter.Entry(width=2)
z30 = tkinter.Entry(width=2)
z31 = tkinter.Entry(width=2)
z32 = tkinter.Entry(width=2)
z33 = tkinter.Entry(width=2)
z34 = tkinter.Entry(width=2)
z35 = tkinter.Entry(width=2)
z36 = tkinter.Entry(width=2)

z28.grid(row=4, column=1)
z29.grid(row=4, column=2)
z30.grid(row=4, column=3)
z31.grid(row=4, column=4)
z32.grid(row=4, column=5)
z33.grid(row=4, column=6)
z34.grid(row=4, column=7)
z35.grid(row=4, column=8)
z36.grid(row=4, column=9)

# 5. Reihe
z37 = tkinter.Entry(width=2)
z38 = tkinter.Entry(width=2)
z39 = tkinter.Entry(width=2)
z40 = tkinter.Entry(width=2)
z41 = tkinter.Entry(width=2)
z42 = tkinter.Entry(width=2)
z43 = tkinter.Entry(width=2)
z44 = tkinter.Entry(width=2)
z45 = tkinter.Entry(width=2)

z37.grid(row=5, column=1)
z38.grid(row=5, column=2)
z39.grid(row=5, column=3)
z40.grid(row=5, column=4)
z41.grid(row=5, column=5)
z42.grid(row=5, column=6)
z43.grid(row=5, column=7)
z44.grid(row=5, column=8)
z45.grid(row=5, column=9)

# 6. Reihe
z46 = tkinter.Entry(width=2)
z47 = tkinter.Entry(width=2)
z48 = tkinter.Entry(width=2)
z49 = tkinter.Entry(width=2)
z50 = tkinter.Entry(width=2)
z51 = tkinter.Entry(width=2)
z52 = tkinter.Entry(width=2)
z53 = tkinter.Entry(width=2)
z54 = tkinter.Entry(width=2)

z46.grid(row=6, column=1)
z47.grid(row=6, column=2)
z48.grid(row=6, column=3)
z49.grid(row=6, column=4)
z50.grid(row=6, column=5)
z51.grid(row=6, column=6)
z52.grid(row=6, column=7)
z53.grid(row=6, column=8)
z54.grid(row=6, column=9)

# 7. Reihe
z55 = tkinter.Entry(width=2)
z56 = tkinter.Entry(width=2)
z57 = tkinter.Entry(width=2)
z58 = tkinter.Entry(width=2)
z59 = tkinter.Entry(width=2)
z60 = tkinter.Entry(width=2)
z61 = tkinter.Entry(width=2)
z62 = tkinter.Entry(width=2)
z63 = tkinter.Entry(width=2)

z55.grid(row=7, column=1)
z56.grid(row=7, column=2)
z57.grid(row=7, column=3)
z58.grid(row=7, column=4)
z59.grid(row=7, column=5)
z60.grid(row=7, column=6)
z61.grid(row=7, column=7)
z62.grid(row=7, column=8)
z63.grid(row=7, column=9)

# 8. Reihe
z64 = tkinter.Entry(width=2)
z65 = tkinter.Entry(width=2)
z66 = tkinter.Entry(width=2)
z67 = tkinter.Entry(width=2)
z68 = tkinter.Entry(width=2)
z69 = tkinter.Entry(width=2)
z70 = tkinter.Entry(width=2)
z71 = tkinter.Entry(width=2)
z72 = tkinter.Entry(width=2)

z64.grid(row=8, column=1)
z65.grid(row=8, column=2)
z66.grid(row=8, column=3)
z67.grid(row=8, column=4)
z68.grid(row=8, column=5)
z69.grid(row=8, column=6)
z70.grid(row=8, column=7)
z71.grid(row=8, column=8)
z72.grid(row=8, column=9)

# 9. Reihe
z73 = tkinter.Entry(width=2)
z74 = tkinter.Entry(width=2)
z75 = tkinter.Entry(width=2)
z76 = tkinter.Entry(width=2)
z77 = tkinter.Entry(width=2)
z78 = tkinter.Entry(width=2)
z79 = tkinter.Entry(width=2)
z80 = tkinter.Entry(width=2)
z81 = tkinter.Entry(width=2)

z73.grid(row=9, column=1)
z74.grid(row=9, column=2)
z75.grid(row=9, column=3)
z76.grid(row=9, column=4)
z77.grid(row=9, column=5)
z78.grid(row=9, column=6)
z79.grid(row=9, column=7)
z80.grid(row=9, column=8)
z81.grid(row=9, column=9)

# Ergebnisreihen
ergebnisausgabereihe1 = tkinter.Entry(main, width=15)
ergebnisausgabereihe2 = tkinter.Entry(main, width=15)
ergebnisausgabereihe3 = tkinter.Entry(main, width=15)
ergebnisausgabereihe4 = tkinter.Entry(main, width=15)
ergebnisausgabereihe5 = tkinter.Entry(main, width=15)
ergebnisausgabereihe6 = tkinter.Entry(main, width=15)
ergebnisausgabereihe7 = tkinter.Entry(main, width=15)
ergebnisausgabereihe8 = tkinter.Entry(main, width=15)
ergebnisausgabereihe9 = tkinter.Entry(main, width=15)

ergebnisausgabereihe1.grid(row=1, column=11)
ergebnisausgabereihe2.grid(row=2, column=11)
ergebnisausgabereihe3.grid(row=3, column=11)
ergebnisausgabereihe4.grid(row=4, column=11)
ergebnisausgabereihe5.grid(row=5, column=11)
ergebnisausgabereihe6.grid(row=6, column=11)
ergebnisausgabereihe7.grid(row=7, column=11)
ergebnisausgabereihe8.grid(row=8, column=11)
ergebnisausgabereihe9.grid(row=9, column=11)

# Schaltfläche Zurück
bback = tkinter.Button(main, text="Zurück", font='Helvetica 9 bold',
                       compound=CENTER, command=back)
bback.grid(row=0, column=10)

# Label über Gitter
lb2 = tkinter.Label(main, text="Ergebnis:", font='Helvetica 11 bold')
lb2.grid(row=0, column=11, columnspan=1)

# erstelle Bilddatei und verkleinere
img_check = PhotoImage(
    file=r"C:\xampp\htdocs\Projekte\Python\Sonstiges\img-check.png")
img_check_resized = img_check.subsample(40, 40)
img_test = PhotoImage(
    file=r"C:\xampp\htdocs\Projekte\Python\Sonstiges\img-test.png")
img_test_resized = img_test.subsample(10, 10)
img_erase = PhotoImage(
    file=r"C:\xampp\htdocs\Projekte\Python\Sonstiges\img-erase.png")
img_erase_resized = img_erase.subsample(40, 40)

# Solve
btest = tkinter.Button(main, text='Solve', font='Helvetica 11 bold',
                       image=img_check_resized, compound=LEFT, command=nullsetztenwennleer)
btest.grid(row=10, column=10)


# Schaltfläche Testergebnisse
btest = tkinter.Button(main, text="Testergebnisse",
                       image=img_test_resized, compound=LEFT, command=testergebnisse)
btest.grid(row=11, column=10)

# Freifläche
lbfrei1 = tkinter.Label(main, text="")
lbfrei1.grid(row=12, column=2, columnspan=1)

# Schaltfläche Löschen
berase = tkinter.Button(main, text="Löschen", foreground="red", font='Helvetica 9 bold',
                        image=img_erase_resized, compound=LEFT, command=zellenleeren)
berase.grid(row=13, column=10)

# Freifläche
lbfrei2 = tkinter.Label(main, text="")
lbfrei2.grid(row=14, column=2, columnspan=1)


main.mainloop()
