def timebale(size,type):
    if type == "hex":
        hexdecimal(size)
    if type == "bin":
        binary(size)
    if type == "dec":
        decimal(size)
def hexdecimal(size):
    toprow(size,"hex")
    row(size,"hex")
def binary(size):
    toprow(size,"bin")
    row(size,"bin")
def decimal(size):
    toprow(size,"dec")
    row(size,"dec")
def toprow(size,type):
    print("x",end="\t")
    longest_int = longest(size,type)
    for i in range(1,int(size)+1):
        print(str(i).rjust(longest_int),end=" ")
def longest(size,type):
    if type == "dec":
        return len(str(size**2))
    if type == "hex":
        return len(hex(size**2)[2:])
    if type == "bin":
        return len(bin(size**2)[2:])
def row(size,type):
    if type == "hex":
        for i in range(1,int(size)+1):
            print()
            print(str(i),end="\t")
            for j in range(1,int(size)+1):
                print((str(hex(i*j))[2:]).rjust(longest(size,type)),end=" ")
    if type == "bin":
        for i in range(1,int(size)+1):
            print()
            print(str(i),end="\t")
            for j in range(1,int(size)+1):
                print((str(bin(i*j))[2:]).rjust(longest(size,type)),end=" ")
    if type == "dec":
        for i in range(1,int(size)+1):
            print()
            print(str(i),end="\t")
            for j in range(1,int(size)+1):
                print(str(i*j).rjust(longest(size,type)),end=" ")
timebale(5,"dec")
print("\n")
timebale(5,"hex")
print("\n")
timebale(5,"bin")
