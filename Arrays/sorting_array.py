#Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

# Input: 
# N = 5
# arr[]= {0 2 1 2 0}
# Output:
# 0 0 1 2 2
# Explanation:
# 0s 1s and 2s are segregated 
# into ascending order.

n = 7
arr = [0,1,2,2,1,0,1]


for i in range(n):
    for i in range(0,n-1,1):
        j=i+1
        if arr[j] < arr[i]:
            arr[i],arr[j] = arr[j],arr[i] 

print(arr)