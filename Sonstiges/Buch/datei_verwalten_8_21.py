import sys
import shutil
import os
import glob

print(glob.glob("le*.txt"))

# Existenz feststellen
if not os.path.exists("lesen_8_4.txt"):
    print("Datei nicht vorhanden")
    sys.exist(0)

# Datei kopieren
shutil.copy("lesen_8_4.txt", "lesen_8_4_kopie.txt")
print(glob.glob("le*.txt"))

# Datei umbenennen
try:
    shutil.move("lesen_8_4_kopie.txt", "lesen_8_4_neu.txt")
except:
    print("Fehler beim Umbenennen")
print(glob.glob("le*.txt"))

# Datei entfernen
try:
    os.remove("lesen_8_4_neu.txt")
except:
    print("Fehler beim Entfernen")
print(glob.glob("le*.txt"))
