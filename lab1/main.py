from random import sample
from search import linear_search, binary_search
from time import time_ns
import matplotlib.pyplot as plt

def run_linear(n):
    data = sample(range(1, n+1), n)

    start_time = time_ns()
    linear_search(data, data[-1])
    end_time = time_ns()

    time_taken = end_time-start_time
    return time_taken

def run_binary(n):
    data = sample(range(1, n+1), n)

    start_time = time_ns()
    binary_search(data, data[-1], 0, len(data)-1)
    end_time = time_ns()

    time_taken = end_time-start_time
    return time_taken

def plot_linear():
    x_vals = []
    y_vals = []
    for i in range(10000, 1000000, 5000):
        x_vals.append(i)
        y_vals.append(run_linear(i))

    plt.plot(x_vals, y_vals)
    plt.title("Linear Search")
    plt.xlabel("Number of Data ( n )")
    plt.ylabel("Execution Time ( t )")
    plt.show()

def plot_binary():
    x_vals = []
    y_vals = []
    
    for i in range(10000, 1000000, 5000):
        x_vals.append(i)
        y_vals.append(run_binary(i))

    plt.plot(x_vals, y_vals)
    plt.title("Binary Search")
    plt.xlabel("Number of Data ( n )")
    plt.ylabel("Execution Time ( t )")
    plt.show()

plot_linear()
plot_binary()