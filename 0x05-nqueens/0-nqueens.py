#!/usr/bin/python3
"""N Queens"""
import sys


a = sys.argv[0]
queen(a)


def refine(lists, d):
    j = []
    k = []
    for h in lists:
        for i in h:
            m = d[i]
            m.append(i)
            if not (set(h).issubset(set(m))):
                j.append(h)
                break
    for f in lists:
        if f not in j:
            if f not in k:
                k.append(f)
    for i in k:
        i.sort()
    final_touches(k)

def final_touches(k):
    p = []
    h = []
    for i in k:
        if i in k[1:]:
            k.remove(i)
    n = len(k[0])
    matrix = [list(range(1 + n * i, 1 + n * (i + 1))) for i in range(n)]
    for m in k:
        for t in m:
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    if matrix[i][j] == t:
                        p.append(i)
                        p.append(j)
                if p != []:
                    h.append(p)
                    p = []
        print(h)
        h = []
    
                        
            
    
def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        return list(a_set & b_set)
    else:
        return None

def evaluate(d, matrix):
    r = []
    all_list = []
    for k in d.keys():
        r.append(k)
        m = d[k]
        for i in m:
            r.append(i)
            if common_member(d[k], d[i]):
                o = common_member(d[k], d[i])
                for h in o:
                    r.append(h)
                if len(r) >= len(matrix):
                    all_list.append(r)
                    r = []
                else:
                    r = []
                    r.append(k)
            else:
                r = []
                r.append(k)
    refine(all_list, d)




def checker(i , j , z, h, l):
    for k in range(1, l):
        if z != i + k or h != j + k:
            continue
        else:
            return 0
    for k in range(1, l):
        if z != i - k or h != j + k:
            continue
        else:
            return 0;
            
    for k in range(1, l):
        if z != i - k or h != j - k:
            continue
        else:
            return 0
            
    for k in range(1, l):
        if z != i + k or h != j - k:
            continue
        else:
            return 0
    return 1


def queen(n):
    matrix = [list(range(1 + n * i, 1 + n * (i + 1))) for i in range(n)]
    l = []
    m = []
    ins = []
    d = {}
    for i in range(n):
        for j in range(n):
            for z in range(n):
                for h in range(n):
                    if z != i and h != j:
                        if checker(i , j , z, h, len(matrix)) == 1:
                            ins.append(z)
                            ins.append(h)
                            l.append(ins)
                            m.append(matrix[z][h])
                            ins = [] #first list to input
            d[matrix[i][j]] = m
            l = []
            m = []
    evaluate(d, matrix)
    return 1
