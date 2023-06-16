#!/usr/bin/python3
"""
Making change
"""


def makeChange(coins, total):
    """determine the fewest number of coins
    needed to meet a given amount total
    """
    d = 0
    if coins == []:
        return -1
    if total <= 0:
        return 0
    sum = 0
    s = coins.copy()
    s.sort(reverse=True)
    for i in s:
        h = i
        if total // h > 0:
            d = h
            break
    if d != h:
        return -1
    a = total // h
    b = total % h
    if b in s:
        sum = a + 1
        return sum
    elif b == 0:
        return a
    else:
        l = makeChange(coins, b)
        if l == -1:
            return -1
        sum = a + l
        return sum
