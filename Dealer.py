from Strategy import Strategy


class Dealer:
    def __init__(self, hand):
        self.hand = hand
        self.strategy = Strategy()

    def display(self):
        print("***** Dealer's Hand *****")
        first_card = self.hand.cards[1][0]
        print("Dealer's first card is : ", first_card)
        print("***** Dealer's Hand End *****")

    def show_all(self):
        print("Dealer's card : ", self.hand.cards[0])
