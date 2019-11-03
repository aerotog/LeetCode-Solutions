import math
from typing import List


def numberOfSubarrays(nums: List[int], k: int) -> int:
    if len(nums) == 0:
        return 0
    if sum(n % 2 != 0 for n in nums) < k:
        return 0

    even_partition_counts = [0]

    for n in nums:
        if n % 2 == 0:
            even_partition_counts[-1] += 1
        else:
            even_partition_counts.append(0)

    print(even_partition_counts)

    sols = 0
    for i in range(len(even_partition_counts)):
        if i + k >= len(even_partition_counts):
            return sols
        # print(f"MULTIPLYING {even_partition_counts[i]} and {even_partition_counts[k]}")
        sols += (even_partition_counts[i]+1) * (even_partition_counts[i+k]+1)

    return sols



    # head = 0
    # tail = 0
    # num_odds = nums[0] % 2 != 0
    # sols = 0
    #
    # #While num heads < k, move head forward
    # #While next head is not odd, move head forward until odd
    # #Once next odd hit, reset head to last odd
    # #While tail not odd, move tail forward
    # #While tail odd move head forward
    #
    #
    # while head <= len(nums) and tail <= len(nums):
    #     if num_odds < k:
    #         head += 1
    #         if head == len(nums):
    #             break
    #
    #         num_odds += nums[head] % 2 != 0
    #     elif nums[head+1] % 2 == 0 and head+1 <= len(nums):
    #         head += 1
    #     else:
    #         num_odds -= nums[tail] % 2 != 0
    #         tail += 1
    #
    #     sub = nums[tail:head+1]
    #     print(sub)
    #
    #     if num_odds >= k:
    #         print("NICE SUB")
    #         sols += 1
    #
    #     if tail == len(nums):
    #         break
    #
    # return sols


nums = [45627,50891,94884,11286,35337,46414,62029,20247,72789,89158,54203,79628,25920,16832,47469,80909]
k = 1

nums = [1,1,2,1,1]
k = 3

print(numberOfSubarrays(nums, k))