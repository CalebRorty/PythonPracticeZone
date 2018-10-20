"""This is my playground Where I mess around with code to see if my ideas
work without creating a bunch of random code inside a project"""

import re

alphaB = ['abcdefghijklmnopqrstuvwxyz']
number = input("please enter a number: ")
a = number[1:]
nNumber = number.replace(a,"")
print (nNumber)
print (len(nNumber))