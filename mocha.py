from condiment_decorator import CondimentDecorator


class Mocha(CondimentDecorator):
    def __init__(self, beverage) -> None:
        super().__init__(beverage)
        self.description += "with Mocha "

    def cost(self) -> float:
        if self.size == "small":
            return super().cost() + 1.0
        elif self.size == "medium":
            return super().cost() + 1.5
        else:
            return super().cost() + 1.75
