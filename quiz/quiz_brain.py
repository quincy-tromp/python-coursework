class QuizBrain:
    '''Models a quiz'''
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_question(self):
        '''Returns True if there are still questions to be answered in the quiz list, 
        False if there's no more questions.'''
        return self.question_number < len(self.question_list)

    def next_question(self):
        '''Ask player the current question.'''
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        player_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").title()  
        self.check_answer(player_answer, current_question.answer)

    def check_answer(self, player_answer, correct_answer):
        '''Checks if the player's answer is right or wrong.'''
        if player_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")       