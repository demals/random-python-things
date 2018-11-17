lower = False
upper = False
symbol = False
number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
user = input("input your password: ")
for i in user:
    if i.islower() == True:
        lower = True
for i in user:
    if i.isupper() == True:
        upper = True
for i in user:
    if i.isupper() == True or i.islower() == True or i in number_list or i == " ":
        continue
    else:
        symbol = True
requirements = "You must have at least"
if len(user) <= 6:
    requirements += " ,6 digits"
if lower == False:
    requirements += " ,1 lowercase letter"
if upper == False:
    requirements += " ,1 uppercase letter"
if symbol == False:
    requirements += " ,1 Symbol"
if len(user) >= 6 and lower == True and upper == True and symbol == True:
    print("password change done")
elif len(user) <= 6 or lower == False or upper == False or symbol == False:
    print(requirements)
