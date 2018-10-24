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

"""------Subjectivly Better Version-------"""

import random

def guess_game():

    rand_num = random.randint(1,10)
    count = 0
    my_num = None

    while my_num != rand_num and my_num != "exit":
        my_num = input("I am thinking of a number between 1 & 9. Or 'exit' ")

        if my_num.lower() == "exit":
            break
        
        my_num = int(my_num)
        
        if my_num < 1 or my_num > 9:
            print ("That is not a valid option, try again.") 
        
        elif my_num > rand_num:
            count += 1
            print ("My number is lower...")

        elif my_num < rand_num:
            count += 1
            print ("My number is bigger...")

        elif my_num == rand_num:
            count += 1
            print (f"{my_num} Correct! You guessed right in {count} guesses")

