#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Bunny:
    def __init__(self, n):
        self._n = n
    def __repr__(self):
        return f'repr: Number of bunnies is: {self._n} ✌'
    def __str__(self):
        return f'str: Number of bunnies is: {self._n}'


def main():
    s = 'Hello, World.'
    print(repr(s)) # repr returns string representation of object

    print(Bunny(10)) # this will call __repr__ method of Bunny class if __str__ is not defined
    
    # this will call __repr__ method of Bunny class
    # if __repr__ is not defined it prints <__main__.Bunny object at 0x037BC7F0>
    print(repr(Bunny(10)))

    # ascii escapes any non-ascii characters (e.g. ✌ to \u270c)
    print(ascii(Bunny(10)))

    # chr() gives the character represented by Unicode number
    print(chr(128406)) # 🖖

    # ord() gives Unicode number for the character
    print(ord('🖖'))

if __name__ == '__main__': main()
