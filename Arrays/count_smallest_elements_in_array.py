#Given an sorted array A of size N. Find number of elements which are less than or equal to given element X.

# Input:
# N = 6
# A[] = {1, 2, 4, 5, 8, 10}
# X = 9
# Output:
# 5
import numpy as np

n = 6
x = 9
count_smallest = 0
arr = np.array = ([1, 2, 4, 5, 8, 10])

for i in arr:
    if i < x:
        count_smallest =+ count_smallest + 1


print(count_smallest)