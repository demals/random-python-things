n = int(input("How many square numbers would you like the know? "))
array = []
for i in range(1,n+1):
    array.append(i**2)
print ("here are the first",n,"square numbers:")
print (*array, sep=',')
