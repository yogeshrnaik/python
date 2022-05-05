from typing import List


# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    # Write your code here
    curr = 1
    time = 0
    for ci in C:
        if curr != ci:
            time += min(abs(ci - curr), (N - ci) + curr)
            curr = ci

    return time


# print(getMinCodeEntryTime(1, 1, [1]))
# print(getMinCodeEntryTime(10, 2, [1, 2]))
# print(getMinCodeEntryTime(10, 3, [1, 2, 3]))
# print(getMinCodeEntryTime(10, 3, [1, 2, 10]))
# print(getMinCodeEntryTime(10, 2, [5, 1]))
# print(getMinCodeEntryTime(50000000, 1, [20000000]))
print(getMinCodeEntryTime(5, 5, [1, 1, 1, 1, 2]))
