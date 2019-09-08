# Beispiel
test = "Das ist ein Beispielsatz; und so weiter"
print("Text: ", test)
print("")

# Beginn mit startswith, Ende mit endswith
print("startswith","endswith")
if test.startswith("Das"):
    print("Text beginnt mit Das")
if not test.endswith("Das"):
    print("Text endet nicht mit Das")
print("")

# Zerlegung in Tupel mit partition
print('test.partition("ei") sucht nach ei')
teile = test.partition("ei")
print("vor der 1. Teilung:", teile[0])
print('test.partition("ei") findet ei und gibt Text davor (entspricht 0) wieder als Tupel')
print("")
print("hinter der 1. Teilung:", teile[2])
print('test.partition("ei") findet ei und gibt Text danach (entspricht 2) wieder als Tupel')
print("")

teile = test.rpartition("ei")
print("vor der 2. Teilung:", teile[0])
print("hinter der 2. Teilung:", teile[2])
print("")

# Zerlegung in Liste mit split
print("test.split()")
wliste = test.split()

for i in range(0, 3):
    print("Element: ", i, wliste[i])

print("")

wliste2 = test.split(";")
print("Element: ", wliste2)

for i in range(0, 2):
    print("Element: ", i, wliste2[i])

