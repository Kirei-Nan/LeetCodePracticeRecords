class Solution:
    def knapsack_2d(self,M,N,space,value):
        dp=[[0]*(N+1) for _ in range(M)]
        for j in range(N+1):
            if j>=space[0]:
                dp[0][j]=value[0]

        for i in range(1,M):
            for j in range(N+1):
                if j>=space[i]:
                    dp[i][j]=max(dp[i-1][j],dp[i-1][j-space[i]]+value[i])
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]

    def knapsack_1d(self,M,N,space,value):#M 代表研究材料的种类，第二个正整数 N，代表小明的行李空间
        dp=[0 for _ in range(N+1)]
        for i in range(M):
            for j in range(N,space[i]-1,-1):
                dp[j] = max(dp[j - space[i]] + value[i], dp[j])
        return dp[-1]

    def getinput(self):
        M, N = map(int, input().split())
        space = list(map(int, input().split()))
        value = list(map(int, input().split()))
        return M,N,space,value


solution=Solution()
M,N,space,value=solution.getinput()
print(solution.knapsack_1d(M,N,space,value))
print(solution.knapsack_2d(M,N,space,value))
