#Given an array A of size N of integers. Your task is to find the minimum and maximum elements in the array.

# Given an array arr[] of size N representing the size of candles which reduce by 1 unit each day. 
# The room is illuminated using the given N candles. Find the maximum number of days the room is without darkness.

# Input:
# N = 6
# A[] = {3, 2, 1, 56, 10000, 167}
# Output:
# min = 1, max =  10000


import numpy as np
import math
arr_min = math.inf
arr_max = -math.inf
n = 6
arr = np.array = ([3, 2, 5, 56, 4, 167])
for i in arr:
    for j in arr:
        if j < i:
            if j < arr_min:
                arr_min = j
        else:
            if j > i:
                if j > arr_max:
                    arr_max = j

print('Menor valor: ',arr_min, "Maior valor: ", arr_max)