user = int(input("which fibonacci number would you like to know? "))
n1 = 1
n2 = 1
counter = 1
while True:
    if counter == user:
        break
    else:
        n1 = n1 + n2
        counter += 1
        if counter == user:
            break
        else:
            n2 = n1 + n2
            counter += 1
            if counter == user:
                break
            else:
                continue
if user%2 == 0:
    print(str(n2))
else:
    print(str(n1))
    
