#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

a = True
b = False
x = ( 'bear', 'bunny', 'tree', 'sky', 'rain' )
y = 'bear'

def ifElse(condition):
    if condition:
        print('expression is true')
    else:
        print('expression is false')

ifElse(a and b) # False
ifElse(y in x) # True
ifElse(y is x[0]) # True
ifElse('Bear' in x) # False
ifElse('bear' in x) # True
ifElse('bear' is not x[1]) # True
