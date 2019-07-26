print('\n\t'"#     #                                         #######")                             
print('\t'"##   ##   ##   #####  ######    #####  #   #    #     # #      #      #    # #    #") 
print('\t'"# # # #  #  #  #    # #         #    #  # #     #     # #      #      #    # ##  ##") 
print('\t'"#  #  # #    # #    # #####     #####    #      #     # #      #      #    # # ## #") 
print('\t'"#     # ###### #    # #         #    #   #      #     # #      #      #    # #    #") 
print('\t'"#     # #    # #    # #         #    #   #      #     # #      #      #    # #    #") 
print('\t'"#     # #    # #####  ######    #####    #      ####### ###### ######  ####  #    #")
print('\n')
print('\n')   
import math
print(2*'\n',"Pythagorean theorem",'\n')

#Auswahlverfahren
choice = int(input("Bitte wähle aus: \n \tMöchtest du die Kathete A berechnen wähle die 1 \n Möchtest du die Kathete B berechnen wähle die 2 \n \tMöchtest du die Hypothenuse C berechnen wähle die 3 \n \t Möchtest du die Distanz Zweier Koordinaten berechnen wähle die 4 \n \t Deine Auswahl ist = "))

#Kathete a
def KatheteASeite():
    print(" \n Die Gleichung in Python sieht so aus: \n a = math.sqrt( ( c**2 - b**2) )")

    def KatheteA(c,b):
        ka = c**2 - b**2
        result = math.sqrt(ka)
        return result

    b = int(input("\n Die Kathe b = "))
    c = int(input("\n Die Hypothenuse c = "))

    print(" \n Die Kathete a ist bei einer Kathete b von",b,"und einer Hypothenuse von",c,"=",KatheteA(c,b))

#Kathete b
def KatheteBSeite():
    print(" \n Die Gleichung in Python sieht so aus: \n b = math.sqrt( ( c**2 - a**2) )")

    def KatheteB(c,a):
        kb = c**2 - a**2
        result = math.sqrt(kb)
        return result

    a = int(input("\n Die Kathe a = "))
    c = int(input("\n Die Hypothenuse c = "))

    print(" \n Die Kathete b ist bei einer Kathete a von",a,"und einer Hypothenuse von",c,"=",KatheteB(c,a))

#Hypotenuse c
def HypothenusenSeite():
    print(" \n Die Gleichung in Python sieht so aus: \n c = math.sqrt( ( a**2 + b**2) )")

    def HypotenuseC(a,b):
        hc = a**2 + b**2
        result = math.sqrt(hc)
        return result

    a = int(input("\n Die Kathe a = "))
    b = int(input("\n Die Kathe b = "))

    print(" \n Die Hypothenuse c ist bei einer Kathete a von",a,"und einer Kathete b von",b,"=",HypotenuseC(a,b))

#an example, suppose you want to find the distance between two points, given by the coordinates (x1, y1) and (x2, y2). By the Pythagorean theorem, the distance is:
def distanceXY():
    print(" \n Die Schritt für Schritt Gleichung in Python sieht so aus: \n Schritt 1 = math.sqrt( ( x2 - x1 )**(2)+( y2 - y1 )**(2) ) \n Schritt 2 = ( x2 - x1 = dx ) ( y2 - y1 = dy ) ) \n Schritt 3 = dx**2 + dy**2 ) ) \n Schritt 4 = math.sqrt(dsquard) )", 2*'\n')

    def distance(x1,y1,x2,y2):
        dx = x2 - x1
        dy = y2 - y1
        dsquard = dx**2 + dy**2
        result = math.sqrt(dsquard)
        return result

    x1 = int(input("\n Koordinate x1 = "))
    y1 = int(input("\n Koordinate y1 = "))
    x2 = int(input("\n Koordinate x2 = "))
    y2 = int(input("\n Koordinate y2 = "))

    print(" \n Die Distanz zwischen 2 Punkten", '\n',"Punkt( x1,y1 )","x1 =",x1,",","y1 =",y1,"und dem \n Punkt( x2,y2 )","x2 =",x2,",","y2 = ", y2 ,"beträgt =", distance(x1,y1,x2,y2))

if choice == 1:
    KatheteASeite()
elif choice == 2:
    KatheteBSeite()
elif choice == 3:
    HypothenusenSeite()
elif choice == 4:
    distanceXY()        

