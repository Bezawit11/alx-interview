#!/usr/bin/python3
"""
lockboxes
"""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, else return False"""
    arr = []
    for i in range(0, len(boxes)):
        arr.append(i)
    l = boxes[0]
    l.append(0)
    for i in l:
        if i < len(boxes):
            for j in boxes[i]:
                if j not in l:
                    l.append(j)
    for a in arr:
        if a not in l:
            return False
    return True
