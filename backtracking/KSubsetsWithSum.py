from typing import List


def canPartitionKSubsets(nums: List[int], k: int) -> bool:
    if sum(nums) % k != 0:
        return False
    targetSum = sum(nums) // k

    nums.sort(reverse=True)
    visited = [False] * len(nums)

    def backtrack(index, count, curSum):
        if count == k - 1:
            return True

        if curSum > targetSum:
            return False

        if curSum == targetSum:
            return backtrack(0, count + 1, 0)

        for j in range(index, len(nums)):
            if not visited[j]:
                visited[j] = True
                if backtrack(j + 1, count, curSum + nums[j]):
                    return True
                visited[j] = False
        return False

    return backtrack(0, 0, 0)
