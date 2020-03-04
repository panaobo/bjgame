class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return " of ".join((self.value, self.suit))

    def get_suit(self):
        return self.suit

    def get_value(self):
        if self.value.isnumeric():
            return int(self.value)
        elif self.value == "A":
            return 1
        else:
            return 10

