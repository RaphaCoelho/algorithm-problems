#Given a sorted array containing only 0s and 1s, find the transition point. 

# Input:
# N = 5
# arr[] = {0,0,0,1,1}
# Output: 3
# Explanation: index 3 is the transition 
# point where 1 begins.


# Input:
# N = 4
# arr[] = {0,0,0,0}
# Output: -1
# Explanation: Since, there is no "1",
# the answer is -1.

import numpy as np
n = 9
arr = np.array = ([0,0,0,0,0,0,1,1,1])


for i in range(0,n-1,1):
    print(i)
    if arr[i] != arr[i+1]:
        arr_transition = i+1
        break
    else:
        arr_transition = -1

    #break


print('Ponto de transição: ', arr_transition)
