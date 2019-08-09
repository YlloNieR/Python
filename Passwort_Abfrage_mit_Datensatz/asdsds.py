

'''
zeilen = [] 

with open ("hello.txt", "rt") as textfile: 
    for zeile in textfile:
        zeilen.append(zeile)

print(len(zeilen))

z = len(Wort) -1

print(len(Wort))
'''

Wort = "ABC"

import mmap

msg = Wort.encode()
word = msg
print('Suche das folgende Zeichen:', word)
print('')

with open('hello.txt', 'r+') as f:
    with mmap.mmap(f.fileno(), 0) as m:
        print('Line: {}'.format(m.readline().rstrip()))
        print(word)

        loc = m.find(word)
        print("a ...",loc)
        print("b ... ",m[loc:loc + len(word)])

        print(m.flush())

        print('a: '.format(m.readline().rstrip()))
        print('a: ',m.readline().rstrip())


       
        print('File  :\n{}'.format(f.readline().rstrip()))


breakpoint



'''

print("\nErgebnis = ")  
if letzterBuchstabe == -1:
    print(False)
else:
    if ersteBuchstabe
        print(True)

'''