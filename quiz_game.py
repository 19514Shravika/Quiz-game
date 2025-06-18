from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

Question_bank=[]
for question in question_data:                  #looping around list of dictionaries in question_data
    question_text=question["text"]              #creating a variable and store text,answer temporarily
    question_answer=question["answer"]
    new_qs=Question(question_text,question_answer)  #create a new object from the Question blueprint
    Question_bank.append(new_qs)                    #append the object to the list and repeat the loop
print(Question_bank)

quiz=QuizBrain(Question_bank)
while quiz.still_has_questions():
    quiz.next_question()


