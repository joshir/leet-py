from typing import List


def solveQueens(n: int) -> List[List[int]]:
    col = set()
    pdiag = set()
    ndiag= set()
    soln = 0

    def backtrack(r):
        if r == n :
            nonlocal soln
            soln += 1
            return

        for c in range(n):
            if c in col or (r+c) in pdiag or (r-c) in ndiag:
                continue
            else:
                col.add(c)
                pdiag.add(r+c)
                ndiag.add(r-c)

                backtrack(r+1)

                col.remove(c)
                pdiag.remove(r + c)
                ndiag.remove(r - c)
    backtrack(0)
    return soln

