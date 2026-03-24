import random

deck = [0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
current_deck = deck.copy()

p1_hand = []
p2_hand = []

def draw_card(current_deck, player_hand):
    pulled_card = deck[random.randint(0 ,len(current_deck)-1)]
    current_deck.remove(pulled_card)
    player_hand.append(pulled_card)
    print(player_hand)
    return(current_deck, player_hand)

def check_end(player_hand):
    if len(player_hand) != len(set(player_hand)):
        print("Player has a duplicate card. This player is out for the round")
        return False
    else:
        print("Player may continue")
        return None

