"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  Created on 25 August, 2017 @ 8:35 PM.
  Copyright © 2017. victor. All rights reserved.
"""

# Linear Regression with gradient descent

import numpy as np
from matplotlib import pyplot as plt


def plot_data(data):
    for _, d in enumerate(data):
        plt.scatter(d[0], d[1])
    plt.title('Linear Regression data')
    plt.xlabel('Bike distance')
    plt.ylabel('Amount of calories lost')
    plt.show()


def squared_error(data, m, b):
    total_error = 0
    for _, d in enumerate(data):
        x = d[0]
        y = d[1]
        total_error += (y - (m * x + b)) ** 2
    return total_error / len(data)


def train(data, m, b, num_iter, learning_rate=1e-3):
    print('Training...')
    for _ in range(num_iter):
        [m, b] = gradient_descent(data, m, b, learning_rate)
    return [m, b]


def gradient_descent(data, m_current, b_current, learning_rate):
    b_gradient = 0
    m_gradient = 0
    n = float(len(data))
    for _, d in enumerate(data):
        x = d[0]
        y = d[1]
        m_gradient += (2 / n) * -x * (y - (m_current * x + b_current))
        b_gradient += (2 / n) * -(y - (m_current * x + b_current))

    new_b = b_current - (learning_rate * b_gradient)
    new_m = m_current - (learning_rate * m_gradient)
    return [new_m, new_b]


def start():
    data = np.genfromtxt('../datasets/data.csv', delimiter=',')
    init_m = 0
    init_b = 0
    learning_rate = 1e-4
    num_iter = 1000
    # Initial error
    err = squared_error(data, init_m, init_b)
    print('Error = {:.4f} for m = {:.2f} and b = {:.2f}'.format(err, init_m, init_b))
    m, b = train(data, init_m, init_b, num_iter, learning_rate)
    # Error after training
    err = squared_error(data, m, b)
    print('After {:,} iterations: error = {:.4f} for m = {:.2f} and b = {:.2f}'.format(num_iter, err, m, b))
    # Plot the data
    plot_data(data)


if __name__ == '__main__':
    start()
"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  Created on 26 August, 2017 @ 9:46 PM.
  Copyright (c) 2017. victor. All rights reserved.
"""
