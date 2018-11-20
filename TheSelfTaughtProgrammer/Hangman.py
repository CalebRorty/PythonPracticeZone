def hangman_board():
    loop = True
    wrong_guesses = 1
    stages = ["", "________      ", "|      |      ",
              "|      0      ", "|     /|\     ",
              "|     / \     ", "|","|________      "]
    while loop:
        if wrong_guesses < len(stages):
            print('\n'.join(stages[0:wrong_guesses+1]))
            wrong_guesses += 1
        else:
            loop = False

def answer_board():
    word = 'caat'
    wrong_guesses = 1
    letters_left = len(word)
    guess_board = "__ " * len(word)
    guess_board = ''.join(list(guess_board))
    print('Guess #' + str(wrong_guesses))
    wrong_guesses += 1
    # how we calc total number of wrong guesses


def user_guess():
    place = []
    answer = 'caat'
    answer = list(answer)
    guess = input('Guess A Letter')
    if guess in answer:
        print(len(answer))
        for i in range(0, len(answer)):
            if guess == answer[i]:
                place.append(i)
    return place

hangman_board()