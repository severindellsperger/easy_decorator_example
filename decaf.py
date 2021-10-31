from beverage import Beverage


class Decaf(Beverage):
    def __init__(self, size="small") -> None:
        description = f"{size} decaf "
        super().__init__(size=size, description=description)

    def cost(self) -> float:
        if self.size == "small":
            return 3.0
        elif self.size == "medium":
            return 4.0
        else:
            return 5.0
