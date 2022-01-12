#Given a sorted array Arr of size N and a number X, you need to find the number of occurrences of X in Arr.

# Input:
# N = 7, X = 2
# Arr[] = {1, 1, 2, 2, 2, 2, 3}
# Output: 4
# Explanation: 2 occurs 4 times in the
# given array.
import numpy as np
arr_occurence = 0
x = 3
n = 7
arr = np.array = ([1, 1, 2, 2, 2, 2, 3])

for i in range(0,n,1):
    print(i)
    if arr[i] == x:
        arr_occurence =+ arr_occurence+1

print('Número de ocorrências encontradas: ', arr_occurence)