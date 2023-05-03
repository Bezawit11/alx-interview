#!/usr/bin/python3
"""minimum operations"""


def minOperations(n):
    """a method that calculates the fewest number of operations 
    needed to result in exactly n H characters in the file
    """
    if n == 0 or n == 1:
        return 0
    s = 'HH'
    sum = 2
    lm = []
    h = n / 2
    if n % 2 == 0:
        for i in range(1, n + 1):
            if n % i == 0 and i < n // 2:
                lm.append(i)
        b = lm[2]
        c = b - len(s)
        k = (h / b) - 2
        sum = sum + 2 + c + k + 2
        return int(sum)
    else:
        for i in range(1, n + 1):
            if n % i == 0 and i < n // 2:
                lm.append(i)
        b = lm[1]
        c = b - len(s)
        k = (h / b) - 2
        sum = sum + 2 + c + k + 2
        return int(sum)
