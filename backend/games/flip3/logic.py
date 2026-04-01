import random
from deck import deck
from players import players

current_deck = deck.copy()
current_player = 2

def draw_card(current_deck, current_player):
    pulled_card = deck[random.randint(0 ,len(current_deck)-1)]
    current_deck.remove(pulled_card)
    current_player["cards"].append(pulled_card)
    print(current_player["cards"])
    return(current_player)

def change_players(current_player):
    i = 0
    game_active = True
    num_of_players = len(players)
    for player in players:
        if player["active"] == True:
            continue
        else:
            game_active = False
            return
    while i < num_of_players:
        next_player = current_player + i
        if next_player >= num_of_players:
            next_player = next_player - 3
        if players[next_player]["active"] == True:
            return(players[next_player])
        i += 1
    
print(change_players(current_player))