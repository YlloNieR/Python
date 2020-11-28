fuelConsumption = 6.8 / 100
oilConsumption = 0.5 / 1000

while True:
    inp = input("Please enter the distance (in km): ")
    fuelConsumptionCalculation = fuelConsumption * float(inp)
    oilConsumptionCalculation = oilConsumption * float(inp)

    print("Your fuelconsumption is",
          round(fuelConsumptionCalculation, 2), "liters per kilometer")
    print("Your oilconsumption is",
          round(oilConsumptionCalculation, 2), "liters per kilometer")
    fuelConsumptionPriceCalculation = fuelConsumptionCalculation * 1.207
    oilConsumptionPriceCalculation = oilConsumptionCalculation * (37.47 / 5)
    print("Your fuelconsumption costs",
          round(fuelConsumptionPriceCalculation, 2), "Euro")
    print("Your oilconsumption costs", round(
        oilConsumptionPriceCalculation, 2), "Euro")
    print("")
