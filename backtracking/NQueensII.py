from typing import List


class Solution:
    def solveQueens(self, n: int) -> List[List[int]]:
        col = set()
        posDiag = set()
        negDiag = set()
        soln = 0

        def backtrack(r):
            if r == n :
                nonlocal soln
                soln += 1
                return

            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                else:
                    col.add(c)
                    posDiag.add(r+c)
                    posDiag.add(r-c)

                    backtrack(r+1)

                    col.remove(c)
                    posDiag.remove(r + c)
                    posDiag.remove(r - c)
        backtrack(0)
        return soln
