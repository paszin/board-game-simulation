# card-game-simulation

A framework for card games.

Teaser: 
 How does the special cards impact the game? Has the starting player an advantage? How does the number of cards and number of players impact the duration?

## About this repository

This repository is for documentation and implementation of the seminar **Simulation** during summer semester 2020 at Hasso Plattner Institute.

Content of the folders:

**report** includes a 15-page documentation about the foundations of discrete-event simulation, the implementation concepts in this framwork, and the evaluation on the card game UNO.

**caga-sim** contains the card-game simulation framework as package.

**experiments** contains experiments with UNO


## About caga-sim


The objective of the implementation is to build a framework that

* maps all main components of discrete-event simulation to the context of card games
* uses an object-oriented approach for intuitive readability
* is generic enough to cover common card games
* keeps the implementation effort low for new player behavior and new games

## Getting started

Clone this repository

`git clone https://github.com/paszin/card-game-simulation.git`

Install GameSimulation Module

`cd card-game-simulation/caga-sim && pip install -e .`


Simulate Uno

```python

import GameSimulation.Games.Uno as Uno
from  GameSimulation.Games.Uno.Player import Player

# run a simulation with 4 players and 7 cards each
# All players are similar, they are implemented in the class Player
game = Uno(number_of_players=4, player_type=Player, cards_per_player=7)
# setup distributes the card
game.setup()

# log the current gamestate
game.gamestate.print_it_nice()

# run the simulation, quiet=False means that the progress will be logged to console
game.simulate(quiet=False)

```

## Experiments

* Simulate Uno: This contains a an example with logging output and the execution of 1000 games of different configuration [Link to jupyter notebook](https://github.com/paszin/card-game-simulation/blob/master/experiments/executed/SimulateUno.ipynb)

* Uno: Impact Of Special Cards: This analyzes the impact of wildcard, plus2 and other special cards on the duration of the game [Link to jupyter notebook](https://github.com/paszin/card-game-simulation/blob/master/experiments/executed/UnoImpactOfSpecialCards.ipynb)

* Uno: Analyze the duration of the game [Link to jupyter notebook](https://github.com/paszin/card-game-simulation/blob/master/experiments/executed/AnalyzeUno.ipynb) 

Ideas for other studies:

* Analyze the power special cards. Does the player with the wildcard+4 always wins? 

## Report

Abstract:
> This report introduces discrete-event simulations and classifies the purpose of discrete-event simulation based on its characteristics. Discrete-event simulations are stochastic, dynamic and based on discrete events. Every simulation is based on a model. A generic model of discrete-event simulation is the queuing of arriving events, followed by the processing of the events. Every event changes the system state. An application of using discrete-event simulation to analyze and balance card games is demonstrated with the example of \uno. The presented approach realizes the main components and the simulation paradigm in a custom implementation of a framework for the simulation of card games. The simulation of \uno\ analyzes the duration of \uno\ games depending on the presence of special cards, number of players and number of initial hand cards. The result is, that a \uno\ game takes normally 10 to 30 rounds to finish.




Example:

```python

class EasyUno(Game):

    def setup():
        

        


```








