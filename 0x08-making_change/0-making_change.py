#!/usr/bin/python3
""" Greedy Algorithm change module"""


def makeChange(coins, total):
    """ A Greedy algorithm to make change
    @coins: currency denomination
    @total: Total amount to be made into change
    Return: Returns the total number of coins used or -1
    """
    num_change = 0
    value_add = 0
    coins.sort(reverse=True)
    if total <= 0:
        return 0
    for values in coins:
        if total >= values:
            value_add = int(total / values)
            total = total - (value_add * values)
            num_change = num_change + value_add
            if total == 0:
                return num_change

    return -1
