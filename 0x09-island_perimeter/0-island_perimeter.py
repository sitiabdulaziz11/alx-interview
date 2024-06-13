#!/usr/bin/python3
""" Module for Island Perimeter
"""

bound_4 = set()
bound_3 = set()
bound_2 = set()
bound_1 = set()


def boundary(grid, i, j):
    """Find cells with either 4, 3, 2 or 1 exposed boundary and add them to
       appropriate set
       Args:
           grid (list): 2d list
           i (int): row number
           j (int): column number
    """
    boundaries = 0
    try:
        if i == 0:
            boundaries += 1
        elif grid[i-1][j] == 0:
            boundaries += 1
    except Exception:
        boundaries += 1
    try:
        if grid[i+1][j] == 0:
            boundaries += 1
    except Exception:
        boundaries += 1
    try:
        if grid[i][j+1] == 0:
            boundaries += 1
    except Exception:
        boundaries += 1
    try:
        if j == 0:
            boundaries += 1
        elif grid[i][j-1] == 0:
            boundaries += 1
    except Exception:
        boundaries += 1

    if boundaries == 1:
        bound_1.add((i, j))
    elif boundaries == 2:
        bound_2.add((i, j))
    elif boundaries == 3:
        bound_3.add((i, j))
    elif boundaries == 4:
        bound_4.add((i, j))


def island_perimeter(grid):
    """
    Function  that returns the perimeter
    of the island described in grid.
    """
    if grid == []:
        return 0
    length = len(grid)
    wdith = len(grid[0])
    for i in range(length):
        for j in range(wdith):
            if grid[i][j] == 1:
                boundary(grid, i, j)
                if len(bound_4) != 0:
                    return 4
    perimeter = (len(bound_3) * 3) + (len(bound_2) * 2) + (len(bound_1))
    return perimeter
