#!/usr/bin/python3
"""
lockboxes
"""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, else return False"""
    l = boxes[0]
    l.append(0)
    for i in l:
        for j in boxes[i]:
            if j not in l:
                l.append(j)
    if len(l) == len(boxes):
        return True
    else:
        return False
