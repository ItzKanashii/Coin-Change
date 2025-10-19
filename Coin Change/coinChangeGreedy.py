def coinChangeGreedy(coins: list[int], target: int) -> int:
    # coins are expected to be sorted in descending order
    count = 0
    for coin in coins:
        while target >= coin:
            target -= coin
            count += 1
    return count if target == 0 else -1


if __name__ == "__main__":
    coins = [25, 10, 5, 1]
    target = 431
    print(coinChangeGreedy(coins, target))