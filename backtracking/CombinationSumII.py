from typing import List


class Solution:
    def comboSum(self, candidates: List[int], target: int) -> List[List[int]]:
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
                dfs(i+1, cur, total + candidates[k])
                cur.pop()
                prev = candidates[k]

        dfs(0, [], 0)
        return res
