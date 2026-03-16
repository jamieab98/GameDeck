def new_board():
    board = ['', '', '', '', '', '', '', '', '']
    print(board)

def apply_move(board, player, location):
    #make sure the move is valid
    if board[location] != '':
        print("You cannot make a move there")
    if board[location] == '':
        print(f'{player} is making a move at location: {location}')
        
    #apply the player's move to the location

    #update the board

    return

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

board = ['X', '', '', '', '', '', '', '', '']
players = ["P1", "P2"]
apply_move(board, "p1", 0)