import random

deck = [0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

current_deck = deck.copy()

def draw_card(current_deck):
    pulled_card = deck[random.randint(0 ,len(current_deck)-1)]
    current_deck.remove(pulled_card)
    return (current_deck, pulled_card)

