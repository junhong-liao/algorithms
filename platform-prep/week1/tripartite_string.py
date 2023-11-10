class counter:
    def __init__(self):
        self.total = 0
        self.encountered = set()

def count_tripartite_splits(s: str):
    if len(s) < 3:
        return 0
    ctr = counter()
    recursive_tripartite_splitter(s, ctr, i = 0, j = 1, k = len(s) - 1)
    return ctr.total

def recursive_tripartite_splitter(s: str, ctr: counter, i: int, j: int, k: int):
    a, b, c = s[i:j], s[j:k], s[k:]
    if (a, b, c) in ctr.encountered:
        return
    ctr.encountered.add((a, b, c))
    if a == "" or b == "" or c == "":
        return
    if a + b != b + c and b + c != a + c and a + b != c + a:
        ctr.total += 1
    recursive_tripartite_splitter(s, ctr, i, j + 1, k)
    recursive_tripartite_splitter(s, ctr, i, j, k - 1)

s = "xxxxx"
print(count_tripartite_splits(s))