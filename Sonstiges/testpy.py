def hanoi(n,f,h,t):
    if n == 0:
            pass
    else:
        hanoi(n-1,f,t,h)

def test(n,f,t,h):
    for i in range(3):
        print(hanoi(n-1,f,t,h))
        
        # hanoi(n-1,h,f,t)


test(3,"A","B","C")