import csv
import timeit
from typing import List, Tuple, Callable
from coinChangeGreedy import coinChangeGreedy
from coinChangeDP import coinChangeDP


def generateCoinChangeCSV(
    coins: List[int],
    target_range: Tuple[int, int],
    minCoinFunction: Callable[[List[int], int], int],
    outFilePath: str
) -> None:
    """
    Generates a CSV file with columns [Amount, No. coins used, Time taken].
    For each target in target_range, calls minCoinFunction(coins, target)
    and records execution time in milliseconds.

    Parameters
    ----------
    coins : list[int]
        List of available coin denominations.
    target_range : tuple[int, int]
        Range of target amounts (inclusive start, inclusive end).
    minCoinFunction : Callable
        Function that computes the minimum number of coins for given coins and target.
    outFilePath : str
        Path to save the output CSV file.
    """

    start, end = target_range
    if start <= 0 or end < start:
        raise ValueError("Invalid target_range. Must be (start > 0, end >= start).")

    with open(outFilePath, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Amount", "No. coins used", "Time taken"])  # header

        for amount in range(start, end + 1):
            elapsed_ms = timeit.timeit(lambda: minCoinFunction(coins, amount), number=5) * 200
            writer.writerow([amount, minCoinFunction(coins, amount), round(elapsed_ms, 6)])


if __name__ == "__main__":
    coins = [25, 20, 10, 5, 1]
    target_range = (1, 1000)
    minCoinFunction1 = coinChangeDP
    minCoinFunction2 = coinChangeGreedy
    outFilePath1 = r"Example\DP_Example.csv"
    outFilePath2 = r"Example\Greedy_Example.csv"
    generateCoinChangeCSV(coins, target_range, minCoinFunction1, outFilePath1)
    generateCoinChangeCSV(coins, target_range, minCoinFunction2, outFilePath2)
    print("Data for Greedy and DP is generated. You can now make Graphs!")
