import sys
import morsen_8_23
import morsen_bildschirm_8_24
import time
import winsound

# Beispieltext codieren


def tonCode(text, code):
    # Zeitschema, Dauer eines Signals in Millisekunden
    signalDauer = {".": 200, "-": 600}

    # Zeitschema, Dauer einer Pause in Sekunden
    signalPause = 0.2
    zeichenPause = 0.6
    wortPause = 1.4

    # Text in Wörter zerlegen
    alleWorte = text.split()

    # Jedes Wort in Text
    for w in range(len(alleWorte)):
        # Übernahme eines Wortes
        wort = alleWorte[w]
        # Jedes Zeichen im Wort
        for z in range(len(wort)):
            # Übernahme eines Zeichens
            zeichen = wort[z]
            # Kontrollausgabe des Zeichens (ausgeblendet siehe morsen_ton_8_25.py)
            # print(zeichen, end="")
            # Versuch, ein Zeichen auszugeben
            try:
                # Übernahme des Morsezeichens für das Zeichen
                # Falls kein Eintrag Dictionary: KeyError
                alleSignale = code[zeichen]
                # Jedes Signal des Morsezeichens
                for s in range(len(alleSignale)):
                    # Übernahme eines Symbols
                    signal = alleSignale[s]
                    # Ausgabe des Symbols, kurz oder lang
                    winsound.Beep(800, signalDauer[signal])
                    # Nach jedem Signal eine Signalpause,
                    # außer nach dem letzten Zeichen
                    if z < len(wort)-1:
                        time.sleep(signalPause)
                # Nach jedem Zeichen eine Zeichenpause,
                # außer nach dem letzten Zeichen
                if z < len(wort)-1:
                    time.sleep(zeichenPause)
            # Falls kein Eintrag im Dictionary: ignorieren
            except KeyError:
                pass
        # Nach Jedem Wort eine Wortpause,
        # außer nach dem letzten Wort
        if w < len(alleWorte)-1:
            print(" ", end="")
            time.sleep(wortPause)


# Lesefunktion aufrufen
code = morsen_8_23.leseCode()

# Eingabefeld
x = input("\nWas für ein Wort möchtest du in Morsesprache hören?\n")

# Schreibfunktion aufrufen
print("\nDer MorseCode von ", x.upper(), " lautet wie folgt:")
morsen_bildschirm_8_24.schreibeCode(x, code)
tonCode(x, code)

print("\nEnde\n", end="")
