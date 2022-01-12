# Given an unsorted array arr[] of size N. Rotate the array to the left (counter-clockwise direction) 
# by D steps, where D is a positive integer. 

# Input:
# N = 5, D = 2
# arr[] = {1,2,3,4,5}
# Output: 3 4 5 1 2
# Explanation: 1 2 3 4 5  when rotated
# by 2 elements, it becomes 3 4 5 1 2.

n = 10
arr = [2,4,6,8,10,12,14,16,18,20]
d = 3



for i in range(0,d,1):
    aux = arr[0]
    arr.pop(0)
    arr.append(aux)

print(arr)