def isAnagramValid(s: str, t: str):
    if len(s) != len(t):
        return False
    sm, tm = {}, {}

    for i in range(len(s)):
        sm[s[i]] = 1 + sm.get(s[i], 0)
        tm[t[i]] = 1 + tm.get(s[i], 0)

    for key in sm:
        if sm[key] != tm.get(key, 0):
            return False
    return True
