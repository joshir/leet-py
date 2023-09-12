def isSubsequence(s, t):
    i, j = 0, 0
    m, n = len(s), len(t)
    if s == "": return True
    if m > n: return False
    while i < m and j < n:
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == m
