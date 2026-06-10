class QuizBrain:

    def __init__(self, questions_list: list):
        self.questions_list = questions_list
        self.answers = {
            "correct": 0,
            "incorrect": 0,
        }

    def retrieve_question(self, index):
        return self.questions_list[index]

    def check_answer(self, index: int, answer: str):

        if self.questions_list[index].answer == answer.capitalize():
            self.answers["correct"] += 1
            return True
        else:
            self.answers["incorrect"] += 1
            return False

    def print_score(self):
        return self.answers
