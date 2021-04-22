from units.base import BaseUnit

from actions.attack import AttackAction
from actions.heal import HealAction
from action_pickers.base import BaseActionPicker


class Player(BaseUnit):
    def __init__(self, action_picker: BaseActionPicker, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.action_picker = action_picker

        self.actions = [
            AttackAction(min_damage=18, max_damage=25),
            AttackAction(min_damage=10, max_damage=35),
            HealAction(min_heal=18, max_heal=25)
        ]

    def attack(self, victim: 'BaseUnit') -> None:
        action = self.action_picker.get_action(self.actions)
        action.perform(attacker=self, victim=victim)

    def receive_heal(self, heal: int) -> None:
        self.health += heal
        print(f'{self.name} is healed by {heal}hp')

    def receive_damage(self, attacker: 'BaseUnit', damage: int) -> None:
        self.health -= damage
        print(f'{attacker.name} dealt {damage} damage to {self.name}')

        if self.health <= 0:
            print(f'### {self.name} died ###')

    def is_alive(self) -> bool:
        return self.health > 0
