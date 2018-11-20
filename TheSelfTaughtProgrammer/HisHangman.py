def hangman(word):
    wrong_guesses = 0
    stages = ["", "________      ", "|      |      ", "|      0      ", "|     /|\     ", "|     / \     ", "|"]
    remaining_letters = list(word)
    letter_board = ["__"] * len(word)
    #creates bored where you see what correct words you guess
    win = False
    print('Welcome to Hangman')
    while wrong_guesses < len(stages) - 1:
        print('\n')
        guess = input("Guess a letter: ")
        guessed_letters = [x for x in range(0, len(word)) if word[x] == guess]
        #loops through every letter in word, and if it == is true, returns position of where letter was true
        if guess in remaining_letters:
        #if guess is still in list of none guessed letters
            for pos in range(0, len(letter_board)):
            #sets value of pos to == 0-length of letter_board
                if pos in guessed_letters:
                    """If the value of guessed_letters (which === numerical value of position of where number is in list
                   words) is == to the value of pos"""
                    letter_board[pos] = guess
                    #sets value of letter_board position 'pos' == to guess
                    remaining_letters[pos] = '$'
                    #sets value of letter in list of remaining_letters == to $ so it doesnt get re-guessed
        else:
            wrong_guesses += 1
            #adds 1 to wrong_guess to make sure if max guess guessed you lose
        print((' '.join(letter_board)))
        print('\n'.join(stages[0: wrong_guesses + 1]))
        if '__' not in letter_board:
            print('You win! The word was:')
            print(' '.join(letter_board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong_guesses]))
        print('You lose! The words was {}'.format(word))

hangman("caat")