count = 20

def multiple_3(i):
    if i % 3 == 0:
        return True
    else:
        return False

def multiple_5(i):
    if i % 5 == 0:
        return True
    else:
        return False

def main():
    global count
    for i in range(count):
        if multiple_3(i) == True or multiple_5(i) == True:
            print(str(i))

main()

