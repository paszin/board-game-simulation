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
        return lambda c: c.number == open_card.number \
                         or c.symbol == open_card.symbol and (open_card.number not in ["+2", "+4"] or not open_card.valid) \
                         or c.symbol == "rainbow" and (open_card.number not in ["+2", "+4"] or not open_card.valid)

    def play(self, game):
        """
        plays a card, or take one from the draw pile
        :param game:
        :return:
        """
        if game.stack.last_card.number == "skip" and game.stack.last_card.valid:
            game.stack.last_card.valid = False
            return game, "pause"
        options = list(filter(Player.get_options_filter(game.stack.last_card), self.hand))
        if not options:
            # check for special card
            if game.stack.last_card.number == "+2":
                for draw_card in filter(lambda c: c.valid and c.number == "+2", game.stack):
                    self.receive(game.draw_pile.pop())
                    self.receive(game.draw_pile.pop())
                    draw_card.valid = False
                return game, "draw cards"
            elif game.stack.last_card.number == "+4":
                for _ in range(4):
                    self.receive(game.draw_pile.pop())
                game.stack.last_card.valid = False
                return game, "draw 4 cards"
            else:
                self.receive(game.draw_pile.pop())
                return game, "draw a card"
        # playing card is possible
        # prefer non rainbow cards at first
        choice = min(options, key=lambda x: 1 if x.symbol == "rainbow" else 0)
        if choice.symbol == "rainbow":
            symbols = [c.symbol for c in self.hand]
            choice.symbol = max(symbols, key=symbols.count)
            if choice.symbol not in ["red", "green", "yellow", "blue"]:
                choice.symbol = "red"
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
