class Strategy:

    def __init__(self):
        pass

    # Hit on soft 17
    def dealer_strategy(self, hand, deck):
        if hand.value[1] < 17:
            hand.add_card(deck.deal(), 1)

