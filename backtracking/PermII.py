from typing import List


def permuteUnique(nums: List[int]) -> List[List[int]]:
    res = []
    visited = [False] * len(nums)

    def dfs(perm: List[int]) -> None:
        if len(perm) == len(nums):
            res.append(perm.copy())
            return

        for i, num in enumerate(nums):
            if visited[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == False:
                continue
            visited[i] = True
            perm.append(num)
            dfs(perm)
            perm.pop()
            visited[i] = False

    nums.sort()
    dfs([])
    return res


if __name__ == '__main__':
    print(permuteUnique([1, 2, 2]))
