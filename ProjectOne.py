"""This is excerise 1 found on PracticePython.org"""

"""Character Input:
    Create a program that asks the user to enter their name and their age. Print out a 
    mesasge addressed to them that tells them the year that they will turn 100 yearse old.
    
    Extras: 
            Add on to the previous program by asking the user for another number and printing out that many copies of 
            the previous message. (Hint: order of operations exists in Python)
            Print out that many copies of the previous message on separate lines. 
            (Hint: the string "\n is the same as pressing the ENTER button)
 """
"""Things I want to change in Future Versions: \n

    Figure out a more optimal way for the while loops with t
    Add More ways to detect wrong answers of age, and name"""


def userInfo():
    print ("Hello! This program is a basic program that \n"
           "Will ask you for your name and age, Then we will \n"
           "calculate the time till you are 100 Years Old.")
    t = True
    while t == True:
        name = input("What is your name? ")
        if len(name) <= 0:
            print("That Is Not A Name Try Again")
        else:
            print("Hello " + name)
            t = False
    t = True
    while t == True:
        age = input("What is your age? ")
        if (len(age) <= 0 or int(age) > 123):
            print("That Is Not Possible Please Try again")
        else:
            print("Hello %s, It Looks Like You Are %s Years Old" % (name,age))
            t = False
    return age

age

def TimeTillOld(age):
    TimeTillOH = 100 - int(age)
    print("Since You Are %s It Is Going To Be %d Years Till You Are 100 Years Old" % (age, TimeTillOld()))
print(TimeTillOld(age))