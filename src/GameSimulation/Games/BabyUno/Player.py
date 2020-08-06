from ..Base import Player as BasePlayer


class Player(BasePlayer):
    """
    Basic Uno Player
    """

    @staticmethod
    def get_options_filter(open_card):
        """

        :param hand:
        :param open_card:
        :return:
        """
        return lambda c: c.symbol == open_card.symbol or c.number == open_card.number

    def play(self, game):
        """
        plays a card, or take one from the draw pile
        :param game:
        :return:
        """
        options = list(filter(Player.get_options_filter(game.stack.last_card), self.hand))
        if not options:
            self.receive(game.draw_pile.pop())
            return game, "draw a card"
        choice = options[0]
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
