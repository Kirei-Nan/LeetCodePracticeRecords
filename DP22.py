def solution(n:int,m:int)->int:
    dp=[0]*(n+1)
    dp[0]=1

    for i in range(1,n+1):
        for j in range(1,m+1):
            if i>=j:
                dp[i]+=dp[i-j]
    return dp[-1]

n,m=map(int,input().split())
print(solution(n,m))