import time

def one(char):
    string = "   " + char
    return string

def two(n,char):
    if n == 1 or n == 4 or n == 7:
        string = " "+char*2+" "
    if n == 2 or n == 3:
        string = "   " + char
    if n == 5 or n == 6:
        string = char + "   "
    return string

def three(n,char):
    if n == 1 or n == 4 or n == 7:
        string = " " + char * 2 + " "
    else:
        string = " "*3 + char
    return string

def four(n,char):
    if n == 1 or n == 2 or n == 3:
        string = char + "  " + char
    if n == 4:
        string = " " + char * 2 + " "
    if n == 5 or n == 6 or n == 7:
        string = " " * 3 + char
    return string

def five(n,char):
    if n == 1 or n == 4 or n == 7:
        string = " " + char * 2 + " "
    if n == 2 or n == 3:
        string = char + " " * 3
    if n == 5 or n == 6:
        string = " " * 3 + char
    return string

def six(n,char):
    if n == 1 or n == 2 or n == 3:
        string = char + " " * 3
    if n == 4 or n == 7:
        string = " " + char * 2 + " "
    if n == 5 or n == 6:
        string = char + "  " + char
    return string

def seven(n,char):
    if n == 1:
        string = " " + char * 2 + " "
    else:
        string = " "*3 + char
    return string

def eight(n,char):
    if n == 1 or n == 4 or n == 7:
        string = " " + char * 2 + " "
    else:
        string = char + "  " + char
    return string

def nine(n,char):
    if n == 1 or n == 4:
        string = " " + char * 2 + " "
    if n == 2 or n == 3:
        string = char + "  " + char
    if n == 5 or n == 6 or n == 7:
        string = " " * 3 + char
    return string

def zero(n,char):
    if n == 1 or n == 7:
        string = " " + char*2 + " "
    else:
        string = char + "  " + char
    return string

def dotdot(n,char):
    if n == 3 or n == 5:
        string =  "  "+ char +"  "
    else:
        string = "     "
    return string

def user():
    user = input("what would you like your ascii character to be? (pick 1): ")
    return user

def timezone():
    user = str(input("what time zone would you like to know the time of?: "))
    return user

def numberpicker(time,i,char):
    if time == 1:
        return one(char)
    if time == 2:
        return two(i,char)
    if time == 3:
        return three(i,char)
    if time == 4:
        return four(i,char)
    if time == 5:
        return five(i,char)
    if time == 6:
        return  six(i,char)
    if time == 7:
        return seven(i,char)
    if time == 8:
        return eight(i,char)
    if time == 9:
        return nine(i,char)
    if time == 0:
        return zero(i,char)

def clock(char):
    while True:
        for i in range(1,8):
            h1 = int((time.strftime("%H")[0]))
            h2 = int((time.strftime("%H"))[1])
            m1 = int((time.strftime("%M"))[0])
            m2 = int((time.strftime("%M"))[1])
            print ((numberpicker(h1,i,char)) + " " + (numberpicker(h2,i,char)) + dotdot(i,char) + (numberpicker(m1,i,char)) + " " + (numberpicker(m2,i,char)))
        print()
        time.sleep(2)
        while True:
            if int(time.strftime("%S")) == 0:
                break

def main():
    #timezone()
    char = user()
    clock(char)
    
main()