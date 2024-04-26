#!/usr/bin/python3
"""Module for rotating an nxn matrix in place"""


def rotate_2d_matrix(matrix: list) -> None:
    """Rotating a 2D matrix inplace"""
    len_of_matrix = len(matrix)
    for i in range(len_of_matrix - 1):
        for j in range(i + 1, len_of_matrix):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    for each_row in matrix:
        mid = len(each_row) // 2
        start = 0
        end = len(each_row) - 1
        for step in range(mid):
            temp = each_row[start + step]
            each_row[start + step] = each_row[end - step]
            each_row[end - step] = temp
