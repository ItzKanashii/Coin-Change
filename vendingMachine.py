def dispense_change(amount_paid, cost, denominations=None):
    """
    Compute the minimal set of coins to return as change in a vending machine.

    Parameters:
    -----------
    amount_paid : int
        The total amount of money provided by the user.
    cost : int
        The price of the selected item.
    denominations : list of int, optional
        Available coin denominations (default is [100, 50, 20, 10, 5, 2, 1]).

    Returns:
    --------
    list of int
        Coins to be dispensed as change.
        If the change cannot be made, returns an empty list.

    Example:
    --------
    >>> dispense_change(150, 104)
    [20, 20, 5, 1]
    """
    if denominations is None:
        denominations = [100, 50, 20, 10, 5, 2, 1]
    balance = amount_paid - cost
    dispensed = []

    # Ensure denominations are in descending order
    denominations.sort(reverse=True)

    for coin in denominations:
        while balance >= coin:
            balance -= coin
            dispensed.append(coin)

    if balance == 0:
        return dispensed
    else:
        return []  # Change cannot be formed


if __name__ == "__main__":
    amount_paid = 500
    cost = 127
    dispensed = dispense_change(amount_paid, cost)
    print(dispensed)
    # Example Output : [100, 100, 100, 50, 20, 2, 1]
