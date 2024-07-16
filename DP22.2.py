n, m = input().split(' ')
n = int(n)
m = int(m)
dp = [0] * (n + 1)
dp[0] = 1
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if (i - j >= 0):
            dp[i] += dp[i - j]

print(dp[n])
