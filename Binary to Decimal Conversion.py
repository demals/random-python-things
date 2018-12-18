import math
def user():
    user = input("input number to convert to binary: ")
    return int(user)
def max_bin_number(number):
    counter = 1
    while True:
        if counter - number > 0:
            break
        else:
            counter *= 2
    return counter
def converter(number,maxbin):
    final_number = ""
    while True:
        maxbin = maxbin - math.ceil(maxbin / 2)
        if maxbin == 0:
            return final_number
        if number - maxbin >= 0:
            number = number - maxbin
            final_number += "1"
        else:
            final_number += "0"
def main():
    number = user()
    bin_number = max_bin_number(number)
    print(converter(number,bin_number))
main()