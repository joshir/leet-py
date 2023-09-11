from typing import List


def combination(n: int, k: int) -> List[List[int]]:
    res = []

    def backtrack(i, comb=[]):
        if len(comb) == k:
            res.append(comb[:])

        for s in range(i, n + 1):
            comb.append(s)
            backtrack(s + 1, comb)
            comb.pop()

    backtrack(1, [])
    return res


if __name__ == '__main__':
    print(combination(4, 2))
