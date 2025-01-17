import matplotlib.pyplot as plt
import numpy as np
import random

# Simple animation test

x_values = []
y_values = []


for _ in range(10):
    x_values.append(random.randint(0, 100))
    y_values.append(random.randint(0, 100))

    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.scatter(x_values, y_values, color="black")
    plt.pause(0.001)

plt.show()