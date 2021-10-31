from abc import ABC, abstractmethod


class Beverage(ABC):
    def __init__(self, description, size) -> None:
        self.description = description
        self.size = size

    @abstractmethod
    def cost() -> float:
        pass
