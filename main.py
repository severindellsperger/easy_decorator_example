from espresso import Espresso
from decaf import Decaf
from mocha import Mocha
from whipped_cream import WhippedCream

espresso1 = Espresso(size="small")
espresso1 = Mocha(espresso1)
print(f"espresso1 - description: {espresso1.description} | cost: {espresso1.cost()}")

espresso2 = Espresso("big")
espresso2 = Mocha(espresso2)
print(f"espresso2 - description: {espresso2.description} | cost: {espresso2.cost()}")

decaf1 = Decaf("medium")
decaf1 = Mocha(decaf1)
decaf1 = WhippedCream(decaf1)
print(f"decaf1 - description: {decaf1.description} | cost: {decaf1.cost()}")
