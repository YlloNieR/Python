for i in range (1,7):
    print("Zahl: ",i)
    if 3 <= i <= 5:
        continue                #unmittelbarer Abbruch des aktuellen Durchlaufs und setzt ihn mit dem nächsten fort, bis dieser fertig dann weiter mit ursprünglichem
    print("Quadrat: ", i*i)