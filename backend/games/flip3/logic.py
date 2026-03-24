import random

deck = [0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
current_deck = deck.copy()

p1 = {'player': 'P1', 'hand': [], 'points': 0, 'status': False}
p2 = {'player': 'P2', 'hand': [], 'points': 0, 'status': False}

current_player = p1

def draw_card(current_deck, current_player):
    pulled_card = deck[random.randint(0 ,len(current_deck)-1)]
    current_deck.remove(pulled_card)
    current_player['hand'].append(pulled_card)
    print(current_player)
    return(current_deck, current_player)

def check_end(current_player):
    if len(current_player['hand']) != len(set(current_player['hand'])):
        current_player['status'] = False
    else:
        #print("Player may continue")
        return None

def add_points(current_player):
    for card in current_player['hand']:
        current_player['points'] += card
    current_player['status'] = False
    return current_player['points']

def next_turn(current_player, p1, p2):
    if p1['status'] == False and p2['status'] == False:
        return None
    elif current_player['status'] == True:
        if current_player['player'] == 'P1' and p2['status'] == True:
            return p2
        elif current_player['player'] == 'P2' and p1['status'] == True:
            return p1
        elif current_player['player'] == 'P1' and p2['status'] == False:
            return p1
        elif current_player['player'] == 'P2' and p1['status'] == False:
            return p2
    elif current_player['status'] == False:
        if current_player['player'] == 'P1':
            return p2
        elif current_player['player'] == 'P2':
            return p1