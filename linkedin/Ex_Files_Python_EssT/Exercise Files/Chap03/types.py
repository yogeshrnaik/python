#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Python uses dynamic typing or also called as "duck typing"
# Type of value is determined by value itself

# imports everything from decimal module
from decimal import *

def printTypeOf(v):
    print(f"Type of {v} is: {type(v)}")

x = 7; printTypeOf(x)
print('--------------------------------------------------------------')
f = 10.5; printTypeOf(f)
f = 4 * 2.5; printTypeOf(f)

# returns a float number even if we are dividing two integers
# this is new behavior in Python 3
f = 7 / 3;  printTypeOf(f)

# using double // we can get integer as the result of the division
i = 7 // 3 # result = 2
printTypeOf(i)

i = 7 // 4 # result = 1
printTypeOf(i)

 # below will return rounded of float (2.0) because one of the numbers (7.0) is float
f = 7.0 // 3; printTypeOf(f)

# reminder
i = 7 % 3 # result = 1 as int
printTypeOf(i)

f = 7.0 % 3 # result = 1.0 as float
printTypeOf(f)

f = 7.0 % 3.5 # result = 0.0 as float
printTypeOf(f)

f = 7.0 % 3.2 # result = 0.5999999999999996 as float
printTypeOf(f)
print('--------------------------------------------------------------')
# floating point precision not good when working with money
x = .1 + .1 + .1 - .3
printTypeOf(x) # result = 5.551115123125783e-17 as float
print('--------------------------------------------------------------')
# Need to pass number as string as we cannot use floating point number because they are not precise
a = Decimal('0.10') # do not pass 0.1 directly. pass it as string '0.1'
b = Decimal('0.3')
x = a + a + a - b
printTypeOf(x) # class 'decimal.Decimal'
print('--------------------------------------------------------------')
s = "seven"
printTypeOf(s)
printTypeOf('seven')
print('--------------------------------------------------------------')
# triple single or double quotes can be used for multi-line string
s = '''
line one
line two'''
printTypeOf(s)
print('--------------------------------------------------------------')
# one can use triple double-quotes as well
s = """
line one
line two"""
printTypeOf(s)
print('--------------------------------------------------------------')
b = True; printTypeOf(b)
print('--------------------------------------------------------------')
none = None; printTypeOf(none)
print('--------------------------------------------------------------')
list = [1,2,3]; printTypeOf(list)
list = ["a", "b"]; printTypeOf(list)
print('--------------------------------------------------------------')
# set is an unordered collection with no duplicate elements
# in below set, java is duplicate which will be removed automatically by set
set = {'python','java','c#','php', 'java'}
printTypeOf(set)
print('--------------------------------------------------------------')
# dict is HashMap
# key "1" will be overwritten by last value ('java8' in this case)
dict = {"1": "java", "2": "python3", "1": "java8"}
printTypeOf(dict)
print('--------------------------------------------------------------')
# String operations
print('one'.capitalize())
print('one'.upper())
print('ONE'.lower())
# place holders are replaced by the values in the order they appear
print('one {} {}'.format(2, 3))

# Swap arguments order by changing place holder sequence
print('one {1} {0}'.format(2, 3))

# We can left adjust using :<spaces_to_adjust and
# right adjust using :>spaces_to_adjust
print('one "{:<9}" "{:>9}"'.format(2, 3))
print('one "{1:<9}" "{0:>9}"'.format(2, 3))

# use zeros to adjust
print('one "{:<09}" "{:>09}"'.format(2, 3))
print('one "{1:<09}" "{0:>09}"'.format(2, 3))

print('one "{:<09}" "{:>09}"'.format(4444, 666666))
print('--------------------------------------------------------------')
# we can left or right adjust using the variable place holders as well
a = 111
b = 22222
print(f'a="{a:<9}", b="{b:>9}"')
print(f'a="{a:<09}", b="{b:>09}"')
print('--------------------------------------------------------------')
