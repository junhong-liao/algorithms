def count_zig_zags(arr: list[int]) -> int:
    start, count = 0, 0
    for start in range(len(arr) - 1): # why does this have to be len(arr) - 1??
        for end in range(start + 1, len(arr)):
            if end - start < 2:
                if arr[end] == arr[start]:
                    break
                # debug
                # print(arr[start:end + 1]) 
                count += 1
            else: # end - start >= 2
                if arr[end] == arr[end - 1]:
                    break
                if arr[end] < arr[end - 1] and arr[end - 1] < arr[end - 2]:
                    break
                if arr[end] > arr[end - 1] and arr[end - 1] > arr[end - 2]:
                    break
                # debug
                # print(arr[start:end + 1])
                count += 1
    return count

test = [9, 8, 7, 6, 5]
test2 = [10, 10, 10]
test3 = [1, 2, 1, 2, 1]
print(count_zig_zags(test))
print(count_zig_zags(test2))
print(count_zig_zags(test3))