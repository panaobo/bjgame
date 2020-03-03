import collections
import json

class Hand:
    def __init__(self):
        self.cards = collections.defaultdict(list)
        self.value = {1: 0}

    def add_card(self, card, hand):
        self.cards[hand].append(card)
        self.calculate_value(card, hand)

    #
    # Calculate value on every card draw
    #
    def calculate_value(self, card, hand):
        has_ace = False
        if card.value.isnumeric():
            self.value[hand] += int(card.value)
        else:
            if card.value == "A":
                has_ace = True
                self.value[hand] += 11
            else:
                self.value[hand] += 10

        if has_ace and self.value[hand] > 21:
            self.value -= 10

    # TODO
    def split_card(self):
        return self.cards

    def get_value_by_hand(self, hand):
        return self.value[hand]

    def display(self):
        print("***** Player Hands *****")
        for key, values in self.cards.items():
            print("This is Hand: ", key)
            print("Cards: ")
            for value in values:
                print(value)
        print("***** End Player Hands *****")



