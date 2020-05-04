class MyClass:
    zahl = 42                       # nicht primitive Variablen
    string = "zeichenkette"         # nicht primitive Variablen
              # nicht primitive Variablen

    def __init__(self,buchstabenneu="a"):
        self.buchstabe = buchstabenneu
        self.string = "asd"
        self.liste = ["a","s","d"] 

    def do_something(self, neuezahl):
        self.zahl = neuezahl
        self.liste.append(neuezahl)

instanz1 = MyClass("a")
instanz2 = MyClass("b")

instanz1.do_something(123) # ändert Zahl von Instanz 1
print(MyClass().liste)
print()
print("Instanz 1")
print(instanz1.zahl)
print(instanz1.string)
print(instanz1.liste)
print()
print("Instanz 2")
print(instanz2.zahl)
print(instanz2.string)
print(instanz2.liste)