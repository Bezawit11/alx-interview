#!/usr/bin/python3
"""log parsing"""


import sys
from signal import signal, SIGPIPE, SIG_DFL 
#Ignore SIG_PIPE and don't throw exceptions on it... (http://docs.python.org/library/signal.html)
signal(SIGPIPE,SIG_DFL) 
 
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
        for k,v in sorted(d.items()):
            if v != 0:
                print("{}: {}".format(k, v))
    except KeyboardInterrupt:
        print('File size:', sum)
        for k,v in sorted(d.items()):
            if v != 0:
                print("{}: {}".format(k, v))
        raise

