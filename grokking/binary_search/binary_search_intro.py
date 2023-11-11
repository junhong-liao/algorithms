"""
    Given:
        arr.sort(): list[int]

    Returns:
        index of 'target', if present in arr.
    
    Clarifications:
        Not sure what order its sorted in
        Can have duplicates
"""

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



