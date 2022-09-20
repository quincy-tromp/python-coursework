from question_model import Question
from data import trivia_data
from quiz_brain import QuizBrain
from art import logo


question_bank = []
for question in trivia_data:
    new_q = Question(q_text=question['question'], q_answer=question['correct_answer'])
    question_bank.append(new_q)

print(logo)
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")