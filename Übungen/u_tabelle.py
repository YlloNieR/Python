# Formatierung von Zeichenketten
print(f"{'Inch':>5}{'cm':>6}")

# Formatierung ganzer Zahlen
for z in range(15, 45, 5):
    print(f"{z:4.2f}{(z * 2.54):8.2f}")
