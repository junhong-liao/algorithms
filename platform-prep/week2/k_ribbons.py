# APPROACH
    # use binary search on sorted list.
    # if greater than first result, ditch everything before that idx
    # if lesser than first result, ditch everything after that idx
        # if a match is found, keep incrementing upwards of that match
    # if a match isnt found at the end of the search, we will still be left with the closest number.
        # if the match is lesser, we subtract until it hits k.
        # if the match is greater, we keep adding until it hits k.

arr = [5, 2, 7, 4, 9]
k = 5

def max_length_for_k_ribbons(arr: list[int], k: int) -> int:
    arr.sort()
    max_length = 0
    low, high, mid = 0, len(arr), 0
    while low <= high:
        mid = (high - low + 1) // 2
        ribbons = count_ribbons(arr, mid)
        if ribbons > k:
            high = mid - 1
        if ribbons == k:
            break # go on to end logic.
        else:
            low = mid + 1
    
    # last mile navigation

    while count_ribbons(arr, mid) < k:
        mid -= 1
    while count_ribbons(arr, mid) >= k:
        mid += 1

# helper to return number of ribbons
def count_ribbons(arr: list[int], n: int) -> int:
    ribbons = 0
    for i in range(len(arr)):
        ribbons += arr[i] // n
    return ribbons