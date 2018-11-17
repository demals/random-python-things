while True:
    userlist = []
    user = (input("input a number: "))
    for i in user:
        userlist.append(i)
    for j in range(len(user)):
        if j == (len(user)-1):
            print (user + " True")
        elif userlist[j] < userlist[j+1]:
            continue
        elif userlist[j] > userlist[j+1]:
            print(user + " False")
            break
        
        
