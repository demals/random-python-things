def display(num1,num2):
    number = bin(int(num1, 2) * int(num2, 2))
    print(num1.rjust(len(number[2:])+1))
    print("x",end="")
    print(num2.rjust(len(number[2:])))
    print("="*(len(number[2:])+1))
    maths(num1,num2,number)
    print("=" * (len(number[2:])+1))
    print(number[2:].rjust(len(number[2:])+1))


def user():
    user = input("Input number in binary: ")
    return user

def program():
    display(user(),user())

def maths(num1,num2,number):
    for i in reversed(range(len(num2))):
        if num2[i] == "1":
            print((num1 + (len(num2) - (i+1)) * "0").rjust(len(number[2:])+1))

program()