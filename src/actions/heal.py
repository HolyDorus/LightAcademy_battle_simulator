from numbers import Number
from random import randint as random_int

from actions.base import BaseAction
from units.base import BaseUnit


class HealAction(BaseAction):
    def __init__(self, min_heal: Number, max_heal: Number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.min_heal = min_heal
        self.max_heal = max_heal

    def perform(self, attacker: BaseUnit, victim: BaseUnit) -> None:
        heal = random_int(self.min_heal, self.max_heal)
        attacker.receive_heal(heal)
