# https://leetcode.com/problems/pancake-sorting/
from typing import List


def pancakeSort(A: List[int]) -> List[int]:
    # Get sorted list, big to small
    # For each in sorted, do moves to get to last position
    # Flip 0..i where i is biggest
    # Flip len(A)
    N = len(A)
    B = sorted(range(1, N+1), key=lambda i: -A[i-1])
    # B = sorted(range(1, N + 1), key=lambda i: -A[i - 1])



    return B





ip = [3,2,4,1]

#

print(pancakeSort(ip))

