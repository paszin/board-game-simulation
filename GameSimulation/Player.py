import random

class Player:
    """
    This is the representation of a human player.
    A player has a name, a hand and knowledge.
        name: Identifier of the instance
        hand: list of cards
        knowledge: tbd
    A player can perform actions. Actions are:
        play:
        finish_turn:
        ask:
        reply:
    """

    def __init__(self, name=None):
        self.name = name
        self.hand = []
        self.knowledge = None

    def __str__(self):
        return f"{self.name or 'Player'}: {' '.join(map(str, self.hand))}"

    def __repr__(self):
        return f"{self.name or 'Player'}: {' '.join(map(str, self.hand))}"

    def receive(self, card):
        """

        :return:
        """
        self.hand.append(card)

    def play(self, game):
        """

        :return:
        """
        # find card with min distance to any stack
        best_fit_per_stack = []
        for i, stack in enumerate(game.card_stacks):
            # transform cards to distance, card
            # find min distance
            # save this tuple as best fit for this stack
            try:
                best_fit_per_stack.append((i, *(min(map(lambda c: (abs(stack.last_card - c), c),
                                                       filter(stack.accept, self.hand))) or 100))
                )
            except ValueError as err:
                best_fit_per_stack.append((i, 100, None))
        stack_i, dist, choice = min(best_fit_per_stack, key=lambda iac: iac[1])
        if dist == 100:
            raise RuntimeError("We lost this game")
        self.hand.remove(choice)
        game.card_stacks[stack_i].push(choice)
        return choice

    def finish_turn(self):
        """

        :return:
        """
        pass

    def ask(self):
        """

        :return:
        """
        pass

    def reply(self):
        """

        :return:
        """
        pass