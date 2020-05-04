import os
import time
# Informationstupel
tu = os.stat("obst_8_15.txt")
print()
print("Ausgangsdatensatz der Datei obst_8_15.txt: \n",tu)
print("\nEinzelne Elemente des Tupels aufgeschlüsselt: ")
# Elemente des Tupels
groesse = tu[6]
print("Byte: ", groesse)

zugr = time.localtime(tu[7])
print("Letzter Zugriff: ",
      time.strftime("%d.%m.%Y %H:%M:%S", zugr))

mod = time.localtime(tu[8])
print("Letzte Modifikation: ",
      time.strftime("%d.%m.%Y %H:%M:%S", mod))

