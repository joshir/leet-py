from typing import List


def search(board: List[List[str]], word: str) -> bool:
    row, col = len(board), len(board[0])  # board is n*m
    visited = set()

    def backtrack(r, c, i=0):
        if i == len(word):
            return True
        if r < 0 or c < 0 or r == row or c == col or board[r][c] != word[i]:
            return False
        if board[r][c] in visited:
            return False

        visited.add((r, c))
        found = backtrack(r + 1, c, i + 1) or backtrack(r, c + 1, i + 1) or backtrack(r - 1, c, i + 1) or backtrack(
            r, c - 1, i + 1)
        visited.remove((r, c))
        return found

    for r in range(row):
        for c in range(col):
            if backtrack(r, c):
                return True
    return False

