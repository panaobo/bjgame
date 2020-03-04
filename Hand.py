import collections
import json


class Hand:
    def __init__(self):
        self.cards = collections.defaultdict(list)
        # index 0 means hard hand
        # index 1 means soft hand
        self.value = collections.defaultdict(list)

    def add_card(self, card, hand):
        self.cards[hand].append(card)
        self.calculate_value(card, hand)

    #
    # Calculate value on every card draw
    #
    def calculate_value(self, card, hand):
        # Dealing the first 2 cards
        card_value = card.get_value()
        if len(self.value[hand]) == 0:
            self.value[hand].insert(0, card_value)
            self.value[hand].insert(1, 11 if card_value == 1 else card_value)
        else:
            self.value[hand][0] += card_value
            self.value[hand][1] += 11 if card_value == 1 else card_value

    # TODO
    def split_card(self):
        return self.cards

    def get_max_by_hand(self, hand):
        if 21 >= self.get_soft_hand(hand) > self.get_hard_hand(hand):
            return self.get_soft_hand(hand)
        else:
            return self.get_hard_hand(hand)

    def get_hard_hand(self, hand):
        return self.value[hand][0]

    def get_soft_hand(self, hand):
        return self.value[hand][1]

    def display(self):
        print("***** Player Hands *****")
        for key, values in self.cards.items():
            print("This is Hand: ", key)
            print("Cards: ")
            for value in values:
                print(value)
        print("***** End Player Hands *****")
