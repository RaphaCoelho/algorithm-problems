# Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array and return it
# In other words, arrange the elements into a sequence such that 
# arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5].....

# Input:
# n = 5
# arr[] = {1,2,3,4,5}
# Output: 2 1 4 3 5
# Explanation: Array elements after 
# sorting it in wave form are 
# 2 1 4 3 5.

import numpy as np
import time

start_time = time.time()

n = 6
arr = np.array = ([1,2,3,4,5,6])
arr_result = np.array = ([])


for i in range(0, n-1,2):
    j = i + 1
    arr_result.append(arr[j])
    arr_result.append(arr[i])

if n%2 !=0:
    arr_result.append(arr[n-1])

print(arr_result)

print("--- %.8fs seconds ---" % (time.time() - start_time))