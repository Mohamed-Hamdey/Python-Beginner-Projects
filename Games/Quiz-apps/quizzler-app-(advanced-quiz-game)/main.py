import requests
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
request = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean")
request.raise_for_status()
data = request.json()["results"]

for question in data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
interface = QuizInterface(quiz)
# while quiz.still_has_questions():
#     quiz.next_question()
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
