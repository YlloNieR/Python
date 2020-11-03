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
        

vererbteInstanz = dog() # weil dog = creature
print(creatures().eyes)
print(creatures().klasse)
print(creatures().eyes)
print()
print(dog().legs)
print(dog().name)
print(dog().eyes) # von creature
print()
print(vererbteInstanz.eyes)     # dog eyes = creature eyes = 2
print(vererbteInstanz.klasse)   
vererbteInstanz.add_number(42)  # dog > add_number > new_number = 42
print(vererbteInstanz.eyes) # gebe 42 aus
vererbteInstanz.look_number(42)  # dog > look_number > self.eyes = look_new_number 
print(vererbteInstanz.eyes)      # dog > look_number > self.eyes = look_new_number > self.live() > self.eyes = 24