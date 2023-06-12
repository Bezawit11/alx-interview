#!/usr/bin/python3
"""
0x07 - Rotate 2D Matrix
"""
def rotate_2d_matrix(m):
    """rotates a 2d matrix by 90 degrees"""
    a = []
    o = []
    f = m.copy()
    m.clear()
    for i in range(len(f)):
        for n in range(len(f)):
            o.append(f[n][i])
        m.append(o)
        o = []
    g = m.copy()
    m.clear()
    for j in g:
        j = j[::-1]
        m.append(j)
