import sys
import morsen_8_23


# Beispieltext codieren
def schreibeCode(text, code):
    for zeichen in text:
        try:
            print(code[zeichen], end=" ")
        except KeyError:
            print(" ", end=" ")
    print()


# Lesefunktion aufrufen
code = morsen_8_23.leseCode()

# Schreibfunktion aufrufen (ausgeblendet siehe morsen_ton_8_25.py)
# schreibeCode("Hallo Welt", code)
