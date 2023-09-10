from typing import List


class Solution:
    def combination(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(i, comb = []):
            if len(comb) == k:
                res.append(comb[:])

            for s in range(i, n + 1):
                comb.append(s)
                backtrack(s+1, comb)
                comb.pop()
        backtrack(1, [])
        return res

if __name__ == '__main__':
    print(Solution().combination(4,2))