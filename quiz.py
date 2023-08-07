from random import randint, choice
class User:
    def __init__(self):
        self.__QAs =[]
        self.__totalScore=0
        self.__continuety = False
        
    def addQA(self, q, a):
       self.__QAs.append((q, a))
       
   
    def getLastQA(self):
        lastQA = self.__QAs[-1]
        return lastQA
    
    def getAllQAs(self):
        return self.__QAs
        
    def addScore(self, n):
        self.__totalScore +=n
        
    def getTotalScore(self):
        return self.__totalScore
        
    def continues(self):
        return self.__continuety
        
    def setContinuety(self, cont):
        self.__continuety = cont
    
"""**************************************"""

class Question:
    pass
    
    def __init__(self, difficulty):
        self.__term1 = randint(1, difficulty)
        self.__term2 = randint(1, difficulty)
        self.__operator = choice(["+", "-", "×", "/"])
        
        
    def getTerm1(self):
        return self.__term1
    
    def getTerm2(self):
        return self.__term2
    
    def evaluate(self):
        t1 = self.getTerm1()
        t2 = self.getTerm2()
        o = self.__operator
        
        value = t1 + t2 if o=="+" else t1-t2 if o== "-" else t1*t2 if o=="×" else t1/t2
        
        return value
    
    def __str__(self):
        t1 = self.getTerm1()
        t2 = self.getTerm2()
        o = self.__operator
        return str(t1) + " "+ o +" "+str(t2) +" = "
        
      

    
    
#"""**************************************"""

class Feedback:
    def __init__(self, qAs, calback):
        self.__qAs = qAs
        self.__tester = calback
        
    def __str__(self):
        qAs = self.__qAs
        feedback = """
 *************************
        FEEDBACK
            
             """
        for i in range(len(qAs)):
            qa = qAs[i]
            q, a = qa
            feedback +=str(1+i) +". "+str(q) + " " + str(a) + (""" Correct\n
            """ if self.__tester((q, a)) else " Wrong, Correction: " + str(q.evaluate()) ) + ""
            
            
        return feedback+ """
 *************************"""
    



"""**************************************"""

class Summary:
    
    def __init__(self, user, level):
        self.__user = user
        self.__level = level
        
    def getTotalQuestion(self):
        questions= self.__user.getAllQAs()
        total = len(questions)
        return total
        
    def getTotalScore(self):
        return self.__user.getTotalScore()
        
    def getCorrectAnswer(self):
        qAs = self.__user.getAllQAs()
        correctQAs = [qa for qa in qAs if isCorrect(qa)]
        return len(correctQAs)
        
    def getWrongAnswer(self):
        qAs = self.__user.getAllQAs()
        allQAs = len(qAs)
        correctQA = [qa for qa in qAs if isCorrect(qa)]
        return allQAs - len(correctQA)
        
     
    def getLevel(self):
        return self.__level;
        
    def getRelativeScore(self):
        allQAs = self.__user.getAllQAs()
        totalQuest = len(allQAs)
        totalCrct = self.getCorrectAnswer()
        
        relativeScore = (totalCrct/totalQuest) * 100
        return relativeScore
        
        
    def __str__(self):
        return """_______________________________ """ + """
        Summary 
        Level: """ + str(self.getLevel()) + """
        Total questions: """ + str(self.getTotalQuestion()) + """
        Total Scores: """ + str(self.getTotalScore()) + """
        Correct answers:  """ + str(self.getTotalScore()) + """
        Wrong answers: """ + str(self.getWrongAnswer()) + """''
        Relative score: """ + str(self.getRelativeScore()) + """
_______________________________"""
    



"""**************************************"""

    
def isCorrect(qa):
    q, a = qa
    value = q.evaluate()
    return value == a
    
    
    
   