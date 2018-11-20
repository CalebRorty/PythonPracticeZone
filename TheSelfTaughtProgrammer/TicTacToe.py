board = ['_'] * 9
whoUp = 1
def print_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])
def playerInput():
    place = input("Please Enter The Spot You Want To Go At (1-9)")
    return place



def move_up(place, whoUp):
    try:
        int(place)
        if int(place) > 9 or int(place) < 0:
            print ('That is not move!')
            print('Go Again.')
            whoUp -= 1
        elif board[int(place) - 1] != '_':
            print('That is not a valid move! Somebody is already in that spot.')
            print('Go Again.')
            whoUp -= 1
        else:
            if whoUp % 2 == 0:
                board[int(place) - 1] = 'O'
            else:
                board[int(place) - 1] = 'X'
    except ValueError:
        print('Not Valid Input')
        print('Go Again.')

        whoUp -= 1
    return whoUp
def game(whoUp):
    done = False
    while not done:
        1print_board()
        whoUp = move_up(playerInput(), whoUp)
        whoUp += 1

        # WIN Check Code
        if ((board[0] in board[1] and board[0] in board[2] and board[0] != '_') or
                (board[3] in board[4] and board[3] in board[5] and board[3] != '_') or
                (board[6] in board[7] and board[6] in board[8] and board[6] != '_') or
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
                print('Player O Won!')
            else:
                print('Player X Won!')
            done = True


game(whoUp)