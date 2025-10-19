import pandas as pd
import matplotlib.pyplot as plt


def minCoinGraph(filePath: str, target_coin_graph: str, target_time_graph: str) -> None:
    """
    Reads CSV file with columns: [Amount, No. coins used, Time taken]
    Generates two smooth line plots with small markers.
    """
    df = pd.read_csv(filePath)
    if not all(col in df.columns for col in ["Amount", "No. coins used", "Time taken"]):
        raise ValueError("CSV must contain columns: 'Amount', 'No. coins used', 'Time taken'")

    low, high = df["Time taken"].quantile([0.01, 0.99])
    df["Clipped Time"] = df["Time taken"].clip(lower=low, upper=high)
    df["Clipped Time"] = df["Clipped Time"].rolling(window=5, min_periods=1).median()

    # Line plot: Amount vs No. coins used
    plt.figure(figsize=(12, 4))
    plt.plot(df["Amount"], df["No. coins used"], linestyle='-', linewidth=1.2, marker='', color='blue')
    plt.title("Amount vs Number of Coins Used")
    plt.xlabel("Amount")
    plt.ylabel("Number of Coins Used")
    plt.grid(True, alpha=0.4)
    plt.tight_layout()
    plt.savefig(target_coin_graph.replace('.png', '.pdf'), format='pdf', bbox_inches='tight')
    plt.savefig(target_coin_graph, dpi=600, bbox_inches='tight')
    plt.close()

    # Line plot: Amount vs Time taken
    plt.figure(figsize=(12, 4))
    plt.plot(df["Amount"], df["Clipped Time"], linestyle='-', linewidth=1.2, color='red')
    plt.title("Amount vs Time Taken (ms)")
    plt.xlabel("Amount")
    plt.ylabel("Time (ms)")
    plt.grid(True, alpha=0.4)
    plt.tight_layout()
    plt.savefig(target_time_graph.replace('.png', '.pdf'), format='pdf', bbox_inches='tight')
    plt.savefig(target_time_graph, dpi=600, bbox_inches='tight')
    plt.close()


def compareGraph(filePathGreedy: str, filePathDP: str, target_coin_graph: str, target_time_graph: str) -> None:
    """
    Compares two CSV files (Greedy and DP) by plotting smooth line graphs.
    """
    g = pd.read_csv(filePathGreedy)
    d = pd.read_csv(filePathDP)

    for df in [g, d]:
        if not all(col in df.columns for col in ["Amount", "No. coins used", "Time taken"]):
            raise ValueError("CSV must contain columns: 'Amount', 'No. coins used', 'Time taken'")

        low, high = df["Time taken"].quantile([0.01, 0.99])
        df["Clipped Time"] = df["Time taken"].clip(lower=low, upper=high)
        df["Clipped Time"] = df["Clipped Time"].rolling(window=5, min_periods=1).mean()

    merged = g.merge(d, on="Amount", suffixes=("_greedy", "_dp"))

    # Compare: Amount vs No. coins used
    plt.figure(figsize=(12, 4))
    plt.plot(merged["Amount"], merged["No. coins used_greedy"], label="Greedy", linewidth=1.3)
    plt.plot(merged["Amount"], merged["No. coins used_dp"], label="DP", linewidth=1.3)
    plt.title("Greedy vs DP: Number of Coins Used")
    plt.xlabel("Amount")
    plt.ylabel("Number of Coins Used")
    plt.legend()
    plt.grid(True, alpha=0.4)
    plt.tight_layout()
    plt.savefig(target_coin_graph.replace('.png', '.pdf'), format='pdf', bbox_inches='tight')
    plt.savefig(target_coin_graph, dpi=600, bbox_inches='tight')
    plt.close()

    # Compare: Amount vs Time taken
    plt.figure(figsize=(12, 4))
    plt.plot(merged["Amount"], merged["Clipped Time_greedy"], label="Greedy", linewidth=1.3)
    plt.plot(merged["Amount"], merged["Clipped Time_dp"], label="DP", linewidth=1.3)
    plt.title("Greedy vs DP: Time Taken (ms)")
    plt.xlabel("Amount")
    plt.ylabel("Time (ms)")
    plt.legend()
    plt.grid(True, alpha=0.4)
    plt.tight_layout()
    plt.savefig(target_time_graph.replace('.png', '.pdf'), format='pdf', bbox_inches='tight')
    plt.savefig(target_time_graph, dpi=600, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    inFilePathGreedy = r"Example\Greedy_Example.csv"
    inFilePathDp = r"Example\DP_Example.csv"
    outFilePathCoinGreedy = r"Example\Greedy_Coin_Example.png"
    outFilePathCoinDp = r"Example\DP_Coin_Example.png"
    outFilePathTimeGreedy = r"Example\Greedy_Time_Example.png"
    outFilePathTimeDP = r"Example\DP_Time_Example.png"
    outFilePathCoinCompare = r"Example\Compare_Coin_Example.png"
    outFilePathTimeCompare = r"Example\Compare_Time_Example.png"
    minCoinGraph(inFilePathGreedy, outFilePathCoinGreedy, outFilePathTimeGreedy)
    minCoinGraph(inFilePathDp, outFilePathCoinDp, outFilePathTimeDP)
    compareGraph(inFilePathGreedy, inFilePathDp, outFilePathCoinCompare, outFilePathTimeCompare)
    print("All example graphs are generated! You can find them in the Example folder")
    print("Png for review and Pdf to add to latex file")
