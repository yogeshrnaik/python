#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
import sys

def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1
    
    # initialize parameters
    if numargs < 1:
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError(f'expected at most 3 arguments, got {numargs}')

    # generator
    i = start
    while i <= stop:
        yield i
        i += step

def main():
    try:
        for i in inclusive_range():
            print(i, end = ' ', flush = True)
        print()
    except TypeError as e:
        print(f'Error: {sys.exc_info()}')
        print(f'Error: {e}')

if __name__ == '__main__': main()
