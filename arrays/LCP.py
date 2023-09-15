import sys
from typing import List


def longestCommonPrefixHelper(s1: str, s2: str) -> int:
    i1, i2, j1, j2 = 0, 0, len(s1), len(s2)
    while i1 < j1 and i2 < j2:
        if s1[i1] == s2[i2]:
            i1 += 1
            i2 += 1
        else:
            return i1
    return min(j1, j2)


def longestCommonPrefix(strs: List[str]) -> str:
    minimum = sys.maxsize
    for i in range(len(strs) - 1):
        minimum = min(minimum, longestCommonPrefixHelper(strs[i], strs[i + 1]))

    if minimum == -1:
        return ""
    else:
        return strs[0][0:minimum]


if __name__ == '__main__':
    print(longestCommonPrefix(["flower", "flow", "flight"]))
