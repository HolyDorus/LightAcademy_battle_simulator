from abc import ABC, abstractmethod

from actions.base import BaseAction


class BaseActionPicker(ABC):
    @abstractmethod
    def get_action(self, actions: list[BaseAction]) -> BaseAction:
        pass
