def generate_rotations(num):
    s = str(num)
    return {s[i:] + s[:i] for i in range(len(s))} 
    # this is returning a set right?
    # what does the set look like afterward?
    # can you define a py dict with list comp too?

def count_rotations_optimized(arr: list[int]) -> int:
    rotations = {}
    for num in arr:
        for r in generate_rotations(num):
            rotations[r] = rotations.get(r, 0) + 1
    count = 0
    for num in arr:
        # subtract one, because we don't want to count the number itself.
        count += rotations.get(str(num), 0) - 1
    return count


    