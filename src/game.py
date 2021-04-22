from random import sample as random_sample

from units import Unit


class Game:
    def __init__(self, units: Unit):
        self.units = units
        self.round = 0

    def run(self) -> None:
        while self.get_number_of_alive_units() > 1:
            self.play_round()

    def play_round(self) -> None:
        attacker, victim = self.get_random_alive_units(count=2)

        attacker.attack(victim)

        self.round += 1
        self.print_current_situation()

    def get_alive_units(self) -> list[Unit]:
        return [unit for unit in self.units if unit.is_alive()]

    def get_number_of_alive_units(self) -> int:
        return len(self.get_alive_units())

    def get_random_alive_units(self, count: int):
        alive_units = self.get_alive_units()
        return random_sample(alive_units, count)

    def print_current_situation(self) -> None:
        print(f'Round {self.round}, Units:')

        for unit in self.units:
            print(f'\t{unit.name}: {unit.health}hp')

        print()
