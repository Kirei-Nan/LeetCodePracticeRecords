class Solution:
    def getinput(self):
        n,capacity=map(int,input().split())
        weights=list(map(int,input().split()))
        values=list(map(int,input().split()))
        return n,capacity,weights,values
    def dp2(self,n,capacity,weights,values):
        dp=[[0]*(capacity+1) for _ in range(n)]

        for i in range(capacity+1):
            if i<weights[0]:
                continue
            dp[0][i]=values[0]

        for i in range(1,n):
            for j in range(capacity+1):
                if j>=weights[i]:
                    dp[i][j]=max(dp[i-1][j],dp[i-1][j-weights[i]]+values[i])
                else:
                    dp[i][j]=dp[i-1][j]

        return dp[-1][-1]
    def dp1(self,n,capacity,weights,values):
        dp=[0]*(capacity+1)

        for i in range(n):
            for j in range(capacity,-1,-1):
                if j>=weights[i]:
                    dp[j]=max(dp[j],dp[j-weights[i]]+values[i])
        return dp[-1]

solution=Solution()
n,capacity,weights,values=solution.getinput()
print(solution.dp1(n,capacity,weights,values))