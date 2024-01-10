class Question:
    def __init__(self, question, answers):
        self.question = question
        self.questionText = question.text
        self.answers = answers
        self.answersText = [
            answer.get_attribute("data-value")
            if answer.get_attribute("data-value")
            else answer.get_attribute("data-answer-value")
            for answer in answers
        ]
