# Given an array of even size N, task is to find minimum value that can be added to an element so that array 
# become balanced. An array is balanced if the sum of the left half of the array elements is equal to the sum 
# of right half.

# Input:
# N = 6
# arr[] = { 1, 2, 1, 2, 1, 3 }
# Output: 2
# Explanation:
# Sum of first 3 elements is 1 + 2 + 1 = 4, 
# Sum of last three elements is 2 + 1 + 3 = 6,
# To make the array balanced you can add 2.

import numpy as np

n = 6
arr = np.array = ([1, 2, 1, 1, 2, 1])

half_point = int(n/2)
left_side_sum = 0
right_side_sum = 0

for i in range(0,half_point,1):
    left_side_sum =+ left_side_sum+arr[i]

for j in range(half_point,n,1):
    right_side_sum =+ right_side_sum+arr[j]

print('Lado esquerdo: ',left_side_sum)
print('Lado direito: ',right_side_sum)

if left_side_sum < right_side_sum:
    print('Para balancear o array, deve-se adicionar ',right_side_sum-left_side_sum, 'ao lado esquerdo')

    arr[half_point-1] =+ arr[half_point-1] + right_side_sum-left_side_sum

    print('Array balanceado', arr)

if left_side_sum > right_side_sum:
    print('Para balancear o array, deve-se adicionar ',left_side_sum-right_side_sum, 'ao lado direito')

    arr[n-1] =+ arr[n-1] + left_side_sum-right_side_sum

    print('Array balanceado', arr)

else:
    print('Array Balanceado: ', arr)

