from itertools import *
from Card import Card
import random


class Deck:
    def __init__(self):
        self.cards = [
            Card(s, v) for s in ["Spades", "Clubs", "Hearts", "Diamonds"]
            for v in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        ]

    def set_x_decks(self, num):
        self.cards = [card for card in self.cards for _ in range(num)]

    def get_deck(self):
        return self.cards

    # TODO
    # Add more shuffle methods
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)

    def deal_x_cards(self, num):
        card_array = []
        if len(self.cards) > num:
            for x in range(1, num):
                card_array.append(self.cards.pop(0))
        return card_array
