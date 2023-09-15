from typing import List


def triangle(numRows: int) -> List[List[int]]:
    res, prev, cur = [[1]], [], []
    for i in range(len(numRows) - 1):
        prev = [0] + res[-1] + [0]
        for j in range(len(res[-1]) + 1):
            cur.append(prev[j] + prev[j + 1])
        cur = []
    return res
