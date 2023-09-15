from typing import List


def permutations(nums: List[int]) -> List[List[int]]:
    res = []

    def backtrack(perm):
        if len(perm) == len(nums):
            res.append(perm[:])
            return
        for i in nums:
            if i not in perm:
                perm.append(i)
                backtrack(perm)
                perm.pop()

    backtrack([])
    return res


if __name__ == '__main__':
    print(permutations([1, 2, 3]))
