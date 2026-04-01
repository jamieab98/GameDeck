from deck import deck
from players import players
import random

CurrentDeck = deck.copy()
CurrentPlayers = players.copy()

def FlipCard(CurrentDeck, CurrentPlayers):
    NumberOfCards = len(CurrentDeck)
    PlayingPlayer = [player for player in CurrentPlayers if player["Turn"]][0]
    PulledCard = CurrentDeck[random.randint(0,NumberOfCards)]
    CurrentDeck.remove(PulledCard)
    PlayingPlayer["Hand"].append(PulledCard)
    return

def NextPlayer(CurrentPlayers):
    
    return

def CheckDup():
    return

def GiveCard():
    return

def Freeze():
    return

def Flip3():
    return

def Stop():
    return

#FlipCard(CurrentDeck, CurrentPlayers)
NextPlayer(CurrentPlayers)