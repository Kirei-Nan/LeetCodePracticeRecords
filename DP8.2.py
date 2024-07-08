class Solution:
    def integerBreak(self, n: int) -> int:
        if n<2:
            return 0
        dp=[0]*(n+1)
        dp[1]=0
        dp[2]=1

        for i in range(3,n+1):
            for j in range(i):
                dp[i]=max(j*(i-j),j*dp[i-j],dp[i])
        return dp[-1]