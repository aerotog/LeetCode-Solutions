# https://leetcode.com/problems/pancake-sorting/
from typing import List


def pancakeSort(A: List[int]) -> List[int]:
    # This can be solved by putting biggest number at the end one at a time
    # Flip up to next biggest number to get to front
    # Flip up to desired position of next biggest number
    # The original position of each number will be changed by each flip

    length = len(A)
    # Get original positions of numbers biggest to smallest
    original_positions = sorted(range(1, length + 1), key=lambda i: -A[i - 1])

    flips = []

    for position in original_positions:
        for flip in flips:
            # Original position moves with each existing flip if included in flip
            if position <= flip:
                # Original position moved by single flip
                position = flip + 1 - position

        # Next moves will be current position of next biggest, then desired position of next biggest
        flips.extend([position, length])
        # The next desired position will be directly before the last insertion
        length -= 1

    return flips


A = [3, 2, 4, 1]

print(pancakeSort(A))
