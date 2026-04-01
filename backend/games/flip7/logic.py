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

def ChangePlayers(CurrentPlayers):
    NumberOfPlayers = len(CurrentPlayers)
    RecentPlayer = [player for player in CurrentPlayers if player["Turn"]][0]
    RecentPlayerPosition = RecentPlayer["Position"]
    i = 0
    while i < NumberOfPlayers:
        j = i + RecentPlayerPosition
        if j >= NumberOfPlayers:
            j -= 4
        if CurrentPlayers[j]["Active"] == True:
            RecentPlayer["Turn"] = False
            CurrentPlayers[j]["Turn"] = True
            NextPlayer = CurrentPlayers[j]
            return
        i += 1
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
ChangePlayers(CurrentPlayers)