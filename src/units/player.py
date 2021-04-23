from units.base import BaseUnit

from actions.attack import AttackAction
from actions.heal import HealAction
from action_picker import ActionPicker


class Player(BaseUnit):
    """Реализация абстрактного класса базового юнита."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.actions = [
            AttackAction(min_damage=18, max_damage=25),
            AttackAction(min_damage=10, max_damage=35),
            HealAction(min_heal=18, max_heal=25)
        ]

    def attack(self, victim: BaseUnit) -> None:
        """
        Реализация абстрактного метода нападения одного юнита на другого.
        Включает в себя выбор события из списка экшенов юнита и последующее
        выполнение выбранного события.
        """
        action = ActionPicker().get_random_action(self.actions)
        action.perform(attacker=self, victim=victim)

    def receive_heal(self, heal: int) -> None:
        """Реализация абстрактного метода получения юнитом хила."""
        self.health += heal
        print(f'{self.name} is healed by {heal}hp')

    def receive_damage(self, attacker: BaseUnit, damage: int) -> None:
        """Реализация абстрактного метода получения юнитом урона."""
        self.health -= damage
        print(f'{attacker.name} dealt {damage} damage to {self.name}')

        if self.health <= 0:
            print(f'### {self.name} died ###')

    def is_alive(self) -> bool:
        """Реализация абстрактного метода проверки жив ли юнит."""
        return self.health > 0
