from math import gcd
from functools import reduce
from typing import List


def isGoodArray(nums: List[int]) -> bool:
    return reduce(gcd, nums) == 1


nums = [12, 5, 7, 23]
assert isGoodArray(nums) is True

nums = [29, 6, 10]
assert isGoodArray(nums) is True

nums = [3, 6]
assert isGoodArray(nums) is False
