import random

rNumber = random.randint(1,10)


def guessGame():
    done = False
    while not done:
        userGuess = input("Please guess a number between 1-9 ")
        intGuess = int(userGuess)
        retStr = ""
        if intGuess == rNumber:
          retStr += "That is correct!"
          done += True
        elif intGuess > rNumber:
           print ("That is too high!")
        elif intGuess < rNumber:
          print ("That is to low!")
    return retStr
    
print(guessGame())
