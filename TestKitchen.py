"""This is my playground Where I mess around with code to see if my ideas
work without creating a bunch of random code inside a project"""

import re

ones = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine'}
tens = {2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety'}
special = {10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen'}

def numberToWord(number):
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
            for i in tens:
                if number == (tens):
                    for i in number:
                        return False



print (numberToWord(22))

#But If We Want The Reverse Of This