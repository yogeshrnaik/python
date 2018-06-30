#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def printSeparator():
    print('*****************************************************************')

# A list comprehension is a list created based on another list or iterator.
def main():
    seq = range(11)
    print_list(seq)
    printSeparator()

    print('Create another list by doubling every element')
    doubleComprehension = [x * 2 for x in seq] # will double every element from seq
    print(doubleComprehension)
    printSeparator()

    print('Create another list having numbers not divisible by 3')
    filtered = [x for x in seq if x % 3 != 0]
    print(filtered)
    printSeparator()

    print('Create list of tuples with number and its square for number not divisible by 3')
    squared = [(x,x**2) for x in seq if x % 3 != 0]
    print(squared)
    printSeparator()

    print('pi rounted to the number of decimal places for each element')
    from math import pi
    squared = [round(pi, i) for i in seq]
    print(squared)
    printSeparator()

    print('Create dictonary using each element as key and value as its square')
    dictSquared =  {x: x**2 for x in seq}
    print(dictSquared)
    printSeparator()

    print('Creating set using comprehension')
    comp = {x for x in 'superduper' if x not in 'pd'}
    print(comp)
    printSeparator()


def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()
