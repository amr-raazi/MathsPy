import matplotlib.pyplot as plt


def collatz(num):
    path = [num]
    while num != 1:
        if not num % 2:
            num = num / 2
        else:
            num = (num * 3) + 1
        path.append(int(num))
    return path


number = 420
path = collatz(number)
print(collatz(number))
path_dict = {}
for i in range(1, len(path)):
    path_dict[i] = path[i]
plt.plot(path_dict.keys(), path_dict.values())
plt.ylabel("Number")
plt.xlabel("Number of steps")
plt.title(f"Collatz path for {number}")
plt.show()
