from ...Base import Player as BasePlayer

from collections import namedtuple, defaultdict
import copy


class Player(BasePlayer):

    @staticmethod
    def select_card(stacks, options):
        best_fit_type = namedtuple("Turn", ["stack", "card", "distance"])
        best_fit = best_fit_type(stack=None, card=None, distance=None)
        for i, stack in enumerate(stacks):
            if not options[i]:
                continue
            c = options[i][0]
            if best_fit.distance and c.distance < best_fit.distance or best_fit.distance is None:
                best_fit = best_fit_type(stack, c, c.distance)
        return best_fit

    def get_best_cards_per_stack(self, game):
        """

        :param game: gamestate
        :return: dict with stack index and array of sorted cards that fit
        """
        best_fit_per_stack = defaultdict(list)
        out_of_options = dict.fromkeys(range(len(game.card_stacks)), False)
        optimal_fit = game.get_jump_card_options()
        # while at least one stack is not out of options
        while not all(out_of_options.values()):
            for i, stack in enumerate(game.card_stacks):
                # all cards are possible options that are accepted on the stack and not already part of the stack
                options = list(filter(lambda card: stack.accept(card) and card not in best_fit_per_stack[i], self.hand))
                if not options:
                    out_of_options[i] = True
                    continue
                # best fit is 10er jump or smallest distance
                # the lower the fit, the better

                def fit_function(c):
                    if c == optimal_fit[i]:
                        return -10
                    if not best_fit_per_stack[i]:
                        return abs(stack.last_card - c)
                    return abs(best_fit_per_stack[i][-1] - c)

                best_fitting_card = copy.deepcopy(min(options, key=fit_function))
                best_fitting_card.distance = fit_function(best_fitting_card)
                best_fit_per_stack[i].append(best_fitting_card)
        return best_fit_per_stack


    def play(self, game):

        # strategy: use 2 best cards
        cards_played = 0
        while cards_played < game.min_card_count:
            options = self.get_best_cards_per_stack(game)
            choice = Player.select_card(game.card_stacks, options)
            if choice.card is None:
                raise RuntimeError("We lost!")
            self.drop(choice.card)
            cards_played += 1
            choice.stack.push(choice.card)
        return game, f"play {choice.card}"

    def finish_turn(self, game):

        while len(self.hand) < game.cards_per_player and game.draw_pile:
            self.receive(game.draw_pile.pop())

        return game