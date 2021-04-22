from numbers import Number
from random import randint as random_int

from actions.base import BaseAction
from units.base import BaseUnit


class AttackAction(BaseAction):
    def __init__(self, min_damage: Number, max_damage: Number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.min_damage = min_damage
        self.max_damage = max_damage

    def perform(self, attacker: BaseUnit, victim: BaseUnit) -> None:
        damage = random_int(self.min_damage, self.max_damage)
        victim.receive_damage(attacker=attacker, damage=damage)
