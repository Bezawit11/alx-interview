#!/usr/bin/python3
"""pprime game"""


def prime(num):
    """checks if a number is a prime no"""
    if num == 2:
        return 1
    if num == 1:
        return 0
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return 0
    else:
        return 1


def check(nums):
    """"decide for the optimal move of player"""
    a = 0
    summ = 0
    h = nums.copy()
    for i in nums:
        f = prime(i)
        if prime(i) == 1:
            for j in h:
                if j % i == 0:
                    a = a + 1
            if a > summ:
                summ = j
                a = 0
    return summ


def maria(n):
    """strategy of player maria"""
    h = n.copy()
    s = check(n)
    if s == 0:
        return 0
    for i in n:
        if i % s == 0:
            h.remove(i)
    return h


def ben(n):
    """strategy of player ben"""
    h = n.copy()
    s = check(n)
    if s == 0:
        return 0
    for i in n:
        if i % s == 0:
            h.remove(i)
    return h


def isWinner(x, nums):
    """returns the name of the winner"""
    if x <= 0 or nums == [0]:
        return None
    h = nums
    mw = 0
    bw = 0
    while x > 0:
        for n in nums:
            k = [i for i in range(1, n + 1)]
            a = maria(k)
            if a == 0:
                bw += 1
                continue
            b = ben(a)
            if b == 0:
                mw += 1
                continue
            x = x - 1
    if mw > bw:
        return 'Maria'
    else:
        return 'Ben'
