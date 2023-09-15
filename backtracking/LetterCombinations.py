from typing import List


def letterCombos(digits: str) -> List[str]:
    res = []
    m = {
        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
        "0": "",
    }

    def backtrack(i=0, cur=[]):
        if i == len(digits):
            res.append(cur[:])
            return

        for j in m[digits[i]]:
            cur.append(j)
            backtrack(i + 1, cur)
            cur.pop()

    digits and backtrack(0, [])
    return res


if __name__ == '__main__':
    print(letterCombos("23"))
