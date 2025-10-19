def coinChangeGreedy(coins: list[int], target: int) -> int:
    # coins are expected to be sorted in descending order
    count = 0
    for coin in coins:
        while target >= coin:
            target -= coin
            count += 1
    return count if target == 0 else -1
