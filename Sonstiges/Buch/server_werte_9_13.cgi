#!C:\Users\Oliver Rein.DESKTOP-6TPP48V\AppData\Local\Programs\Python\Python38-32\python.exe

# Modul cgi
import cgi
import cgitb

# Ausgabe bei Fehler
cgitb.enable()

# Objekt der Klasse FieldStorage
form = cgi.FieldStorage()

# HTML-Dokument mit Variablen
print("Content-type: text/html")
print()

print("<!DOCTYPE html><html>")
print("<head><meta charset:'utf8'></head>")
print("<body>")

# Auswertung Formularfeld
if "nn" in form:
    print("<p><b>Registrierte Daten:</b></p>")
    print("<p>Nachnamen:<br />")
    try:
        print(form["nn"].value)
    except:
        for element in form["nn"]:
            print(element.value, "<br />")
    print("</p>")
else:
    print("<p><b>Keine Daten gesendet</b></p>")

print("</body>")
print("</html>")
