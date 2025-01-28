from ui import QuizInterface  # Import your GUI
from question_model import Question  # Import the Question class (or define it here)
from quiz_brain import QuizBrain  # Import the QuizBrain class
from data import question_data  # Import your question data

# Build the question bank
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Create an instance of QuizBrain and start the GUI
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
