

import sys
sys.path.insert(0, "/home/paszin/Documents/board-game-simulation/src/GameSimulation/")

from Games.BabyUno import Game, Player, InteractivePlayer
import numpy as np

import time

import random
random.seed(1419265)

import matplotlib.pyplot as plt




players = [Player(i) for i in range(1, 4)]
players.append(InteractivePlayer("Me"))

game = Game(players=players, cards_per_player=5)
game.setup()
game.simulate(quiet=False, turns=100)
