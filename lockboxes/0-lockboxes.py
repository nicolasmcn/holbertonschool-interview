#!/usr/bin/python3
"""Determine if all boxes can be opened."""
def canUnlockAll(boxes):
"""function check if all the boxes can be open"""

    n = len(boxes)
    opened_boxes = set([0])
    keys = boxes[0]
    stack = keys.copy()

    while stack:
        key = stack.pop()

        if key < n and key not in opened_boxes:
            opened_boxes.add(key)
            for new_key in boxes[key]:
                if new_key not in opened_boxes:
                    stack.append(new_key)

    return len(opened_boxes) == n

