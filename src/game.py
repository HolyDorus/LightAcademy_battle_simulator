from random import sample as random_sample

from actions import ActionPicker, AttackAction, HealAction


class Unit:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

        self.actions = [
            AttackAction(min_damage=18, max_damage=25),
            AttackAction(min_damage=10, max_damage=35),
            HealAction(min_heal=18, max_heal=25)
        ]

    def attack(self, victim: 'Unit'):
        action = ActionPicker(self.actions).get_random_action()
        action.perform(attacker=self, victim=victim)

    def receive_heal(self, heal: int):
        self.health += heal
        print(f'{self.name} is healed by {heal}hp')

    def receive_damage(self, attacker: 'Unit', damage: int):
        self.health -= damage
        print(f'{attacker.name} dealt {damage} damage to {self.name}')

        if self.health <= 0:
            print(f'### {self.name} died ###')

    def is_alive(self):
        return self.health > 0


class Computer(Unit):
    MIN_HEALTH_PERCENT_TO_MULTIPLY_HEAL_CHANCE = 35
    HEALING_CHANCE_MULTIPLIER = 5

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_health = self.health

    def attack(self, victim: Unit):
        health_percent = self.health * 100 / self.start_health

        if health_percent > self.MIN_HEALTH_PERCENT_TO_MULTIPLY_HEAL_CHANCE:
            return super().attack(victim=victim)

        print(f'* Healing chance increases x{self.HEALING_CHANCE_MULTIPLIER}')

        self.change_healing_chance_multiplier(self.HEALING_CHANCE_MULTIPLIER)
        super().attack(victim=victim)
        self.change_healing_chance_multiplier(1)

    def change_healing_chance_multiplier(self, multiplier):
        for action in self.actions:
            if isinstance(action, HealAction):
                action.chance_multiplier = multiplier


class Game:
    def __init__(self, units: Unit):
        self.units = units
        self.round = 0

    def run(self):
        while self.get_number_of_alive_units() > 1:
            self.play()

    def play(self):
        alive_units = self.get_alive_units()
        attacker, victim = random_sample(alive_units, 2)

        attacker.attack(victim)

        self.round += 1
        self.print_current_situation()

    def print_current_situation(self):
        print(f'Round {self.round}, Units:')

        for unit in self.units:
            print(f'\t{unit.name}: {unit.health}hp')

        print()

    def get_alive_units(self) -> list[Unit]:
        return [unit for unit in self.units if unit.is_alive()]

    def get_number_of_alive_units(self) -> int:
        return len(self.get_alive_units())


if __name__ == '__main__':
    game = Game([
        Unit(name='Player', health=100),
        Computer(name='Computer', health=100)
    ])
    game.run()
