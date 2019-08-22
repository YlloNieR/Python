x1 = input("x1 = ")
y1 = input("y1 = ")

def compare(x1,y1):
    if x1 > y1:
        return 1
    elif x1 == y1:
        return 0
    elif x1 < y1:
        return -1
 
print("Wenn compare(x1=" ,x1 ,",y1=" ,y1 ,") returns =",compare(x1,y1))