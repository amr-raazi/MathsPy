import time
import matplotlib.pyplot as plt

direction_data = []
x = 0
y = 0
x_data = []
y_data = []
count = 0
limit = 1000000
import random

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
plt.pause(0.1)
plt.show()
