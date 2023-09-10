from typing import List


class Solution:
    def subset(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()
            backtrack(i+1, subset)

        backtrack(0, [])
        return res

if __name__ == '__main__':
    print(Solution().subset([1,2,3]))