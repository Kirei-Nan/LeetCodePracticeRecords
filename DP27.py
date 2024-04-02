def multiple_knapsack(weights, values, amounts, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for j in range(capacity, weights[i] - 1, -1):
            for k in range(1, amounts[i] + 1):
                if j >= k * weights[i]:
                    dp[j] = max(dp[j], dp[j - k * weights[i]] + k * values[i])

    return dp[capacity]

# 测试
weights = [2, 3, 4]
values = [3, 4, 5]
amounts = [4, 3, 2]
capacity = 10

max_value = multiple_knapsack(weights, values, amounts, capacity)
print("最大价值:", max_value)