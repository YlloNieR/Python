def sorter(a, b, c):
    print("sorting...")
    tmp = 0
    if a > c:
        tmp = c
        c = a
        a = tmp

    if b > c:
        tmp = c
        c = b
        b = tmp

    if a > b:
        tmp = b
        b = a
        a = tmp

    print("VAR1 = ", a)
    print("VAR2 = ", b)
    print("VAR3 = ", c)


a = 9.6
b = 3.4
c = 3.7

print("## Sorter ##")
print("VAR1 = ", a)
print("VAR2 = ", b)
print("VAR3 = ", c)

sorter(a, b, c)
