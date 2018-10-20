""" This is Project Two of the projects I am practicing from PracticePython.com"""

"""Exercise 2

Ask the user for a number. Depending on whether the number is even or odd, print out
an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:
    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
    If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

def oddOrEven():
    value = input("Please enter a number and we wil see if it is odd or even: ")
    if isinstance(value, str):
        return ("This is not a number")

    else:
        return ("This is False!")

print(oddOrEven())
