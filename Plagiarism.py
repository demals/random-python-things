def compare():
    essay1 = open("essay1.txt","r")
    essay2 = open("essay2.txt","r")
    string = essay1.read()
    essay1_array = string.split(". ")
    string = essay2.read()
    essay2_array = string.split(". ")
    same = compare_elements_same(essay1_array,essay2_array)
    dif = compare_elements_dif(essay1_array,essay2_array)
    print("the essays are " + str(((same)/(dif+same))*100) + "%" + " the same.")
def compare_elements_same(array1,array2):
    a1 = set(array1)
    a2 = set(array2)
    return len(a1 & a2)
def compare_elements_dif(array1,array2):
    a1 = set(array1)
    a2 = set(array2)
    total = len(a1-a2) + len(a2-a1)
    return total

compare()