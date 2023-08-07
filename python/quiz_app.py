from quiz import *
from prompts import *
is_taking = True

while is_taking:
    user = User()
    dif_level = eval(input(DIFFICULTY)) *100
    user.setContinuety(True)
    while user.continues():
        question = Question(dif_level)
        ans = eval(input(question))
        user.addQA(question, ans)
        qa = user.getLastQA()
        if isCorrect(qa):
            user.addScore(1)
            print("Correct!")
        else:
            print("Wrong!")
        print("Total score:  "+ str(user.getTotalScore()))
        continues = input(CONTINUETY)
        continues = bool(eval(continues))
        user.setContinuety(continues)
    
    feedback = Feedback(user)
    summary = Summary(user, level)
    print(feedback)
    print(summary)
    retakes = eval(input(RETAKING_PROMPT))
    


