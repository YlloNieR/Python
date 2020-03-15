import statistics

# Mittelwerte einer Liste
probe1 = [5, 2, 4, 17]
print("Arithmetischer Mittelwert: ", statistics.mean(probe1))
# Mitterlwert = mean = Summe der Werte geteilt durch ihre Anzahl
print("Harmonischer Mittelwert: ", statistics.harmonic_mean(probe1))
# harmonischer Mitterlwert = mean = Summe der Werte geteilt durch ihre Kehrwerte
print()

# Median
# Mitte der Zahlenmenge
print("Median: ", statistics.median(probe1))
probe2 = [5, 2, 4, 17, 3]
print("Median: ", statistics.median(probe2))
print()

# Unterer Median
# Mitte der Zahlenmenge, low wertet nach unteren Wert ab
print("Unterer Median: ", statistics.median_low(probe1))
print("Unterer Median: ", statistics.median_low(probe2))
print()

# Oberer Median
# Mitte der Zahlenmenge, high wertet nach oberen Wert auf
print("Oberer Median: ", statistics.median_high(probe1))
print("Oberer Median: ", statistics.median_high(probe2))
print()

# Tupel, Werte eines Dictionary
probe3 = (5, 2, 4, 17)
print("aus Tupel: ", statistics.mean(probe3))
probe4 = {'D': 5, 'NL': 2, 'CH': 4, 'F': 17}
print("aus Dictionary: ", statistics.mean(probe4.values()))
