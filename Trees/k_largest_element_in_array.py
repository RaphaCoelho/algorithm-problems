# Given an array Arr of N positive integers, find K largest elements from the array. 
# The output elements should be printed in decreasing order.

# Input:
# N = 5, K = 2
# Arr[] = {12, 5, 787, 1, 23}
# Output: 787 23
# Explanation: 1st largest element in the
# array is 787 and second largest is 23.


n = 7
k = 3
arr = [1, 23, 12, 9, 30, 2, 50]


for i in range(n):
    for i in range(0,n-1,1):
        j=i+1
        if arr[j] < arr[i]:
            arr[i],arr[j] = arr[j],arr[i]
for i in range(n-1,n-1-k,-1):
    print(arr[i])