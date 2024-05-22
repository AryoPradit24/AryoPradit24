import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                 
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def measure_time(algorithm, data):
    start_time = time.time()
    algorithm(data)
    end_time = time.time()
    return end_time - start_time

# Generate random data for testing
data_size = 200
random_data = [random.randint(1,200) for _ in range(data_size)]

# Measure time for Bubble Sort
bubble_sort_time = measure_time(bubble_sort, random_data.copy())
print(f"Bubble Sort Time:{bubble_sort_time:.6f} seconds")


# Measure time for QuickSort
quick_sort_time = measure_time(quick_sort, random_data.copy())
print(f"QuickSort Time:{quick_sort_time:.6f} seconds")
