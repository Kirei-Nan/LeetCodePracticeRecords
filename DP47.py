class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp=[[0]*(1+len(s)) for _ in range(len(t)+1)]

        for i in range(1,len(t)+1):
            for j in range(1,len(s)+1):
                if s[j-1]==t[i-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        if dp[-1][-1]==len(s):
            return True
        return False