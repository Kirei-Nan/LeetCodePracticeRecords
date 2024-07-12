class Solution:
    def is_valid(self,row:int,col:int,val:int,board:List[List[str]]):
        n=len(board)
        for i in range(n):
            if board[row][i]==str(val):
                return False
        for j in range(n):
            if board[j][col]==str(val):
                return False
        start_row=(row//3)*3
        start_col=(col//3)*3
        for row in range(start_row,start_row+3):
            for col in range(start_col,start_col+3):
                if board[row][col]==str(val):
                    return false
        return True
    def backtracking(self,board: List[List[str]]):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != '.': continue
                for k in range(1,10):
                    if self.is_valid(i,j,k,board):
                        board[i][j] = str(k)
                        if self.backtracking(board):
                            return True
                        board[i][j] = '.'
                return False
        return True
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtracking(board)
