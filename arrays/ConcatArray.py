from typing import List


def concat(nums: List[int]):
    res = []
    for n in nums:
        res.append(n)
    for n in nums:
        res.append(n)

    return res