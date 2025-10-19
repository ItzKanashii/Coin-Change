from coinChangeDP import coinChangeDP
from coinChangeGreedy import coinChangeGreedy
from GenerateData import generateCoinChangeCSV
from GenerateGraphs import minCoinGraph, compareGraph


def parse_testcases(file_path: str):
    """
    Parses a text file describing coin denominations, target ranges, and labels.
    Format example:
        25 10 5 1
        1 1000
        Standard
    Returns a list of tuples: (coins, (start, end), name)
    """
    testcases = []
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith('%')]

    # Group every 3 lines as one test case
    for i in range(0, len(lines), 3):
        coins = list(map(int, lines[i].split()))
        start, end = map(int, lines[i + 1].split())
        name = lines[i + 2].strip()
        testcases.append((coins, (start, end), name))
    return testcases


def main():
    testcases = parse_testcases("testcase.txt")

    for coins, target_range, name in testcases:
        print(f"\nProcessing test case: {name}")
        base_name = name.lower()

        # File names
        greedy_csv = f"projectFile\\datasets\\greedy_{base_name}.csv"
        dp_csv = f"projectFile\\datasets\\dp_{base_name}.csv"

        greedy_coin_graph = f"projectFile\\graphs\\greedy_coins_{base_name}_plot.png"
        greedy_time_graph = f"projectFile\\graphs\\greedy_time_{base_name}_plot.png"

        dp_coin_graph = f"projectFile\\graphs\\dp_coins_{base_name}_plot.png"
        dp_time_graph = f"projectFile\\graphs\\dp_time_{base_name}_plot.png"

        compare_coin_graph = f"projectFile\\graphs\\compare_coins_{base_name}_plot.png"
        compare_time_graph = f"projectFile\\graphs\\compare_time_{base_name}_plot.png"

        # Generate CSVs
        print("  Generating Greedy data...")
        generateCoinChangeCSV(coins, target_range, coinChangeGreedy, greedy_csv)
        minCoinGraph(greedy_csv, greedy_coin_graph, greedy_time_graph)

        print("  Generating DP data...")
        generateCoinChangeCSV(coins, target_range, coinChangeDP, dp_csv)
        minCoinGraph(dp_csv, dp_coin_graph, dp_time_graph)

        # Compare results
        print("  Comparing Greedy vs DP...")
        compareGraph(greedy_csv, dp_csv, compare_coin_graph, compare_time_graph)

    print("\nAll test cases processed successfully.")


if __name__ == "__main__":
    main()
