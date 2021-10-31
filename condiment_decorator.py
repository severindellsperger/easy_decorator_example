from abc import abstractmethod
from beverage import Beverage


class CondimentDecorator(Beverage):
    def __init__(self, beverage) -> None:
        self.beverage = beverage
        super().__init__(description=self.beverage.description, size=self.beverage.size)

    def cost(self) -> float:
        return self.beverage.cost()