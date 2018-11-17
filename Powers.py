user = (input("how many do you want?: "))
gap_1 = len(user)
gap_2 = (gap_1 ** 2)
print(("x" + " " * gap_1 + "x^2" + " " * gap_2 + "x^3"))
for i in range(1,(int(user)+1)):
    ans_1 = str(i ** 2)
    ans_2 = str(i ** 3)
    print((str(i) + ans_1.rjust(gap_1 + 3) + ans_2.rjust(gap_2 + 3)))