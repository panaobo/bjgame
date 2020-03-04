import collections
import json


class Hand:
    def __init__(self):
        self.cards = collections.defaultdict(list)
        # index 0 means hard hand
        # index 1 means soft hand
        self.value = collections.defaultdict(list)

    def add_card(self, card, hand_num):
        self.cards[hand_num].append(card)
        self.calculate_value(card, hand_num)

    #
    # Calculate value on every card draw
    #
    def calculate_value(self, card, hand_num):
        # Dealing the first 2 cards
        card_value = card.get_value()
        if len(self.value[hand_num]) == 0:
            self.value[hand_num].insert(0, card_value)
            self.value[hand_num].insert(1, 11 if card_value == 1 else card_value)
        else:
            self.value[hand_num][0] += card_value
            self.value[hand_num][1] += 11 if card_value == 1 else card_value

    # TODO
    def split_card(self):
        return self.cards

    def get_max_by_hand(self, hand_num):
        if 21 >= self.get_soft_hand(hand_num) > self.get_hard_hand(hand_num):
            return self.get_soft_hand(hand_num)
        else:
            return self.get_hard_hand(hand_num)

    def get_hard_hand(self, hand_num):
        return self.value[hand_num][0]

    def get_soft_hand(self, hand_num):
        return self.value[hand_num][1]

    def display(self, name):
        print("***** {} Hands *****".format(name))
        for key, values in self.cards.items():
            print("This is Hand: ", key)
            print("Cards: ")
            for value in values:
                print(value)
        print("***** {}  End Hands *****".format(name))

    def __str__(self):
        all_hands = ""
        for key, values in self.cards.items():
            hand = "This is hand {} : ".format(key)
            cards = ""
            for value in values:
                cards = cards + str(value) + ", "
            all_hands = all_hands + \
                        hand + cards
        return all_hands
