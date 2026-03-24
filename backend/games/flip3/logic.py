import random

deck = [0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
current_deck = deck.copy()

p1 = {'hand': [], 'points': 0, 'status': True}
p2 = {'hand': [], 'points': 0, 'status': True}

def draw_card(current_deck, player):
    pulled_card = deck[random.randint(0 ,len(current_deck)-1)]
    current_deck.remove(pulled_card)
    player['hand'].append(pulled_card)
    print(player['hand'])
    return(current_deck, player['hand'])

def check_end(player):
    if len(player['hand']) != len(set(player['hand'])):
        print("Player has a duplicate card. This player is out for the round")
        return False
    else:
        print("Player may continue")
        return None

def add_points(player):
    for card in player['hand']:
        player['points'] += card
    return player['points']

def change_turn(player):
    print(player['status'])

change_turn(p1)