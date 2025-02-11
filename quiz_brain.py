import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        if self.still_has_questions():
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
            q_text = html.unescape(self.current_question.text)
            return f"Q.{self.question_number}: {q_text}"
        else:
            return None  # Indicates no more questions

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        is_correct = user_answer.lower() == correct_answer.lower()

        if is_correct:
            self.score += 1

        # Return feedback instead of printing directly
        return {
            "is_correct": is_correct,
            "correct_answer": correct_answer,
            "score": self.score,
            "question_number": self.question_number
        }
