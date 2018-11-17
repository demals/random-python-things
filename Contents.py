def length(text):
    counter = 0
    for i in text:
        if i.isupper() == True or i.islower() == True:
            counter += 1
    print("Text has "+str(counter)+" letters")
def capital(text):
    counter = 0
    for i in text:
        if i.isupper() == True:
            counter += 1
    print("Text has "+str(counter)+" capital letters")
def numbers(text):
    number_list = ["1","2","3","4","5","6","7","8","9","0"]
    counter = 0
    for i in text:
        if i in number_list:
            counter += 1
    print("Text has "+str(counter)+" numbers in it")
def symbols(text):
    number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    counter = 0
    for i in text:
        if i.isupper() == True or i.islower() == True or i in number_list or i == " ":
            continue
        else:
            counter += 1
    print("Text has "+str(counter)+" symbols")
user = input("Input text: ")
length(user)
capital(user)
numbers(user)
symbols(user)