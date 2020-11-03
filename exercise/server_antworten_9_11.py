import urllib.request

# Eingabedaten
pnn = input("Bitte den Nachnamen eingeben: ")
pvn = input("Bitte den Vornamen eingeben: ")

# sendet Daten
u = urllib.request.urlopen("http://localhost/Projekte/Python/Sonstiges/Buch/server_antworten_9_11.php?nn="
                           + pnn + "&vn=" + pvn)

# Empfang der Antwort und Ausgabe
li = u.readlines()
u.close()
for element in li:
    print(element)
