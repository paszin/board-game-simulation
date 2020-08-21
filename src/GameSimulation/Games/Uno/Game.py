from ..Base import Game as BaseGame, CardStack, Card, GameState

from ..Base.CardStack import EmptyStackError

class Game(BaseGame):

    @staticmethod
    def generate_cards():
        """
        4 colors
        2 x numbers 1 - 9 per color
        total: 56 cards
        :return:
        """
        cards = []
        for color in ["red", "blue", "yellow", "green"]:
            cards.append(Card(number=0, symbol=color))
            for n in list(range(1, 10)) + ["+2", "skip"]:
                for i in range(2):
                    cards.append(Card(number=n, symbol=color))
        for i in range(4):
            cards.append(Card(symbol="rainbow", number="0"))
            cards.append(Card(symbol="rainbow", number="+4"))
        return cards


    @staticmethod
    def re_shuffle_draw_pile(game_state):
        """

        :param game:
        :return:
        """
        game_state.draw_pile.add_cards(game_state.stack.copy_cards())
        game_state.draw_pile.shuffle()
        return game_state

    def setup(self, cards=None):
        """
        1 Card Stack (with one open card)
        1 Draw Pile
        Hand Cards for each player
        """

        stack = CardStack("Discard Pile")
        draw_pile = CardStack("Draw Pile", cards or Game.generate_cards())
        draw_pile.shuffle()
        # every player gets cards
        for _ in range(self.cards_per_player):
            for p in self.players:
                p.receive(draw_pile.pop())

        # one open card for the stack
        stack.push(draw_pile.pop())

        # shuffle draw_pile if empty
        self.set_error_handler(EmptyStackError, Game.re_shuffle_draw_pile)

        self.gamestate = GameState(stack=stack, draw_pile=draw_pile, players=self.players)

    def check_gamestate(self, game):
        """triggered after each player"""
        if len(game.draw_pile) < 2:
            game.draw_pile.cards = Game.generate_cards()
            game.draw_pile.shuffle()
        return game



