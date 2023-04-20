#!/usr/bin/python3
"""
pascal's triangle
"""

from math import factorial

def pascal_triangle(n):
    """function that returns a list of lists"""
    l = []
    a = []
    if n <= 0:
        return [[]]
    for i in range(n):
	    for j in range(i+1):
		  # nCr = n!/((n-r)!*r!)
		    l.append(factorial(i)//(factorial(j)*factorial(i-j)))
	    a.append(l)
	    l = []
    return a
  
