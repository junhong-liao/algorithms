"""
Given:
    arr: list[int], input
    k: int, num we need to window_sum to >=

Returns:
    min len(subarr) >= k
    else 0 if no such subarray exists

Approach:
    
    1 Expand. 
    2 if sum of current window >= K, shrink until it isnt. 
    3 Before it isnt, keep track of updating length and update the min
    4 Return min length
    
"""

# my version 

import math

def smallest_contiguous_subarr_greater_than_k(arr: list[int], k: int):
    start, window_sum, min_len = 0, 0, math.inf

    # initially forgot to address empty case, and the case with one element.
    if not arr:
        return 0
    
    if len(arr) == 1:
        if arr[0] >= k:
            return 1
        else:
            return 0

    for end in range(len(arr)):
        window_sum +=  arr[end]
        while window_sum >= k and start < end:
            min_len = min(min_len, end - start + 1)
            window_sum -= arr[start]
            start += 1
    return min_len

k = 7
arr = [2, 1, 5, 2, 3, 2]

print(smallest_contiguous_subarr_greater_than_k(arr, k))

# grokking version

class Solution:
    def smallest_subarray_sum(self, s, arr):
        window_sum = 0
        min_len = math.inf
        start = 0

        for end in range(len(arr)):
            window_sum += arr[end]
            while window_sum >= s:
                min_length = min(min_length, end - start + 1)
                window_sum -= arr[start]
                start += 1
        if min_len == math.inf:
            return 0
        return min_len