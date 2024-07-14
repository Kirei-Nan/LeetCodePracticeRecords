N, V = map(int, input().split())
arr = [tuple(map(int, line.splint())) for line in stdin]

dp=[0]*(V+1)
for w,v in arr:
    for j in range(w,V+1):
        dp[j]=max(dp[j],dp[j-w]+v)
print(dp[-1])