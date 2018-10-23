"""This is my playground Where I mess around with code to see if my ideas
work without creating a bunch of random code inside a project"""


<<<<<<< HEAD
def duplicate_count(text):
=======

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


list = [160, 3, 1719, 19, 11, 13, -21]

def oddOrEven(number):
    listOdd = []
    listEven = []
    for i in number:
        if i % 2 == 0:
            listEven.append(i)
        else:
            listOdd.append(i)
            
    if len(listEven) < 2:
        return listEven.pop()
    else:

        return list.pop()
    
print (oddOrEven(list))
>>>>>>> 9ae368c65fe5a4d62264bd94af801d9b755fc95a
