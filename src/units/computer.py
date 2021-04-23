from numbers import Number

from units.player import Player, BaseUnit
from actions.heal import HealAction


class Computer(Player):
    """
    Класс, который наследует поведение класса Player и переопределяет некоторые
    его методы.
    """
    MIN_HEALTH_PERCENT_TO_MULTIPLY_HEAL_CHANCE = 35
    HEALING_CHANCE_MULTIPLIER = 10

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_health = self.health

    def attack(self, victim: BaseUnit) -> None:
        """
        Переопределение метода атаки на юнита. Увеличение шанса применить
        событие хила, если у атакующего процент здоровья меньше указанного.
        """
        health_percent = self.health * 100 / self.start_health

        if health_percent > self.MIN_HEALTH_PERCENT_TO_MULTIPLY_HEAL_CHANCE:
            return super().attack(victim=victim)

        print(f'* Healing chance increases x{self.HEALING_CHANCE_MULTIPLIER}')

        self.change_healing_chance_multiplier(self.HEALING_CHANCE_MULTIPLIER)
        super().attack(victim=victim)
        self.change_healing_chance_multiplier(1)

    def change_healing_chance_multiplier(self, multiplier: Number) -> None:
        """Метод изменения множителя шанса событий хила."""
        for action in self.actions:
            if isinstance(action, HealAction):
                action.chance_multiplier = multiplier
