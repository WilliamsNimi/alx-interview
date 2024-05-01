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
    coins.sort()
    if total == 0 or total < 0:
        return 0
    for values in coins:
        maxVal = coins[-1]
        if total >= maxVal:
            value_add = int(total / maxVal)
            total = total - (value_add * maxVal)
            num_change = num_change + value_add
            coins.pop(-1)
            if (total % maxVal) == 0:
                return num_change
        else:
            coins.pop(-1)
            if coins == []:
                return -1

    return -1
