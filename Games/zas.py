infile = open('zwischenspeicher.txt', 'r')
mean = 0
numbers = [float(line) for line in infile.readlines()]
mean = sum(numbers)
