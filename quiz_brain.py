class QuizBrain():
    def __init__(self,question_list):
        self.question_number=0
        self.score=0
        self.question_list=question_list

    def still_has_questions(self):
        if self.question_number<len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        choice=input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(choice,current_question.answer)

    def check_answer(self,user_choice,correct_answer):
        if user_choice==correct_answer:
            self.score+=1
            print("You got it right!")
        else:
            print("That's wrong. ")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")





        # if choice=="True":
        #     score+=1
        #     total_qs=self.question_number
        #     if choice==current_question.answer:
        #         print("You got it right! ")
        #         print(f"The correct answer was: {current_question.answer}")
        #         print(f"Your current score is: {score/self.question_number}")

