import random

def menu():
        print("1.Play\n2.HighScore\n3.Add Questions\n4.Quit")
        user = int(input())
        return user

def endgame():
    print("Goodbye!")

def quiz():
    try:
        file = open("quizquestons.txt","r")
    except:
        print("error: file not found, please use option 3.Add Questions to create a new file")
        return None
    all_questions = file.read().split("\n")
    question_list = []
    len(question_list)
    while True:
        line = random.choice(all_questions)
        if len(question_list) == 10:
            break
        elif line not in question_list and line != "":
            question_list.append(line)
        else:
            continue
    file.close()
    score = 0
    for qa in question_list:
        question,answer = qa.split("¬")
        print(question)
        user = input()
        if user == answer:
            print("Correct")
            score += 1
        else:
            print("Wrong")
    try:
        file = open("quizhighscore.txt","r")
        highscore = file.readline()
    except:
        file = open("quizhighscore.txt","w")
    file.close()
    try:
        current_user,current_score = highscore.split("¬")
    except:
        current_score = 0
    try:
        if int(current_score) < score:
            winner(score)
        else:
            print("you didn't get a highscore")
            return None
    except:
        return None

def winner(score):
    file = open("quizhighscore.txt", "w")
    user_name = input("what is your name? ")
    file.write(user_name + "¬" + str(score))
    file.close()
    user = input("Would you like to add a question? (1.Yes 2.No) ")
    print("Well Done"+user_name+"you got the highscore")
    if user == 1:
        ask_question()
    return None

def add_questions():
    try:
        file = open("quizquestons.txt","a")
    except:
        file = open("quizquestons.txt","w")
    file.write(ask_question() + "\n")
    file.close()

def ask_question():
    string = ""
    user = input("What is the question? ")
    string += user
    user = input("What is the answer? ")
    string += "¬" + user
    return string

def highscore():
    file = open("quizhighscore.txt","r")
    print(file.read())
    file.close()
    return None

def game():
    while True:
        user = menu()
        if user == 1:
            quiz()
        if user == 2:
            highscore()
        if user == 3:
            add_questions()
        if user == 4:
            endgame()
            break
game()
