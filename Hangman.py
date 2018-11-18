import random

def difficulty(n):
    if n == 1:
        return ["black","blue","brown","grey","green","orange","pink","purple","red","white","yellow"]
    if n == 2:
        return {"acres","adult","advice","arrangement","attempt","August","Autumn","border"}
    if n == 3:
        return ["abruptly","absurd","abyss","affix","askew","avenue","awkward","axiom","azure","bagpipes","bandwagon","banjo"]
def game():
    user = int(input("Select difficulty:\n1.Easy\n2.Medium\n3.HARD!!!\n"))
    word = random_word(user)
    letter_guess = []
    dead = 0
    while True:
        ascii_man(dead)
        line = blank_line(word,letter_guess)
        print("Word: " + line + " Letters Used:" + ', '.join(map(str, letter_guess)))
        letter_guess = user_letter_guess(letter_guess)
        if letter_guess[-1] == word:
            gamewin()
            return None
        if letter_guess[-1] not in word:
            dead += 1
        if dead == 7:
            ascii_man(dead)
            gameover(word)
            return None
        conditon = winner_check(word,letter_guess)
        if conditon == "win":
            gamewin()
            return None


def gameover(word):
    print("game over you lost. the word was " + word)

def gamewin():
    print("you won!")

def winner_check(word,letter_list):
    wordlen = len(word)
    correct = 0
    for i in word:
        if i in letter_list:
            correct += 1
    if correct == wordlen:
        return "win"
    else:
        return None


def user_letter_guess(letter_guess):
    while True:
        user = input("guess a letter any letter: ")
        if user in letter_guess:
            print ("yo mate, you guessed that already")
            continue
        else:
            break
    letter_guess.append(user)
    return letter_guess

def ascii_man(n):
    if n == 0:
        return None
    if n == 1:
        print("-----")
    if n == 2:
        print("  | ")
        print("  | ")
        print("  | ")
        print("  | ")
        print("-----")
    if n == 3:
        print("  |-------")
        print("  | ")
        print("  | ")
        print("  | ")
        print("  | ")
        print("-----")
    if n == 4:
        print("  |-------")
        print("  |      |")
        print("  | ")
        print("  | ")
        print("  | ")
        print("-----")
    if n == 5:
        print("  |-------")
        print("  |      |")
        print("  |      o")
        print("  | ")
        print("  | ")
        print("-----")
    if n == 6:
        print("  |-------")
        print("  |      |")
        print("  |      o")
        print("  |     -|-")
        print("  | ")
        print("-----")
    if n == 7:
        print("  |-------")
        print("  |      |")
        print("  |      o")
        print("  |     -|-")
        print("  |     / \\")
        print("-----")

def all_letters():
    letter_list = []
    for i in range(65,91):
        letter_list.append(chr(i))
    return letter_list


def word_letter_list(word):
    word_letter_list = []
    for i in range(word):
        word_letter_list.append(i)
    return word_letter_list

def blank_line(word,letter_guess):
    string = ""
    for i in word:
        if i not in letter_guess:
            string += "□"
        else:
            string += i
    return string

def random_word(n):
    word_list = difficulty(n)
    word = random.choice(word_list)
    return word


def menu():
    print("HANGMAN_GAME")
    print("Menu:")
    print("1.Play")
    print("2.Exit")

def main():
    menu()
    user = input()
    if int(user) != 1:
        print("Good Bye!")
    else:
        game()

main()