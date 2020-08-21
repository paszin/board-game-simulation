
from .Card import Card

class GameState:

    def __init__(self, stack=None, card_stacks=None, draw_pile=None, **kwargs):
        self.stack = stack
        self.card_stacks = card_stacks
        self.draw_pile = draw_pile
        for key, value in kwargs.items():
            setattr(self, key, value)



    # TODO: move to Game
    @property
    def min_card_count(self):
        if len(self.draw_pile) > 0:
            return 2
        return 1

    # TODO: move to Game
    def get_jump_card_options(self):
        """

        :return: list with cards that are suiteable to do a jump by 10
        """
        options = {}
        for i, stack in enumerate(self.card_stacks):
            if stack.accept(stack.last_card + 1):
                # counting up stack
                options[i] = Card(number=stack.last_card - 10)
            else:
                # counting down stack
                options[i] = Card(number=stack.last_card + 10)
        return options



