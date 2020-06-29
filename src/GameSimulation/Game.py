from . import Card, CardStack, Player, GameState

class Game:

    # RULES
    @staticmethod
    def accept_counting_up(stack, card):
        return stack.last_card < card or stack.last_card - 10 == card

    @staticmethod
    def accept_counting_down(stack, card):
        return stack.last_card > card or stack.last_card + 10 == card

    def __init__(self, players_count, cards_per_player):
        self.players_count = players_count
        self.cards_per_player = cards_per_player

        self.players = [Player(i) for i in range(1, self.players_count + 1)]



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
        self.gamestate = GameState(card_stacks=card_stacks, draw_pile=draw_pile, cards_per_player=self.cards_per_player)

    def play(self, quiet=False):
        # game logic
        turn = 0
        if not quiet:
            print(f"Round {turn}\n", "\n".join(map(str, self.players)), "\n", self.gamestate.card_stacks, "\n")
        while True:
            current_player = self.players[turn % len(self.players)]
            try:
                self.gamestate, choice = current_player.play(self.gamestate)
            except RuntimeError as err:
                self.score = len(self.gamestate.draw_pile) + sum(map(len, [p.hand for p in self.players]))
                if not quiet:
                    print(err)
                    print("Remaining Cards", self.score)
                break
            else:
                self.gamestate = current_player.finish_turn(self.gamestate)
            turn += 1
            if not quiet:
                print(f"Round {turn} (Player {current_player.name})\n",
                  "\n".join(map(str, self.players)),
                  "\n",
                  self.gamestate.card_stacks,
                  "\n",
                  sep="", end="")

    def evaluate(self):
        pass