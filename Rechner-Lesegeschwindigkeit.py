print('\n\t'"#     #                                         #######")                             
print('\t'"##   ##   ##   #####  ######    #####  #   #    #     # #      #      #    # #    #") 
print('\t'"# # # #  #  #  #    # #         #    #  # #     #     # #      #      #    # ##  ##") 
print('\t'"#  #  # #    # #    # #####     #####    #      #     # #      #      #    # # ## #") 
print('\t'"#     # ###### #    # #         #    #   #      #     # #      #      #    # #    #") 
print('\t'"#     # #    # #    # #         #    #   #      #     # #      #      #    # #    #") 
print('\t'"#     # #    # #####  ######    #####    #      ####### ###### ######  ####  #    #")
print('\n')
print('\n')
print("\n\n\t24 Kapitel & 228 Seiten")
KapitelJetz = input("\tBitte gib an welches Kapitel du momentan liest = ")
SeiteJetz = input("\tBitte gib an bei welcher Seite du momentan liest = ")
print("")

import datetime
z = (datetime.date.today() - datetime.date(2019, 7, 23)).days
print("\tbegonnen am 23.07.2019, vergangene Tage = ",z)
TageGelsen = input("\tBitte gib an wieviele Tage du schon an diesem Buch gelesen hast ohne Pause = ")

KapitelGesamt = 24.0  
SeitenGesamt = 228
Rest = float(KapitelGesamt) - float(KapitelJetz)
Rest2 = float(SeitenGesamt) - float(SeiteJetz)
LeseD = float(TageGelsen) / float(KapitelJetz)
RestZeitLese = float(LeseD) * float(Rest)
RestZeitLeseSeiten = float(LeseD) * float(Rest2)
UmrechnungInStunden = float(RestZeitLese)*24
UmrechnungInMinuten = float(UmrechnungInStunden)*60
print("")
print("\t Ergebnis")
print("_______________________________________\n")
print("\tDu hast noch ",int(Rest),"Kapitel vor dir.")
print("\tUnd noch ",int(Rest2),"Seiten.\n")
print("\tDeine Durchschnittliche Lesegeschwindigkeit beträgt = ",float(LeseD),"Kapitel pro Tag.")
print("\tMit der jetzigen Lesegeschwindikeit brauchst du noch =")
print("")
print("\t",float(RestZeitLese),"Tage")
print("\t",UmrechnungInStunden," Stunden")
print("\t",UmrechnungInMinuten," Minuten.")