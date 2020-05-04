class creatures:
    eyes = 2
    def __init__(self):
        self.klasse = "mammal"
    
    def live(self):
        self.eyes = 24

class dog(creatures):
    legs = 4
    name = "Basko"

    def __init__(self):
        creatures.__init__(self)    # constructor für zugang Oberklassse
        
    def add_number(self,new_number):
        self.eyes = new_number
    
    def look_number(self,look_new_number):
        self.eyes = look_new_number
        self.live()
        
    def live(self):
        creatures.live(self)        # es kann auf eyes Oberklasse zugegriffen werden
        self.legs = 43              # es wird auf legs hier zugegriffen
vererbteInstanz = dog() # weil dog = creature
vererbteInstanz.live()
print(vererbteInstanz.eyes)