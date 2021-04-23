from random import uniform as random_float

from actions.base import BaseAction


class ActionPicker:
    """Класс, предназначенный для выбора некого события из списка событий."""
    def get_random_action(self, actions: list[BaseAction]) -> BaseAction:
        """
        Метод выбора случайного события из списка событий с учетом шанса
        выпадения. Примеры вероятности выпадения событий:
        Список событий:
            SomeAction(chance=1) - 33%
            SomeAction(chance=1) - 33%
            SomeAction(chance=1) - 33%

        Список событий:
            SomeAction(chance=1) - 25%
            SomeAction(chance=2) - 50%
            SomeAction(chance=1) - 25%

        Вероятность выпадения события можно рассчитать по следующей формуле:
            100 / s * c,
        где
            s - сумма всех шансов в списке событий,
            c - шанс конкретного события
        """
        self.chances_sum = 0
        self.fill_chance_limits(actions)

        rf = random_float(0, self.chances_sum)

        for action in actions:
            if action.lower_limit <= rf < action.upper_limit:
                return action

        return actions[-1]

    def fill_chance_limits(self, actions: list[BaseAction]) -> None:
        """
        Метод, предназначенный для заполнения полей lower_limit и upper_limit у
        всех переданных событий.
        """
        for action in actions:
            real_chance = action.chance * action.chance_multiplier

            action.lower_limit = self.chances_sum
            action.upper_limit = self.chances_sum + real_chance
            self.chances_sum += real_chance
