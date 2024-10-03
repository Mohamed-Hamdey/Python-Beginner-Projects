# from question_model import Question
# from data import question_data
# from quiz_brain import QuizBrain

# question_bank = []
# for question in question_data:
#     question_text = question["text"]
#     question_answer = question["answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)

# quiz = QuizBrain(question_bank)


# while quiz.still_has_questions():
#     quiz.next_question()
#     quiz.check_answer()
# print("You have completed the quiz !")
# print(f"Your final score is {quiz.score}.") 
from turtle import *
from random import random


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")


h = Turtle()
h.shape("turtle")
side = 3
color_choices = ["red", "blue", "green", "orange", "purple", "yellow", "black", "pink", "gray"]


def draw(cs, c_angle, sides):
    for _ in range(sides):
        h.color(cs)
        h.forward(100)
        h.right(c_angle)


for i in range(8):
    r_color = random.choice(color_choices)
    angle = ((side - 2) * 180) / side
    draw(cs=r_color, c_angle=angle, sides=side)
    side = side + 1

screen.exitonclick()