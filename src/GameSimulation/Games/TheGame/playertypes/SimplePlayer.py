
def play(self, game):
    """

    :return:
    """
    # find n cards with min distance to any stack
    game = copy.deepcopy(game)
    min_card_count = game.min_card_count
    turn = []
    full_hand_count = len(self.hand)
    for play_card_counter in range(full_hand_count):
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
        # no move possible
        if dist == 100:
            break
        # enough cards to play and no good match
        if len(turn) >= min_card_count and dist > 3:
            break
        try:
            self.hand.remove(choice)
            turn.append(choice)
            game.card_stacks[stack_i].push(choice)
        except Exception as err:
            print(self.hand)
            print(choice)
            raise Exception(err)

    if len(turn) < game.min_card_count:
        raise RuntimeError("We lost.")
    return game, turn
