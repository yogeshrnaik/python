#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def printSeparator():
    print('*****************************************************************')

def main():
    x = 10
    print(isinstance(x, int))
    print(isinstance(x, float))
    printSeparator()

    print(id(x)) # prints unique number representing this object

if __name__ == '__main__': main()
