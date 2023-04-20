#!/usr/bin/python3
"""
pascal's triangle
"""

def factorial(x):
    """calculate factorial of number"""
    if x == 0:
        return 1
    else:
        return (x * factorial(x-1))

def pascal_triangle(n):
    """function that returns a list of lists"""
    b = []
    a = []
    if n <= 0:
        return [[]]
    for i in range(n):
        for j in range(i+1):
            # nCr = n!/((n-r)!*r!)
            b.append(factorial(i)//(factorial(j)*factorial(i-j)))
        a.append(b)
        b = []
    return a
 
