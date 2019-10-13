# https://leetcode.com/problems/gas-station/
from typing import List

# gas = [1, 2, 3, 4, 5]
# cost = [3, 4, 5, 1, 2]
gas = [3,3,4]
cost = [3,4,4]

# Brute force O(n^2) is too slow
# Try moving window? Two indexes. Add front, remove back
def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    tank = 0
    start_index = 0
    next_index = 0

    n = len(gas)

    while start_index < n:

        if tank < 0:
            tank -= gas[start_index] - cost[start_index]
            start_index += 1
        else:
            tank += gas[next_index] - cost[next_index]
            next_index = (next_index + 1) % n

            if next_index == start_index and tank >= 0:
                return start_index

    return -1


print(canCompleteCircuit(gas, cost))
