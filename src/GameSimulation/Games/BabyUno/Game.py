from ..Base import Game as BaseGame, CardStack, Card, GameState


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
            for n in range(1, 10):
                for i in range(2):
                    cards.append(Card(number=n, symbol=color))
        return cards

    def setup(self):
        """
        1 Card Stack (with one open card)
        1 Draw Pile
        Hand Cards
        :return:
        """

        stack = CardStack()
        draw_pile = CardStack("Draw Pile", Game.generate_cards())
        draw_pile.shuffle()
        # every player gets cards
        for _ in range(self.cards_per_player):
            for p in self.players:
                p.receive(draw_pile.pop())

        # one open card for the stack
        stack.push(draw_pile.pop())

        self.gamestate = GameState(stack=stack, draw_pile=draw_pile)
