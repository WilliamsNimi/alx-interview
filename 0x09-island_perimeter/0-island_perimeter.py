#!/usr/bin/python3
""" Island perimeter module """


def island_perimeter(grid):
    """ Calculate the perimeter of an island"""
    len_row = len(grid)
    if (len_row > 0):
        len_col = len(grid[0])
    perimeter = 0
    for row in range(len_row):
        for col in range(len_col):
            if grid[row][col] == 1:
                if row == 0 or (row < len_row - 1 and grid[row + 1][col] == 0):
                    perimeter += 1
                if col == 0 or (col < len_col - 1 and grid[row][col + 1] == 0):
                    perimeter += 1
                if row == len_row - 1 or (row > 0 and grid[row - 1][col] == 0):
                    perimeter += 1
                if col == len_col - 1 or (col > 0 and grid[row][col - 1] == 0):
                    perimeter += 1

    return perimeter
