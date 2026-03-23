import random

deck = [0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

def draw_card(deck):
    pulled_card = deck[random.randint(0 ,len(deck)-1)]
    print(pulled_card)