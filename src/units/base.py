from abc import ABC, abstractmethod


class BaseUnit(ABC):
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health
        self.actions = []

    @abstractmethod
    def attack(self, victim: 'BaseUnit') -> None:
        pass

    @abstractmethod
    def receive_heal(self, heal: int) -> None:
        pass

    @abstractmethod
    def receive_damage(self, attacker: 'BaseUnit', damage: int) -> None:
        pass

    @abstractmethod
    def is_alive(self) -> bool:
        pass
