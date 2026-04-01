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
        
def randomCombo ():
    numList=["0","1","2","3","4","5","6","7","8","9"]
    randomCombos = []
    for i in range (5):
        randomIndex=random.randint(0,len(numList))
        randomCombos.append(randomIndex)
    return randomCombos



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
yare = randomCombo()
baka= ["1","2","3","4","5"]
print(randomCombo())
print(CheckRightandRight(guess,yare))




