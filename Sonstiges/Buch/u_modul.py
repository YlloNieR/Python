import u_modul_finanz
print("Berechnung des monatlich zu zahlenden Steuerbetrages vom Bruttolohn")
steuerImport1 = u_modul_finanz.steuer(1800)
steuerImport2 = u_modul_finanz.steuer(2200)
steuerImport3 = u_modul_finanz.steuer(2500)
steuerImport4 = u_modul_finanz.steuer(2900)
steuerImportList = (steuerImport1, steuerImport2, steuerImport3, steuerImport4)

# Hauptprogramm
# Ausgabe
for bruttolohn in range(0, 4):
    print("Von", steuerImportList[bruttolohn][0], "EURO ergibt sich bei einem", steuerImportList[bruttolohn][1],
          "% -iger Versteuerung, ein Steuerbetrag in Höhe von", steuerImportList[bruttolohn][2], "EURO.")
