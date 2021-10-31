from beverage import Beverage


class Espresso(Beverage):
    def __init__(self, size) -> None:
        description = f"{size} espresso "
        super().__init__(description, size)

    def cost(self) -> float:
        if self.size == "small":
            return 4.0
        elif self.size == "medium":
            return 5.0
        else:
            return 6.0