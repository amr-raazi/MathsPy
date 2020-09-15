import matplotlib.pyplot as plt
import matplotlib as mpl
import random
mpl.rc('lines', linewidth=4)
x = y = count = 0
x_data = []
y_data = []
limit = 1000
while count < limit:
    direction = random.randint(0, 3)
    count += 1
    plt.title("Random Walk")
    if direction == 0:
        x -= 1
    if direction == 1:
        x += 1
    if direction == 2:
        y += 1
    if direction == 3:
        y -= 1
    x_data.append(x)
    y_data.append(y)
    plt.plot(x_data, y_data)
    plt.pause(1)
    print(x, y)
plt.show()
