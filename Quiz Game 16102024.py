# A quiz game made by Isaac Earl
import sys
class QuizQuestion:
    def __init__(self, question, answer, hints):
        self.hints = hints
        self.question = question
        self.answer = answer

    def guess(self, user_input):
        return user_input.strip().lower() == self.answer.strip().lower()


questions = [
    QuizQuestion("What is the mob?", "Creeper", ["It hisses nearby", "It breaks blocks", "Its green"]),
    QuizQuestion("What is the item?", "Bucket", ["Its made using 3 iron", "You can use it to pick up water", "It's a bucket..."]),
    QuizQuestion("What is the mob?", "Enderman", ["Its tall", "It picks up blocks", "It can teleport"])
]


import random
quit = False
while not quit:    
    quiz_question = random.choice(questions)
    print(quiz_question.question)
    for hint in quiz_question.hints:
        print(f"the hint is: {hint}")
        inp = input("Input your answer, type 'q' to quit.")
        if inp.strip() == 'q':
            quit = True
        elif quiz_question.guess(inp):
            print("you got it right")
            break
        else:
            print("you got it wrong. try again, noob.")


sys.exit()
