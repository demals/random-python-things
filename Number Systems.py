def user():
    user = int(input("input a number: "))
    return user
def decimal(n):
    return n
def hexadecimal(n):
    string = hex(n)[2:]
    return string
def binary(n):
    string = bin(n)[2:]
    return string
def largest_d(n):
    if len(str(n)) < 7:
        return 7
    else:
        return len(str(n))
def largest_h(n):
    string = hex(n)[2:]
    if len(string) < 11:
        return 11
    else:
        return len(str(string))
def largest_b(n):
    string = bin(n)[2:]
    if len(string) < 6:
        return 6
    else:
        return len(str(string))
def top_row(n):
    string = ""
    string += ("Decimal").rjust(largest_d(n))
    string += "|"
    string += ("Hexadecimal").rjust(largest_h(n))
    string += "|"
    string += ("Binary").rjust(largest_b(n))
    return string

def main():
    n = user()
    print(top_row(n))
    for i in range(n+1):
        string = ""
        string += (str(decimal(i))).rjust(largest_d(n))
        string += "|"
        string += (str(hexadecimal(i))).rjust(largest_h(n))
        string += "|"
        string += (str(binary(i))).rjust(largest_b(n))
        print(string)
main()