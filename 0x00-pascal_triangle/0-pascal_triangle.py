#!/usr/bin/python3
"""module to code pascal's triangle in python
"""


def pascal_triangle(n):
    """a function that returns a list of lists of
    integers representing the Pascal’s triangle of n.


    Args:
        n (int): number of rows.
    """
    outerlist = []
    if n <= 0:
        return outerlist

    for row in range(n):
        innerlist = []
        for column in range(row + 1):
            if column == 0 or column == row:
                innerlist.append(1)
            else:
                innerlist.append(outerlist[row-1]
                                 [column-1] + outerlist[row-1][column])
        outerlist.append(innerlist)

    return outerlist
