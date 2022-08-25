from Guessing_game.student import Question


question_bank = [
    "what the color of the red sea?.\n(a)red\n(b)colorless\n(c)blue\n\n",
    "what is the fastest land animal on earth?.\n(a)rat\n(b)goat\n(c)cheetah\n\n",
    "what the colour of a banana?.\n(a)red\n(b)orange\n(c)yellow\n\n",
    "what is the squart root of 4?.\n(a)16\n(b)10\n(c)34\n\n"
]

questions  = [
    Question(question_bank[0],"b"),
    Question(question_bank[1],"c"),
    Question(question_bank[2],"c"),
    Question(question_bank[3],"ax")
]

def run_test(questions):
    score = 0 
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
run_test(questions)