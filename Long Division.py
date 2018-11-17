def user_n():
    string = int(input("input 1st number "))
    return string
def user_d():
    string = int(input("input 2nd number "))
    return string
def answer(n,d):
    if n%d == 0:
        string = str(int(n / d))
    else:
        string = str(int(n/d)) + "r" + str(n%d)
    return string
def maths_1(n,d):
    string = str(d) + "|" + str(n)
    return string
def number_picker(n,d):
    for i in range(1,len(str(n))+1):
        if int(str(n)[0:i])/d >= 1:
            return int(str(n)[0:i])
def new_n(n,x):
    amount = len(str(x))
    return int(str(n)[amount:])
def minus_number(n,d):
    number = (n//d)*d
    return number
def minus_ans(n,minus_bit):
    answer = n - minus_bit
    return answer
def main():
    n= user_n()
    d = user_d()
    length = 1+len(str(d)) + len(str(answer(n,d)))
    print((answer(n,d).rjust(length)))
    print(maths_1(n,d))
    length = 1 + len(str(d)) + len(str(minus_number(number_picker(n,d),d)))
    while True:
        try:
            n_new = number_picker(n,d)
            minus_bit = minus_number(n_new,d)
            string = "-" + str(minus_bit)
            print(string.rjust(length))
            print(("─" * (len(string)+1)).rjust(length +1 ))
            ans = minus_ans(n_new,minus_bit)
            print(str(ans).rjust(length))
            n_new = new_n(n,n_new)
            n = int(str(ans) + str(n_new))
            length += 1
            print((str(ans) + str(n_new)[:1]).rjust(length))
        except:
            break
main()