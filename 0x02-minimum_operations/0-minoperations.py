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
            if h % i == 0 and i <= n / 2:
                lm.append(i)
                if i != 1 and i != 2:
                    break
        c = lm[-1] - len(s)
        if h == lm[-1]:
            return int(sum + 2 + c)
        sum = sum + (h / lm[-1]) + 2 + c
        return int(sum)
    else:
        if n == 2 or n == 3:
            return n
        for i in range(1, n + 1):
            if n % i == 0 and i < n // 2:
                lm.append(i)
        b = lm[-1]
        c = b - len(s)
        sum = sum + (n / lm[-1]) + c
        return int(sum)
    
