#from Question import Question


class Question:
    def __init__(self,prompt,answer):
        self.prompt = prompt
        self.answer = answer


question_prompt = [
    "what color is banana?\n(a) Red \n(b) Black \n(c) Yellow \n(d) Red\nEnter Answer : ",
    "what color is orange?\n(a) Red \n(b) orange \n(c) Yellow \n(d) brown\nEnter Answer : ",
    "what color is strawberry?\n(a) Red \n(b) Black \n(c) Yellow \n(d) Red\nEnter Answer : "
]

questions = [
    Question(question_prompt[0], "c"),
    Question(question_prompt[1], "b"),
    Question(question_prompt[2], "a")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)
