import random

deck = [0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
current_deck = deck.copy()

p1 = {'player': 'P1', 'hand': [], 'points': 0, 'status': False}
p2 = {'player': 'P2', 'hand': [], 'points': 0, 'status': True}

def draw_card(current_deck, player):
    pulled_card = deck[random.randint(0 ,len(current_deck)-1)]
    current_deck.remove(pulled_card)
    player['hand'].append(pulled_card)
    print(player['hand'])
    return(current_deck, player['hand'])

def check_end(player):
    if len(player['hand']) != len(set(player['hand'])):
        player['status'] = False
    else:
        print("Player may continue")
        return None

def add_points(player):
    for card in player['hand']:
        player['points'] += card
    player['status'] = False
    return player['points']

def change_turn(player):
    if p1['status'] == False and p2['status'] == False:
        next_player = None
    elif player == p1 and p2['status'] == True:
        next_player = p2
    elif player == p1 and p2['status'] == False:
        next_player = p1
    elif player == p2 and p1['status'] == True:
        next_player = p1
    elif player == p2 and p1['status'] == False:
        next_player = p2
    return next_player

