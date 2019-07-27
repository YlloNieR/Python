class Person:
    def __init__(self,surname,familyname,profession):
        self.surname = surname                  #Variable 1 Typ String
        self.familyname = familyname            #Variable 2 Typ String
        self.profession = profession            #Variable 3 Typ String
        self.skills = []                        #List
        self.car = ""                           #String
    
    def addSkill(self,skill):
        self.skills.append(skill)               #ermöglicht Skill add

p1 = Person("Eric","Bauer","engineer")
p2 = Person("Jane","Foster","manager")
p3 = Person("Birgit","UNKNOWN","homeless")
p4 = Person("Tyler","Durden","bare knuckle fighter")


print(p1.surname + " is an " + p1.profession)
print(p2.surname)

p1.addSkill("solve math problems")              #added skill
p1.addSkill("designs progress programs")
p2.addSkill("balance a budget")

print(p1.skills)
print(p2.skills)

p2.car = "Tesla"

print(p2.car)
print(p1.car)
