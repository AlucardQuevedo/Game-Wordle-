import random
import math

def CheckRightandRight(guess_as_list,actual_combo):
    index=0
    correctNum=["X","X","X","X","X"]
    while index<len(guess_as_list):
        if actual_combo[index]==guess_as_list[index]:
            correctNum.pop(index)
            correctNum.insert(index,actual_combo[index])
        elif guess_as_list[index] in actual_combo:
            correctNum.pop(index)
            correctNum.insert(index,"O")
        index=index+1
    return correctNum
        
def randomCombo():
    return random.sample(["0","1","2","3","4","5","6","7","8","9"], 5)
#Chatgpt let us know about this


print("YO this is our wordle game")
print("We basically gonna think of a 5 digits combo")
print("Then you gonna guess it")
print("If you get the right number and in right place, we'll put the number")
print("If you get the right number but not the right place, we'll put O")
print("If you get the wrong number, we'll put an X")
print("\n\nYou got 5 chances, _ _ _ _ _")
FrCombo=randomCombo()
remainingTries=5
solved=False

#Starts the Loop of asking
while remainingTries > 0 and solved==False:
    guess=input()

    if CheckRightandRight(guess,FrCombo)==FrCombo:
        print (CheckRightandRight(guess,FrCombo))
        solved=True
    else: 
        print (CheckRightandRight(guess,FrCombo))
        remainingTries=remainingTries-1

#Death Screen
if remainingTries==0:
    print("Sorry dawg you didn't win\n\n"
    "correct combo was," ,FrCombo)

#The Win Screen
if solved==True:
    print ("\n\nAYE GOOD JOB YOU GOT THE COMBOO CORRECT") 








# TESTING
# guess=input()
# guess=list(guess)
# print(guess)
# yare = randomCombo()
# baka= ["1","2","3","4","5"]
# print(yare)
# print(CheckRightandRight(guess,yare))
