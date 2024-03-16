#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """check if all boxes can be opened"""
    n = len(boxes)
    keys = [0]
    for key in keys:
        for new_key in boxes[key]:
            if new_key not in keys and new_key < n:
                keys.append(new_key)
    if len(keys) == n:
        return True
    return False
