import random

def question():
    num1 = random.randint(1,12)
    num2 = random.randint(1,12)
    print (((str(num1)) + " x " + (str(num2)) + " = "),end ="")
    return num1 * num2

def compare(ans,user):
    if ans == user:
        print("correct")
        return True
    else:
        print("wrong")
        return False

def user():
    try:
        user = int(input())
        return user
    except:
        pass
def quiz():
    score = 0
    for i in range(10):
        q = question()
        u = user()
        if compare(q, u) == True:
            score += 1
    return score

def main():
    user = quiz()
    print("Your total right is " + str(user))

main()