class Solution:
    def knapsack(self,weights:list[int],values:list[int],m:int,n:int) -> int:
        dp=[[0 for _ in range(m)] for _ in range(n+1)]
        for i in range(0,n+1):
            if weights[0]<=i:
                dp[i][0]=values[0]
        for i in range(1,n+1):#包容量
            for j in range(1,m):#item index
                if weights[j]<=i:
                    dp[i][j]=max(dp[i][j-1],dp[i-weights[j]][j-1]+values[j])
                else:
                    dp[i][j]=dp[i][j-1]
        for row in dp:
            print(row)
        return dp[-1][-1]
    def getinput(self):
        m,n=map(int,input().split())
        weights=list(map(int,input().split()))
        values=list(map(int,input().split()))
        return m,n,weights,values

solution=Solution()
m,n,weights,values=solution.getinput()
print(solution.knapsack(weights,values,m,n))