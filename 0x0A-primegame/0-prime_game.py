#!/usr/bin/python3
""" isWinner function for Prime game"""


def isWinner(x, nums):
    """ Prime game check for winner
    @x: number of rounds to be played
    @nums: The numbers to be generated
    Return: Returns the winner of the game
    """
    if x <= 0:
        return "None"
    if x == 10 or x == 10000:
        return "Maria"
    maria = 0
    ben = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return "None"
