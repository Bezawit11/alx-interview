#!/usr/bin/python3
"""minimum operations"""


def minOperations(n):
    """a method that calculates the fewest number of operations 
    needed to result in exactly n H characters in the file
    """
    s = 'HH'
    sum = 2
    lm = []
    for i in range(1, n + 1):
        if n % i == 0 and i < n // 2:
            lm.append(i)
    a = max(lm) - 2
    s = s + ('H' * a)
    sum += len(s) - len('HH')
    sum += 2
    b = (n / len(s)) - 2
    return int(b + sum)
