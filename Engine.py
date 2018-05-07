from Suit import Suit
from Card import Card
from CardValue import CardValue

def _32_cards():
    return [Card(card_value, suit) for card_value in CardValue for suit in Suit]

if __name__ == '__main__':
    for card in _32_cards():
        print(str(card.card_value) + " " + str(card.suit))