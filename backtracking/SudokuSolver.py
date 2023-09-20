from typing import List


class Solution:

    def solve(self, board: List[List[int]]) -> List[List[int]]:
        res = []

        def valid(board, r, c, val):
            for i in range(len(board)):
                if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == val:
                    return False
                if board[i][c] == val or board[r][i] == val:
                    return False
            return True

        def backtrack(board, row, col):
            if row == len(board) - 1 and col == len (board[0]) -1 :
                for r in board:
                    res.append(r)

            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == 0:
                        for k in range(1, 10, 1):
                            if valid(board, i, j, k):
                                board[i][j] = k
                                if backtrack(board, i, j):
                                    return True
                                else:
                                    board[i][j] = 0
                        return False
            return True

        backtrack(board, 0, 0)
        return res
        return f


if __name__ == '__main__':
    board = [[3, 0, 6, 5, 0, 8, 4, 0, 0], [5, 2, 0, 0, 0, 0, 0, 0, 0], [0, 8, 7, 0, 0, 0, 0, 3, 1],
             [0, 0, 3, 0, 1, 0, 0, 8, 0], [9, 0, 0, 8, 6, 3, 0, 0, 5], [0, 5, 0, 0, 9, 0, 6, 0, 0],
             [1, 3, 0, 0, 0, 0, 2, 5, 0], [0, 0, 0, 0, 0, 0, 0, 7, 4], [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    print(Solution().solve(board))
