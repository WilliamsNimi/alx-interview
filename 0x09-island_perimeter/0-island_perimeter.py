#!/usr/bin/python3
""" Island perimeter module """
from typing import List
def island_perimeter(grid: List) -> int:
    """ Calculate the perimeter of an island """
    count = 0
    for i in grid:
        for j in i:
            if j == 1:
                count+=1

    return (count * 2) + 2
