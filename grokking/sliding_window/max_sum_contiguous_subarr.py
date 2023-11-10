"""
Given:
    arr: list[int]
    k: [int]

Returns:
    result: max sum of any continuous subarr, where len() == k

Approach:
    max = float('-inf')
    start = 0
    slide end 
    if end >= K - 1
        calculate max
        subtract start
        incr start 
    
"""

# my version

def max_sum_contiguous_subarr(arr: list[int], k: int) -> int:
    start, window_sum = 0, 0 
    max_sum = float('-inf')
    for end in range(len(arr)):
        window_sum += arr[end]
        if end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[start]
            start += 1
    return max_sum


k = 3
arr = [2,1,5,1,3,2]

print(max_sum_contiguous_subarr(arr, k))


# grokking version

class Solution:
    def max_sub_array_of_size_k(self, k, arr):
        max_sum, window_sum = 0, 0
        start = 0

        for end in range(len(arr)):
            window_sum += arr[end]
            if end >= k - 1:
                max_sum = max(max_sum, window_sum)
                window_sum -= arr[start]
                start += 1
        return max_sum

def main():
    sol = Solution()
    print("Maximum sum of a subarray of size K: " +
        str(sol.max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " +
        str(sol.max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

main()