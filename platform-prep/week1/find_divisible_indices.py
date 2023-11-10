# take 2

def find_divisible_indices(a: list[int], k: int) -> int:

    ...
# inefficient
def find_divisible_indices(a: list[int], k: int) -> int:
    count = 0
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if (a[i] + a[j]) % k == 0:
                count += 1
    return count

a = [1, 2, 3, 4, 5]
k = 3
print(find_divisible_indices(a, k))

# O(n) solution
def find_divisible_indices(a: list[int], k: int) -> int:
    count = 0
    remainder_count = [0] * k
    for i in range(len(a)):
        remainder = a[i] % k
        complement = (k - remainder) % k
        count += remainder_count[complement]
        remainder_count[remainder] += 1
    return count


