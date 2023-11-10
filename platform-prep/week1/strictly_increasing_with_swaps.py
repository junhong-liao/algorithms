def check_strictly_increasing_with_swaps(numbers: list[int]) -> int:
    swaps = 0
    for i in range(len(numbers)):
        if numbers[i] == 0:
            continue
        if numbers[i] > numbers[i]:
            continue
        # now, this means numbers[i] <= numbers[i]:
        if swaps > 0:
            return False
        check_swappability(numbers, numbers[i - 1], numbers[i])

# swaps i, j
def check_swappability(n0, n1, n2) -> bool:
    n_string, n2_string = str(n1), str(n2)
    
    # Case 1 make j smaller than k
    for i in range(len(n_string)):
        for j in range(len(n_string)):
            temp = n_string[i]
            n_string[i] = n_string[j]
            n_string[j] = temp
            if int(n_string) < n2 and int(n_string) > arr[i - 1]:
                return True
    
    n_string, n2_string = str(n), str(n2)
    
    # Case 2 make n2 bigger than n
    for i in range(len(n2_string))
        for j in range(len(n2_string))
            temp = n2_string[i]
            n2_string[i] = n2_string[j]
            n2_string[j] = temp
            if int(n2_string) > n:
                return True
    
    # both cases failed to maintain the requirements for strictly increasing arr.
    return False