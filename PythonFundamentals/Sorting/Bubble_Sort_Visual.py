import matplotlib.pyplot as plt
import numpy as np
import time

def visualize_sort():
    nums = [5, 3, 8, 6, 7, 2]
    n = len(nums)

    fig, ax = plt.subplots()
    bars = ax.bar(range(len(nums)), nums, color='blue')

    def update_bars(nums):
        for bar, height in zip(bars, nums):
            bar.set_height(height)
        plt.pause(0.5)  # Pause to visualize each step

    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
                ax.clear()
                bars = ax.bar(range(len(nums)), nums, color='blue')
                update_bars(nums)
        if not swapped:
            break

    plt.show()

visualize_sort()
