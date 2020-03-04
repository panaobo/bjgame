class Player:

    def __init__(self, name, hands):
        self.hands = hands
        self.name = name

    def display(self):
        for hand in self.hands:
            hand.display(self.name)
