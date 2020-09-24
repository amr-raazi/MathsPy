import random
import time
import matplotlib as plt

limit = int(input("Limit"))
delay = int(input("Delay"))
memory = []
if not limit > 0:
    exit()


class Coin:
    def __init__(self, side):
        self.side = side


def coin_flip():
    side = random.randint(0, 1)
    coin = Coin(side)
    return coin.side


for i in range(limit):
    memory.append(coin_flip())
for i in memory:
    if i == 0:
        print("Heads")
    else:
        print("Tails")
    time.sleep(delay)
heads_count = memory.count(0)
tails_count = memory.count(1)
percentage_of_heads = heads_count / limit * 100
percentage_of_tails = tails_count / limit * 100
print(f"Number of Heads: {heads_count}, Number of Tails: {tails_count}")
print(f"Heads percent: {percentage_of_heads}%, Tails percent: {percentage_of_tails}%")
if abs(percentage_of_tails - 50) > 5:
    print(f"Statistically significant as n={abs(percentage_of_tails - 50)}")
else:
    print(f"Statistically insignificant as n={abs(percentage_of_tails - 50) / 100}")
