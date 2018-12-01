array = [1,2,3,4,5]

def map2(array,function):
    for i in array:
        print (function(i))
def squared(i):
    return (i**2)

map2(array,squared)