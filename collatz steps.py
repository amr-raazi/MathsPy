import matplotlib.pyplot as plt


def collatz(num):
    num_of_steps = 0
    while num != 1:
        if not num % 2:
            num = num / 2
        else:
            num = (num * 3) + 1
        num_of_steps += 1
    return num_of_steps


collatz_dict = {}
limit = 1000
for i in range(1, limit):
    collatz_dict[i] = collatz(i)
keys = list(collatz_dict.keys())
values = list(collatz_dict.values())
plt.plot(keys, values)
plt.ylabel("Collatz number of steps")
plt.title("Collatz")
plt.show()
