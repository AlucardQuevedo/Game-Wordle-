

import random
import math

def CheckIndex(guess_as_list,actual_combo):
    x="yes"
    i=0
    for letter in guess_as_list:
        while i<len(actual_combo):
            check

    actual_combo


def randomCombo ():
    numList=[0,1,2,3,4,5,6,7,8,9]
    randomCombo = []
    for i in range (4):
        randomIndex=random.randint[0,len(numList)]
        randomCombo.append(randomIndex)
        
    return randomCombo
        
  





print("YO this is our wordle game")
print("We basically gonna think of a 5 digits combo")
print("Then you gonna guess it")
print("If you get the right number and in right place, we'll put the number")
print("If you get the right number but not the right place, we'll put O")
print("If you get the wrong number, we'll put an X")
print("\n\nYou got 5 chances, _ _ _ _ _")
guess=input()
guess=list(guess)
print(guess)



