# https://leetcode.com/problems/rotate-array/
from typing import List

def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    length = len(nums)
    ans = [None] * length
    for i in range(length):
        if (i + k) < length - 1:
            ans[i + k] = nums[i]
        else:
            ans[i + k - length] = nums[i]
    for i in range(length):
        nums[i] = ans[i]


nums = [1, 2]
rot = 3

rotate(nums, rot)

print(nums)
