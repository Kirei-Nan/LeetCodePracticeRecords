class Solution:
    def knapsack_2d(self,M,N,weights,values):
        dp=[[0]*M for _ in range(N+1)]
        for i in range(N+1):
            if i>=weights[0]:
                dp[i][0]=values[0]

        for i in range(N+1):
            for j in range(1,M):
                if i>=weights[j]:
                    dp[i][j]=max(dp[i][j-1],dp[i-weights[j]][j-1]+values[j])
                else:
                    dp[i][j]=dp[i][j-1]
        # for row in dp:
        #     print(row)
        return dp[-1][-1]
    def knapsack_1d(self,M,N,weights,values):
        dp=[0]*(N+1)
        for j in range(M):
            for i in range(N,j-1,-1):
                dp[i] = max(dp[i], dp[i - weights[j]] + values[j])
        print(dp)
        return dp[-1]


solution=Solution()
M,N=map(int,(input().split()))
weights=list(map(int,(input().split())))
values=list(map(int,(input().split())))
# print(solution.knapsack_2d(M,N,weights,values))
print(solution.knapsack_1d(M,N,weights,values))

