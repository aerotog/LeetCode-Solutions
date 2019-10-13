# https://leetcode.com/problems/search-a-2d-matrix/
from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    if len(matrix) == 0:
        return False

    row = 0
    for i in range(len(matrix) - 1):
        if matrix[i+1][0] > target:
            row = i
            break
        row = i+1

    for i in range(len(matrix[row])):
        if matrix[row][i] == target:
            return True
        if matrix[row][i] > target:
            return False

    return False


m = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
t = 11

print(searchMatrix(m, t))
