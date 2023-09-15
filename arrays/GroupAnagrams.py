from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    res = {}
    for string in strs:
        s = ''.join(sorted(string))
        res.get(s, []).append(s)

    return list(res.values())
