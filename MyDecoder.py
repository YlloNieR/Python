






def shiftcypherfileReadOnly(filename):
    with open(filename, 'rb') as f:
        content = f.read()
    print("\nbytes object: ", content)
    content = "".join(map(chr, content))
    print("converted to String ", content)
    print("Hint: * could be Spaces")
    stern = ord("*")
    space = ord(" ")
    print("\t* = ", ord("*"), "\n\tSPACE = ", ord(" "), "\n")
    print("difference: ", stern, " - ", space, " = ", stern-space)


def shiftcypherfile(filename, shiftStart, shiftEnd):
    with open(filename, 'rb') as f:
        content = f.read()
    content = "".join(map(chr, content))
    splitContent = split(content)
    arr = []
    add = shiftStart
    for i in range(shiftStart, shiftEnd):
        for j in range(len(splitContent)):
            arr.append(chr(ord(splitContent[j])+add))

        print("shift:", add, " decrypted: ", "".join(arr))
        add += 1
        arr = []


def shiftcypherString(cipherString, shiftCountEnd):
    content = cipherString
    splitContent = split(content)
    arr = []
    add = 0
    for i in range(0, shiftCountEnd):
        for j in range(len(splitContent)):
            arr.append(chr(ord(splitContent[j])+add))

        print("shift:", add, " decrypted: ", "".join(arr))
        add += 1
        arr = []


def split(x):
    return list(x)

print("Decoder")
print("Choose an option")
options1 = int(input("option 1 - Shift cipher alias Caesar Cipher\n"))
if options1 == 1:
    print("Shift cipher")    
    options2 = int(input("option 1 - file\noption 2 - String\n"))
    if options2 == 1:
        filename = input("filename? ")
        shiftcypherfileReadOnly(filename)
        shiftCountStart = int(input("shift starts at? "))
        shiftCountEnd = int(input("shift ends at? "))
        shiftcypherfile(filename, shiftCountStart, shiftCountEnd)
    else:
        cipherString = input("String? ")
        shiftCountEnd = int(input("shift ends at? "))

        shiftcypherString(cipherString, shiftCountEnd)
else:
    print("Unfortunately this does not exist, yet!")

