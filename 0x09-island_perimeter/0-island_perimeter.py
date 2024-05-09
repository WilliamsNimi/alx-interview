#!/usr/bin/python3
""" Island perimeter module """


def island_perimeter(grid):
    """ Calculate the perimeter of an island """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 1:
                perimeter += 4
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    perimeter -= 2

                if j < len(grid) - 1 and grid[i][j + 1] == 1:
                    perimeter -= 2

    return perimeter
