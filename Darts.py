def score():
    total = 0
    for i in range(1,4):
        user = input("dart " + str(i) +" B = Bull ,Be = Bull's Eye: ")
        try:
            user = int(user)
            multiplier = input("was that in the 1) 2x zone, 2) 3x zone or 3) none ")
            if multiplier == 1:
                user = user * 2
            if multiplier == 2:
                user = user * 3
        except:
            if user == "B":
                user = 25
            elif user == "Be":
                user = 50
        total += user
    return total

print(score())