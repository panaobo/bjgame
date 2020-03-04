class Strategy:

    def __init__(self):
        pass

    # Hit on soft 17
    @staticmethod
    def dealer_strategy(hand, deck):
        # Dealer should just have 1 hand
        while True:
            if hand.get_hard_hand() >= 17:
                break
            elif 21 >= hand.get_soft_hand() > 17:
                break
            else:
                hand.add_card(deck.deal())

    # Basic player strategy
    # No Split or Double down
    @staticmethod
    def player_strategy(hand, deck):
        while True:
            while True:
                if hand.get_hard_hand() >= 17:
                    break
                elif 21 >= hand.get_soft_hand() > 17:
                    break
                else:
                    hand.add_card(deck.deal())
