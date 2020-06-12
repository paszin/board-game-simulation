class GameState:

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def min_card_count(self):
        if len(self.draw_pile) > 0:
            return 2
        return 1
