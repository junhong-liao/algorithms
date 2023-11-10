# can you show me how to use the zip function in python?
# https://stackoverflow.com/questions/13704860/zip-lists-in-python

def count_matches(pattern: str, source: str) -> int:
    vowels = set(['a', 'e', 'i', 'o', 'u', 'y'])
    conversion, count = "", 0
    for s in source:
        if s in vowels:
            conversion += "0"
        else:
            conversion += "1"

    for start in range(len(conversion) - len(pattern)):
        end = start + len(pattern)
        if conversion[start:end] == pattern:
            count += 1
    return count


# write 10 distinct test cases covering edge cases of the problem 


