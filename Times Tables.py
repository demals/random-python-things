user=int(input('how big would you liek this thing?: '))
print("x",end="\t")
for leng in range (1,user+1):
            print(leng, end="\t")
print("\n")
for row in range(1,user+1):
    print(row, end="\t")
    for col in range(1,user+1):
        print(row*col, end="\t")
    print("")
