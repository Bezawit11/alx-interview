#!/usr/bin/python3
"""log parsing"""


import sys
from signal import signal, SIGPIPE, SIG_DFL
#
s

if __name__ == '__main__':
    lm = []
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
            lm.append(line)
            if len(lm) == 10:
                break
        for i in lm:
            try:
                sum += int(i.split()[-1])
            except BaseException:
                pass
            try:
                key = i.split()[-2]
                if key in d.keys():
                    d[key] += 1
            except BaseException:
                pass
        print('File size:', sum)
        for k, v in sorted(d.items()):
            if v != 0:
                print("{}: {}".format(k, v))
    except KeyboardInterrupt:
        print('File size:', sum)
        for k, v in sorted(d.items()):
            if v != 0:
                print("{}: {}".format(k, v))
        raise
