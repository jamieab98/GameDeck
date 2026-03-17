def new_board():
    board = ['', '', '', '', '', '', '', '', '']
    return board

def apply_move(board, player, location):
    new_board = board.copy()
    #make sure the move is valid
    if new_board[location] != '':
        raise ValueError("That location is alreay occupied")

    #apply the player's move to the location
    if player == "P1":
        symbol = "X"
    else:
        symbol = "O"
    new_board[location] = symbol

    #update the board
    return new_board

def check_winner(board):
    winner_situations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    #see if the winning conditions have been met
    for situation in winner_situations:
        check = []
        for position in situation:
            check.append(board[position])

    #if a player has won, return the winner
        if check[0] == check[1] == check[2] and check[0] != '':
            print("Game over")
            return {'Winner': check[0]}
            
    #if no player has won, do nothing
    return {'Winner': None}

def check_tie(board):
    #see if the board has been filled with no winning conditions

    #if a game is a tie, return that the game is a tie

    return

def next_player(player):
    #check who just took a valid turn
    
    #switch to the other player

    return 

board = ['X', 'X', 'X', '', '', '', '', '', '']

check_winner(board)