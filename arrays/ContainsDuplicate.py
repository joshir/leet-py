from typing import List

def isDuplicate(nums: List[int]):
    s = set()
    for i in nums:
        if i in s:
            return True
        s.add(i)
    return False