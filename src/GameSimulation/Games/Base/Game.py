import copy


class Game:
    """
    Basic Framework for card games
    """

    def __init__(self, players=None, cards_per_player=None, player_type=None, players_count=None):
        """
        provide a list with players or provide a player class and players_count
        :param players:
        :param cards_per_player:
        :param player_type:
        :param players_count:
        """
        self.cards_per_player = cards_per_player

        if players:
            self.players = players
        elif player_type and players_count:
            self.players = [player_type(i) for i in range(1, players_count + 1)]
        else:
            raise ValueError("provide a list with players or provide a player class and players_count")

        self.score = None
        self.gamestate_history = []

    def setup(self):
        """
        must be implemented by derived class
        :return:
        """
        pass

    def simulate(self, quiet=True, turns=None):
        """

        :param quiet:
        :param turns: execute x number of turns
        :return:
        """
        # generic game logic
        turn = 0
        while True:
            if not quiet:
                print(f"Round {turn}\n",  # Round (Turn)
                      "\n".join(map(str, self.players)) + "\n",  # Player Cards
                      self.gamestate.card_stacks or self.gamestate.stack  # open cards (stack/stacks)
                      )
            current_player = self.players[turn % len(self.players)]
            try:
                self.gamestate, choice = current_player.play(self.gamestate)
            except RuntimeError as err:
                if not quiet:
                    print(err)
                    print("Game Over")
                    self.gamestate_history.append(self.gamestate)
                    print("\n".join(map(str, self.players)) + "\n",  # Player Cards
                          self.gamestate.card_stacks or self.gamestate.stack, "\n"  # open cards (stack/stacks)
                          )
                break
            else:
                if not quiet:
                    print(f"Player {current_player.name}: {choice}\n")
                self.gamestate = current_player.finish_turn(self.gamestate)
                self.gamestate_history.append(copy.deepcopy(self.gamestate))
            turn += 1
            if turns and turn >= turns:
                break
        self.finish()

    def evaluate(self):
        pass

    def finish(self):
        pass
