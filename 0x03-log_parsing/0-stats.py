#!/usr/bin/python3
"""log parsing"""


import sys
 
if __name__ == '__main__':
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
        print('File size:', sum)
        for k,v in d.items():
            if v != 0:
                print("{}: {}".format(k, v))
    except KeyboardInterrupt:
        print('File size:', sum)
        for k,v in d.items():
            if v != 0:
                print("{}: {}".format(k, v))
        raise

