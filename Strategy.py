class Strategy:

    def __init__(self):
        pass

    # Hit on soft 17
    @staticmethod
    def dealer_strategy(hand, deck):
        hit = True
        while hit:
            if hand.get_soft_hand(hand) <= 17 and hand.get_hard_hand(hand) < 17:
                hand.add_card(deck.deal(), 1)

