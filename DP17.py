class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp=[[0]*(m+1) for _ in range(n+1)]

        for str in strs:
            one=0
            zero=0
            for s in str:
                if s=='1':
                    one+=1
                else:
                    zero+=1
            for i in range(n,one-1,-1):
                for j in range(m,zero-1,-1):
                    dp[i][j]=max(dp[i][j],dp[i-one][j-zero]+1)
        return dp[-1][-1]
