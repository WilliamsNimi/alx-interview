#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    This is  function to print out the numbers in pascal's triangle
    @n: This is the line number of the function to print
    Return: It returns the list with the relevant pascal values
    """
    if (n == 0):
        return ([])
    if (n == 1):
        return ([[1]])
    if (n == 2):
        return ([[1, 1]])
    level2 = [1, 1]
    level3 = []
    overall_list = [[1], [1, 1]]
    j = 2
    while (j < n):
        level3 = []
        control = len(level2) + 1
        for i in range(control):
            if i == 0 or i == (control - 1):
                level3.append(1)
            else:
                level3.append(level2[i-1] + level2[i])
        level1 = level2
        level2 = level3
        overall_list.append(level3)
        j += 1
    return overall_list
