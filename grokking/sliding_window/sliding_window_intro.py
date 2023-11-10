# intro to sliding window

# when dealing with arr or list, we are asked to find or calculate something among all the subarrays of a given size

# given an arr, find average of each subarr of 'k' contiguous elements inside it

"""
Approach:
    define window_sum as float
    for end in the range len(arr),
    slide the window auto if the end ptr isnt past K - 1.
        zero index means not being past K - 1 is just not being length K.
        once its past K - 1, it will always stay the same length. Length K.
    append window avg ((float)sum / K) to result
    subtract start from sum
    increment start ptr
    return result
"""

class Solution:
    def find_averages_of_subarrays(self, K, arr):
        result = list()
        # set window_sum to float pre-emptively
        # what happens if window_sum is not a float?
        # doesn't python still do it for us?
        window_sum, start = 0.0, 0
        for end in range(len(arr)):
            window_sum += arr[end]
            if end >= K - 1:
                result.append(window_sum / K)
                window_sum -= arr[start]
                start += 1
        return result
    
