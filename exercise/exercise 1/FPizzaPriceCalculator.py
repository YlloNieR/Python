emptyPizzaPrice = 6.50
pizzaToppingPrice = 0.50
tmp = 0
pizzaCount = 0
pizzaToppingCount = 0
endOption = 'y'

while endOption == 'y':
    pizzaCount += 1
    inp = input("How many pizza toppings do you want at this pizza?\n")   
    pizzaToppingCount = pizzaToppingCount + int(inp)
    calculatePrice = (int(inp) * pizzaToppingPrice) + emptyPizzaPrice

    tmp = tmp + calculatePrice
    print("Current costs for",pizzaCount,"pizzas and",pizzaToppingCount,"toppings:",tmp,"Euro",)
    inp2 = input("Do you want one more pizza?(y/n)\n")    
    endOption = inp2


print("This will cost you",tmp,"Euro")