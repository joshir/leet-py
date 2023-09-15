from typing import List


def replace(nums: List[int]):
    max_i, prev = -1, 0

    for i in range(len(nums)-1,-1,-1):
        prev = nums[i]
        nums[i] = max_i
        max_i = max(prev, max_i)
    return nums

