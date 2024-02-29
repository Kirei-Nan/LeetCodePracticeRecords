class Solution(object):
    def isValid(self, chessboard, col, row):
        for i in range(row):
            if chessboard[i][col]=="Q":
                return False
        i,j=row-1,col-1
        while i>=0 and j>=0:
            if chessboard[i][j]=="Q":
                return False
            i-=1
            j-=1

        i,j=row-1,col+1
        while i>=0 and j<len(chessboard):
            if chessboard[i][j]=="Q":
                return False
            i-=1
            j+=1
        return True
    def backtrack(self,result,row,n,chessboard):
        if row==n:
            result.append(chessboard[:])
            return
        for col in range(n):
            if self.isValid(chessboard, col, row):
                chessboard[row]=chessboard[row][:col]+"Q"+chessboard[row][col+1:]
                self.backtrack(result,row+1,n,chessboard)
                chessboard[row] = chessboard[row][:col] + "." + chessboard[row][col + 1:]
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result=[]
        chessboard=["."*n for _ in range(n)]
        self.backtrack(result,0,n,chessboard)
        return result
