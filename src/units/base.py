from abc import ABC, abstractmethod


class BaseUnit(ABC):
    """Абстрактный класс базового юнита."""
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health
        self.actions = []

    @abstractmethod
    def attack(self, victim: 'BaseUnit') -> None:
        """Абстрактный метод нападения одного юнита на другого."""
        pass

    @abstractmethod
    def receive_heal(self, heal: int) -> None:
        """Абстрактный метод получения юнитом хила."""
        pass

    @abstractmethod
    def receive_damage(self, attacker: 'BaseUnit', damage: int) -> None:
        """Абстрактный метод получения юнитом урона от другого юнита."""
        pass

    @abstractmethod
    def is_alive(self) -> bool:
        """Абстрактный метод проверки жив ли юнит."""
        pass
