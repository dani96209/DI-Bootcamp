def answers_questions():
    questions_asks =  {"What is Baby Yoda's real name?": "grogu",
        "Where did Obi-Wan take Luke after his birth?":"tatooine",
         "What year did the first Star Wars movie come out?": "1977",
         "Who built C-3PO?": "anakin skywalker",
         "Anakin Skywalker grew up to be who?": "darth vader",
        "What species is Chewbacca?": "wookiee"}
    correct_answers=0
    incorrect_answers=0
    wrong_answers=[]
    
    for question,answer in questions_asks.items():
      user_answer=input(question)
      if user_answer == answer:
            correct_answers += 1
      else:
            incorrect_answers += 1
            wrong_answers.append((question, user_answer))
    
    print( correct_answers, incorrect_answers, wrong_answers)
    return correct_answers, incorrect_answers, wrong_answers
answers_questions()

def information_correct_incorrect_answers():
      
      correct_answers, incorrect_answers, wrong_answers = answers_questions()
      print(f"The number of incorrect answers is {incorrect_answers}")
      print(f" The number of good answers is {correct_answers} ")

information_correct_incorrect_answers()


      

