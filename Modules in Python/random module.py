# random module:
import random

# Some common functions from this module:
# 1. random() -> Gives a random decimal number between 0 and 1. Example:
print(random.random())

# 2. randint(a, b) -> Gives a random integer number between a and b,
# including a and b. Example:
print(random.randint(1, 10))

# 3. choice() -> Gives a random choice from a given itreable. Example:
print(random.choice("Akshat"))
print(random.choice([1, 2, 3]))

# 4. shuffle() -> Shuffles a given iterable in place. Example:
my_list = [10, 15, 12, 4]
random.shuffle(my_list)
print(my_list)
