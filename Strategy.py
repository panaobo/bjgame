class Strategy:

    def __init__(self):
        pass

    # Hit on soft 17
    @staticmethod
    def dealer_strategy(hand, deck):
        # Dealer should just have 1 hand
        hand_num = 1
        while True:
            if hand.get_hard_hand(hand_num) >= 17:
                break
            elif hand.get_soft_hand(hand_num) > 17:
                if hand.get_hard_hand(hand_num) < 17:
                    hand.add_card(deck.deal(), hand_num)
                break
            else:
                hand.add_card(deck.deal(), hand_num)

