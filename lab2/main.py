from random import sample
from sort import insertion_sort, merge_sort
from time import time_ns
import matplotlib.pyplot as plt

# Function to Run Insertion Sort and Return Time Taken to run sorting algorithm.
def run_insertion(n):
    data = sample(range(1, n+1), n)

    start_time = time_ns()
    insertion_sort(data)
    end_time = time_ns()

    time_taken = end_time-start_time
    return time_taken

def plot_insertion():
    x_vals = []
    y_vals = []
    
    for i in range(10000,100000+1,10000):
        x_vals.append(i)
        y_vals.append(run_insertion(i))
        
    plt.plot(x_vals,y_vals)
    plt.suptitle("Insertion Sort.")
    plt.xlabel('No. of Data')
    plt.ylabel('Execution Time in ns')
    plt.show()

# Function to Run Insertion Sort and Return Time Taken to run sorting algorithm.
def run_merge(n):
    data = sample(range(1, n+1), n)
    data.sort(reverse=True)

    start_time = time_ns()
    merge_sort(data, 0, len(data)-1)
    end_time = time_ns()

    time_taken = end_time-start_time
    return time_taken

def plot_merge():
    x_vals = []
    y_vals = []
    
    for i in range(100000,1000000+1,10000):
        x_vals.append(i)
        y_vals.append(run_merge(i))
        
    plt.plot(x_vals,y_vals)
    plt.suptitle("Merge Sort.")
    plt.xlabel('No. of Data')
    plt.ylabel('Execution Time in ns')
    plt.show()

plot_insertion()
plot_merge()