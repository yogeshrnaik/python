#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def printSeparator():
    print('*****************************************************************')

def main():
    printSeparator()
    print("Variable arguments...")
    varArgsExample('meow', 'grrr', 'purr')
    
    printSeparator()
    print("Variable argument with tuple...")
    t = ('meow', 'grrr', 'purr')
    # need to use * in front of variable name to convert tuple into variable args
    varArgsExample(*t)
    
    printSeparator()
    print("Variable argument with list...")
    l = ['hey', 'hello', 'hi']
    varArgsExample(*l)

    printSeparator()
    print("Variable argument with set...")
    s = {'set-elem1', 'set-elem1', 'set-elem2'} # order won't be guaranted
    varArgsExample(*s)

    printSeparator()
    print("Variable argument with dictonary: only keys ...")
    d = {'one': 1, 'two': 2, 'three': 3}
    varArgsExample(*d) # the keys gets passed
    
    printSeparator()
    print("Variable argument with dictonary: only values...")
    varArgsExample(*d.values()) # pass values
    
    printSeparator()
    print("Variable argument with dictonary: each entry as (key, value) tuple...")
    varArgsExample(*d.items()) # pass key and value tuple
    
    printSeparator()
    print("Variable argument with range...")
    varArgsExample(*range(1, 4)) # 1, 2, 3 is passed
    print()
    r = range(-3, 0)
    varArgsExample(*r) # -3, -2, -1 is passed

    printSeparator()
    print("Variable argument but no arguments passed...")
    varArgsExample() # if we pass nothing
    printSeparator()

# Variable length argument list
# we can treat it like a Sequence (it is a tuple actually)
def varArgsExample(*args):
    print(f'Type of *args is: {type(args)}') # type is tuple
    if len(args):
        for s in args:
            print(s)
    else: print('No arguments received')

if __name__ == '__main__': main()
