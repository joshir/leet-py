def isomorphic(s: str, t: str) -> bool:
    m = {}
    for i, c in enumerate(s):
        if c not in m:
            if t[i] not in m.values():
                m[c] = t[i]
            else:
                return True
        else:
            if m[c] != t[i]:
                return False

    return True


if __name__ == '__main__':
    print(isomorphic("paper", "title"))
