"""This is my playground Where I mess around with code to see if my ideas
work without creating a bunch of random code inside a project"""

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
                print (letter)
                string = string.replace(letter,'')

    print (f'If we remove all of the vowels we are left with "{string}"')
print(vowelRemove(userInfo()))