from typing import List


def comboSum(candidates: List[int], target: int) -> List[List[int]]:
    sorted(candidates)
    res = []

    def dfs(i, cur, total):
        if total == target:
            res.append(cur[:])
            return
        if i == len(candidates) or total > target:
            return
        prev = -1
        for k in range(i, len(candidates)):
            if prev == candidates[k]:
                continue
            cur.append(candidates[k])
            dfs(i + 1, cur, total + candidates[k])
            cur.pop()
            prev = candidates[k]

        dfs(0, [], 0)
        return res


if __name__ == '__main__':
    print(comboSum([1, 2, 3, 4], 6))
