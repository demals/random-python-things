user = int(input("Input a number: "))
starter = 10
counter = 0
print(str(user) + (" = "), end ='')
for i in reversed(range (len(str(user)))):
    counter += 1
    print (str(((user // starter ** i)%10) * starter ** i),end = ' ')
    if i == 0:
        break
    else:
        print ("+",end = ' ')
        continue
    
