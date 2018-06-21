#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 42
y = 73

if x < y:
    z = 112
    print('x < y: x is {} and y is {}'.format(x, y))
    print(f'x < y: x is {x} and y is {y}')

print(f'z is accessible here: {z} because z is defined inside a block and\n' +
'block do not define scope of variables in Python.\n' +
'Only Functions, objects and modules define the scope in Python.')