from typing import List


def subset(nums: List[int]) -> List[List[int]]:
    res = []

    def backtrack(i, s):
        if i == len(nums):
            res.append(s[:])
            return
        s.append(nums[i])
        backtrack(i + 1, s)
        s.pop()
        backtrack(i + 1, s)

    backtrack(0, [])
    return res


if __name__ == '__main__':
    print(subset([1, 2, 3]))
