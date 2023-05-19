#!/usr/bin/python3
"""log parsing"""


import sys
import errno
 
l = []
d = {'200': 0,
     '301': 0,
     '400': 0,
     '401': 0,
     '403': 0,
     '404': 0,
     '405': 0,
     '500': 0
 }
sum = 0
try:
    for line in sys.stdin:
        l.append(line)
        if len(l) == 10:
            break
    for i in l:
        sum += int(i.split()[-1])
        key = i.split()[-2]
        if key in d.keys():
            d[key]+= 1
    print('File size: sum')
    for k,v in d.items():
        print(k, v)
finally:
    print_msg(d, sum)
