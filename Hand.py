import collections

class Hand:
    def __init__(self):
        self.cards = []
        # index 0 means hard hand
        # index 1 means soft hand
        self.value = []

    def add_card(self, card):
        self.cards.append(card)
        self.calculate_value(card)

    #
    # Calculate value on every card draw
    #
    def calculate_value(self, card):
        # Dealing the first 2 cards
        card_value = card.get_value()
        if len(self.value) == 0:
            self.value.insert(0, card_value)
            self.value.insert(1, 11 if card_value == 1 else card_value)
        else:
            self.value[0] += card_value
            self.value[1] += 11 if card_value == 1 else card_value

    # TODO
    def split_card(self):
        return self.cards

    def get_max_by_hand(self):
        if 21 >= self.get_soft_hand() > self.get_hard_hand():
            return self.get_soft_hand()
        else:
            return self.get_hard_hand()

    def get_hard_hand(self):
        return self.value[0]

    def get_soft_hand(self):
        return self.value[1]

    def display(self, name):
        print("***** {} Hands *****".format(name))
        print(*self.cards, sep='\n')
        print("***** {}  End Hands *****".format(name))

    def __str__(self):
        cards = []
        for card in self.cards:
            cards.append(str(card))
        return ', '.join(cards)
