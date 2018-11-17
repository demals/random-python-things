pass_counter = 0
swap_counter = 0
comparisons_counter = 0
numbers_list = []
userinp = input("input numbers: ")
numbers_list = list(map(str,userinp.split()))
longest = 0
for i in range(len(numbers_list)):
    if (len(numbers_list[i])) > longest:
        longest = len(numbers_list[i])
for i in numbers_list:
    print(i.rjust(longest),end = " ")
print()
for i in range(1,len(numbers_list)):
    while True:
        if i == 0:
            pass_counter += 1
            for j in numbers_list:
                print(j.rjust(longest),end = " ")
            print(" Pass: " + str(pass_counter))
            break
        elif int(numbers_list[i]) < int(numbers_list[i-1]):
            numbers_list[i], numbers_list[i-1] = numbers_list[i-1], numbers_list[i]
            swap_counter += 1
            comparisons_counter += 1
            i = i-1
            for j in numbers_list:
                print(j.rjust(longest),end = " ")
            print()
        else:
            comparisons_counter += 1
            i = i-1
print("Comparisons: "+str(comparisons_counter))
print("Swaps: "+str(swap_counter))
            
