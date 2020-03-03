class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return " of ".join((self.suit, self.value))

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value
