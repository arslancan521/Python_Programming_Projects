from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []



for question in question_data:
    question_ = question["text"]
    answer_ = question["answer"]
    question_class = Question(question_,answer_)
    question_bank.append(question_class)

quiz = QuizBrain(question_bank)

while quiz.is_still_continue():
    quiz.next_question()

print(f"The Quiz is ended. Your score is : {quiz.score} / {len(question_bank)}")
