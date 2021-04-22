from abc import ABC
from numbers import Number

from actions import ActionPicker, AttackAction, HealAction


class Unit(ABC):
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

        self.actions = [
            AttackAction(min_damage=18, max_damage=25),
            AttackAction(min_damage=10, max_damage=35),
            HealAction(min_heal=18, max_heal=25)
        ]

    def attack(self, victim: 'Unit') -> None:
        action = ActionPicker(self.actions).get_random_action()
        action.perform(attacker=self, victim=victim)

    def receive_heal(self, heal: int) -> None:
        self.health += heal
        print(f'{self.name} is healed by {heal}hp')

    def receive_damage(self, attacker: 'Unit', damage: int) -> None:
        self.health -= damage
        print(f'{attacker.name} dealt {damage} damage to {self.name}')

        if self.health <= 0:
            print(f'### {self.name} died ###')

    def is_alive(self) -> bool:
        return self.health > 0


class Player(Unit):
    pass


class Computer(Unit):
    MIN_HEALTH_PERCENT_TO_MULTIPLY_HEAL_CHANCE = 35
    HEALING_CHANCE_MULTIPLIER = 5

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_health = self.health

    def attack(self, victim: Unit) -> None:
        health_percent = self.health * 100 / self.start_health

        if health_percent > self.MIN_HEALTH_PERCENT_TO_MULTIPLY_HEAL_CHANCE:
            return super().attack(victim=victim)

        print(f'* Healing chance increases x{self.HEALING_CHANCE_MULTIPLIER}')

        self.change_healing_chance_multiplier(self.HEALING_CHANCE_MULTIPLIER)
        super().attack(victim=victim)
        self.change_healing_chance_multiplier(1)

    def change_healing_chance_multiplier(self, multiplier: Number) -> None:
        for action in self.actions:
            if isinstance(action, HealAction):
                action.chance_multiplier = multiplier
