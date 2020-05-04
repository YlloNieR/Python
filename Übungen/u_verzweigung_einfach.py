print("Berechnung des Steuerbetrages")

# Eingabe Bruttoeinkommen

print("Bitte geben Sie Ihr monatliches Bruttogehalt in EURO ein: ")
a = input()
bruttogehalt = int(a)

# Verzweigung
if bruttogehalt > 2500:
    print("\nBei Ihrem Bruttolohn sind 22% Steuern fällig.")
    steuerbetrag = bruttogehalt * 0.22
    print("Somit beträgt ihr Steuerbetrag", steuerbetrag, "EURO")
else:
    print("\nBei Ihrem Bruttolohn sind 18% Steuern fällig.")
    steuerbetrag = bruttogehalt * 0.18
    print("Somit beträgt ihr Steuerbetrag", steuerbetrag, "EURO.")
