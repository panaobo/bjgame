from Deck import Deck
from Dealer import Dealer
from Player import Player
from Hand import Hand
from Strategy import Strategy


class Game:
    num_of_decks = 6

    def __init__(self):
        self.deck = Deck()
        self.deck.set_x_decks(self.num_of_decks)
        self.deck.shuffle()
        # 1 Dealer with 1 Player
        self.dealer = Dealer(Hand())
        self.player = Player(Hand())
        # Control the whole game
        self.playing = True
        # Control one hand
        self.game_over = False

    def play(self):

        while self.playing:
            for i in range(2):
                self.dealer.hand.add_card(self.deck.deal(), 1)
                self.player.hand.add_card(self.deck.deal(), 1)

            self.player.display()
            print()
            self.dealer.display()

            self.check_blackjack()

            while not self.game_over:
                hand = 1
                player_turn = True

                # Player's turn
                choice = input("Please choose [Hit / Stick] ").lower()
                while choice not in ["h", "s", "hit", "stick"] and player_turn:
                    choice = input("Please enter 'hit' or 'stick' (or H/S) ").lower()

                    if choice in ['hit', 'h']:
                        self.player.hand.add_card(self.deck.deal(), 1)
                        self.player.display()
                    elif choice in ['stick', 's']:
                        player_turn = False

                    if self.player_is_over(hand):
                        self.game_over = True
                        player_turn = False
                        print("You Lost!")

                # Dealer's turn
                Strategy.dealer_strategy(self.dealer.hand, self.deck)
                self.check_final_result(hand)
                self.play_again()
                self.game_over = True

    def check_blackjack(self):
        if self.player.hand.get_max_by_hand(1) == 21 or self.dealer.hand.get_max_by_hand(1) == 21:
            print("game over")
            print(self.dealer.show_all())
            self.game_over = True

    def player_is_over(self, hand):
        return self.player.hand.get_max_by_hand(hand) > 21

    def check_final_result(self, hand):
        print("Final Results")
        print("Your Hand: ", self.player.hand.display())
        print("Dealer's Hand: ", self.dealer.hand.display())

        player_value = self.player.hand.get_max_by_hand(hand)
        dealer_value = self.dealer.hand.get_max_by_hand(hand)

        if player_value > dealer_value:
            print("Player Win!")
        elif dealer_value > player_value:
            print("Dealer Win!")
        else:
            print("Draw Game!")

    def play_again(self):
        again = input("Play Again? [Y/N] ")
        while again.lower() not in ["y", "n"]:
            again = input("Please enter Y or N ")
        if again.lower() == "n":
            print("Thanks for playing!")
            self.playing = False
        else:
            # Refresh hand
            self.dealer = Dealer(Hand())
            self.player = Player(Hand())


if __name__ == "__main__":
    game = Game()
    game.play()
