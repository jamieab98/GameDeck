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
    #see if the winning conditions have been met

    #if a player has won, return the winner

    #if no player has won, do nothing

    return

def check_tie(board):
    #see if the board has been filled with no winning conditions

    #if a game is a tie, return that the game is a tie

    return

def next_player(player):
    #check who just took a valid turn
    
    #switch to the other player

    return 

board = ['', '', '', '', '', '', '', '', '']
players = ["P1", "P2"]
apply_move(board, "P1", 0)
apply_move(board, "P2", 1)