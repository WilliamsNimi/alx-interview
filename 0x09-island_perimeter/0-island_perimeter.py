#!/usr/bin/python3
""" Island perimeter module """


def island_perimeter(grid):
    """ Calculate the perimeter of an island
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 1:
                perimeter += 4
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    perimeter -= 2

                if j < len(grid) - 1 and grid[i][j + 1] == 1:
                    perimeter -= 2 """
    length_of_row = len(grid)
    if (length_of_row > 0):
        length_of_column = len(grid[0])
    perimeter = 0
    for row in range(length_of_row):
        for column in range(length_of_column):
            if grid[row][column] == 1:
                if row == 0 or (row < length_of_row - 1 and grid[row+1][column] == 0):
                    perimeter += 1
                if column == 0 or (column < length_of_column - 1 and grid[row][column+1] == 0):
                    perimeter += 1
                if row == length_of_row - 1 or (row > 0 and grid[row-1][column] == 0):
                    perimeter += 1
                if column == length_of_column - 1 or (column > 0 and grid[row][column - 1] == 0):
                    perimeter += 1

    return perimeter
