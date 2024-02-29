class Solution(object):
    def isValid(self,row,col,val,board):
        for i in range(len(board)):
            if board[i][col]==str(val):
                return False
        for j in range(len(board[0])):
            if board[row][j]==str(val):
                return False
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(start_row,start_row+3):
            for j in range(start_col,start_col+3):
                if board[i][j]==str(val):
                    return False
        return True
    def backtrack(self,board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] !=".":
                    continue
                for k in range(1,10):
                    if self.isValid(i,j,k,board):
                        board[i][j] = str(k)
                        if self.backtrack(board):
                            return True
                        board[i][j] = '.'
                return False
        return True

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.backtrack(board)