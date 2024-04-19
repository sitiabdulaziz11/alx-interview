#!/usr/bin/python3
"""Module to determine if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Method that determines if all the boxes can be opened.
    """
    if not isinstance(boxes, list):
        return False

    if len(boxes) == 0:
        return False

    num_boxes = len(boxes)
    visited_box = [False] * num_boxes
    visited_box[0] = True

    stack = [0]  # Using a stack for iterative DFS

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key < num_boxes and not visited_box[key]:
                visited_box[key] = True
                stack.append(key)

    return all(visited_box)
