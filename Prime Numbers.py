counter = 0
prime = 1
while True:
    prime += 1
    if counter == 100:
        break
    else:
        for i in range (2,prime+1):
            if i == prime:
                print(prime,end = ",")
                counter += 1
                break            
            if prime%i == 0:
                break
            else:
                continue
