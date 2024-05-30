#!/usr/bin/python3
"""
Function that rotates an nxn 2D matrix 90 degrees
clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2d square matrix 90 degrees clockwise in-place
    """
    n = len(matrix)
    for i in range(n):
        for k in range(i):
            temp = matrix[i][k]
            matrix[i][k] = matrix[k][i]
            matrix[k][i] = temp
    for i in range(n):
        for j in range(int(n / 2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n-1-j]
            matrix[i][n-1-j] = temp
