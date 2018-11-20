"""This is a program that asks for a sentence, and removes
   all of the vowels (excluding y) from said sentence"""


vowels = ['a','e','i','o','u']


def userInfo():
    userString = input('Please enter a sentence: ')
    userString = userString.lower()

    return userString

def vowelRemove(string):
    stringLength = len(string)
    for i in range(0,(stringLength+1)):
        letter = (string[(i-1):i])
        for iV in vowels:
            if iV == letter:
                string = string.replace(letter,'')
    print("Computing...")


    return (f'If we remove all of the vowels we are left with "{string}"')

print (vowelRemove(userInfo()))
