from game import Game
from units.player import Player
from units.computer import Computer


if __name__ == '__main__':
    game = Game([
        Player(name='Player', health=100),
        Computer(name='Computer', health=100)
    ])
    game.run()
