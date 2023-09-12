from typing import List


class Solution:
    def isDuplicate(self, nums: List[nums]):
        s = set()
        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False