user = input("Input text: ")
if user.lower() == (user.lower()[::-1]):
    print(user)
    print(user[::-1])
    print("True")
else:
    print("false")