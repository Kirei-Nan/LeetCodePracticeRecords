class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp=[[0]*n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0]==1:
                break
            dp[i][0]=1
        for i in range(n):
            if obstacleGrid[0][i]==1:
                break
            dp[0][i]=1
        for i in range(1,m):
            for j in range(n):
                if not obstacleGrid[i][j]:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]