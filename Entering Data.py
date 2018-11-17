array = []
while True:
    user = int(input("input a number"))
    if user == 0:
        break
    else:
        array.append(user)
        print(sorted(array))
    
    
