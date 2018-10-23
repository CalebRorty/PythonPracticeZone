userInput = input("Please Enter A String ")

def palindrome(userInput):
    return "That is a palindrome" if userInput == userInput[::-1] else "This is not a palindrome"
    
print (palindrome(userInput))
