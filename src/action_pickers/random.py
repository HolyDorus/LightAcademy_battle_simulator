from random import uniform as random_float

from actions.base import BaseAction
from action_pickers.base import BaseActionPicker


class RandomActionPicker(BaseActionPicker):
    def get_action(self, actions: list[BaseAction]) -> BaseAction:
        self.chances_sum = 0
        self.fill_chance_limits(actions)

        rf = random_float(0, self.chances_sum)

        for action in actions:
            if action.lower_limit <= rf < action.upper_limit:
                return action

        return actions[-1]

    def fill_chance_limits(self, actions: list[BaseAction]) -> None:
        for action in actions:
            real_chance = action.chance * action.chance_multiplier

            action.lower_limit = self.chances_sum
            action.upper_limit = self.chances_sum + real_chance
            self.chances_sum += real_chance
