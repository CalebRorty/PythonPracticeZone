"""This is a program that takes a number you input and returns it back as a number in-words or vise versa
    EX:
        20 = Twenty
        Twenty = 20
"""

from time import sleep
ones = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine'}
tens = {2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety'}
special = {10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen'}
alphaB = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

wOnes = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6',
         'seven': '7', 'eight': '8', 'nine': '9',
         'ten': '10', 'forty': '4', 'fifty': '5', 'sixty': '6'}
wSpecial = {'Eleven':'11', 'Twelve':'12', 'Thirteen':'13', 'Fourteen':'14', 'Fifteen':'15',
            'Sixteen':'16', 'Seventeen':'17', 'Eighteen':'18', 'Nineteen':'19',
            'Twenty':'9', 'Thirty': '3', 'Seventy': '7', 'Eighty': '8', 'Ninety': '9'}

print("This Program Converts A Number To It's In-Words Version, Or Vise Versa")
number = input("What number would you like to use? ")
def numberToWord(number):
    print ("Computing...")
    sleep(1)
    number = int(number)
    if number < 10:
        for key in ones:
            if number == key:
                return (ones[number])
    elif number == 10:
        return special[10]
    elif (number > 10 and number < 20):
        for key in special:
            if number == key:
                return (special[number])
    elif number >= 20:
        nNumber = number // 10
        rNumber = number % 10
        for i in tens:
            if nNumber == i:
                return (tens[nNumber] + '-' + ones[rNumber])
    else:
        return ("Zero")

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



