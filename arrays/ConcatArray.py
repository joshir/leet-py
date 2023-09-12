from typing import List


class Solution:
    def concat(self, nums: List[int]):
        res = []
        for n in nums:
            res.append(n)
        for n in nums:
            res.append(n)

        return res