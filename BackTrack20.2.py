class Solution:
    def isValid(self, row: int, col: int, chessboard: List[str]):
        for i in range(row):
            if chessboard[i][col] == "Q":
                return False
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        i = row - 1
        j = col + 1
        while i >= 0 and j < len(chessboard):
            if chessboard[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True

    def backtracking(self, chessboard: List[str], curRow: int, n: int, result: List[List[str]]):
        if curRow  == n:
            result.append(chessboard[:])
            return
        for col in range(n):
            if self.isValid(curRow, col, chessboard):
                chessboard[curRow] = chessboard[curRow][:col] + "Q" + chessboard[curRow][col + 1:]
                self.backtracking(chessboard, curRow + 1, n, result)
                chessboard[curRow] = chessboard[curRow][:col] + "." + chessboard[curRow][col + 1:]

    def solveNQueens(self, n: int) -> List[List[str]]:
        chessboard = ["." * n for _ in range(n)]
        result = []
        self.backtracking(chessboard, 0, n, result)
        return result
