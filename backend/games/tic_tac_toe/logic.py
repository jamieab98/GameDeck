def new_board():
    board = ['', '', '', '', '', '', '', '', '']
    return board

def apply_move(board, player, location):
    new_board = board.copy()
    if new_board[location] != '':
        raise ValueError("That location is alreay occupied")

    if player == "P1":
        symbol = "X"
    else:
        symbol = "O"
    new_board[location] = symbol

    return new_board

def check_winner(board):
    winner_situations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for situation in winner_situations:
        a,b,c = situation
        if board[a] == board[b] == board[c] and board[a] != '':
            return board[a]
    return None

def check_tie(board):
    if '' not in board:
        return 'Nobody. It is a tie'
    
    else:
        return None

def next_player(player):
    if player == "P1":
        return 'P2'
    else:
        return 'P1'