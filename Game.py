from Deck import Deck
from Dealer import Dealer
from Player import Player
from Hand import Hand
from Strategy import Strategy


class Game:
    num_of_decks = 6
    initial_card_num = 2

    def __init__(self):
        self.deck = Deck()
        self.deck.set_x_decks(self.num_of_decks)
        self.deck.shuffle()
        # 1 Dealer with 1 Player
        self.dealer = Dealer(Hand())
        # Player can have multiple hands
        self.player = Player("tutu", [Hand()])
        # Control the whole game
        self.playing = True
        # Control one hand
        self.game_over = False
        # Control player decision round
        self.player_turn = True

    def play(self):

        while self.playing:
            for i in range(self.initial_card_num):
                self.dealer.hand.add_card(self.deck.deal())
                # TODO
                self.player.hands[0].add_card(self.deck.deal())

            self.player.display()
            print()
            self.dealer.display()

            self.check_blackjack()

            while not self.game_over:
                # Player's turn
                print()
                choice = input("Please enter 'hit' or 'stand' (or H/S) ").lower()
                while choice in ["h", "s", "hit", "stick"] and self.player_turn:

                    if choice in ['hit', 'h']:
                        print("___Player Hit___")
                        self.player.hands[0].add_card(self.deck.deal())
                        self.player.display()
                    elif choice in ['stand', 's']:
                        self.player_turn = False
                        break

                    if self.player_is_over():
                        self.game_over = True
                        self.player_turn = False
                        print("You Lost!")
                    else:
                        choice = input("Please enter 'hit' or 'stick' (or H/S) ").lower()

                # Dealer's turn
                if self.game_over:
                    self.dealer.show_all()
                else:
                    Strategy.dealer_strategy(self.dealer.hand, self.deck)
                    self.check_final_result()
                    self.game_over = True
            self.play_again()

    def check_blackjack(self):
        # TODO
        if self.player.hands[0].get_max_by_hand() == 21 or self.dealer.hand.get_max_by_hand() == 21:
            print("game over")
            print(self.dealer.show_all())
            self.game_over = True

    def player_is_over(self):
        # TODO
        if self.player.hands[0].get_max_by_hand() > 21:
            print("Player Bust!")
            return True
        return False

    def check_final_result(self):
        print("Final Results : ")
        self.player.display()
        self.dealer.show_all()

        # TODO
        player_value = self.player.hands[0].get_max_by_hand()
        dealer_value = self.dealer.hand.get_max_by_hand()

        if dealer_value > 21:
            print("Dealer Bust")
            print("Player Win!")
        elif dealer_value == player_value:
            print("Draw Game!")
        elif player_value > dealer_value:
            print("Player Win!")
        else:
            print("Dealer Win!")

    def play_again(self):
        again = input("Play Again? [Y/N] ")
        while again.lower() not in ["y", "n"]:
            again = input("Please enter Y or N ")
        if again.lower() == "n":
            print("Thanks for playing!")
            self.playing = False
        else:
            # TODO Refresh hand
            self.dealer = Dealer(Hand())
            self.player = Player("tutu", [Hand()])
            # Reset flag
            self.player_turn = True
            self.game_over = False


if __name__ == "__main__":
    game = Game()
    game.play()
