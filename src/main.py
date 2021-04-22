from game import Game
from action_pickers.random import RandomActionPicker
from units.player import Player
from units.computer import Computer


if __name__ == '__main__':
    game = Game([
        Player(
            name='Player',
            health=100,
            action_picker=RandomActionPicker()
        ),
        Computer(
            name='Computer',
            health=100,
            action_picker=RandomActionPicker()
        )
    ])
    game.run()
