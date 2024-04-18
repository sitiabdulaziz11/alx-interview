#!/usr/bin/python3
"""Module to determine if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    method that determines if all the boxes can be opened.
    """

    if (type(boxes)) is not list and len(boxes) == 0:
        return False

    visited_box = [False] * len(boxes)
    visited_box[0] = True

    def dfs(box_number):
        """Depth first search algorithm

        Args:
            box_number (_type_): variable
            that indicate the boxes number or index of box.
        """
        visited_box[box_number] = True

        for key in boxes[box_number]:
            if key < len(boxes) and not visited_box[key]:
                dfs(key)
    dfs(0)

    return all(visited_box)
