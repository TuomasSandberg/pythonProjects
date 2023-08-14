from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

questions = []
for question in question_data:
    question_text = question["text"]
    answer = question["answer"]
    new_question = Question(question_text, answer)
    questions.append(new_question)


quiz = QuizBrain(questions)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"your final score was {quiz.score}/{quiz.question_number}")
