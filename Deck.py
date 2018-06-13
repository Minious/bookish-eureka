from CardValue import CardValue
from Card import Card
from Suit import Suit


class Deck:

    def __init__(self):
        self.cards = []

    @property
    def __32_cards(self):
        return [Card(card_value, suit) for card_value in CardValue for suit in Suit]
