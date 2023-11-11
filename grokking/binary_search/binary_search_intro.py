"""
    Given:
        arr.sort(): list[int]

    Returns:
        index of 'target', if present in arr.
    
    Clarifications:
        Not sure what order its sorted in
        Can have duplicates
"""

# original

def binary_search(arr: list[int], target: int) -> int:
    low, high = 0, len(arr)
    while low < high:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        if arr[mid] > target:
            high = mid - 1
    return -1

# issues:
# edge case: empty list?
# lacks ascending or descending logic (reversed)
# high should be len(arr) - 1, not len(arr)

# corrected

def binary_serach(arr: list[int], target: int) -> int:
    if not arr:
        return -1
    
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# GTCI

# middle = start + (end-start)/2

# middle = int(start/2 + end/2)

# we can figure out the sort order simply by looking at the start and end elements
# if the start is greater than the end, we know its descending. Otherwise, vice versa.

class Solution:
    def binary_search(self, arr, key):
        start, end = 0, len(arr) - 1
        isAscending = arr[start] < arr[end]
        





