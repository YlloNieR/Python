import webbrowser

#Variante 1
#on Windows OS
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
url = "https://github.com/YlloNieR"
webbrowser.get(chrome_path).open(url)

#Variante 2
webbrowser.open("Http://google.us")
print("Ende")