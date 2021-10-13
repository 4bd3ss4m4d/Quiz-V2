# Quiz Brain Class
from random import shuffle


class QuizBrain:

    def __init__(self, question_list, score=0):
        self.current_question = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        for question in self.question_list:
            # Print question
            print(f"Q.{1 + self.current_question}: {question.questiontxt}")
            # show question options:
            answer_options = []
            for answer_option in question.incorrect_answers:
                answer_options.append(answer_option)
            answer_options.append(question.correct_answer)
            shuffle(answer_options)
            print("One of the following answers is correct:")
            for option in answer_options:
                print(f"   {option}")
            answer = input("Answer : ")
            if self.check_answer(question, answer):
                self.score += 1
            self.current_question += 1

    def check_answer(self, question, answer):
        if answer == question.correct_answer:
            return True
        return False

    def show_score(self):
        print(f"Your score is {self.score} ")



