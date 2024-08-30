#!/usr/bin/python3
"""Determine if all boxes can be opened."""


def canUnlockAll(boxes):
    """ Method that determines if all boxes can be opened """

    for i in range(1, len(boxes)):
        list_lock = []
        a = 0
        for b in boxes:
            if a != i:
                list_lock.extend(b)
            a += 1
        if i not in list_lock:
            return False
    return True
