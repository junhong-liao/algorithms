"""
Given:
    s: str
    k: int

Returns:
    result: int, len(substr) with lesser or equal to k.

Approach:
    len(dict) = number of keys, but not efficient
    if len(dict) > k, we need to remove from start ptr, and increment
    here, we should check the length with every addition 

    * assume k is less than or equal to the length of the given string

"""

def longest_substr_with_k_distinct_chars(s: str, k: int):
    counter = dict()
    start, max_len = 0, 0

    if not s:
        return max_len

    for end in range(len(s)):
        if s[end] not in counter:
            counter[s[end]] = 0
        counter[s[end]] += 1
        distinct_chars = len(counter)

        # update max with each addition, if meets condition
        if distinct_chars <= k:
            max_len = max(max_len, end - start + 1)

        # shrink window whever curr_len is greater than k
        while distinct_chars > k:
            # revised
            counter[s[start]] -= 1
            if counter[s[start]] == 0:
                del counter[s[start]]
                distinct_chars -= 1
            start += 1
                
            # # original 
            # if counter[s[start]] == 1:
            #     del counter[s[start]]
            #     distinct_chars -= 1
            # else:
            #     counter[s[start]] -= 1
            # start += 1
    return max_len

    # be wary of string manipulation and the need to go one level deeper
    # counter[s[index]], as opposed to counter[index]

    # grokking

    class Solution:
        def longest_substring_with_k_distinct(self, str1, k):
            start = 0
            max_len = 0
            char_frequency = {}

            for end in range(len(str1)):
                right_char = str1[end]
                if right_char not in char_frequency:
                    char_frequency[right_char] = 0
                char_frequency[right_char] += 1

                while len(char_frequency) > k:
                    left_char = str1[start]
                    char_frequency[left_char] -= 1
                    if char_frequency[left_char] == 0:
                        del char_frequency[left_char]
                    start += 1
                
                # while loop doesnt activate if things are okay

                max_length = max(max_length, end - start + 1)
             return max_length
