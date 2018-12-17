def encode(text,key):
    key_numbers = key_array(text,key)
    text_numbers = text_array(text)
    cipher_text_numbers = array_adder(key_numbers,text_numbers)
    print("Key: ".ljust(len("ciphertext: "))+cipher_text_letters(key_numbers))
    print("Plaintext: ".ljust(len("ciphertext: "))+cipher_text_letters(text_numbers))
    print("Ciphertext: " + cipher_text_letters(cipher_text_numbers))

def key_array(text,key):
    key_value = []
    for i in range(len(text)):
        if i > len(key)-1:
            i = i%len(key)
        key_value.append(ord(key[i]))
    return key_value

def text_array(text):
    text_value = []
    for i in text:
        text_value.append(ord(i))
    return text_value

def array_adder(array1,array2):
    final_array = []
    for i in range(len(array2)):
        number = (array1[i] + array2[i])-97
        if number > 122:
            number = (array1[i] + array2[i]) - 97 - 26
        final_array.append(number)
    return final_array

def cipher_text_letters(array):
    cipher_text = ""
    for letter in array:
        cipher_text += chr(letter)
    return cipher_text

encode("sendtroopsatdawn","cat")