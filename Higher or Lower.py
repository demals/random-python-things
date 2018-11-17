import random
cards = ["1","2","3","4","5","6","7","8","9","10","J","Q","K"]
counter = 0
while True:
    guess = random.choice(cards)
    print("The card is: " + str(guess))
    user = input("higher or lower? ")
    guess2 = random.choice(cards)
    while True:
        if guess2 == "J" or guess2 == "Q" or guess2 == "K":
            ord(guess2)
            break
        else:
            value = chr(int(guess2))
            break
    while True:
        if guess == "J" or guess == "Q" or guess == "K":
            ord(guess)
            break
        else:
            value = chr(int(guess))
            break
    if user == "lower" and guess2 < guess:
        print("Well done! you guessed correctly")
        counter += 1
    elif user == "higher" and guess2 > guess:
        print("Well done! you guessed correctly")
        counter += 1
    else:
        print("Wrong")
        break
print("Well done! you guessed " +str(counter)+ " correctly")
