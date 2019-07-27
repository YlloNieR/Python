import webbrowser

print('\n\t'"######                  ######                                          ")  
print('\t'"#     # # ###### #####  #     # ######  ####  #    # #    # ###### #####  ") 
print('\t'"#     # # #      #    # #     # #      #    # #    # ##   # #      #    # ") 
print('\t'"######  # #####  #    # ######  #####  #      ###### # #  # #####  #    # ") 
print('\t'"#     # # #      #####  #   #   #      #      #    # #  # # #      #####  ") 
print('\t'"#     # # #      #   #  #    #  #      #    # #    # #   ## #      #   #  ") 
print('\t'"######  # ###### #    # #     # ######  ####  #    # #    # ###### #    # ") 
print('\n')
print('\n')
print('\n\t'"#     #                                         #######")                             
print('\t'"##   ##   ##   #####  ######    #####  #   #    #     # #      #      #    # #    #") 
print('\t'"# # # #  #  #  #    # #         #    #  # #     #     # #      #      #    # ##  ##") 
print('\t'"#  #  # #    # #    # #####     #####    #      #     # #      #      #    # # ## #") 
print('\t'"#     # ###### #    # #         #    #   #      #     # #      #      #    # #    #") 
print('\t'"#     # #    # #    # #         #    #   #      #     # #      #      #    # #    #") 
print('\t'"#     # #    # #####  ######    #####    #      ####### ###### ######  ####  #    #")
print('\n')
print('\n')

nFreund = int(input("\tBitte geb an wieviel Bier dein Freund hat = "))
nEgo = int(input("\tBitte geb an wieviel Bier gekauft hast = "))

sure = input("\tBist du sicher das das alles ist?   ")

print("\tDie Biermenge deines Freundes beträgt ",nFreund," addiert mit deiner Biermenge von ",nEgo," ergibt das")
print("\tviel zu wenig!!!!")

asd = input("\t\t\t\t-------------------------->>>>>>>>>>>")

chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
url = "https://www.youtube.com/watch?v=RfCofCkKKk8"
webbrowser.get(chrome_path).open(url)

