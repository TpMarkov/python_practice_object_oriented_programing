from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

for i in range(0, len(question_bank)):
    current_question = quiz.retrieve_question(i).question
    answer = input(f"Q.{i + 1} {current_question} (True or False): ")
    if quiz.check_answer(i, answer):
        print("Correct!")
    else:
        print("Incorrect!")

print(
    f"Quiz Completed!\nCorrect answers are {quiz.print_score()["correct"]}\nWrong answers: {quiz.print_score()['incorrect']}")
