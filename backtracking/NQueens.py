from typing import List


class Solution:
    def solveQueens(self, n: int)-> List[List[int]]:
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [['.'] * n for i in range(n)]

        def backtrack(r):
            if r == n :
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                else:
                    col.add(c)
                    posDiag.add(r+c)
                    posDiag.add(r-c)
                    board[r][c] = "Q"

                    backtrack(r+1)

                    col.remove(c)
                    posDiag.remove(r + c)
                    posDiag.remove(r - c)
                    board[r][c] = "."
        backtrack(0)
        return res
