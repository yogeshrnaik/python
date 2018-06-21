#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 1
y = 2

if x < y:
    print('x < y: x is {} and y is {}'.format(x, y))
    print(f'x < y: x is {x} and y is {y}')

# you can put the single statement under if/else block on same line
if x < y:   print(f'x < y: x is {x} and y is {y}')
elif x > y: print(f'x > y: x is {x} and y is {y}')
else:       print(f'x and y are same: {x} = {y}')
