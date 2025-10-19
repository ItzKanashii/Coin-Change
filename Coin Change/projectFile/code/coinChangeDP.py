def coinChangeDP(coins: list[int], target: int) -> int:
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    for x in range(1, target + 1):
        for coin in coins:
            if coin <= x:
                dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[target] if dp[target] != float('inf') else -1
