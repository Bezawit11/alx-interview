#!/usr/bin/python3
def for_each(l):
    count = 0
    print(l)
    for i in range(len(l)):
        for z in range(len(l)):
            if l[i][0] != l[z][0]:
                if l[i][1] != l[z][1]:
                    count += 1
                    print("found " + str(l[z][0]) + "," + str(l[z][1]) + str(l[i]))
        print("/////")

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

def queen(matrix):
    l = []
    ins = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for z in range(len(matrix)):
                for h in range(len(matrix)):
                    if z != i and h != j:
                        if checker(i , j , z, h, len(matrix)) == 1:
                            print(matrix[z][h], end=",") 
                            ins.append(z)
                            ins.append(h)
                            l.append(ins)
                            ins = [] #first list to input
            for_each(l)
            l = []
            print(" for " + str(matrix[i][j]))
    return l

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

queen(matrix)
