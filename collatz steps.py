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


limit = 100
collatz_dict = {i: collatz(i) for i in range(1, limit)}
plt.plot(list(collatz_dict.keys()), list(collatz_dict.values()))
plt.ylabel("Collatz number of steps")
plt.title("Collatz")
plt.show()
