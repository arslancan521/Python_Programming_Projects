from question_model import Question

class QuizBrain:
    def __init__(self, question_bank):
        self.question_bank = question_bank
        self.score = 0
        self.question_number = 0

    def check_answer(self, user_answer,correct_answer ):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"Congrats, your answer is correct. Your score : {self.score} / {self.question_number + 1}")
        else:
            print(f"Your answer is wrong. Your score is : {self.score} / {self.question_number + 1}")


    def next_question(self):

        user_answer = input(f"Q{self.question_number + 1} : {self.question_bank[self.question_number].question} ? True / False:")
        self.check_answer(user_answer, self.question_bank[self.question_number].answer)
        self.question_number += 1

    def is_still_continue(self):
        return self.question_number < len(self.question_bank)




