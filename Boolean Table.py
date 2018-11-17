def andd(a,b):
    if a == 0 or b == 0:
        print("0",end ="   ")
    else:
        print("1",end ="   ")
def orr(a,b):
    if a == 1 or b == 1:
        print("1",end ="  ")
    else:
        print("0",end ="  ")
def xor(a,b):
    if a != b:
        print("1",end ="   ")
    else:
        print("0",end ="   ")
def nott(a,b):
    if a == 0 or b == 0:
        print("1",end ="   ")
    else:
        print("0",end ="   ")
def nor(a,b):
    if a == 0 and b == 0:
        print("1",end ="   ")
    else:
        print("0",end ="   ")
print("a b and or xor not nor")
for i in range(0,4):
    print()
    binary = '{0:02b}'.format(i)
    binary = list(binary)
    a = int(binary[0])
    b = int(binary[1])
    print(a,end =" ")
    print(b,end =" ")
    andd(a,b)
    orr(a,b)
    xor(a,b)
    nott(a,b)
    nor(a,b)