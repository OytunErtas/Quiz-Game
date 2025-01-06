from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

question_bank = []

for question in question_data:
    q = question["question"]
    a = question["correct_answer"]
    q_obj = Question(q,a)
    question_bank.append(q_obj)


quiz = QuizBrain(question_bank)


while quiz.still_has_question() is True:
    quiz.next_question()

print("You have finished the Quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
