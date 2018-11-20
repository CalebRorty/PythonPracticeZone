"""This is a program that takes a number you input and returns it back as a number in-words or vise versa
    EX:
        20 = Twenty
        Twenty = 20
"""

from time import sleep

ones = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
special = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
           17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
tens = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
print("This Program Converts A Number To It's In-Words Version, Or Vise Versa")
number = input("What number would you like to use? ")


def numberToWord(number):
    retStr = ""
    print("Computing...")
    sleep(1)
    number = int(number)

    if number < 0:
        number = abs(number)
        nNumber = number // 10
        rNumber = number % 10
        retStr += ('Negative ' + tens[nNumber] + '-' + ones[rNumber])

    elif number < 10:
        retStr += ones[number]

    elif (number >= 10 and number < 20):
        retStr += special[number]

    elif (number < 100 and number >= 20):
        nNumber = number // 10
        rNumber = number % 10
        retStr += tens[nNumber] + '-' + ones[rNumber]


    return retStr

print (numberToWord(number))

"""def userInfo():
    number = input("What number would you like to convert? ")
    a = number[1:]
    nNumber = number.replace(a, "")
    nNumber = nNumber.lower()
    for i in alphaB:
        if nNumber == i:
            return (wordToNumber(number))

    else:
        return (numberToWord(number))"""



