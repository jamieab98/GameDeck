import random

deck = [0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
current_deck = deck.copy()

p1_hand = []
p2_hand = []

def draw_card(current_deck, player_hand):
    pulled_card = deck[random.randint(0 ,len(current_deck)-1)]
    current_deck.remove(pulled_card)
    player_hand.append(pulled_card)
    return (current_deck, player_hand)

print(draw_card(current_deck, p1_hand))
print(draw_card(current_deck, p2_hand))
print(draw_card(current_deck, p1_hand))
print(draw_card(current_deck, p2_hand))