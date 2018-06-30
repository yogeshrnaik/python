#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def printSeparator():
    print('*****************************************************************')

def main():
    # this creates a set of characters present in this string
    # duplicate characters are removed and we get unordered unique characters
    a = set("abc")
    b = set("ab12.")
    print_set(a)
    print_set(b)
    printSeparator()

    # we can sort set
    print('Sorted set')
    print_set(sorted(a))
    print_set(sorted(b))
    printSeparator()

    # we can use minus operator on two sets to get items that are in 1st set but are not there in 2nd set
    print('get items that are in 1st set but are not there in 2nd set')
    print(f'a - b : {a-b}.\nType of a-b : {type(a-b)}') # this returns a set
    printSeparator()
    
    # we can use or(|) operator on two sets to get items that are either set 1 or 2 or both
    print('get items that are either set 1 or 2 or both')
    ab = a|b
    print_set(ab)
    print(f'Type of a|b : {type(a|b)}')
    printSeparator()

    # get items that are in set 1 or 2 but not both
    print('get items that are in set 1 or 2 but not both')
    aOrB = a ^ b
    print_set(aOrB)
    printSeparator()

    # get items that are in set 1 and 2
    print('get items that are in set 1 and 2')
    aAndB = a & b
    print_set(aAndB)
    printSeparator()
    
    # set() takes an iterable
    a = set(range(10))
    print_set(a)
    printSeparator()

def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')

if __name__ == '__main__': main()
