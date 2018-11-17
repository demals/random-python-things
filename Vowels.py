vowels = ["a","e","i","o","u","A","E","I","O","U"]
user = input("Input text: ")
text = ""
for letter in user:
    if letter not in vowels:
        text += letter
print(text)