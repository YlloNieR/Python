print("Berechnung des monatlich zu zahlenden Steuerbetrages")
# Eingabe Bruttoeinkommen

print("Bitte geben Sie Ihr monatliches Bruttogehalt in EURO ein: ")
a = input()
bruttogehalt = int(a)
print("Bitte geben Sie an ob Sie verheiratet oder ledig sind: ")
familienstand = input()

# Verwendung von operator and
if bruttogehalt > 4000 and familienstand == "ledig":
    print("\nAls Lediger AN bei Ihrem Bruttolohn sind 26% Steuern fällig.")
    steuerbetrag = bruttogehalt * 0.26
    print("Somit beträgt ihr Steuerbetrag", steuerbetrag, "EURO")

elif bruttogehalt > 4000 and familienstand == "verheiratet":
    print("\nAls Verheirateter AN bei Bei Ihrem Bruttolohn sind 22% Steuern fällig.")
    steuerbetrag = bruttogehalt * 0.22
    print("Somit beträgt ihr Steuerbetrag", steuerbetrag, "EURO.")

# Verwendung von operator not
elif bruttogehalt <= 4000 and not familienstand == "verheiratet":
    print("\nAls Lediger AN bei Ihrem Bruttolohn sind 22% Steuern fällig.")
    steuerbetrag = bruttogehalt * 0.22
    print("Somit beträgt ihr Steuerbetrag", steuerbetrag, "EURO.")

elif bruttogehalt <= 4000 and familienstand == "verheiratet":
    print("\nAls Verheirateter AN bei Ihrem Bruttolohn sind 18% Steuern fällig.")
    steuerbetrag = bruttogehalt * 0.18
    print("Somit beträgt ihr Steuerbetrag", steuerbetrag, "EURO.")
