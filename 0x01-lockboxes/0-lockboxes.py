#!/usr/bin/python3
"""
can we open all boxes?
"""


def canUnlockAll(boxes):
    """ Return True if all boxes can be opened, else return False """
    if boxes is None:
        return False

    boxlen = len(boxes)
    visited = set()
    stack = [0]

    while stack:
        current_box = stack.pop()

        if current_box not in visited:
            visited.add(current_box)

            for key in boxes[current_box]:
                if key < boxlen and key not in visited:
                    stack.append(key)

    return len(visited) == boxlen
