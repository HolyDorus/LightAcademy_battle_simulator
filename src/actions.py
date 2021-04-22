from abc import ABC, abstractmethod
from numbers import Number
from random import uniform as random_float, randint as random_int


class BaseAction(ABC):
    def __init__(self, chance: Number = 1, chance_multiplier: Number = 1):
        self.chance = chance
        self.chance_multiplier = chance_multiplier
        self.lower_limit = 0
        self.upper_limit = 0

    @abstractmethod
    def perform(self, attacker: 'Unit', victim: 'Unit') -> None:
        pass


class AttackAction(BaseAction):
    def __init__(self, min_damage: Number, max_damage: Number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.min_damage = min_damage
        self.max_damage = max_damage

    def perform(self, attacker: 'Unit', victim: 'Unit') -> None:
        damage = random_int(self.min_damage, self.max_damage)
        victim.receive_damage(attacker=attacker, damage=damage)


class HealAction(BaseAction):
    def __init__(self, min_heal: Number, max_heal: Number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.min_heal = min_heal
        self.max_heal = max_heal

    def perform(self, attacker: 'Unit', victim: 'Unit') -> None:
        heal = random_int(self.min_heal, self.max_heal)
        attacker.receive_heal(heal)


class ActionPicker:
    def __init__(self, actions: list[BaseAction]):
        self.actions = actions
        self.chances_sum = 0
        self.fill_chance_limits()

    def fill_chance_limits(self) -> None:
        for action in self.actions:
            real_chance = action.chance * action.chance_multiplier

            action.lower_limit = self.chances_sum
            action.upper_limit = self.chances_sum + real_chance
            self.chances_sum += real_chance

    def get_random_action(self) -> BaseAction:
        rf = random_float(0, self.chances_sum)

        for action in self.actions:
            if action.lower_limit <= rf < action.upper_limit:
                return action

        return self.actions[-1]
