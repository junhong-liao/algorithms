
# given: array of integers
# returns total pairs that are divisible by k
def find_divisible_indices(a: list[int], k: int) -> int:
    remainders = dict()
    pairs = 0
    for index in a:
        r = index % k
        if r not in remainders:
            remainders[r] = 0 
        remainders[r] += 1
        if r == 0:
            pairs += remainders[r] - 1 # we have already counted the pair
            continue
        if k - r not in remainders:
            continue
        pairs += remainders[k - r]
    return pairs

print(find_divisible_indices([1, 2, 3, 4, 5, 6], 1))