from ..Base import Game as BaseGame, CardStack, Card, GameState


class Game(BaseGame):
    """
    The Game
    """

    # RULES
    @staticmethod
    def accept_counting_up(stack, card):
        return stack.last_card < card or stack.last_card - 10 == card

    @staticmethod
    def accept_counting_down(stack, card):
        return stack.last_card > card or stack.last_card + 10 == card

    def setup(self):

        # there are 4 card stacks
        card_stacks = [CardStack() for _ in range(4)]

        card_stacks[0].name = "1UP"
        card_stacks[0].push(Card(number=1))
        card_stacks[0].set_acceptance_rule(Game.accept_counting_up)

        card_stacks[1].name = "1UP"
        card_stacks[1].push(Card(number=1))
        card_stacks[1].set_acceptance_rule(Game.accept_counting_up)

        card_stacks[2].name = "100DOWN"
        card_stacks[2].push(Card(number=100))
        card_stacks[2].set_acceptance_rule(Game.accept_counting_down)

        card_stacks[3].name = "100DOWN"
        card_stacks[3].push(Card(number=100))
        card_stacks[3].set_acceptance_rule(Game.accept_counting_down)

        # and a draw pile
        draw_pile = CardStack("Draw Pile", [Card(number=i) for i in range(2, 100)])
        draw_pile.shuffle()

        # every player gets cards
        for _ in range(self.cards_per_player):
            for p in self.players:
                p.receive(draw_pile.pop())

        # set this as gamestate
        self.gamestate = GameState(card_stacks=card_stacks, draw_pile=draw_pile, players=self.players,
                                   cards_per_player=self.cards_per_player) # relevant for drawing new cards

    def finish(self):
        self.score = len(self.gamestate.draw_pile) + sum(map(len, [p.hand for p in self.players]))
