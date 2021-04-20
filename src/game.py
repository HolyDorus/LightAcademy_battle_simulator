from random import randint as random_int

from actions import ActionType, Action, ActionPicker


class BaseUnit:
    FIRST_ATTACK_DAMAGE_RANGE = (18, 25)
    SECOND_ATTACK_DAMAGE_RANGE = (10, 35)
    HEAL_RANGE = (18, 25)

    def __init__(self, health: int):
        self.health = health

        self.action_list = [
            Action(
                action_type=ActionType.FIRST_ATTACK,
                chance=1.0,
                callback=self.action_first_attack
            ),
            Action(
                action_type=ActionType.SECOND_ATTACK,
                chance=1.0,
                callback=self.action_second_attack
            ),
            Action(
                action_type=ActionType.HEAL,
                chance=1.0,
                callback=self.action_heal
            )
        ]

    def attack(self, victim: 'BaseUnit'):
        action_function = self.get_random_action_function()
        action_function(victim)

    def get_random_action_function(self):
        action = ActionPicker(self.action_list).get_random_action()
        return action.function

    def action_first_attack(self, victim: 'BaseUnit'):
        damage = random_int(*self.FIRST_ATTACK_DAMAGE_RANGE)
        victim.receive_damage(attacker=self, damage=damage)

    def action_second_attack(self, victim: 'BaseUnit'):
        damage = random_int(*self.SECOND_ATTACK_DAMAGE_RANGE)
        victim.receive_damage(attacker=self, damage=damage)

    def action_heal(self, victim: 'BaseUnit'):
        heal = random_int(*self.HEAL_RANGE)
        self.receive_heal(heal)

    def receive_heal(self, heal: int):
        self.health += heal
        print(f'{self.name} is healed by {heal}hp')

    def receive_damage(self, attacker: 'BaseUnit', damage: int):
        self.health -= damage
        print(f'{attacker.name} dealt {damage} damage to {self.name}')

    @property
    def name(self) -> str:
        return type(self).__name__


class Player(BaseUnit):
    pass


class Computer(BaseUnit):
    MIN_HEALTH_PERCENT_TO_MULTIPLY_HEAL_CHANCE = 35
    HEALING_CHANCE_MULTIPLIER = 100

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_health = self.health

    def get_random_action_function(self):
        health_percent = self.health * 100 / self.start_health

        if health_percent > self.MIN_HEALTH_PERCENT_TO_MULTIPLY_HEAL_CHANCE:
            action = ActionPicker(self.action_list).get_random_action()
            return action.function

        print(
            f'* Healing chance increases x{self.HEALING_CHANCE_MULTIPLIER}'
        )

        action = ActionPicker(self.action_list, chance_multiply={
                ActionType.HEAL: self.HEALING_CHANCE_MULTIPLIER
            }
        ).get_random_action()
        return action.function


class Game:
    def __init__(self, player: Player, computer: Computer):
        self.player = player
        self.computer = computer
        self.round = 0

    def play(self):
        if random_int(0, 1):
            self.player.attack(victim=self.computer)
        else:
            self.computer.attack(victim=self.player)

        self.round += 1
        self.print_current_situation()

    def is_game_over(self) -> bool:
        if self.computer.health <= 0:
            print(f'*** {self.player.name} won ***')
            return True
        elif self.player.health <= 0:
            print(f'*** {self.computer.name} won ***')
            return True

        return False

    def print_current_situation(self):
        print(
            f'Current situation (round {self.round}):\n'
            f'\tPlayer: {self.player.health}hp\n'
            f'\tComputer: {self.computer.health}hp\n'
        )


if __name__ == '__main__':
    game = Game(
        player=Player(100),
        computer=Computer(100)
    )

    while not game.is_game_over():
        game.play()
