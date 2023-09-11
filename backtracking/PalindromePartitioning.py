def partition(s: str):
    res = []
    cur = []

    def dfs(i=0):
        if i == len(s):
            res.append(cur[:])
            return
        for k in range(i, len(s)):
            if palindrome(s, i, k):
                cur.append(s[i: k + 1])
                dfs(k + 1)
                cur.pop()

    def palindrome(s, i, k):
        while i < k:
            if s[i] == s[k]:
                i += 1
                k -= 1
            else:
                return False
        return True

    dfs()
    return res

