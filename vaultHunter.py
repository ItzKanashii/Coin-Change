# File: vaultHunter.py
"""
Compute Vault Hunter coin change for a given transaction.

Currency denominations:
- Bronze = 1
- Silver = 9 bronze
- Gold = 81 bronze
- Platinum = 729 bronze
"""


def compute_vault_coin(amount_paid, cost):
    """
    Compute the number of platinum, gold, silver, and bronze coins
    to give as change for a Vault Hunter transaction.

    Parameters:
    -----------
    amount_paid : dict
        A dictionary specifying coins paid, e.g.,
        {'platinum': 2, 'gold': 0, 'silver': 3, 'bronze': 5}
    cost : dict
        A dictionary specifying the cost, same format as amount_paid

    Returns:
    --------
    dict
        A dictionary with keys 'platinum', 'gold', 'silver', 'bronze',
        representing the number of coins of each type to return as change.
        Returns 'error' if total paid is less than total cost.
    """

    # Coin values in bronze
    coin_values = {'platinum': 729, 'gold': 81, 'silver': 9, 'bronze': 1}

    # Convert amount_paid and cost to total bronze
    total_paid = sum(amount_paid.get(coin, 0) * value for coin, value in coin_values.items())
    total_cost = sum(cost.get(coin, 0) * value for coin, value in coin_values.items())

    balance = total_paid - total_cost
    if balance < 0:
        return 'error'  # Not enough paid

    # Compute change in coins
    change = {}
    for coin, value in coin_values.items():
        count, balance = divmod(balance, value)
        change[coin] = count

    return change


# Example usage
if __name__ == "__main__":
    amount_paid = {'platinum': 5, 'gold': 0, 'silver': 2, 'bronze': 0}
    cost = {'platinum': 1, 'gold': 3, 'silver': 2, 'bronze': 5}

    change = compute_vault_coin(amount_paid, cost)
    print(change)
    # Example Output: {'platinum': 3, 'gold': 5, 'silver': 8, 'bronze': 4}
