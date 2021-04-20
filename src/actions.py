from enum import Enum
from random import uniform as random_float


class ActionType(Enum):
    FIRST_ATTACK = 1
    SECOND_ATTACK = 2
    HEAL = 3


class Action:
    def __init__(self, action_type, chance, function):
        self.action_type = action_type
        self.chance = chance
        self.function = function


class ActionPicker:
    def __init__(self, actions: list[Action], chance_multiply=None):
        self.chances_sum = 0
        self.action_chances = []
        chance_multiply = chance_multiply if chance_multiply else {}

        for action in actions:
            mult = chance_multiply.get(action.action_type)

            if mult:
                new_chance = action.chance * mult
                action_dict = {
                    'instance': action,
                    'lower_limit': self.chances_sum,
                    'upper_limit': self.chances_sum + new_chance
                }
                self.chances_sum += new_chance
            else:
                action_dict = {
                    'instance': action,
                    'lower_limit': self.chances_sum,
                    'upper_limit': self.chances_sum + action.chance
                }
                self.chances_sum += action.chance

            self.action_chances.append(action_dict)

    def get_random_action(self):
        rf = random_float(0, self.chances_sum)

        for action in self.action_chances:
            if action['lower_limit'] <= rf < action['upper_limit']:
                return action['instance']

        return self.action_chances[-1]['instance']
