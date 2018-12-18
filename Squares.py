def top(size):
    print("n".center(longest(size,"n")),end="")
    print(" | ",end="")
    print("decimal".center(longest(size,"dec")),end="")
    print(" | ",end="")
    print("binary".center(longest(size,"bin")),end="")
    print(" | ",end="")
    print("hexadecimal".center(longest(size,"hex")),end="")

def longest(size,type):
    if type == "n":
        return len(str(size))
    if type == "dec":
        if len(str(size**2)) < len("decimal"):
            return len("decimal")
        else:
            return len(str(size**2))
    if type == "hex":
        if len(hex(size ** 2)[2:]) < len("hexadecimal"):
            return len("hexadecimal")
        else:
            return len(hex(size ** 2)[2:])
    if type == "bin":
        if len(bin(size**2)[2:]) < len("binary"):
            return len("binary")
        else:
            return len(bin(size**2)[2:])

def row(size):
    for i in range(1,int(size)+1):
        print()
        print(str(i).rjust(longest(size,"n")),end="")
        print(" | ", end="")
        print(str(i**2).rjust(longest(size,"dec")), end="")
        print(" | ", end="")
        print(str(bin(int(i*i))[2:].rjust(longest(size,"bin"))), end="")
        print(" | ", end="")
        print(str(hex(int(i*i))[2:].rjust(longest(size,"hex"))), end="")

def user():
    user = input("how big would you like this thing? ")
    return int(user)

def main():
    size = user()
    top(size)
    row(size)

main()