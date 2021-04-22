from abc import ABC, abstractmethod
from numbers import Number

from units.base import BaseUnit


class BaseAction(ABC):
    def __init__(self, chance: Number = 1, chance_multiplier: Number = 1):
        self.chance = chance
        self.chance_multiplier = chance_multiplier
        self.lower_limit = 0
        self.upper_limit = 0

    @abstractmethod
    def perform(self, attacker: BaseUnit, victim: BaseUnit) -> None:
        pass
