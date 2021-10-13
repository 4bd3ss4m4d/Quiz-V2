# Quiz Program V2

from data import questions_bank
from question import Question
from quiz_brain import QuizBrain


def main():
    # Control flow
    again = 'y'
    while again == 'y':

        print("Welcome to The Quiz V2 Program!")

        # Print a list of all available question categories
        category_list = ["General Knowledge", "Geography"]
        print("Here is a list of all the available question categories: ")
        for category in category_list:
            print("   " + category)

        # get user's question category input
        category_chosen = input("What question category would you like?: ").title()
        while category_chosen not in category_list:
            category_chosen = input("Wrong input! What question category would you like?: ").title()

        # Print a list of all available question difficulties
        difficulty_list = ["easy", "medium", "hard"]
        print('Choose one the following quiz difficulties: ')
        for difficulty in difficulty_list:
            print("   " + difficulty.title())

        # Get user's quiz difficulty input
        difficulty_chosen = input("What quiz difficulty would you like?: ").lower()
        while difficulty_chosen not in difficulty_list:
            difficulty_chosen = input("Wrong input! What quiz difficulty would you like? : ").lower()

        # Create a list of questions depending on user's category and difficulty chosen
        quiz_question_list = []
        for question in questions_bank:
            if question["category"] == category_chosen and question["difficulty"] == difficulty_chosen:
                quiz_question_list.append(question)

        # Create question instances from Question class
        questions = []
        for item in quiz_question_list:
            category = item["category"]
            qstype = item["type"]
            difficulty = item["difficulty"]
            questiontxt = item["question"]
            correct_answer = item["correct_answer"]
            incorrect_answers = item["incorrect_answers"]

            qst = Question(category, qstype, difficulty, questiontxt, correct_answer, incorrect_answers)
            questions.append(qst)

        # Create a Quiz attribute from quiz_brain class
        quiz = QuizBrain(questions)
        quiz.next_question()
        quiz.show_score()

        again = input("To play again, type 'y' to quit type 'q': ")


main()
