from condiment_decorator import CondimentDecorator


class WhippedCream(CondimentDecorator):
    def __init__(self, beverage) -> None:
        super().__init__(beverage)
        self.description += "with whipped cream"

    def cost(self) -> float:
        if self.beverage.size == "small":
            return self.beverage.cost() + 1.75
        elif self.beverage.size == "medium":
            return self.beverage.cost() + 2.25
        else:
            return self.beverage.cost() + 2.75
