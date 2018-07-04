#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def printSeparator():
    print('*****************************************************************')

def len_and_reverse(x):
    print(f'x={x}')
    print(f'len(x)={len(x)}')
    print('Reversed list:', list(reversed(x)))
    print('Reversed tuple:', tuple(reversed(x)))
    printSeparator()

def sum_example(x):
    print('sum of tuple: ', sum(x))
    print('10 + sum of tuple:', sum(x, 10))
    printSeparator()

def min_max(x):
    print('min:', min(x))
    print('max:', max(x))
    printSeparator()

def any_all(x):
    print(any(x)) # returns True if any number in x is non-zero
    print(any((0, 0, 0))) # False
    printSeparator()
    
    print(all(x)) # returns True if all numbers in x is non-zero
    print(all((0, 0, 10))) # False
    print(all((-50, 5, 10))) # True
    printSeparator()

def zip_example():
    x = (1, 2, 3)
    y = (9, 8, 7, 6)
    z = zip(x, y) # ((1, 9), (2, 8), (3, 7)) - extra numbers are ignored
    for i in z:
        print(i)
    printSeparator()

def enumerate_example(x):
    print(f'Enumerating {type(x)}...')
    for i, v in enumerate(x): # enumerate gives us index (i) and value (v)
        print(f'index: {i} and value: {v}')
    printSeparator()

def enumerate_examples():
    x = ('cat', 'dog', 'horse', 'rabbit')
    enumerate_example(x)
    enumerate_example(['cat', 'dog']) # works for list as well
    enumerate_example({'cat', 'dog', 'cat'}) # works for set as well

    d = {'cat': 'KITTEN', 'dog': 'PUPPY', 'cat': 'KITTY'}
    enumerate_example(d) # enumerate works on dictonary keys by default
    enumerate_example(d.items())
    enumerate_example(d.values())

def main():
    x = (1, 2, 3, 4, 5)
    len_and_reverse(x)
    sum_example(x)
    min_max(x)
    any_all(x)
    zip_example()
    enumerate_examples()

if __name__ == '__main__': main()
