def ai():
    while True:
        question = input("Ask a question: ")
        database = check_database(question)
        if database == "no":
            add_question_and_answer_to_database(question)

def check_database(question):
    try:
        file = open("questions.txt","r")
        everything = file.read()
    except:
        file = open("questions.txt", "w")
    file.close()
    everything_list = everything.split("\n")
    try:
        answer = 1 + everything_list.index(question.upper())
        print(everything_list[answer])
    except:
        return "no"

def add_question_and_answer_to_database(question):
    file = open("questions.txt","a")
    file.write("\n" + question.upper())
    answer = input("What is the answer to this question? ")
    file.write("\n" + answer)
    file.close()

ai()