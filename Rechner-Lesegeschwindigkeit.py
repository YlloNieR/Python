print("24 Kapitel")
KapitelJetz = input("Bitte gib an welches Kapitel du momentan liest = ")
import datetime
z = (datetime.date.today() - datetime.date(2019, 7, 23)).days
print("begonnen am 23.07.2019, vergangene Tage = ",z)
TageGelsen = input("Bitte gib an wieviele Tage du schon an diesem Buch gelesen hast ohne Pause = ")

KapitelGesamt = 24.0  
Rest = float(KapitelGesamt) - float(KapitelJetz)
LeseD = float(TageGelsen) / float(KapitelJetz)
RestZeitLese = float(LeseD) * float(Rest) 

print("Du hast noch ",float(Rest),"vor dir.")
print("Deine Durchschnittliche Lesegeschwindigkeit beträgt = ",float(LeseD),"pro Tag.")
print("Mit der jetzigen Lesegeschwindikeit brauchst du noch = ",float(RestZeitLese),"Tage.")