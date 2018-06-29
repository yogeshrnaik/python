#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import time

def printSeparator():
    print('*****************************************************************')

def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1) * 1000} ms')
    return wrapper


@elapsed_time
def big_sum():
    num_list = []
    for num in (range(0, 100000)):
        num_list.append(num)
    print(f'Big sum: {sum(num_list)}')

# we can decorate more than one function with same function
@elapsed_time
def anotherFunction():
    print('inside anotherFunction()...')

def main():
    printSeparator()
    big_sum()
    printSeparator()
    anotherFunction()
    printSeparator()

if __name__ == '__main__': main()
