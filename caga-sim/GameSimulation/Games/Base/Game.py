import copy


class Game:
    """
    Basic Framework for card games
    """

    def __init__(self, players=None, cards_per_player=None, player_type=None, number_of_players=None):
        """
        provide a list with players or provide a player class and players_count
        :param players:
        :param cards_per_player:
        :param player_type:
        :param number_of_players:
        """
        self.cards_per_player = cards_per_player

        if players:
            self.players = players
        elif player_type and number_of_players:
            self.players = [player_type(i) for i in range(1, number_of_players + 1)]
        else:
            raise ValueError("provide a list with players or provide a player class and number_of_players")

        self.score = None
        self.gamestate_history = []
        self.turn = 0
        self.exception_handlers = {}

    def setup(self):
        """
        must be implemented by derived class
        :return:
        """
        pass

    def check_gamestate(self, game):
        return game

    def get_next_player(self, game):
        return game, self.players[self.turn % len(self.players)]

    def simulate(self, quiet=True, turns=None):
        """

        :param quiet:
        :param turns: execute x number of turns
        :return:
        """
        # generic game logic
        self.turn = 0
        while True:
            if not quiet:
                print(f"Round {self.turn}\n",  # Round (Turn)
                      "\n".join(map(str, self.players)) + "\n",  # Player Cards
                      self.gamestate.card_stacks or self.gamestate.stack  # open cards (stack/stacks)
                      )
            self.gamestate, current_player = self.get_next_player(self.gamestate)
            try:
                self.gamestate, choice = current_player.play(self.gamestate)
            except RuntimeError as err:
                self.gamestate_history.append(self.gamestate)
                if not quiet:
                    print(err)
                    print("Game Over")
                    print("\n".join(map(str, self.players)) + "\n",  # Player Cards
                          self.gamestate.card_stacks or self.gamestate.stack, "\n"  # open cards (stack/stacks)
                          )
                break
            except Exception as err:
                # check ig exception handler exists, if yes run the handler and uodate the gamestate
                found = False
                for exc, handler in self.exception_handlers.items():
                    if type(err) == exc:
                        found = True
                        self.gamestate = handler(self.gamestate)
                if not found:
                    print(self.gamestate)
                    print(err)
                    raise err
            else:
                if not quiet:
                    print(f"Player {current_player.name}: {choice}\n")
                self.gamestate = current_player.finish_turn(self.gamestate)
                self.gamestate_history.append(copy.deepcopy(self.gamestate))
                self.turn += 1
            # self.gamestate = self.check_gamestate(self.gamestate)
            if turns and self.turn >= turns:
                break
        self.finish()


    def evaluate(self):
        pass

    def finish(self):
        pass

    def set_error_handler(self, exc, handler):
            """

            :return:
            """
            self.exception_handlers[exc] = handler
