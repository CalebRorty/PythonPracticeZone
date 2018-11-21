board = ['_'] * 6 + [' '] * 3
#Creates Traditional Tic-Tac-Toe Board
whoUp = 1
#Creates Variable 'whoUp' odds are X evens are O
def print_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])
    #Prints game board
def playerInput():
    place = input("Please Enter The Spot You Want To Go At (1-9)")
    return place
    #Gets spot where player wants to place item
def move_up(place, whoUp):
    try:
        place = int(place)
        #Checks if value is number or not
        if int(place) > 9 or int(place) < 0:
            #Checks if number is valid move
            print ('That is not move!')
            print('Go Again.')
            whoUp -= 1
        #checks if valid spot on board
        elif place > 0 and place < 7 and board[place - 1] != '_':
            print('That is not a valid move! Somebody is already in that spot.')
            print('Go Again.')
            whoUp -= 1
        elif place > 6 and place < 10 and board[place - 1] != ' ':
            print('That is not a valid move! Somebody is already in that spot.')
            print('Go Again.')
            whoUp -= 1
        #checks if spot already has
        else:
            #Places X or O depending on who is up
            if whoUp % 2 == 0:
                board[place - 1] = 'O'
            else:
                board[place - 1] = 'X'
    except ValueError:
        print('Not Valid Input')
        print('Go Again.')
        whoUp -= 1
    return whoUp
def game(whoUp):
    done = False
    while not done:
        print_board()
        whoUp = move_up(playerInput(), whoUp)
        whoUp += 1

        # WIN Check Code
        if ((board[0] in board[1] and board[0] in board[2] and board[0] != '_') or
                (board[3] in board[4] and board[3] in board[5] and board[3] != '_') or
                (board[6] in board[7] and board[6] in board[8] and board[6] != ' ') or
                # LEFT - RIGHT Wins
                (board[0] in board[3] and board[0] in board[6] and board[0] != '_') or
                (board[1] in board[4] and board[1] in board[7] and board[1] != '_') or
                (board[2] in board[5] and board[2] in board[8] and board[2] != '_') or
                # UP - DOWN Wins
                (board[0] in board[4] and board[0] in board[8] and board[0] != '_') or
                (board[2] in board[4] and board[2] in board[6] and board[2] != '_')):
            # DIAG0NALE Wins

            print_board()
            whoUp += 1
            if whoUp % 2 == 0:
                #Checks who is up, if even then O's are up
                print('Player O Won!')
                break
            else:
                print('Player X Won!')
                break

        if board[0-5] != '_' and board[6-8] != ' ':
            print_board()
            print ("It's A Tie!")
            break
            #Should check for TIE but goes off to soon at certain circumstances



game(whoUp)