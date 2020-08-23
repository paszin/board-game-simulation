from .Player import Player as BaseUnoPlayer


class Player(BaseUnoPlayer):
    """
    Basic Uno Player
    """

    def play(self, game):
        """
        plays a card, or take one from the draw pile
        :param game:
        :return:
        """
        options = list(filter(Player.get_options_filter(game.stack.last_card), self.hand))
        if not options:
            new_card = game.draw_pile.pop()
            print("You are out of options, here is a new card:", new_card)
            self.receive(new_card)
            return game, "draw a card"
        print("Your hand: ", self.hand)
        print("Enter the number of the card you want to play")
        for i, card in enumerate(options, start=1):
            print(f"{i}: {card}")
        choice_i = int(input())
        choice = options[choice_i - 1]
        self.drop(choice)
        game.stack.push(choice)
        if not self.hand:
            raise RuntimeError("Player wins!")
        return game, "play a card"

    def finish_turn(self, game):
        """
        do nothing
        :param game:
        :return:
        """
        return game
